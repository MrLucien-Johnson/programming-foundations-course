# AI — Module 05: Safety and Policy Basics

## Overview
Build safe defaults: handle sensitive data, refusals, and prompt injection attempts.

**Included examples (tool-agnostic):**
- RAG-based Q&A over docs (how to answer only from provided sources)

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
1) Safety basics: sensitive data, harmful instructions, and refusals (45 min)
2) Policy-as-constraints: what the system will not do (35 min)
3) Prompt injection basics: untrusted input boundaries (45 min)
4) Safer outputs: disclaimers, citations to provided text, and abstention (40 min)

## Exercises
### Core
- Write a safety checklist for a summarizer and apply it to 10 test cases.
- Design refusal/redirect behaviors for unsafe requests.

### Better
- Add a “source-only” constraint for doc Q&A and test hallucination reduction.
- Add red-team prompts (injection, data exfiltration attempts) and test responses.

### Beast Mode
- Define a severity model (low/med/high) and required actions for each.
- Design an escalation path (handoff to human, logs, blocklists) for high-risk cases.

## Mini-Project
### Brief
Create a safety pack: checklist + red-team test set + response guidelines.

### Acceptance Criteria
- Checklist covers privacy, harmful content, and prompt injection.
- Red-team set includes at least 10 adversarial prompts.

## Testing Requirements
- Safety tests run as part of the evaluation loop.
- Failures are recorded with category and mitigation notes.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Treating user input as trusted instructions.
- No plan for unsafe outputs or sensitive data exposure.
- “Refuse everything” instead of safe redirection where appropriate.

## Stretch Resources
- (Placeholder) Add links to general AI safety and secure prompting references.
