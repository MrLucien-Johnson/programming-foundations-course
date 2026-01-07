# AI — Module 03: Prompt Patterns

## Overview
Use reusable prompt patterns to improve reliability: checklists, decomposition, critique, and verification.

**Included examples (tool-agnostic):**
- Data extraction into JSON (free text → structured fields)

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
1) Decomposition: break tasks into steps without leaking chain-of-thought (45 min)
2) Checklist pattern: “must include” fields + validation hints (40 min)
3) Critique-and-revise: separate drafting from review (45 min)
4) Self-consistency: multiple drafts + choose best via rubric (40 min)

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


## Common Mistakes
- Asking for JSON but not specifying schema/required fields.
- Ignoring ambiguity and forcing made-up values.
- No repair strategy for invalid outputs.

## Stretch Resources
- (Placeholder) Add links to structured prompting and validation patterns.
