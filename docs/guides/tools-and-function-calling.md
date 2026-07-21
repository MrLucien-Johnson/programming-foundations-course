# Tools & Function Calling

Give models the ability to call tools (search, calculators, APIs) without losing control.

## When tools help

- The model needs **fresh or private data** you did not paste in.
- Answers need **exact computation** or structured lookups.
- You want the model to **propose an action**, and your code to **execute** it.

## Safe design

1. **Declare** each tool with a clear name, purpose, and parameter schema.
2. **Validate** every argument in your code before calling the real API.
3. **Least privilege** — only expose tools the task needs.
4. **Human or policy gate** for destructive actions (send email, delete, pay).
5. **Log** tool calls and results for debugging and audits.

## Prompt pattern

```text
You may call tools only when needed.
Prefer answering from the provided context first.
If a tool fails, explain the failure and suggest a fallback.
Never invent a tool result.
```

## Common failure modes

| Failure | Mitigation |
|---|---|
| Calls the wrong tool | Narrow descriptions; add examples |
| Invents parameters | Strict schema validation; reject and retry |
| Loops forever | Max steps; force a final answer |
| Leaks secrets into args | Redact; blocklist sensitive fields |

## Practice on this site

- Module: [Advanced Prompting & Tool Use](../course-viewer.html?path=languages/ai/intermediate/modules/01-advanced-prompting-tool-use.md)
- Related: [Agentic Workflows](guide-viewer.html?path=guides/agent-workflows.md), [Structured Outputs](guide-viewer.html?path=guides/structured-outputs.md)
