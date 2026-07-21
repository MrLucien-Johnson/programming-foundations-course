# Evaluation & Testing

If you cannot measure quality, you cannot improve it. This guide shows how to evaluate prompts and AI features on this site.

## Build a small eval set

Aim for **10–30 cases** early on:

- **Good** — clear inputs with an obvious correct answer
- **Bad** — empty, huge, or hostile inputs
- **Ambiguous** — missing details the model should flag

For each case record: input, expected behaviour, and pass/fail rule.

## What to measure

| Metric | Meaning |
|---|---|
| Correctness | Meets the stated goal |
| Format | Matches schema / template |
| Grounding | No invented facts |
| Safety | Refuses or redacts when required |
| Latency / cost | Within your budget |

## Simple harness

1. Store cases in a spreadsheet or JSON file.
2. Run the same prompt version against all cases.
3. Score pass/fail (human or automated checks).
4. Log the prompt version ID with the score.
5. Change one thing; re-run; compare.

## Iteration log template

```text
Version: v3
Change: Added "do not invent deadlines" rule
Pass rate: 18/24 (was 14/24)
Regressions: case 7 format broke
Next: Fix format example; keep the new rule
```

## Avoid these traps

- Judging by one demo conversation
- Changing five prompt pieces at once
- No regression set (old bugs return silently)

## Practice on this site

- [Evaluation & Iteration](../course-viewer.html?path=languages/ai/beginner/modules/04-evaluation-and-iteration.md)
- [Model Evaluation & Testing](../course-viewer.html?path=languages/ai/intermediate/modules/04-model-evaluation-and-testing.md)
- [Evals at Scale](../course-viewer.html?path=languages/ai/advanced/modules/03-evals-at-scale.md)
