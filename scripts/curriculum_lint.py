#!/usr/bin/env python3
from pathlib import Path
import sys

# Configuration: update to match curriculum structure.
LANGUAGES = [
    "python",
    "csharp",
]

EXPECTED_MODULE_FILENAMES = [
    "module-01.md",
    "module-02.md",
    "module-03.md",
    "module-04.md",
    "module-05.md",
    "module-06.md",
    "module-07.md",
    "module-08.md",
]

REQUIRED_HEADINGS = [
    "Overview",
    "Learning Outcomes",
    "Prerequisites",
    "Lessons",
    "Exercises",
    "Mini-Project",
    "Testing Requirements",
    "Rubric",
    "Common Mistakes",
    "Stretch Resources",
]

LEVELS = ["intermediate", "advanced"]
REQUIRED_PROJECT_FILES = ["mini-project-1.md", "mini-project-2.md", "capstone.md"]


def extract_headings(markdown_text: str) -> list:
    headings = []
    in_code_block = False
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if not stripped.startswith("#"):
            continue
        hash_count = len(stripped) - len(stripped.lstrip("#"))
        if hash_count == 0:
            continue
        heading_text = stripped[hash_count:].strip()
        if not heading_text:
            continue
        while heading_text.endswith("#"):
            heading_text = heading_text[:-1].rstrip()
        if heading_text:
            headings.append(heading_text)
    return headings


def relative_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def check_headings(file_path: Path, root: Path, missing_headings, out_of_order):
    text = file_path.read_text(encoding="utf-8")
    headings = extract_headings(text)
    required_set = set(REQUIRED_HEADINGS)
    first_occurrence = {}
    for index, heading in enumerate(headings):
        if heading in required_set and heading not in first_occurrence:
            first_occurrence[heading] = index

    missing = [h for h in REQUIRED_HEADINGS if h not in first_occurrence]
    if missing:
        missing_headings.append(
            f"{relative_path(file_path, root)}: missing {', '.join(missing)}"
        )
        return

    actual_order = [
        heading
        for heading, _ in sorted(first_occurrence.items(), key=lambda item: item[1])
    ]
    if actual_order != REQUIRED_HEADINGS:
        out_of_order.append(
            f"{relative_path(file_path, root)}: expected {REQUIRED_HEADINGS}, found {actual_order}"
        )


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    languages_root = root / "languages"

    missing_files = []
    wrong_filenames = []
    missing_headings = []
    out_of_order = []

    for language in LANGUAGES:
        language_dir = languages_root / language
        for level in LEVELS:
            level_dir = language_dir / level
            if not level_dir.is_dir():
                missing_files.append(f"{relative_path(level_dir, root)}/ (directory)")
                continue

            readme_path = level_dir / "README.md"
            if not readme_path.is_file():
                missing_files.append(relative_path(readme_path, root))

            modules_dir = level_dir / "modules"
            module_files = []
            if not modules_dir.is_dir():
                missing_files.append(f"{relative_path(modules_dir, root)}/ (directory)")
            else:
                module_files = sorted(p.name for p in modules_dir.glob("*.md"))
                expected_set = set(EXPECTED_MODULE_FILENAMES)
                actual_set = set(module_files)
                for filename in sorted(expected_set - actual_set):
                    missing_files.append(
                        relative_path(modules_dir / filename, root)
                    )
                for filename in sorted(actual_set - expected_set):
                    wrong_filenames.append(
                        relative_path(modules_dir / filename, root)
                    )

            projects_dir = level_dir / "projects"
            if not projects_dir.is_dir():
                missing_files.append(f"{relative_path(projects_dir, root)}/ (directory)")
            else:
                for project_file in REQUIRED_PROJECT_FILES:
                    project_path = projects_dir / project_file
                    if not project_path.is_file():
                        missing_files.append(relative_path(project_path, root))

            if modules_dir.is_dir():
                for filename in module_files:
                    module_path = modules_dir / filename
                    if module_path.is_file():
                        check_headings(
                            module_path,
                            root,
                            missing_headings,
                            out_of_order,
                        )

    if missing_files or wrong_filenames or missing_headings or out_of_order:
        if missing_files:
            print("Missing files or directories:")
            for item in missing_files:
                print(f"  - {item}")
        if wrong_filenames:
            print("Wrong module filenames:")
            for item in wrong_filenames:
                print(f"  - {item}")
        if missing_headings:
            print("Missing required headings:")
            for item in missing_headings:
                print(f"  - {item}")
        if out_of_order:
            print("Headings out of order:")
            for item in out_of_order:
                print(f"  - {item}")
        print("Curriculum lint failed.")
        return 1

    print("Curriculum lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
