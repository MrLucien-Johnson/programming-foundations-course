# AI Beginner — Mini Project 2: Meeting Notes → Actions

## Overview
- **Goal**: Convert meeting notes into action items with owners, due dates (if present), and follow-ups.
- **Expected effort**: 1–2 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- Outputs a structured format (table or JSON).
- Evaluation harness includes messy notes and missing owner/date cases.
- Safety checklist: avoid inventing owners/dates; ask clarifying questions.
- Cost/latency plan with a token/time budget.
- Fallback strategy for missing data (ask/abstain/human review).

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- Schema/format adherence checked for every case.
- At least 1 negative test: must ask a question or abstain.

## Deliverables
- `README.md` + run instructions.
- `eval/` notes dataset + expected action fields + scoring rubric.
- Prompt versions + iteration log.

## Suggested Run Steps
- Run on at least 20 notes samples and score results.
