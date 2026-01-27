# AI — Module 03: Evals at Scale

## Overview
Run evaluations reliably at scale: datasets, sampling, automation, and CI gating.

**Included examples (tool-agnostic):**
- Customer support summarisation (large eval sets + drift checks)
- JSON extraction (schema + rule-based checks as scalable evals)

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
1) Eval architecture: datasets, runners, scoring, reporting (55 min)
2) Sampling strategies and drift detection (45 min)
3) Human evaluation at scale: rubrics + calibration (45 min)
4) CI integration: gates, baselines, and rollback triggers (45 min)

## Exercises
### Core
- Design a scalable eval runner spec (batching, retries, budgets).
- Define a drift metric and a monitoring cadence.

### Better
- Add stratified sampling (by category, language, customer tier).
- Define “stop-the-line” criteria for regressions.

### Beast Mode
- Add shadow evaluation for live traffic (privacy-safe).
- Design a labeling workflow and calibration plan for human raters.

## Mini-Project
### Brief
Write an eval-at-scale plan for a production AI feature.

### Acceptance Criteria
- Includes datasets, automation, gates, budgets, and rollback criteria.

## Testing Requirements
- Runs are reproducible: versioned prompts, datasets, and scoring rules.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Relying only on live user feedback instead of proactive evals.
- No budget controls for large eval runs.

## Stretch Resources
- (Placeholder) Add links to evaluation frameworks and best practices.
