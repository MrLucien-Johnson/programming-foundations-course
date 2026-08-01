# AI — Module 03: Prompt Patterns

> **Voiceover lesson (with captions & read-along transcript):** [Prompt patterns](../../../../docs/tutorials.html#ai-prompt-patterns) — then continue with the written lesson below.

## Overview
Reusable prompt patterns make AI work more reliable. Instead of inventing a new prompt every time, you apply proven structures: checklists, decomposition, critique-and-revise, and verification.

**Included examples (tool-agnostic):**
- Data extraction into JSON (free text → structured fields)

## Learning Outcomes
- Design extraction prompts that emit valid structured fields.
- Specify required-field checklists and missing-data behavior.
- Add a review/repair pass that fixes structure without inventing facts.
- Build an error taxonomy and track reductions across iterations.
- Cover tricky cases with targeted few-shot examples.

## Prerequisites
- Module 02 (Prompting Basics): role, task, constraints, and output format.
- Willingness to iterate: run tests, record failures, and improve.

## Why patterns matter

A one-off prompt can work once and fail the next day. Patterns give you a **repeatable recipe**:

| Pattern | What it does | When to use it |
|---|---|---|
| Checklist | Forces required fields and “missing” rules | Extraction, forms, summaries with must-have items |
| Decomposition | Breaks a big job into clear steps | Multi-part tasks, long documents |
| Critique-and-revise | Separates drafting from review | Quality-sensitive writing or structured output |
| Verify / repair | Checks format, then fixes without new facts | JSON, tables, anything that must parse |

## Concept 1 — Checklist pattern

**Idea:** Tell the model exactly which fields must appear, and what to do when the source does not contain them.

**Weak prompt:**
> Extract useful info from this email.

**Stronger prompt (checklist):**
> Extract these fields from the email only: `name`, `account_id`, `issue`, `urgency` (`low` / `medium` / `high`).  
> If a field is missing, set it to `null` and add a note in `missing_fields`.  
> Do not invent values that are not in the email.

**Why it works:** The model cannot “helpfully guess” a name or urgency when your checklist forbids it.

## Concept 2 — Decomposition (without leaking private chain-of-thought)

**Idea:** Break the task into steps the model should follow, but keep the **output** clean for the user.

Example steps for a support email:
1. Identify the customer and account identifiers present in the text.
2. Summarise the issue in one sentence.
3. Assign urgency using only explicit cues (words like “urgent”, “asap”, or deadlines).
4. Emit JSON matching the schema.

Ask for the **final JSON**, not a long internal monologue. You want reliable structure, not noisy reasoning text.

## Concept 3 — Critique-and-revise

**Idea:** Do not ask one prompt to draft *and* perfectly validate itself in one breath. Use two passes:

1. **Draft:** Produce the best first answer.
2. **Review:** Given the draft + original source, flag missing fields, contradictions, or invented facts — then repair.

This mirrors how humans write: draft, then edit.

## Worked example — email → JSON

**Source email (shortened):**
> Hi, I'm Alex Chen on account A-4412. Our billing page shows the wrong plan since Monday. Please fix today if possible.

**Target schema:**
```json
{
  "name": "string or null",
  "account_id": "string or null",
  "issue": "string",
  "urgency": "low|medium|high",
  "missing_fields": []
}
```

**Good output:**
```json
{
  "name": "Alex Chen",
  "account_id": "A-4412",
  "issue": "Billing page shows the wrong plan since Monday",
  "urgency": "high",
  "missing_fields": []
}
```

**Why `high`?** The email says “fix today if possible” — an explicit time pressure cue. If that phrase were absent, prefer `medium` or ask rather than guessing panic.

**Repair pass example:** If the draft returns invalid JSON (trailing comma, markdown fences), a repair prompt should fix **syntax only** and refuse to invent a missing `account_id`.

## Guided Walkthrough
Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/beginner/starter-pack` into a new working folder.
2. Write one checklist-style extraction prompt for customer emails.
3. Apply a second pattern (critique-and-revise or repair) to the same task.
4. Compare outputs side by side on the same 5 sample emails.
5. Document why the winning pattern fails less often.
6. Note assumptions, tradeoffs, and next steps in a short README section.

## Starter Pack

Use the starter pack in `languages/ai/beginner/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Design a JSON extraction prompt for customer emails (name, account, issue, urgency).
- Add a checklist of required fields and what to do if missing.

### Better
- Add a second “review” pass that flags missing fields or contradictions.
- Add examples for tricky cases (multiple issues, sarcasm, non-English fragments).

### Beast Mode
- Implement a “repair” prompt: fix invalid JSON into valid JSON without changing meaning.
- Create a small error taxonomy and track reductions across iterations.

## Mini-Project
### Brief
Build an “extract → validate → repair” workflow for JSON extraction.

### Acceptance Criteria
- Produces valid JSON for at least 90% of the evaluation set.
- Documents how missing/ambiguous fields are handled.

## Testing Requirements
- A validator (even manual) checks JSON validity and required fields.
- Re-run after changes and record deltas.

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
- Asking for JSON but not specifying schema/required fields.
- Ignoring ambiguity and forcing made-up values.
- No repair strategy for invalid outputs.
- Putting draft and review in one vague prompt so failures are hard to debug.

## Stretch Resources

- Prompting guide: https://www.promptingguide.ai/
- OpenAI guides: https://platform.openai.com/docs/guides
