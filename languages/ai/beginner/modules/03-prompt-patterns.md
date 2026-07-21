# AI — Module 03: Prompt Patterns

## Overview
Use reusable prompt patterns to improve reliability: checklists, decomposition, critique, and verification.

**Included examples (tool-agnostic):**
- Data extraction into JSON (free text → structured fields)

## Learning Outcomes
- Design extraction prompts that emit valid structured fields.
- Specify required-field checklists and missing-data behavior.
- Add a review/repair pass that fixes structure without inventing facts.
- Build an error taxonomy and track reductions across iterations.
- Cover tricky cases with targeted few-shot examples.

## Prerequisites
- Comfort writing clear, structured English.
- Basic familiarity with APIs and JSON (helpful but not required in beginner).
- Willingness to iterate: you’ll run tests, record failures, and improve.

## Lessons
1) Decomposition: break tasks into steps without leaking chain-of-thought (45 min)
2) Checklist pattern: “must include” fields + validation hints (40 min)
3) Critique-and-revise: separate drafting from review (45 min)
4) Self-consistency: multiple drafts + choose best via rubric (40 min)

## Guided Walkthrough
Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/beginner/starter-pack` into a new working folder.
2. Review the module goals and plan how you will apply prompt patterns to improve reliability.
3. Select two prompt patterns and apply them to the same task.
4. Compare outputs side by side and pick the best pattern.
5. Document why the winning pattern works better.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/ai/beginner/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Design a JSON extraction prompt for customer emails (name, account, issue, urgency).
- Add a checklist of required fields and what to do if missing.

### Better
- Add a second “review” pass that flags missing fields or contradictions.
- Add examples for tricky cases (multiple issues, sarcasm, non-English fragments).

### Beast Mode
- Implement a “repair” prompt: fix invalid JSON into valid JSON without changing meaning.
- Create a small error taxonomy and track reductions across iterations.

## Mini-Project
### Brief
Build an “extract → validate → repair” workflow for JSON extraction.

### Acceptance Criteria
- Produces valid JSON for at least 90% of the evaluation set.
- Documents how missing/ambiguous fields are handled.

## Testing Requirements
- A validator (even manual) checks JSON validity and required fields.
- Re-run after changes and record deltas.

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
- Asking for JSON but not specifying schema/required fields.
- Ignoring ambiguity and forcing made-up values.
- No repair strategy for invalid outputs.

## Stretch Resources

- [Prompting Guide](guide-viewer.html?path=guides/prompting-guide.md) — pattern table and examples
- [Practical AI Workflows](guide-viewer.html?path=guides/practical-ai.md) — critique-and-revise loops
- Browse all docs in [Guides](guides.html)
