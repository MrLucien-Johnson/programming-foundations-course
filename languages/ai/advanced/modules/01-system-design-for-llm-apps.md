# AI — Module 01: System Design for LLM Apps

## Overview
Design end-to-end LLM application architectures: data flows, boundaries, scaling, and safety constraints.

**Included examples (tool-agnostic):**
- RAG-based Q&A over docs (architecture and scaling plan)
- Agent workflow for multi-step task (bounded loops + tool isolation)

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
1) Requirements → constraints → architecture (55 min)
2) Components: retrieval, generation, tools, storage, and caching (55 min)
3) Multi-tenancy and data isolation (45 min)
4) Versioned prompts/evals as first-class artifacts (45 min)

## Exercises
### Core
- Create an architecture diagram and data flow for one LLM feature.
- Identify failure modes and propose fallbacks for each.

### Better
- Add scaling considerations: caching layers, queues, and backpressure.
- Define SLOs for latency and quality with error budgets.

### Beast Mode
- Design a migration plan for changing schemas/prompts with backward compatibility.
- Add a privacy-by-design plan (minimization, retention, access controls).

## Mini-Project
### Brief
Write a system design doc for a production LLM app with eval/safety/cost plans.

### Acceptance Criteria
- Includes architecture, eval harness plan, safety checklist, cost/latency plan, fallback strategy.

## Testing Requirements
- Design includes test strategy across unit/integration/e2e + eval gates.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Treating the model as a single black box without boundaries.
- No plan for scaling or failure, leading to outages/cost spikes.

## Stretch Resources
- (Placeholder) Add links to system design references for AI applications.
