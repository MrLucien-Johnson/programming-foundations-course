#!/usr/bin/env python3
"""Apply Codecademy-style skill quizzes to all language tracks."""

from __future__ import annotations

import copy
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from quiz_skill_banks import BANKS  # noqa: E402

LANG_DIRS = [
    "python",
    "csharp",
    "go",
    "java",
    "kotlin",
    "rust",
    "sql",
    "swift",
    "typescript",
    "ai",
]

# Language-specific tooling question injected into intermediate 02-testing-and-quality.
TOOLING_Q = {
    "python": {
        "lo": 5,
        "q": "In this course's Python tooling, which command runs lint checks?",
        "choices": [
            "`ruff check .`",
            "`ruff format .`",
            "`python -m pytest`",
            "`git push --force`",
        ],
        "answer": "A",
        "explain": "`ruff check .` lints; format and pytest are separate quality steps.",
    },
    "csharp": {
        "lo": 5,
        "q": "In this course's C# tooling, which command runs the test suite?",
        "choices": [
            "`dotnet test`",
            "`dotnet format`",
            "`git push --force`",
            "`docker system prune`",
        ],
        "answer": "A",
        "explain": "`dotnet test` runs the suite; format is a style gate, not the test runner.",
    },
    "go": {
        "lo": 5,
        "q": "In this course's Go tooling, which command runs the test suite?",
        "choices": [
            "`go test ./...`",
            "`go fmt ./...`",
            "`git push --force`",
            "`docker system prune`",
        ],
        "answer": "A",
        "explain": "`go test ./...` runs package tests across the module.",
    },
    "java": {
        "lo": 5,
        "q": "In this course's Java tooling, which command typically runs unit tests (Maven)?",
        "choices": [
            "`mvn test`",
            "`git push --force`",
            "`docker system prune`",
            "`curl localhost`",
        ],
        "answer": "A",
        "explain": "`mvn test` (or the Gradle equivalent) is the standard unit-test gate.",
    },
    "kotlin": {
        "lo": 5,
        "q": "In this course's Kotlin/Gradle tooling, which task runs unit tests?",
        "choices": [
            "`./gradlew test`",
            "`git push --force`",
            "`docker system prune`",
            "`curl localhost`",
        ],
        "answer": "A",
        "explain": "Gradle's `test` task runs the JUnit suite for the project.",
    },
    "rust": {
        "lo": 5,
        "q": "In this course's Rust tooling, which command runs the test suite?",
        "choices": [
            "`cargo test`",
            "`cargo clippy`",
            "`git push --force`",
            "`docker system prune`",
        ],
        "answer": "A",
        "explain": "`cargo test` runs tests; `clippy` is the lint gate.",
    },
    "sql": {
        "lo": 5,
        "q": "In this course's SQL tooling, which practice best acts as an automated quality gate?",
        "choices": [
            "Run migration + query validation / pgTAP (or equivalent) in CI",
            "`git push --force`",
            "Only format SQL by hand never in CI",
            "Skip EXPLAIN forever",
        ],
        "answer": "A",
        "explain": "SQL tracks rely on migration/query validation (and often pgTAP/sqlfluff) as gates.",
    },
    "swift": {
        "lo": 5,
        "q": "In this course's Swift tooling, which command runs the test suite?",
        "choices": [
            "`swift test`",
            "`git push --force`",
            "`docker system prune`",
            "`curl localhost`",
        ],
        "answer": "A",
        "explain": "`swift test` runs XCTest via SwiftPM.",
    },
    "typescript": {
        "lo": 5,
        "q": "In this course's TypeScript tooling, which command commonly runs unit tests?",
        "choices": [
            "`npm test` / `npx vitest` (or Jest)",
            "`git push --force`",
            "`docker system prune`",
            "`curl localhost`",
        ],
        "answer": "A",
        "explain": "Vitest/Jest via npm scripts is the usual unit-test gate; ESLint/Prettier are separate.",
    },
}


def bank_for(lang: str, level: str) -> dict:
    if (lang, level) in BANKS:
        return BANKS[(lang, level)]
    if ("*", level) in BANKS:
        return BANKS[("*", level)]
    raise KeyError(f"No bank for {lang}/{level}")


def letter(i: int) -> str:
    return "ABCD"[i]


def replace_outcomes(text: str, outcomes: list[str]) -> str:
    """Replace Learning Outcomes or Topics section with skill outcomes."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    replaced = False
    while i < len(lines):
        stripped = lines[i].strip()
        if not replaced and stripped in ("## Learning Outcomes", "## Topics"):
            out.append("## Learning Outcomes\n")
            for outcome in outcomes:
                out.append(f"- {outcome}\n")
            out.append("\n")
            i += 1
            while i < len(lines) and (
                lines[i].startswith("- ") or lines[i].strip() == ""
            ):
                if lines[i].startswith("## "):
                    break
                i += 1
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            replaced = True
            continue
        out.append(lines[i])
        i += 1
    if not replaced:
        # Insert after first heading block
        out = []
        i = 0
        inserted = False
        while i < len(lines):
            out.append(lines[i])
            if not inserted and lines[i].startswith("# "):
                # skip blank after title
                i += 1
                while i < len(lines) and lines[i].strip() == "":
                    out.append(lines[i])
                    i += 1
                out.append("## Learning Outcomes\n")
                for outcome in outcomes:
                    out.append(f"- {outcome}\n")
                out.append("\n")
                inserted = True
                continue
            i += 1
        return "".join(out)
    return "".join(out)


def quiz_title_from_lesson(lesson_text: str, slug: str) -> str:
    first = lesson_text.splitlines()[0].lstrip("# ").strip() if lesson_text else slug
    # Drop trailing emoji noise; keep module name
    return first


def render_quiz(title: str, meta: dict) -> str:
    lines = [
        f"# {title} Quiz: Test Your Understanding",
        "",
        "## Instructions",
        "",
        "Answer these questions about the skills in this module's learning outcomes.",
        "Try from memory first — then check the answers file for explanations.",
        "",
        "## Questions",
        "",
    ]
    for idx, item in enumerate(meta["questions"], start=1):
        lo = item["lo"]
        lines.append(f"### Question {idx}: {item['q']}")
        lines.append(f"**Checks outcome {lo}:** {meta['outcomes'][lo - 1]}")
        lines.append("")
        for c_i, choice in enumerate(item["choices"]):
            text = choice
            if len(choice) >= 3 and choice[0] in "ABCD" and choice[1:3] in (") ", ") "):
                text = choice[3:].lstrip()
            elif len(choice) >= 3 and choice[0] in "ABCD" and choice[1] == ")":
                text = choice[2:].lstrip()
            lines.append(f"{letter(c_i)}) {text}  ")
        lines.append("")
        lines.append("**Your answer:** _______________")
        lines.append("")
        lines.append("---")
        lines.append("")
    n = len(meta["questions"])
    almost = max(1, n - 2)
    lines.extend(
        [
            "## Check Your Answers",
            "",
            "Once you finish, check the answers file for explanations.",
            "",
            "## How Did You Do?",
            "",
            f"- **{n}/{n} correct:** Excellent — you can apply this module's outcomes.",
            f"- **{almost}-{n - 1} correct:** Strong — review the missed outcome(s).",
            f"- **0-{almost - 1} correct:** Revisit the lessons for those outcomes, then retry.",
            "",
            "---",
            "",
            "**Good luck!** Check your answers when you are ready.",
            "",
        ]
    )
    return "\n".join(lines)


def render_answers(title: str, meta: dict) -> str:
    lines = [f"# {title} Quiz Answers", ""]
    for idx, item in enumerate(meta["questions"], start=1):
        lo = item["lo"]
        ans = item["answer"]
        ans_i = "ABCD".index(ans)
        choice_text = item["choices"][ans_i]
        if len(choice_text) >= 3 and choice_text[0] in "ABCD" and choice_text[1] == ")":
            choice_text = choice_text[2:].lstrip()
        lines.append(f"## Question {idx}: {item['q']}")
        lines.append(f"**Answer: {ans}** — {choice_text}")
        lines.append("")
        lines.append(f"**Outcome {lo}:** {meta['outcomes'][lo - 1]}")
        lines.append("")
        lines.append(f"**Explanation:** {item['explain']}")
        lines.append("")
        lines.append("---")
        lines.append("")
    n = len(meta["questions"])
    almost = max(1, n - 2)
    lines.extend(
        [
            "## How Did You Do?",
            "",
            f"- **{n}/{n} correct:** Excellent! You are ready to move on.",
            f"- **{almost}-{n - 1} correct:** Great work — review the missed outcomes.",
            f"- **0-{almost - 1} correct:** Revisit the module lessons, then try again.",
            "",
        ]
    )
    return "\n".join(lines)


def render_alignment(lang: str, level: str, bank: dict) -> str:
    lines = [
        f"# {lang} / {level} — Quiz Alignment Sheet",
        "",
        "Codecademy-style mapping: each learning outcome is tested by at least one quiz item.",
        "",
        f"Track: `languages/{lang}/{level}/modules/`",
        "",
    ]
    for slug, meta in bank.items():
        lines.append(f"## {slug}")
        lines.append("")
        lines.append("| Outcome | Quiz questions |")
        lines.append("|---|---|")
        buckets: dict[int, list[int]] = {i + 1: [] for i in range(len(meta["outcomes"]))}
        for qi, item in enumerate(meta["questions"], start=1):
            buckets[item["lo"]].append(qi)
        for i, outcome in enumerate(meta["outcomes"], start=1):
            qs = ", ".join(f"Q{n}" for n in buckets[i]) or "—"
            lines.append(f"| LO{i}: {outcome} | {qs} |")
        lines.append("")
    return "\n".join(lines)


def prepare_meta(lang: str, level: str, slug: str, meta: dict) -> dict:
    prepared = copy.deepcopy(meta)
    if (
        lang != "ai"
        and level == "intermediate"
        and slug == "02-testing-and-quality"
        and lang in TOOLING_Q
    ):
        # Ensure outcome 5 exists for tooling LO
        if len(prepared["outcomes"]) < 5:
            prepared["outcomes"].append(
                "Use lint, format, and typecheck (or language-equivalent gates) as automated quality gates."
            )
        prepared["questions"].append(TOOLING_Q[lang])
    return prepared


def process_track(lang: str, level: str) -> tuple[int, int]:
    mod_dir = ROOT / "languages" / lang / level / "modules"
    if not mod_dir.is_dir():
        return 0, 0
    try:
        bank = bank_for(lang, level)
    except KeyError:
        return 0, 0

    updated = 0
    missing = 0
    applied: dict[str, dict] = {}

    for slug, meta in bank.items():
        lesson = mod_dir / f"{slug}.md"
        quiz = mod_dir / f"{slug}.quiz.md"
        answers = mod_dir / f"{slug}.quiz-answers.md"
        if not lesson.exists():
            print(f"  SKIP missing lesson {lang}/{level}/{slug}")
            missing += 1
            continue
        prepared = prepare_meta(lang, level, slug, meta)
        # validate coverage
        covered = {q["lo"] for q in prepared["questions"]}
        needed = set(range(1, len(prepared["outcomes"]) + 1))
        if needed - covered:
            print(f"  WARN incomplete coverage {lang}/{level}/{slug}: {needed - covered}")

        lesson_text = lesson.read_text(encoding="utf-8")
        new_lesson = replace_outcomes(lesson_text, prepared["outcomes"])
        lesson.write_text(new_lesson, encoding="utf-8", newline="\n")

        title = quiz_title_from_lesson(lesson_text, slug)
        quiz.write_text(render_quiz(title, prepared), encoding="utf-8", newline="\n")
        answers.write_text(render_answers(title, prepared), encoding="utf-8", newline="\n")
        applied[slug] = prepared
        updated += 1

    if applied:
        sheet = ROOT / "languages" / lang / level / "QUIZ-ALIGNMENT.md"
        sheet.write_text(
            render_alignment(lang, level, applied), encoding="utf-8", newline="\n"
        )
    return updated, missing


def main() -> None:
    total_u = total_m = 0
    for lang in LANG_DIRS:
        levels = ["beginner", "intermediate", "advanced"] if lang == "ai" else ["intermediate", "advanced"]
        for level in levels:
            u, m = process_track(lang, level)
            if u or m:
                print(f"{lang}/{level}: updated={u} missing={m}")
            total_u += u
            total_m += m
    print(f"DONE updated={total_u} missing={total_m}")


if __name__ == "__main__":
    main()
