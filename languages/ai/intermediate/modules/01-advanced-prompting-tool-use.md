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

## Guided Walkthrough


Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/intermediate/starter-pack` into a new working folder.
2. Review the module goals and plan how you will design tool-aware prompts with validation.
3. Write a tool contract and validation rules.
4. Add tool selection logic to your prompt.
5. Test with success and failure cases.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack


Use the starter pack in `languages/ai/intermediate/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

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


## Verification Checklist

Before moving on, confirm the following:

- Run the module tests and confirm they pass.
- Verify the primary feature works with normal and edge-case inputs.
- Update the README with setup, run, and test commands.

## Common Mistakes
- Letting the model call tools with missing/ambiguous parameters.
- No verification of tool results before presenting them to users.
- Unlimited retries that increase cost and latency.

## Stretch Resources


- Tools guide: https://platform.openai.com/docs/guides/tools
- Prompting techniques: https://www.promptingguide.ai/techniques

