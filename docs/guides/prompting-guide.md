# Prompting Guide

A practical, tool-agnostic guide to writing prompts that produce reliable results. Use this instead of leaving the site for third-party prompting courses.

## Core idea

A good prompt is a **mini specification**: goal, inputs, constraints, output format, and what to do when uncertain.

## The five parts of a strong prompt

1. **Role / context** — who the model is acting as, and why.
2. **Goal** — one clear outcome in plain language.
3. **Inputs** — the data the model may use (and what it must ignore).
4. **Constraints** — tone, length, policies, “do not invent facts.”
5. **Output shape** — bullets, JSON, table, or a fixed template.

### Example

```text
You are a careful assistant for customer support.

Goal: Summarise the customer message into issue, urgency, and next steps.

Inputs: Use only the message below. Do not invent account details.

Constraints:
- Keep under 120 words
- If information is missing, say "insufficient info" for that field
- Neutral, professional tone

Output format:
- Issue:
- Urgency: low | medium | high
- Next steps: (1–3 bullets)
```

## Useful patterns

| Pattern | When to use | Tip |
|---|---|---|
| Instruction + format | Everyday tasks | Put the format last so it is hard to miss |
| Few-shot examples | Style or edge cases | 2–4 short examples beat one long one |
| Chain of steps | Multi-part reasoning | Ask for steps, then the final answer |
| Critique & revise | Quality passes | “List flaws, then rewrite” |
| Grounded only | Summaries, RAG | “Only use provided text” |

## Iteration loop

1. Write a one-page spec (goal, inputs, outputs, failures).
2. Run 5–10 test cases (good, bad, ambiguous).
3. Log failures by category (invented facts, wrong format, refused, etc.).
4. Change one thing at a time.
5. Re-run the same cases and compare.

## Common mistakes

- Vague goals (“make this better”).
- No output format.
- Measuring success on a single cherry-picked example.
- Letting the model invent sources or numbers.

## Next steps on this site

- Course: [AI Prompt Creation](../ai-course.html)
- Related guides: [Practical AI Workflows](guide-viewer.html?path=guides/practical-ai.md), [Evaluation & Testing](guide-viewer.html?path=guides/evaluation-guide.md)
