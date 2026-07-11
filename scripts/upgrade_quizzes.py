#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import random
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

LIST_ITEM_RE = re.compile(r"^\s*(?:-|\*|\d+\))\s+(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


@dataclass
class Question:
    prompt: str
    options: list[str]
    correct_index: int
    explanation: str
    kind: str


CORE_TEMPLATES = [
    "You're preparing a submission and need to meet the Core bar. Which action is required?",
    "To satisfy the Core requirements, which step must be included?",
    "A reviewer checks the Core checklist. Which action should they see?",
    "Which task best matches the Core expectations for this module?",
    "Your goal is to meet the minimum passing bar. Which action fulfills the Core criteria?",
    "Which step would keep the work within the Core scope?",
]

BETTER_TEMPLATES = [
    "You already met Core. Which action qualifies as a Better upgrade?",
    "Which improvement moves a Core submission to the Better tier?",
    "Which option is listed under Better work for this module?",
    "Which enhancement is a Better-level upgrade (not Beast Mode)?",
    "To earn a Better evaluation, which action should you add?",
    "Which step is explicitly called out as Better work?",
]

BEAST_TEMPLATES = [
    "Which action pushes the work into Beast Mode?",
    "Which task is explicitly listed as a Beast Mode upgrade?",
    "To reach Beast Mode, which improvement should you choose?",
    "Which option represents a Beast Mode enhancement?",
    "Which action qualifies as a Beast Mode stretch?",
]

ACCEPTANCE_TEMPLATES = [
    "Which requirement is part of the mini-project acceptance criteria?",
    "Your project passes review only if which condition is true?",
    "Which item is explicitly required in the acceptance criteria?",
    "Which acceptance criterion must be satisfied before submission?",
    "A reviewer approves the mini-project when which condition is met?",
]

TESTING_TEMPLATES = [
    "CI is failing because {issue}. Which testing requirement addresses this?",
    "A reviewer flags {issue}. Which testing requirement resolves it?",
    "Your tests are blocked by {issue}. Which requirement should you enforce?",
    "Which testing requirement is most relevant to this issue: {issue}?",
    "Which testing requirement should you apply given this issue: {issue}?",
]

TESTING_GENERIC_TEMPLATES = [
    "Which testing requirement must be satisfied before submission?",
    "Which requirement belongs in the testing checklist for this module?",
    "Which testing requirement should be verified in CI for this module?",
]

MISTAKE_TEMPLATES = [
    "A reviewer reports: {issue}. Which mistake does this reflect?",
    "Your teammate says: {issue}. Which common mistake is this?",
    "Which common mistake matches this scenario: {issue}?",
    "This happened during review: {issue}. Which mistake is it?",
]

MISTAKE_GENERIC_TEMPLATES = [
    "Which behavior is listed as a common mistake for this module?",
    "Which option represents a common mistake to avoid?",
]

OUTCOME_TEMPLATES = [
    "A reviewer asks what capability you demonstrated. Which outcome matches?",
    "Which outcome should you be able to show after finishing this module?",
    "Which statement is one of the learning outcomes for this module?",
]

TOPIC_TEMPLATES = [
    "Which topic is covered in this module?",
    "Which topic belongs to this module's outline?",
    "A learner asks what you'll study next. Which topic fits?",
    "Which topic appears in this module?",
    "Which topic is included in this module's Topics list?",
    "Which topic would you expect in this module?",
    "Which topic is called out in this module?",
    "Which topic is part of the module's coverage?",
    "Which topic is on the module outline?",
    "Which topic would you highlight when describing this module?",
]

DELIVERABLE_TEMPLATES = [
    "Which deliverable should you produce for this module?",
    "Which output is listed as a required deliverable?",
    "Which deliverable would satisfy the module expectations?",
    "A reviewer expects which deliverable from this module?",
    "Which deliverable is explicitly listed for this module?",
    "Which deliverable would you submit to complete this module?",
    "Which deliverable belongs to this module's expectations?",
    "Which deliverable is required before moving on?",
]


def _normalize_heading(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


def _clean_item(text: str) -> str:
    cleaned = text.strip()
    cleaned = cleaned.replace("**", "")
    cleaned = cleaned.replace("__", "")
    cleaned = cleaned.replace("`", "")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def _parse_module(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {
        "outcomes": [],
        "lessons": [],
        "core": [],
        "better": [],
        "beast": [],
        "acceptance": [],
        "testing": [],
        "mistakes": [],
        "topics": [],
        "deliverables": [],
    }

    current_h2 = ""
    current_h3 = ""

    for line in text.splitlines():
        heading_match = HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            if level == 2:
                current_h2 = _normalize_heading(title)
                current_h3 = ""
            elif level == 3:
                current_h3 = _normalize_heading(title)
            continue

        item_match = LIST_ITEM_RE.match(line)
        if not item_match:
            continue

        item = _clean_item(item_match.group(1))
        if not item:
            continue

        if current_h2 == "learning-outcomes":
            sections["outcomes"].append(item)
        elif current_h2 == "lessons":
            sections["lessons"].append(item)
        elif current_h2 == "exercises":
            if current_h3 == "core":
                sections["core"].append(item)
            elif current_h3 == "better":
                sections["better"].append(item)
            elif current_h3 == "beast-mode":
                sections["beast"].append(item)
        elif current_h2 == "mini-project" and current_h3 == "acceptance-criteria":
            sections["acceptance"].append(item)
        elif current_h2 == "testing-requirements":
            sections["testing"].append(item)
        elif current_h2 == "common-mistakes":
            sections["mistakes"].append(item)
        elif current_h2 == "topics":
            sections["topics"].append(item)
        elif current_h2 == "deliverables":
            sections["deliverables"].append(item)

    return sections


def _stable_seed(value: str) -> int:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return int(digest[:8], 16)


def _unique_items(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def _select_item(items: list[str], rng: random.Random, used: set[str]) -> str | None:
    available = [item for item in items if item not in used]
    if not available:
        return None
    choice = rng.choice(available)
    used.add(choice)
    return choice


def _select_items(
    items: list[str], count: int, rng: random.Random, used: set[str]
) -> list[str]:
    if not items or count <= 0:
        return []
    chosen: list[str] = []
    for _ in range(count):
        item = _select_item(items, rng, used)
        if item:
            chosen.append(item)
        else:
            chosen.append(rng.choice(items))
    return chosen


def _build_options(
    answer: str,
    pools: list[list[str]],
    rng: random.Random,
    max_generic: int = 1,
) -> tuple[list[str], int]:
    generic = [
        "Skip testing and trust the first result.",
        "Ignore error handling for edge cases.",
        "Ship changes without documentation.",
        "Avoid measuring results or performance.",
        "Change multiple variables at once so you cannot compare outcomes.",
        "Jump to the next module without verifying results.",
        "Treat every request as safe without review.",
    ]

    candidates: list[str] = []
    for pool in pools:
        candidates.extend(pool)
    candidates = _unique_items([item for item in candidates if item != answer])
    rng.shuffle(candidates)

    options = [answer]
    for candidate in candidates:
        if len(options) >= 4:
            break
        options.append(candidate)

    if len(options) < 4 and max_generic > 0:
        for candidate in generic:
            if len(options) >= 4:
                break
            if candidate not in options:
                options.append(candidate)

    if len(options) < 4:
        filler = [item for item in candidates if item not in options]
        for candidate in filler:
            if len(options) >= 4:
                break
            options.append(candidate)

    rng.shuffle(options)
    correct_index = options.index(answer)
    return options, correct_index


def _choose_template(
    templates: list[str], used_prompts: set[str], rng: random.Random
) -> str:
    shuffled = templates[:]
    rng.shuffle(shuffled)
    for template in shuffled:
        if template not in used_prompts:
            used_prompts.add(template)
            return template
    template = shuffled[0]
    used_prompts.add(template)
    return template


def _testing_issue(requirement: str) -> str | None:
    lowered = requirement.lower()
    if "flake" in lowered or "deterministic" in lowered:
        return "tests are flaky and fail intermittently"
    if "isolated" in lowered or "schema" in lowered or "database" in lowered:
        return "database tests are polluting shared data"
    if "lint" in lowered or "format" in lowered or "typecheck" in lowered:
        return "lint/format/type errors are breaking CI"
    if "integration" in lowered:
        return "feature tests fail when hitting real boundaries"
    if "unit test" in lowered:
        return "a reviewer wants proof of correctness and regressions"
    return None


def _mistake_issue(mistake: str) -> str | None:
    lowered = mistake.lower()
    if "(" in mistake and ")" in mistake:
        detail = mistake.split("(", 1)[1].rsplit(")", 1)[0].strip()
        return detail
    if "over-mocking" in lowered:
        return "tests assert implementation details instead of outcomes"
    if "input validation" in lowered:
        return "bugs appear on unexpected inputs because validation was skipped"
    if "automated test" in lowered:
        return "CI has no automated test run before release"
    if "performance" in lowered and "measure" in lowered:
        return "a performance claim was made without benchmarks"
    if "happy path" in lowered:
        return "only happy-path cases were tested"
    return None


def _format_issue(issue: str) -> str:
    return issue.strip().rstrip(".")


def _build_question(
    kind: str,
    prompt: str,
    answer: str,
    pools: list[list[str]],
    rng: random.Random,
    explanation: str,
) -> Question:
    options, correct_index = _build_options(answer, pools, rng)
    return Question(
        prompt=prompt,
        options=options,
        correct_index=correct_index,
        explanation=explanation,
        kind=kind,
    )


def _build_questions(
    title: str, sections: dict[str, list[str]], rng: random.Random
) -> list[Question]:
    used_prompts: set[str] = set()
    used_items: dict[str, set[str]] = {
        key: set() for key in sections.keys()
    }

    questions: list[Question] = []

    def select(kind: str, count: int) -> list[str]:
        items = sections.get(kind, [])
        return _select_items(items, count, rng, used_items[kind])

    plan = [
        ("core", 2),
        ("better", 2),
        ("beast", 1),
        ("acceptance", 2),
        ("testing", 2),
        ("mistakes", 1),
    ]

    chosen: dict[str, list[str]] = {kind: select(kind, count) for kind, count in plan}
    total = sum(len(items) for items in chosen.values())
    target = 10

    if total < target:
        fallback_order = [
            "core",
            "acceptance",
            "better",
            "beast",
            "testing",
            "mistakes",
            "topics",
            "deliverables",
            "outcomes",
        ]
        while total < target:
            added = False
            for kind in fallback_order:
                item = _select_item(sections.get(kind, []), rng, used_items[kind])
                if item:
                    chosen.setdefault(kind, []).append(item)
                    total += 1
                    added = True
                    if total >= target:
                        break
            if not added:
                break

    if total < target and sections["outcomes"]:
        outcomes = sections["outcomes"]
        for _ in range(target - total):
            item = _select_item(outcomes, rng, used_items["outcomes"])
            if item:
                chosen.setdefault("outcomes", []).append(item)
                total += 1
                if total >= target:
                    break

    if total < target:
        refill_kinds = [
            kind
            for kind in [
                "core",
                "better",
                "beast",
                "acceptance",
                "testing",
                "mistakes",
                "topics",
                "deliverables",
                "outcomes",
            ]
            if sections.get(kind)
        ]
        if refill_kinds:
            while total < target:
                kind = rng.choice(refill_kinds)
                chosen.setdefault(kind, []).append(rng.choice(sections[kind]))
                total += 1

    def pools_for(kind: str) -> list[list[str]]:
        return [
            sections.get(other, [])
            for other in [
                "core",
                "better",
                "beast",
                "acceptance",
                "testing",
                "mistakes",
                "topics",
                "deliverables",
                "outcomes",
            ]
            if other != kind
        ]

    for answer in chosen.get("core", []):
        prompt = _choose_template(CORE_TEMPLATES, used_prompts, rng)
        explanation = "This action is listed under the Core exercises for the module."
        questions.append(
            _build_question(
                "core",
                prompt,
                answer,
                pools_for("core"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("better", []):
        prompt = _choose_template(BETTER_TEMPLATES, used_prompts, rng)
        explanation = "This is explicitly listed in the Better exercises section."
        questions.append(
            _build_question(
                "better",
                prompt,
                answer,
                pools_for("better"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("beast", []):
        prompt = _choose_template(BEAST_TEMPLATES, used_prompts, rng)
        explanation = "This action is part of the Beast Mode upgrades."
        questions.append(
            _build_question(
                "beast",
                prompt,
                answer,
                pools_for("beast"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("acceptance", []):
        prompt = _choose_template(ACCEPTANCE_TEMPLATES, used_prompts, rng)
        explanation = "This requirement appears in the mini-project acceptance criteria."
        questions.append(
            _build_question(
                "acceptance",
                prompt,
                answer,
                pools_for("acceptance"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("testing", []):
        issue = _testing_issue(answer)
        if issue:
            issue = _format_issue(issue)
            template = _choose_template(TESTING_TEMPLATES, used_prompts, rng)
            prompt = template.format(issue=issue)
        else:
            prompt = _choose_template(TESTING_GENERIC_TEMPLATES, used_prompts, rng)
        explanation = "This requirement appears in the Testing Requirements section."
        questions.append(
            _build_question(
                "testing",
                prompt,
                answer,
                pools_for("testing"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("mistakes", []):
        issue = _mistake_issue(answer)
        if issue:
            issue = _format_issue(issue)
            template = _choose_template(MISTAKE_TEMPLATES, used_prompts, rng)
            prompt = template.format(issue=issue)
        else:
            prompt = _choose_template(MISTAKE_GENERIC_TEMPLATES, used_prompts, rng)
        explanation = "This is listed in the Common Mistakes section to avoid."
        questions.append(
            _build_question(
                "mistake",
                prompt,
                answer,
                pools_for("mistakes"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("outcomes", []):
        prompt = _choose_template(OUTCOME_TEMPLATES, used_prompts, rng)
        explanation = "This statement appears in the Learning Outcomes section."
        questions.append(
            _build_question(
                "outcome",
                prompt,
                answer,
                pools_for("outcomes"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("topics", []):
        prompt = _choose_template(TOPIC_TEMPLATES, used_prompts, rng)
        explanation = "This topic is listed in the module outline."
        questions.append(
            _build_question(
                "topic",
                prompt,
                answer,
                pools_for("topics"),
                rng,
                explanation,
            )
        )

    for answer in chosen.get("deliverables", []):
        prompt = _choose_template(DELIVERABLE_TEMPLATES, used_prompts, rng)
        explanation = "This deliverable is required in the module expectations."
        questions.append(
            _build_question(
                "deliverable",
                prompt,
                answer,
                pools_for("deliverables"),
                rng,
                explanation,
            )
        )

    rng.shuffle(questions)
    return questions[:10]


def _format_quiz(title: str, questions: list[Question]) -> str:
    lines = [
        f"# {title} Quiz: Test Your Understanding",
        "",
        "## 📝 Instructions",
        "",
        "Answer these questions about what you learned. Try to answer from memory first!",
        "",
        "## 🧪 Questions",
        "",
    ]
    for index, question in enumerate(questions, start=1):
        lines.append(f"### Question {index}: {question.prompt}")
        for opt_index, option in enumerate(question.options):
            letter = chr(ord("A") + opt_index)
            lines.append(f"{letter}) {option}")
        lines.append("")
        lines.append("**Your answer:** _______________")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.extend(
        [
            "## ✅ Check Your Answers",
            "",
            "Once you finish, check the answers file for explanations.",
            "",
            "## 🎯 How Did You Do?",
            "",
            "- **10/10 correct:** Excellent! You understand the module well. 🎉",
            "- **8-9/10 correct:** Great work! Review the ones you missed.",
            "- **0-7/10 correct:** Review the module and try again. 💪",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def _format_answers(title: str, questions: list[Question]) -> str:
    lines = [f"# {title} Quiz Answers", ""]
    for index, question in enumerate(questions, start=1):
        lines.append(f"## Question {index}: {question.prompt}")
        letter = chr(ord("A") + question.correct_index)
        correct_text = question.options[question.correct_index]
        lines.append(f"**Answer: {letter}** - {correct_text}")
        lines.append("")
        lines.append(f"**Explanation:** {question.explanation}")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.extend(
        [
            "## 🎯 How Did You Do?",
            "",
            "- **10/10 correct:** Excellent! You are ready to move on.",
            "- **8-9/10 correct:** Good work! Review the missed concepts.",
            "- **0-7/10 correct:** Review the module and try again.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def _module_title(text: str, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def main() -> int:
    module_paths = sorted(
        {
            path
            for path in list(ROOT.glob("languages/*/intermediate/modules/*.md"))
            + list(ROOT.glob("languages/*/advanced/modules/*.md"))
            if ".quiz" not in path.name
        }
    )
    if not module_paths:
        raise SystemExit("No modules found to process.")

    for module_path in module_paths:
        text = module_path.read_text(encoding="utf-8")
        title = _module_title(text, module_path)
        sections = _parse_module(text)
        seed = _stable_seed(str(module_path.relative_to(ROOT)))
        rng = random.Random(seed)

        questions = _build_questions(title, sections, rng)
        if len(questions) < 10:
            raise SystemExit(f"Failed to build enough questions for {module_path}")

        quiz_path = module_path.with_name(f"{module_path.stem}.quiz.md")
        answers_path = module_path.with_name(f"{module_path.stem}.quiz-answers.md")

        quiz_path.write_text(_format_quiz(title, questions), encoding="utf-8")
        answers_path.write_text(_format_answers(title, questions), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
