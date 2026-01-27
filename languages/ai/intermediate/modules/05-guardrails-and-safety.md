# AI — Module 05: Guardrails and Safety

## Overview
Implement practical guardrails: input validation, output constraints, injection defenses, and safe fallbacks.

**Included examples (tool-agnostic):**
- RAG Q&A over docs (source-only + refusal when no evidence)
- Agent workflow (tool constraints + audit logs)

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
1) Threats and harms: injection, data leakage, unsafe content (45 min)
2) Input controls: allowlists, redaction, and instruction boundaries (45 min)
3) Output controls: schemas, policies, and refusal patterns (45 min)
4) Safety testing: red-team sets and escalation paths (40 min)

## Exercises
### Core
- Create a safety checklist for your chosen use case and apply it to 30 test cases.
- Add prompt injection tests and verify proper refusal/containment.

### Better
- Design an escalation policy (route to human, block, or safe-complete).
- Add logging fields needed for audits (without storing sensitive content).

### Beast Mode
- Design a “safety gate” in CI: fail if safety tests regress.
- Add a privacy threat model for stored prompts/outputs.

## Mini-Project
### Brief
Build a guardrails plan + red-team dataset + mitigation notes for one app.

### Acceptance Criteria
- Includes input/output controls and a documented fallback strategy.
- Includes a red-team dataset and a safety gate concept.

## Testing Requirements
- Safety tests are part of your evaluation harness.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Trusting user content as instructions.
- Logging sensitive data without a retention/redaction plan.
- Refusing too broadly instead of safe redirection.

## Stretch Resources
- (Placeholder) Add links to secure prompting and safety testing techniques.
