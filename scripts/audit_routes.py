#!/usr/bin/env python3
"""Static-site route integrity audit for docs/.

Exit code 1 if a primary route file is missing or a critical href target is absent.
Prints a short report suitable for AUDIT-LOG follow-ups.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PRIMARY_ROUTES = [
    "index.html",
    "start-here.html",
    "courses.html",
    "tutorials.html",
    "help.html",
    "support.html",
    "account.html",
    "python-course.html",
    "csharp-course.html",
    "ai-course.html",
    "course-viewer.html",
    "quiz-viewer.html",
    "certificate.html",
    "tracks.html",
    "promo.html",
    "standards.html",
    "styles.css",
    "site.js",
    "config.js",
    "course-index.json",
]

HREF_RE = re.compile(r"""(?:href|src)=["']([^"'#]+)""", re.I)


def local_target(url: str) -> str | None:
    if not url or url.startswith(("http://", "https://", "mailto:", "data:", "//")):
        return None
    if "${" in url or "{{" in url:
        return None
    path = url.split("?")[0].split("#")[0]
    if not path or path.startswith("../"):
        # allow repo markdown paths referenced from viewer query strings only
        return None
    if path.endswith(".md"):
        return None
    return path


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for name in PRIMARY_ROUTES:
        path = DOCS / name
        if not path.exists():
            errors.append(f"MISSING primary route: {name}")

    html_files = sorted(DOCS.glob("*.html"))
    for html in html_files:
        text = html.read_text(encoding="utf-8", errors="replace")
        for match in HREF_RE.finditer(text):
            target = local_target(match.group(1))
            if not target:
                continue
            candidate = (html.parent / target).resolve()
            try:
                candidate.relative_to(DOCS.resolve())
            except ValueError:
                warnings.append(f"{html.name} -> escapes docs/: {target}")
                continue
            if not candidate.exists():
                # ignore dynamic query-only pages that exist as shell
                if target.startswith("course-viewer.html") or target.startswith("quiz-viewer.html"):
                    continue
                errors.append(f"{html.name} -> broken local link: {target}")

    print("=== Route audit ===")
    print(f"docs: {DOCS}")
    print(f"html pages: {len(html_files)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")
    for line in errors:
        print("ERROR: " + line)
    for line in warnings[:20]:
        print("WARN: " + line)
    if len(warnings) > 20:
        print(f"WARN: … {len(warnings) - 20} more")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
