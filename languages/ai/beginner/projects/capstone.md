# AI Beginner — Capstone: Practical AI Workflow Pack

## Overview
- **Goal**: Deliver a small, end-to-end AI workflow that is testable, safe, and cost-aware.
- **Expected effort**: 3–5 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- Includes at least **two** workflows: (1) summarization, (2) structured extraction.
- Evaluation harness with datasets (≥50 total cases) and pass/fail thresholds.
- Safety checklist + red-team dataset (≥20 adversarial cases).
- Cost/latency plan with budgets and a method to estimate/track usage.
- Fallback strategy for: low confidence, missing evidence, tool errors (if any).
- Clear documentation and prompt/versioning strategy.

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- Eval harness must be runnable and produce a report.
- Safety tests must be runnable and produce pass/fail outcomes.

## Deliverables
- `README.md` with clear run steps and how to reproduce results.
- `eval/` datasets, scoring, and a summary report.
- `safety/` checklist + red-team prompts + mitigations.
- `ops/` cost/latency plan + fallback strategy.

## Suggested Run Steps
- Run eval harness and safety tests; iterate until thresholds are met.
