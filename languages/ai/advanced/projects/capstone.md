# AI Advanced — Capstone: Production-Ready LLM Application

## Overview
- **Goal**: Deliver a production-grade LLM system design + implementation prototype with operational evidence.
- **Expected effort**: 10–20 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- System design doc with scaling plan, reliability patterns, and security threat model.
- Evaluation harness (repeatable) with regression gates; includes scale/sampling plan.
- Safety checklist + red-team suite + mitigations; privacy/governance plan.
- Cost/latency plan with budgets, measurement approach, and optimization plan.
- Fallback strategy: degraded modes, human escalation, and rollback strategy.
- Observability plan: quality/cost/latency metrics, traces, and incident triggers.
- Production incident playbooks + at least one drill run.

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- Eval harness, safety suite, and drills must be runnable and produce reports.
- Regression gate thresholds are documented and enforced.

## Deliverables
- `README.md` with run steps and how to reproduce reports.
- Architecture + threat model + governance plan documents.
- Eval harness + datasets + reports.
- Safety suite + red-team results.
- Ops pack: budgets, monitoring, playbooks, and drill results.

## Suggested Run Steps
- Run evals, safety suite, and at least one drill; include reports in deliverables.
