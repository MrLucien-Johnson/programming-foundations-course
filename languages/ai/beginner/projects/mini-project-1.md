# AI Beginner — Mini Project 1: Support Ticket Summarizer

## Overview
- **Goal**: Turn raw support tickets into concise summaries and next steps with constraints and evaluation.
- **Expected effort**: 1–2 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- Prompt/spec includes goal, constraints, and output format.
- Include examples: at least 10 tickets of varying quality.
- Evaluation harness: rubric scoring for factuality, completeness, and tone.
- Safety checklist: handle sensitive data and harmful requests.
- Cost/latency plan: budgets and how you enforce them.
- Fallback strategy: ask clarifying questions or abstain when insufficient info.

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- At least 20 evaluation cases with categories and expected properties.
- Re-run eval after every prompt change and record results.

## Deliverables
- `README.md` with setup/run/test instructions.
- `prompts/` with versioned prompts and change notes.
- `eval/` dataset + scoring rubric + results.
- Short write-up: what improved across iterations and why.

## Suggested Run Steps
- Run eval harness (manual or scripted) on the dataset.
- Record results and iterate at least 3 times.
