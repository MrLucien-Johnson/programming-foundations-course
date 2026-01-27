# AI — Module 01: AI Foundations

## Overview
Understand what LLMs are good at, what they’re bad at, and how to frame AI work as engineering work.

**Included examples (tool-agnostic):**
- Customer support summarisation (issue → summary + next steps)
- Meeting notes → action items (notes → owners + deadlines)

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
1) What LLMs do (and don't do): pattern completion, not truth (45 min)
2) The engineering loop: spec → prompt → evaluate → iterate (50 min)
3) Failure modes: hallucinations, brittleness, prompt injection basics (45 min)
4) Working with constraints: tone, length, format, policies (40 min)

## Exercises
### Core
- Write a one-page spec for a summarizer: inputs, outputs, constraints, and “do not do” list.
- Create a 10-case evaluation set (good, bad, ambiguous) and define success criteria.

### Better
- Add edge cases: empty input, conflicting instructions, sensitive information.
- Record failure categories (e.g., missing actions, invented facts) and counts.

### Beast Mode
- Add a “grounding rule” (only use provided text) and measure how it changes failures.
- Design a fallback behavior when input is low quality (ask clarifying question or return “insufficient info”).

## Mini-Project
### Brief
Build a “Prompt Spec” template and apply it to a summarization use case.

### Acceptance Criteria
- Spec includes goal, constraints, examples, and failure modes.
- Includes a 10-case evaluation set and an iteration log.

## Testing Requirements
- Maintain a small eval set and rerun after each prompt change.
- Document at least 3 iterations and what improved/worsened.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Skipping the spec and jumping straight to prompt tinkering.
- Measuring success by a single cherry-picked example.
- Letting the model invent facts rather than constraining it to source text.

## Stretch Resources
- (Placeholder) Add an introductory LLM evaluation guide.
- (Placeholder) Add a primer on hallucinations and mitigation strategies.
