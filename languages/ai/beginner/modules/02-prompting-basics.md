# AI — Module 02: Prompting Basics

## Overview
Learn how to write prompts like specifications: define role, task, constraints, and output shape.

**Included examples (tool-agnostic):**
- Meeting notes → actions (notes → JSON actions with owners)
- Customer support summarisation (ticket → summary + sentiment + category)

## Learning Outcomes
- Translate a vague request into a clear goal, constraints, and success criteria.
- Produce prompts/specs that are repeatable (not “one-off magic prompts”).
- Build a small evaluation loop: test cases, metrics, and iteration notes.
- Apply safety and policy basics: refuse/redirect, handle sensitive data, reduce hallucinations.
- Document and version changes so improvements are explainable.

## Prerequisites
- Comfort writing clear, structured English.
- Basic familiarity with APIs and JSON (helpful but not required in beginner).
- Willingness to iterate: you’ll run tests, record failures, and improve.

## Lessons
1) Prompt anatomy: context, task, constraints, and success criteria (45 min)
2) Few-shot examples: when to use them and how to keep them short (45 min)
3) Delimiters and quoting: making input boundaries explicit (35 min)
4) Asking for uncertainty: when to say “I don't know” (35 min)

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


## Common Mistakes
- Vague instructions like “be helpful” without constraints.
- No delimiter between instructions and user content.
- Overlong prompts that hide the essential rules.

## Stretch Resources
- (Placeholder) Add a short guide on prompt structure patterns.
