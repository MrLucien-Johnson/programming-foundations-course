# AI — Module 02: Structured Outputs and Schemas

## Overview
Make outputs machine-consumable: JSON schemas, strict formatting, validation, and repair loops.

**Included examples (tool-agnostic):**
- Data extraction into JSON (emails/notes → schema)

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
1) Define schemas: required fields, types, and constraints (45 min)
2) Prompt for structure: examples, forbidden fields, and null handling (45 min)
3) Validate + repair: detect invalid outputs and recover safely (50 min)
4) Versioning: schema changes and backward compatibility (40 min)

## Guided Walkthrough


Follow these steps to turn the lesson into a real, working deliverable.

1. Copy the starter pack from `languages/ai/intermediate/starter-pack` into a new working folder.
2. Review the module goals and plan how you will generate structured outputs that pass validation.
3. Define a JSON schema for the output.
4. Add schema instructions to the prompt.
5. Validate outputs with at least 5 test cases.
6. Document decisions in a short README section (assumptions, tradeoffs, next steps).

## Starter Pack


Use the starter pack in `languages/ai/intermediate/starter-pack` for a clean baseline.

Inside the pack:
- A prompt spec template.
- An evaluation notes template.
- A place to capture workflow decisions.

## Exercises
### Core
- Design a schema for customer support tickets (category, summary, urgency, actions).
- Create a 30-case dataset and measure JSON validity + required-field completeness.

### Better
- Add a repair prompt that fixes invalid JSON without adding new information.
- Add schema versioning notes and a migration plan.

### Beast Mode
- Add a “strict mode” validator and a fallback response when validation fails.
- Design a red-team set that tries to inject extra fields or instructions.

## Mini-Project
### Brief
Build a JSON extraction pipeline: extract → validate → repair → final.

### Acceptance Criteria
- Valid JSON for ≥95% of cases; clear handling for missing data.
- Schema documented with examples and failure handling.

## Testing Requirements
- Automated validation against schema; repair attempts are capped.

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
- Schemas that don't match real inputs.
- Repair prompts that “invent” values.
- No plan for schema evolution.

## Stretch Resources


- Structured outputs: https://platform.openai.com/docs/guides/structured-outputs
- JSON schema basics: https://json-schema.org/learn/getting-started-step-by-step

