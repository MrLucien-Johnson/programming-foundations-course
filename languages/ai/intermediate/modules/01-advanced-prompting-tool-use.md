# AI — Module 01: Advanced Prompting: Tool Use

## Overview
Design prompts that reliably call tools/functions: explicit contracts, error handling, and verification—without vendor-specific features.

**Included examples (tool-agnostic):**
- Meeting notes → actions (tool use: calendar/task creation as “tools”, simulated)
- Customer support summarisation (tool use: knowledge lookup as “tool”, simulated)

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
1) From instruction to contract: inputs/outputs, allowed actions, and constraints (50 min)
2) Tool selection: routing rules, confidence thresholds, and refusal states (45 min)
3) Verification: validate tool results before responding (45 min)
4) Error handling: retries, timeouts, partial failures (45 min)

## Exercises
### Core
- Write a tool contract for “create_task(title, owner, due_date)” (or equivalent).
- Design prompts that choose between: answer, ask clarifying question, or call tool.

### Better
- Add a verification step: check that tool output matches the request before replying.
- Add retry rules with budgets and explicit error messages.

### Beast Mode
- Add adversarial inputs that attempt to override tool constraints.
- Design an audit log schema for tool calls (who/what/when/why).

## Mini-Project
### Brief
Build a tool-use prompt suite for meeting notes → actions with validation and fallbacks.

### Acceptance Criteria
- Has clear contracts, error handling, and a verification step.
- Includes an eval set of at least 20 cases, including failures.

## Testing Requirements
- End-to-end workflow tested with simulated tool failures and timeouts.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Letting the model call tools with missing/ambiguous parameters.
- No verification of tool results before presenting them to users.
- Unlimited retries that increase cost and latency.

## Stretch Resources
- (Placeholder) Add links to general tool-calling design patterns.
