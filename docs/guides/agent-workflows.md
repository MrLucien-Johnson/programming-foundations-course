# Agentic Workflows

Agents chain model steps (and tools) toward a goal. Keep them useful by limiting autonomy and checking results.

## Agent vs single prompt

| Single prompt | Agent |
|---|---|
| One shot answer | Plan → act → observe → repeat |
| You supply all context | May fetch tools/data mid-flight |
| Easy to evaluate | Needs step limits and audits |

## Minimal agent loop

1. **Plan** — break the goal into steps.
2. **Act** — call a tool or draft an intermediate result.
3. **Observe** — read the tool result or critique.
4. **Decide** — continue, retry, ask the user, or finish.
5. **Stop** — hard cap on steps and time.

## Control knobs

- Max steps / max tool calls
- Allowed tools only
- Require a final structured summary
- Pause for human approval on risky steps
- Persist a trace of every decision

## Prompt skeleton

```text
Goal: {goal}
You may use these tools: {tool list}
After each tool result, briefly state what you learned.
Stop when the goal is met or you are blocked.
End with a Final Answer section.
Never invent tool results.
```

## Failure patterns

- Endless planning with no progress → force an action or stop
- Ignoring tool errors → require explicit error handling
- Scope creep → restates the original goal each turn

## Practice on this site

- [Agentic Workflows module](../course-viewer.html?path=languages/ai/intermediate/modules/06-agentic-workflows.md)
- Related: [Tools & Function Calling](guide-viewer.html?path=guides/tools-and-function-calling.md), [Reliability & Fallbacks](guide-viewer.html?path=guides/reliability-fallbacks.md)
