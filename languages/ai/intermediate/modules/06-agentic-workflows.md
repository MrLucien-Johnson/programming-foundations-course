# AI — Module 06: Agentic Workflows

## Overview
Design multi-step agents with explicit planning, tool boundaries, stop conditions, and verification.

**Included examples (tool-agnostic):**
- Agent workflow for a multi-step task (research → draft → verify → deliver)

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
1) Agent loop: plan → act → observe → verify (50 min)
2) Memory and state: what to store, what not to store (45 min)
3) Stop conditions and safety rails (45 min)
4) Decomposition and delegation: sub-tasks and checklists (40 min)

## Guided Walkthrough


Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/intermediate/starter-pack` into a new working folder.
2. Review the module goals and plan how you will design multi-step agent workflows.
3. Define agent roles and responsibilities.
4. Design the handoff protocol between steps.
5. Test with a multi-step scenario.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack


Use the starter pack in `languages/ai/intermediate/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Design an agent workflow spec for “triage support tickets and draft responses”.
- Add a verification step that checks facts only against provided sources.

### Better
- Add a tool budget and stop conditions; show how it prevents runaway loops.
- Add a “human approval” checkpoint for high-risk actions.

### Beast Mode
- Add adversarial cases that try to make the agent leak secrets or ignore constraints.
- Add a “post-run report” format (actions taken, evidence, uncertainties).

## Mini-Project
### Brief
Build an agent workflow design doc with test cases, budgets, and verification.

### Acceptance Criteria
- Explicit tool boundaries, stop conditions, and verification requirements.
- Includes an evaluation set with failures and adversarial prompts.

## Testing Requirements
- Agent tested with simulated failures (tool down, partial data, conflicting instructions).

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
- No verification step—agent confidently ships wrong results.
- Unbounded loops (no budgets/timeouts).
- Storing sensitive data as “memory” without a policy.

## Stretch Resources


- Agent patterns: https://www.promptingguide.ai/
- OpenAI tools guide: https://platform.openai.com/docs/guides/tools

