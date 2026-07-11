# AI — Module 06: Workflows and Automation

## Overview
Combine prompts into a workflow: input → transform → validate → output, with clear handoffs.

**Included examples (tool-agnostic):**
- Agent workflow for a multi-step task (plan → execute → verify)

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
1) Workflow design: stages, contracts, and error handling (45 min)
2) Tool-agnostic automation: templates, variables, and logs (40 min)
3) Human-in-the-loop: where reviewers add the most value (35 min)
4) Fallback strategies: abstain, ask, or route to human (40 min)

## Guided Walkthrough
Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/beginner/starter-pack` into a new working folder.
2. Review the module goals and plan how you will design repeatable prompt workflows.
3. Map the workflow from input to output with clear steps.
4. Define handoff points and required context.
5. Test the workflow with real inputs.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/ai/beginner/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Design a 3-step workflow for meeting notes: extract actions → verify → produce final.
- Add a simple fallback policy for uncertain outputs.

### Better
- Add logging fields: input id, prompt version, result category, time/cost estimate.
- Add retry rules and a maximum attempt budget.

### Beast Mode
- Design a multi-step “agentic” workflow with explicit stop conditions and verification.
- Add an audit log format and a privacy-safe redaction step.

## Mini-Project
### Brief
Build a workflow spec for meeting notes → actions that includes validation + fallback.

### Acceptance Criteria
- Each step has an input/output contract.
- Includes a fallback strategy and a small evaluation set.

## Testing Requirements
- Workflow tested end-to-end on at least 10 cases.
- Includes a simple “retry budget” and “stop if uncertain” rule.

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

- You can restate the module goal in your own words.
- You have run at least one evaluation pass.
- You documented what improved and what did not.

## Common Mistakes
- No boundaries between steps (everything in one giant prompt).
- No stop conditions—workflow runs forever or amplifies errors.
- No tracking of versions/results, making regressions invisible.

## Stretch Resources

- Prompting guide: https://www.promptingguide.ai/
- OpenAI guides: https://platform.openai.com/docs/guides

