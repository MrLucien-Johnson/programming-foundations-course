#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

REQUIRED_LANGUAGES = [
    "typescript",
    "python",
    "sql",
    "java",
    "csharp",
    "go",
    "rust",
    "kotlin",
    "swift",
    "ai",
]

AI_LANGUAGE = "ai"
CORE_LEVELS = ["intermediate", "advanced"]
AI_LEVELS = ["beginner", "intermediate", "advanced"]


def require_dir(path: Path, errors: list[str], label: str) -> None:
    if not path.is_dir():
        errors.append(f"Missing directory: {label} ({path})")


def require_file(path: Path, errors: list[str], label: str) -> None:
    if not path.is_file():
        errors.append(f"Missing file: {label} ({path})")


def require_md_files(path: Path, errors: list[str], label: str) -> None:
    if not path.is_dir():
        errors.append(f"Missing directory: {label} ({path})")
        return
    md_files = list(path.glob("*.md"))
    if not md_files:
        errors.append(f"Expected at least one .md file in {label} ({path})")


def check_language(root: Path, language: str, errors: list[str]) -> None:
    language_dir = root / "languages" / language
    require_dir(language_dir, errors, f"languages/{language}")
    require_file(language_dir / "CERTIFICATION.md", errors, f"{language} CERTIFICATION.md")

    levels = AI_LEVELS if language == AI_LANGUAGE else CORE_LEVELS
    for level in levels:
        level_dir = language_dir / level
        require_dir(level_dir, errors, f"{language}/{level}")
        require_md_files(level_dir / "modules", errors, f"{language}/{level}/modules")
        require_md_files(level_dir / "projects", errors, f"{language}/{level}/projects")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    require_dir(root / "scripts", errors, "scripts")
    require_file(
        root / ".github" / "workflows" / "curriculum-lint.yml",
        errors,
        "curriculum-lint workflow",
    )
    require_dir(root / "assessments" / "rubrics", errors, "assessments/rubrics")
    require_dir(root / "assessments" / "checklists", errors, "assessments/checklists")
    require_dir(
        root / "assessments" / "certifications",
        errors,
        "assessments/certifications",
    )
    require_dir(root / "languages", errors, "languages")

    for language in REQUIRED_LANGUAGES:
        check_language(root, language, errors)

    if errors:
        print("Curriculum lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Curriculum lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
