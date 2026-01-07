# AI — Module 04: Model Evaluation and Testing

## Overview
Treat LLM work like software testing: datasets, baselines, regression tests, and quality gates.

**Included examples (tool-agnostic):**
- Customer support summarisation (rubric + regression set)
- Data extraction into JSON (schema validation as a test)

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
1) Define metrics: task success, format adherence, groundedness (45 min)
2) Build an eval harness: inputs → outputs → scoring (55 min)
3) Regression gates: prevent quality drift (45 min)
4) Human evaluation: rubrics and inter-rater consistency (40 min)

## Exercises
### Core
- Create an eval harness outline for one task and run it on 50 cases.
- Define pass/fail thresholds (e.g., 90% schema validity, 80% rubric score).

### Better
- Add adversarial cases (injection, contradictions) and track separate scores.
- Add a regression report format (what changed, what broke, why).

### Beast Mode
- Design A/B testing rules for prompt versions with rollback criteria.
- Add cost/latency metrics to the harness.

## Mini-Project
### Brief
Build a lightweight evaluation harness spec + dataset + reporting template.

### Acceptance Criteria
- Harness is repeatable and can be re-run after changes.
- Includes a regression gate and report format.

## Testing Requirements
- Evaluation run is deterministic where possible (fixed inputs, logged settings).

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- No baseline or thresholds—can't tell if you improved.
- Only measuring “vibes” instead of repeatable outcomes.
- Mixing data leakage into eval sets (training-like artifacts).

## Stretch Resources
- (Placeholder) Add links to evaluation methodologies and common metrics.
