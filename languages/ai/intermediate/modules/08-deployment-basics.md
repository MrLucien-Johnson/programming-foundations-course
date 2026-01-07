# AI — Module 08: Deployment Basics

## Overview
Ship an AI feature safely: config, versioning, rollout, and operational readiness.

**Included examples (tool-agnostic):**
- RAG Q&A (deployment checklist + eval gate)
- Data extraction JSON (schema/versioning in rollout)

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
1) Environments: dev/stage/prod configs and secrets handling (45 min)
2) Versioning: prompts, schemas, and datasets (45 min)
3) Rollouts: canary, feature flags, and rollback criteria (45 min)
4) CI checks: eval gates, safety tests, and smoke tests (40 min)

## Exercises
### Core
- Create a deployment checklist for one AI feature.
- Define rollback criteria based on eval results and user-impact signals.

### Better
- Design a prompt versioning scheme and a change log format.
- Add a smoke test plan for your most important flows.

### Beast Mode
- Design a staged rollout with shadow evaluation and a rollback trigger.
- Add an incident response “first 30 minutes” checklist.

## Mini-Project
### Brief
Produce a deploy plan for an AI feature including evaluation + safety gates.

### Acceptance Criteria
- Includes release strategy, evaluation gate, and rollback plan.
- Includes safe config/secrets practices.

## Testing Requirements
- Pre-deploy: run eval harness + safety tests; post-deploy: run smoke tests.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Deploying prompt changes without a version or rollback strategy.
- No staging environment or test dataset.
- No plan for incidents or user-reported failures.

## Stretch Resources
- (Placeholder) Add links to release strategies and safe deployment playbooks.
