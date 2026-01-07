# AI Intermediate — Mini Project 1: JSON Extraction Pipeline

## Overview
- **Goal**: Extract structured JSON from messy customer communications with validation + repair.
- **Expected effort**: 2–3 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- JSON schema with required fields + null handling rules.
- Validation + repair loop with capped attempts.
- Evaluation harness: schema validity and field completeness metrics.
- Safety checklist for sensitive data + injection attempts.
- Cost/latency plan: budgets, caching/early exits if applicable.
- Fallback strategy when validation fails repeatedly (abstain / human review).

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- Automated schema validation and report generation.
- Regression gate: fail if validity/completeness drops below threshold.

## Deliverables
- `schema/` with documented schema and versions.
- `eval/` dataset (≥50) + metrics report.
- `prompts/` versioned prompts + change log.

## Suggested Run Steps
- Run evaluation and produce a report; demonstrate at least 2 iterations with improvements.
