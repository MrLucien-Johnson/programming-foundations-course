# AI — Module 05: Observability and Monitoring for LLM Apps

## Overview
Instrument AI systems: quality metrics, cost/latency, tracing, and alerts tied to user impact.

**Included examples (tool-agnostic):**
- Customer support summarisation (quality + safety monitoring)
- RAG Q&A (groundedness + abstention monitoring)

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
1) What to measure: quality, safety, cost, latency (50 min)
2) Logging and tracing: correlation IDs and privacy-safe logs (45 min)
3) Dashboards and alerting strategy (45 min)
4) Detecting regressions and drift in production (45 min)

## Exercises
### Core
- Define SLIs/SLOs for an AI feature and map them to metrics.
- Design a dashboard layout and alert thresholds.

### Better
- Add a “quality sampling” plan (privacy-safe) and escalation steps.
- Design tracing across steps (retrieval, generation, tools).

### Beast Mode
- Design an on-call playbook for “quality drop” and “cost spike” incidents.
- Add a canary evaluation that runs continuously.

## Mini-Project
### Brief
Create an observability plan and incident triggers for an LLM app.

### Acceptance Criteria
- Includes quality, safety, cost, and latency signals.

## Testing Requirements
- Monitoring validates fallbacks are working and not harming UX.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Logging sensitive user data without redaction.
- Alerting on everything (no signal-to-noise strategy).

## Stretch Resources
- (Placeholder) Add links to observability principles and monitoring patterns.
