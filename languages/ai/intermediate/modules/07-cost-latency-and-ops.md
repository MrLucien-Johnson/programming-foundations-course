# AI — Module 07: Cost, Latency, and Ops

## Overview
Plan and control cost/latency: budgets, caching, batching, and operational guardrails.

**Included examples (tool-agnostic):**
- Customer support summarisation (caching + routing)
- RAG Q&A (context trimming + abstention)

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
1) Define budgets: tokens/requests, latency SLOs, and guardrails (45 min)
2) Reduce cost: caching, summarization, and context trimming (45 min)
3) Reduce latency: parallel steps, smaller contexts, early exits (45 min)
4) Ops basics: logs, metrics, and alerts (40 min)

## Guided Walkthrough


Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/intermediate/starter-pack` into a new working folder.
2. Review the module goals and plan how you will optimize for cost and latency.
3. Measure baseline latency and token usage.
4. Apply one optimization and re-measure.
5. Document the tradeoffs.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack


Use the starter pack in `languages/ai/intermediate/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Create a cost/latency plan for one workflow (budgets + how to enforce).
- Define what happens when budgets are exceeded (fallback).

### Better
- Design a caching strategy and what cache keys should be.
- Add an “early exit” rule when confidence is low.

### Beast Mode
- Add a monitoring plan: what metrics, what dashboards, what alerts.
- Design a canary/rollback plan for prompt version releases.

## Mini-Project
### Brief
Write an ops plan for your AI feature: budgets, monitoring, and fallbacks.

### Acceptance Criteria
- Includes explicit budgets and a fallback strategy.
- Includes metrics to track quality, cost, and latency.

## Testing Requirements
- Evaluation harness records cost/latency per run (even estimated).

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

- Run the module tests and confirm they pass.
- Verify the primary feature works with normal and edge-case inputs.
- Update the README with setup, run, and test commands.

## Common Mistakes
- No budgets, leading to runaway cost.
- Optimizing for cost while silently harming quality.
- No observability—failures are invisible until users complain.

## Stretch Resources


- Latency optimization: https://platform.openai.com/docs/guides/latency-optimization
- Monitoring guide: https://opentelemetry.io/docs/

