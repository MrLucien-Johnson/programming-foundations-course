# AI — Module 08: Production Incident Playbooks

## Overview
Be ready for production: incident types, triage, communication, mitigations, and postmortems.

**Included examples (tool-agnostic):**
- Customer support summarisation (quality regressions)
- RAG Q&A (grounding failures)
- Agent workflows (tool abuse / runaway loops)

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
1) Incident categories: quality drop, safety event, cost spike, outage (45 min)
2) Triage workflow: detect → contain → mitigate → recover (50 min)
3) Playbooks: step-by-step actions and ownership (45 min)
4) Postmortems: root cause, prevention, and follow-up evals (45 min)

## Guided Walkthrough


Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/advanced/starter-pack` into a new working folder.
2. Review the module goals and plan how you will prepare incident response playbooks.
3. Write an incident runbook for a failure scenario.
4. Define escalation paths and owners.
5. Run a tabletop exercise and capture lessons.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack


Use the starter pack in `languages/ai/advanced/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Write an incident playbook for a cost spike and for a safety regression.
- Define immediate mitigations (feature flag off, degraded mode, stricter filters).

### Better
- Add “incident drills”: simulate failures and verify playbook effectiveness.
- Add communication templates (internal + user-facing) for common incidents.

### Beast Mode
- Add automated detection rules that trigger playbook steps.
- Design a post-incident improvement loop: update evals + guardrails.

## Mini-Project
### Brief
Create an incident response package: playbooks + drills + postmortem template.

### Acceptance Criteria
- Includes detection signals, mitigations, and follow-up prevention work.

## Testing Requirements
- Incidents are tested via drills; playbooks are updated based on results.

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
- No clear ownership or steps during incidents.
- Mitigations that increase risk (e.g., disabling safety checks).

## Stretch Resources


- Incident response: https://sre.google/workbook/incident-response/
- Postmortems: https://sre.google/sre-book/postmortem-culture/

