# AI — Module 06: Reliability and Fallbacks

## Overview
Design resilient systems: retries, timeouts, idempotency, degraded modes, and human fallback.

**Included examples (tool-agnostic):**
- Agent workflow (bounded loops + fallback to human)
- Meeting notes → actions (validation + repair + human approval)

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
1) Reliability patterns: retries, timeouts, backoff, budgets (50 min)
2) Degraded modes: cached responses, smaller contexts, rule-based fallbacks (45 min)
3) Idempotency and safe tool execution (45 min)
4) Chaos testing and failure injection (45 min)

## Guided Walkthrough


Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/advanced/starter-pack` into a new working folder.
2. Review the module goals and plan how you will build fallback strategies for failures.
3. Define fallback behavior for low-quality inputs.
4. Test fallback scenarios and document results.
5. Add retries/timeouts with guardrails.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack


Use the starter pack in `languages/ai/advanced/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Design a fallback strategy for each top failure mode (model down, retrieval empty, tool error).
- Define retry budgets and stop conditions.

### Better
- Add failure-injection tests to your harness (simulate outages/timeouts).
- Add degraded-mode rules (abstain, ask, cached answer).

### Beast Mode
- Design a human-in-the-loop queue with SLA and escalation.
- Add post-incident review template focusing on prevention.

## Mini-Project
### Brief
Write a reliability plan + fallback strategy + failure tests for an LLM app.

### Acceptance Criteria
- Fallback strategy is explicit, testable, and tied to budgets/SLOs.

## Testing Requirements
- Harness includes simulated failures and verifies safe behavior.

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
- Unlimited retries that amplify outages and cost spikes.
- No degraded-mode behavior; app just fails hard.

## Stretch Resources


- Resilience patterns: https://learn.microsoft.com/en-us/azure/architecture/patterns/
- SRE book: https://sre.google/books/

