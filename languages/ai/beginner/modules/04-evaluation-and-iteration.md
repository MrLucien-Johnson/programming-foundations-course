# AI — Module 04: Evaluation and Iteration

## Overview
Treat prompt work like engineering: define metrics, build test cases, run regressions, and keep an iteration log.

**Included examples (tool-agnostic):**
- Customer support summarisation (quality rubric + regression set)

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
1) Define success metrics: accuracy, format adherence, coverage (45 min)
2) Build an eval set: represent real inputs + edge cases (45 min)
3) Regression testing: don't trade one failure for another (40 min)
4) Iteration discipline: one change at a time + notes (35 min)

## Exercises
### Core
- Create a rubric for summaries (factual, complete, actionable, tone).
- Build a 20-case regression set and score baseline vs improved prompt.

### Better
- Add “golden answers” for 5 cases and compare outputs qualitatively.
- Track failure categories and target the biggest ones first.

### Beast Mode
- Write a simple evaluation harness outline (inputs → outputs → scoring).
- Add confidence thresholds and fallback rules (ask question / abstain).

## Mini-Project
### Brief
Produce a small evaluation harness spec and a 20-case dataset for one task.

### Acceptance Criteria
- Dataset includes edge cases and at least 3 adversarial inputs.
- Rubric is clear enough that two people would score similarly.

## Testing Requirements
- Run evaluation after every change and keep results in an iteration log.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Only testing on “happy path” examples.
- No baseline—can't prove improvement.
- Changing prompt, temperature, and examples at once.

## Stretch Resources
- (Placeholder) Add links to evaluation best practices and datasets.
