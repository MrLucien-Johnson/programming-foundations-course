# AI — Module 04: Security Threat Modeling for LLM Apps

## Overview
Threat model LLM applications: injection, data exfiltration, tool abuse, and supply chain risks.

**Included examples (tool-agnostic):**
- Agent workflow for multi-step task (tool abuse + constraints)
- RAG Q&A over docs (permissions-aware retrieval)

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
1) Threat modeling workflow: assets, attackers, entry points (50 min)
2) Prompt injection and data exfiltration defenses (55 min)
3) Tool security: least privilege, allowlists, and audit logs (45 min)
4) Secure data handling: redaction, retention, and access control (45 min)

## Exercises
### Core
- Create a threat model for one app: list threats and mitigations.
- Design a red-team suite that targets top threats.

### Better
- Add a least-privilege tool policy and verify via tests.
- Add data minimization and retention rules to the design.

### Beast Mode
- Design incident response for security events (triage + containment).
- Add a supply-chain policy for prompt/eval artifacts.

## Mini-Project
### Brief
Produce a security threat model + red-team plan + mitigations for an LLM app.

### Acceptance Criteria
- Includes tool security, data security, and injection defenses.

## Testing Requirements
- Security tests included in the evaluation harness and CI gate.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Treating retrieved content as trusted instructions.
- Over-permissioned tools without audit logs.

## Stretch Resources
- (Placeholder) Add links to secure system design and threat modeling references.
