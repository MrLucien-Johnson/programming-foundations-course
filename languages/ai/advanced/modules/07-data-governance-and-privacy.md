# AI — Module 07: Data Governance and Privacy

## Overview
Handle data responsibly: minimization, retention, access control, consent, and auditability.

**Included examples (tool-agnostic):**
- RAG Q&A (permissions + leakage prevention)
- Customer support summarisation (PII redaction + retention)

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
1) Data classification and minimization (45 min)
2) Retention, deletion, and audit logs (45 min)
3) Access control for RAG and multi-tenant data (50 min)
4) Privacy-by-design in prompts and evaluations (45 min)

## Guided Walkthrough


Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/advanced/starter-pack` into a new working folder.
2. Review the module goals and plan how you will protect sensitive data and compliance.
3. Classify data types and retention rules.
4. Add redaction rules and access controls.
5. Document privacy and compliance steps.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack


Use the starter pack in `languages/ai/advanced/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Create a data handling policy for your app: what is stored, for how long, and why.
- Design a redaction strategy and test it on sample inputs.

### Better
- Add access-control-aware retrieval and test “no leakage” scenarios.
- Define a safe logging schema that avoids storing raw sensitive text.

### Beast Mode
- Design audit queries/reports (who accessed what, when, and for what purpose).
- Add a privacy review checklist to releases.

## Mini-Project
### Brief
Produce a governance plan for an LLM app (privacy + access control + audit).

### Acceptance Criteria
- Includes retention, minimization, access control, and auditability.

## Testing Requirements
- Tests include “data should not appear” negative cases.

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
- Logging raw prompts/outputs indefinitely.
- Ignoring multi-tenant isolation and permissions in retrieval.

## Stretch Resources


- NIST privacy framework: https://www.nist.gov/privacy-framework
- Data governance intro: https://www.cio.com/article/220234/what-is-data-governance.html

