# AI — Module 04: Evaluation and Iteration

> **Voiceover lesson (with captions & read-along transcript):** [Evaluation & iteration](../../../../docs/tutorials.html#ai-evaluation) — then continue with the written lesson below.

## Overview
Treat prompt work like engineering: define what “good” means, build test cases, score outputs the same way each time, and keep an iteration log. Without evaluation, you cannot tell if a prompt change helped or quietly broke something else.

**Included examples (tool-agnostic):**
- Customer support summarisation (quality rubric + regression set)

## Learning Outcomes
- Create a rubric scorers can apply consistently.
- Build a regression set and compare baseline vs improved prompts.
- Use golden answers for qualitative spot checks.
- Prioritize fixes by failure-category frequency.
- Add abstain/fallback rules tied to confidence thresholds.

## Prerequisites
- Modules 01–03: foundations, prompting basics, and at least one prompt pattern.
- Willingness to measure before and after a change.

## Why evaluate?

AI can sound confident while being wrong. Evaluation is your quality control.

Ask three questions of every answer:
1. **Accuracy** — Are the facts true and grounded in the input?
2. **Completeness** — Did it answer the whole request?
3. **Usefulness** — Could a teammate act on this without guessing?

If you cannot score those consistently, you are guessing — not improving.

## Concept 1 — Define success metrics

Pick metrics that match the job. For a support summary:

| Metric | Meets (example) |
|---|---|
| Factual | No invented order IDs, names, or policies |
| Complete | Issue + next step both present |
| Actionable | A human knows what to do next |
| Tone | Professional, no blame language |
| Format | Required headings or JSON fields present |

Write the rubric so **two people would score similarly**. Vague rubrics (“be good”) fail.

## Concept 2 — Build an evaluation set

Aim for **at least 10–20 cases**, not just happy paths:

- Clear, clean inputs (should succeed)
- Empty or tiny inputs (should refuse or ask)
- Ambiguous inputs (should clarify, not invent)
- Adversarial / messy inputs (injection attempts, conflicting dates)

Store each case with: input text, expected behaviour notes, and optional golden answer.

## Concept 3 — Iterate with discipline

Rules that keep you honest:
1. Change **one** thing at a time (prompt wording *or* examples *or* temperature — not all three).
2. Rerun the **same** eval set after every change.
3. Log: what you changed, score before/after, and which failure categories moved.

If accuracy rose but format collapsed, you traded one failure for another — catch that with regression.

## Worked example — scoring a summary

**Input ticket:** customer says the app crashes on login after the last update; they need a workaround before a client demo tomorrow.

**Rubric (1–5 each):** factual, complete, actionable, tone.

**Weak AI output:** “Sorry for the inconvenience. Please try again later.”  
→ Low completeness and actionability. Sounds polite; helps nobody.

**Stronger output:**
- Restates the crash-on-login symptom
- Notes the time pressure (demo tomorrow)
- Suggests next steps: collect OS/app version, try safe-mode login, escalate if reproducible
- Does **not** invent a bug ID that was never provided

Score both. Then revise the prompt to require: symptom, impact, next steps, and “unknowns” list. Rescore. That is an iteration loop.

## Guided Walkthrough
Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/beginner/starter-pack` into a new working folder.
2. Define success metrics and failure categories for one task you care about.
3. Build a small eval set (include at least one empty and one conflicting case).
4. Run the set on your baseline prompt and record scores.
5. Make one improvement, rerun, and summarise the delta.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack

Use the starter pack in `languages/ai/beginner/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Create a rubric for summaries (factual, complete, actionable, tone).
- Build a 20-case regression set and score baseline vs improved prompt.

### Better
- Add “golden answers” for 5 cases and compare outputs qualitatively.
- Track failure categories and target the biggest ones first.

### Beast Mode
- Write a simple evaluation harness outline (inputs → outputs → scoring).
- Add confidence thresholds and fallback rules (ask question / abstain).

## Mini-Project
### Brief
Produce a small evaluation harness spec and a 20-case dataset for one task.

### Acceptance Criteria
- Dataset includes edge cases and at least 3 adversarial inputs.
- Rubric is clear enough that two people would score similarly.

## Testing Requirements
- Run evaluation after every change and keep results in an iteration log.

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
- Only testing on “happy path” examples.
- No baseline — can't prove improvement.
- Changing prompt, temperature, and examples at once.
- Accepting the first polished answer because it *sounds* right.

## Stretch Resources

- Prompting guide: https://www.promptingguide.ai/
- OpenAI guides: https://platform.openai.com/docs/guides
