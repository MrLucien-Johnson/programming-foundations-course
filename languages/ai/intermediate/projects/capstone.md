# AI Intermediate — Capstone: End-to-End LLM Feature (RAG + Guardrails)

## Overview
- **Goal**: Ship a production-leaning LLM feature: structured outputs, RAG, guardrails, and ops discipline.
- **Expected effort**: 5–10 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- One primary feature (choose one): support assistant, meeting action extractor, or doc Q&A.
- Evaluation harness with datasets and regression gates.
- Safety checklist + red-team suite + mitigation notes.
- Cost/latency plan with budgets and measured estimates.
- Fallback strategy: degraded mode + human escalation path.
- Prompt/schema/versioning strategy documented.

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- CI-like gate: evaluation + safety suite must pass before “release”.

## Deliverables
- `README.md` with run steps, architecture overview, and how to rerun evals.
- `eval/` runner + datasets + report output.
- `safety/` checklist + red-team prompts + results.
- `ops/` cost/latency plan + fallback strategy + monitoring plan.

## Suggested Run Steps
- Run eval + safety tests and attach reports as outputs.
