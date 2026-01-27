# AI Advanced — Mini Project 2: Reliability + Fallbacks Drill

## Overview
- **Goal**: Design and test reliability strategies with failure injection and incident playbooks.
- **Expected effort**: 3–5 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- Failure injection scenarios: model outage, tool timeout, empty retrieval, cost spike.
- Fallback behavior for each scenario.
- Incident playbooks with detection signals and mitigation steps.
- Cost/latency plan with budgets + enforcement mechanisms.

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- Drills must be runnable and produce pass/fail outputs.

## Deliverables
- Playbooks + drill results + improvement actions.
- Updated eval/safety sets based on incident learnings.

## Suggested Run Steps
- Run drills and record outcomes; update the system design accordingly.
