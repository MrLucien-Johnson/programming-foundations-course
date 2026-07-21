# Practical AI Workflows

How to use AI for real work without guessing — and without leaving Programming Foundations for other course sites.

## Start with a task spec

Before you open a chat window, write:

- **Goal** — what success looks like
- **Inputs** — what you will provide
- **Outputs** — exact shape you need
- **Constraints** — length, tone, policies
- **Failure modes** — empty input, conflicting instructions, missing facts

This turns prompting into engineering instead of trial-and-error.

## Everyday workflows

### 1) Summarise with grounding

Ask the model to use only the text you paste. Require “insufficient info” when something is missing.

### 2) Meeting notes → action items

Provide notes, then request owners, deadlines, and open questions in a fixed template.

### 3) Draft → critique → revise

First draft for speed, second pass that lists problems, third pass that fixes them against your checklist.

### 4) Transform formats

Turn messy notes into tables, JSON, or ticket descriptions. Always specify the schema or headings.

## Guardrails you can reuse

- “Do not invent facts, URLs, or citations.”
- “If unsure, ask one clarifying question.”
- “Refuse requests that ask for private data you were not given.”
- “Keep answers under N words unless I ask for detail.”

## Checklist before you trust an answer

- [ ] Output matches the requested format
- [ ] Claims are backed by your inputs (or clearly marked as general knowledge)
- [ ] Edge cases you care about were tested
- [ ] Sensitive data was not pasted into a tool you do not trust

## Next steps on this site

- Beginner module: [AI Foundations](../course-viewer.html?path=languages/ai/beginner/modules/01-ai-foundations.md)
- Guides: [Prompting Guide](guide-viewer.html?path=guides/prompting-guide.md), [AI Safety & Security](guide-viewer.html?path=guides/ai-safety-security.md)
