# AI — Module 02: Prompting Basics

> **Voiceover lesson (with captions & transcript):** [AI Prompting basics](../../../../docs/tutorials.html#ai-prompting)

## Overview
Learn how to write prompts like specifications: define role, task, constraints, and output shape.

**Included examples (tool-agnostic):**
- Meeting notes → actions (notes → JSON actions with owners)
- Customer support summarisation (ticket → summary + sentiment + category)

## Learning Outcomes
- Write prompts with explicit constraints and output format.
- Separate instructions from user content with clear delimiters.
- Add few-shot examples that demonstrate the desired behavior.
- Handle missing info with clarify-or-refuse rules.
- Score outputs on format, factuality, and helpfulness.

## Prerequisites
- Comfort writing clear, structured English.
- Basic familiarity with APIs and JSON (helpful but not required in beginner).
- Willingness to iterate: you’ll run tests, record failures, and improve.

## Lessons
1) Prompt anatomy: context, task, constraints, and success criteria (45 min)
2) Few-shot examples: when to use them and how to keep them short (45 min)
3) Delimiters and quoting: making input boundaries explicit (35 min)
4) Asking for uncertainty: when to say “I don't know” (35 min)

## Guided Walkthrough
Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/beginner/starter-pack` into a new working folder.
2. Review the module goals and plan how you will create prompts with clarity, structure, and constraints.
3. Draft an initial prompt with role, task, input, and output format.
4. Add constraints (tone, length, refusal rules) and test against 5 cases.
5. Iterate once and document the improvement.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/ai/beginner/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Write prompts that produce consistent bullet summaries for 10 support tickets.
- Add explicit constraints: no invented policies; only use input text.

### Better
- Add a structured output request (headings or JSON fields) and test for compliance.
- Add a “clarify or refuse” rule when missing key info (e.g., no owner in notes).

### Beast Mode
- Create adversarial inputs (prompt injection attempts) and verify the prompt resists them.
- Define a scorecard (format adherence, factuality, helpfulness) and track results.

## Mini-Project
### Brief
Create a prompt pack for meeting-notes-to-actions with a repeatable test set.

### Acceptance Criteria
- Prompt includes clear constraints, output format, and at least 3 examples.
- Evaluation set includes messy notes and missing details.

## Testing Requirements
- Format compliance checked (manual or simple script).
- At least 1 negative test (should refuse or ask a question).

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Verification Checklist
Before moving on, confirm the following:

- You can restate the module goal in your own words.
- You have run at least one evaluation pass.
- You documented what improved and what did not.

## Common Mistakes
- Vague instructions like “be helpful” without constraints.
- No delimiter between instructions and user content.
- Overlong prompts that hide the essential rules.

## Stretch Resources

- Prompting guide: https://www.promptingguide.ai/
- OpenAI guides: https://platform.openai.com/docs/guides

