# AI — Module 06: Workflows and Automation

> **Voiceover lesson (with captions & read-along transcript):** [Workflows & automation](../../../../docs/tutorials.html#ai-workflows) — then continue with the written lesson below.

## Overview
Real AI work is rarely one magic prompt. You combine steps into a workflow: input → transform → validate → output, with clear handoffs and human checkpoints where mistakes would hurt.

**Included examples (tool-agnostic):**
- Multi-step task (plan → execute → verify)
- Meeting notes → actions with validation before send

## Learning Outcomes
- Design multi-step workflows with explicit step I/O contracts.
- Add verification steps before accepting intermediate outputs.
- Set retry budgets and stop conditions for uncertain results.
- Log privacy-safe audit fields for each run.
- Define fallbacks when a step fails or confidence is low.

## Prerequisites
- Modules 01–05: prompting, patterns, evaluation, and safety basics.
- You can write a small eval set and a refusal rule.

## Why workflows beat giant prompts

One huge prompt tries to do everything and fails quietly. A workflow:
- Makes each step testable
- Limits how far a bad intermediate answer can travel
- Shows where a human should approve

## Concept 1 — Steps with contracts

For each step, write:

| Field | Meaning |
|---|---|
| Input | What must be present to start |
| Output | Exact shape (bullets, JSON fields, etc.) |
| Failure | What happens if input is bad or output fails checks |

Example — meeting notes pipeline:
1. **Extract** actions → `{task, owner, due}` list (owners may be `null`)
2. **Verify** → flag missing owners/dates; do not invent people
3. **Format** → final checklist for humans
4. **Approve** → human sends or edits before it leaves the team

## Concept 2 — Human-in-the-loop

Put humans where cost of error is high:
- External email send
- Money, access, or policy changes
- Medical/legal/financial decisions
- Anything irreversible

AI can draft; humans approve. That is still automation — just safer automation.

## Concept 3 — Retry budgets and stop conditions

Without stop rules, workflows amplify errors.

Example rules:
- Retry format repair at most **2** times.
- If required fields are still missing, **ask a clarifying question** or **abstain**.
- If confidence is low (conflicting dates, empty notes), **route to human** — do not guess.

## Concept 4 — Privacy-safe logging

Log enough to debug, not enough to leak:
- Input id / hash (not full private text when avoidable)
- Prompt version
- Step results category (`ok`, `needs_human`, `refused`)
- Time / rough cost estimate

Redact secrets before logs leave your machine.

## Worked example — notes → actions

**Input notes:** “Alex to send revised quote by Friday. Sam will check inventory. Pricing TBD with finance.”

**Step 1 extract (good):**
- Task: send revised quote — Owner: Alex — Due: Friday
- Task: check inventory — Owner: Sam — Due: null
- Task: confirm pricing with finance — Owner: null — Due: null

**Step 2 verify:** marks two items needing human fill-in (due date / owner).

**Step 3:** human completes owners/dates, then the list is ready to share.

**Bad giant-prompt behaviour:** invents “Due: tomorrow” and “Owner: Jordan” to look complete. Your workflow’s verify step is there to catch that.

## Guided Walkthrough
Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/beginner/starter-pack` into a new working folder.
2. Map a workflow from input to output with 3–5 clear steps.
3. Write an I/O contract for each step.
4. Mark handoff points that need a human.
5. Test the workflow with real inputs (include one messy case).
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
- No stop conditions — workflow runs forever or amplifies errors.
- No tracking of versions/results, making regressions invisible.
- Skipping human approval on irreversible actions.

## Stretch Resources

- Prompting guide: https://www.promptingguide.ai/
- OpenAI guides: https://platform.openai.com/docs/guides
