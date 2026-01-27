#!/usr/bin/env python3
"""
Promote language folders from languages/<lang>/... to <lang>/... at repo root.

Default behavior:
- DRY RUN (no changes) unless --apply is set
- Will NOT overwrite existing root folders unless --overwrite is set
- Copies contents (preserves metadata where possible)
- Optionally remove old languages/<lang> after copy with --delete-source

Example:
  python3 scripts/promote_languages_to_root.py --dry-run
  python3 scripts/promote_languages_to_root.py --apply
  python3 scripts/promote_languages_to_root.py --apply --overwrite
  python3 scripts/promote_languages_to_root.py --apply --delete-source
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import List, Tuple


DEFAULT_SKIP = {"python", "c"}  # existing top-level languages you don't want touched


def iter_language_dirs(languages_dir: Path) -> List[Path]:
    if not languages_dir.exists() or not languages_dir.is_dir():
        return []
    return sorted(
        [p for p in languages_dir.iterdir() if p.is_dir() and not p.name.startswith(".")]
    )


def copy_tree(src: Path, dst: Path, overwrite: bool, dry_run: bool) -> List[Tuple[Path, Path]]:
    """
    Copy src directory contents into dst directory.
    Returns list of (src_item, dst_item) copied.
    """
    copied: List[Tuple[Path, Path]] = []
    dst.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(src):
        root_path = Path(root)
        rel = root_path.relative_to(src)
        target_root = dst / rel

        if not dry_run:
            target_root.mkdir(parents=True, exist_ok=True)

        # Ensure directories exist
        for d in dirs:
            td = target_root / d
            if not dry_run:
                td.mkdir(parents=True, exist_ok=True)

        # Copy files
        for f in files:
            sfile = root_path / f
            dfile = target_root / f

            if dfile.exists() and not overwrite:
                raise FileExistsError(f"Refusing to overwrite existing file: {dfile}")

            copied.append((sfile, dfile))
            if not dry_run:
                dfile.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(sfile, dfile)

    return copied


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--languages-dir", default="languages", help="Source languages directory (default: languages)")
    parser.add_argument("--apply", action="store_true", help="Actually perform changes (default: dry-run)")
    parser.add_argument("--dry-run", action="store_true", help="Force dry-run (default if --apply not set)")
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting existing files at destination")
    parser.add_argument("--delete-source", action="store_true", help="Delete languages/<lang> after successful copy")
    parser.add_argument(
        "--include",
        nargs="*",
        default=None,
        help="Only include these languages (e.g. --include typescript java). Default: all found.",
    )
    parser.add_argument(
        "--skip",
        nargs="*",
        default=sorted(DEFAULT_SKIP),
        help=f"Languages to skip (default: {sorted(DEFAULT_SKIP)})",
    )

    args = parser.parse_args()
    repo_root = Path.cwd()
    languages_dir = (repo_root / args.languages_dir).resolve()

    dry_run = args.dry_run or not args.apply
    overwrite = bool(args.overwrite)

    if not languages_dir.exists():
        print(f"ERROR: '{languages_dir}' does not exist.")
        return 2

    language_dirs = iter_language_dirs(languages_dir)
    if args.include:
        include_set = set(args.include)
        language_dirs = [p for p in language_dirs if p.name in include_set]

    skip_set = set(args.skip or [])
    language_dirs = [p for p in language_dirs if p.name not in skip_set]

    if not language_dirs:
        print("No language directories to process.")
        return 0

    print(f"Repo root: {repo_root}")
    print(f"Source:    {languages_dir}")
    print(f"Mode:      {'DRY-RUN' if dry_run else 'APPLY'}")
    print(f"Overwrite: {overwrite}")
    print(f"Delete src after copy: {bool(args.delete_source)}")
    print(f"Skipping:  {sorted(skip_set)}")
    print("")

    processed = []
    for src_lang_dir in language_dirs:
        lang = src_lang_dir.name
        dst_lang_dir = repo_root / lang

        print(f"==> {lang}")
        if dst_lang_dir.exists():
            # If destination exists, we only proceed if it looks safe or overwrite is enabled.
            # We never delete the destination; we only copy into it.
            print(f"    Destination exists: {dst_lang_dir}")
            if not overwrite:
                # We still can copy if there are no collisions, but safest is to refuse unless user enables overwrite.
                # We'll attempt and error if collision occurs.
                print("    Note: overwrite is OFF; copy will fail if any file collisions are found.")

        try:
            copied = copy_tree(src_lang_dir, dst_lang_dir, overwrite=overwrite, dry_run=dry_run)
        except FileExistsError as e:
            print(f"    ERROR: {e}")
            print("    Tip: re-run with --overwrite if you want to replace destination files.")
            return 1

        print(f"    Files to copy: {len(copied)}")
        if dry_run:
            # Show a short preview
            preview = copied[:10]
            for s, d in preview:
                print(f"      {s.relative_to(repo_root)} -> {d.relative_to(repo_root)}")
            if len(copied) > 10:
                print(f"      ... (+{len(copied) - 10} more)")
        processed.append((lang, src_lang_dir, dst_lang_dir))

        if args.delete_source:
            if dry_run:
                print(f"    Would delete source: {src_lang_dir.relative_to(repo_root)}")
            else:
                shutil.rmtree(src_lang_dir)
                print(f"    Deleted source: {src_lang_dir.relative_to(repo_root)}")

        print("")

    print("DONE. Processed languages:")
    for lang, src, dst in processed:
        print(f" - {lang}: {src.relative_to(repo_root)} -> {dst.relative_to(repo_root)}")

    if dry_run:
        print("\nThis was a dry-run. Re-run with --apply to make changes.")
    else:
        print("\nChanges applied. Review with: git status")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
