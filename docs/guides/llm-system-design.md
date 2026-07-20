# LLM System Design

Architecture patterns for apps that use large language models — kept on this site so you can learn without third-party course hop-offs.

## Building blocks

```text
Client → API gateway → Orchestrator → (Retriever / Tools / Model) → Validator → Response
                              ↘ logs, metrics, traces
```

- **Orchestrator** — chooses prompts, tools, retries
- **Retriever** — optional RAG index
- **Model client** — provider-agnostic wrapper
- **Validator** — schema, safety, grounding checks
- **Store** — prompts, traces, feedback (with retention rules)

## Common patterns

| Pattern | Use when |
|---|---|
| Single-shot prompt | Simple transforms and drafts |
| RAG + grounded answer | Knowledge from your docs |
| Tool-calling agent | Needs live data or actions |
| Router | Cheap model vs expensive model by difficulty |
| Human-in-the-loop | High-stakes decisions |

## Design questions

1. What is the user job-to-be-done in one sentence?
2. What must never be invented?
3. What data is in-scope for this user?
4. What is the latency budget?
5. How do we evaluate success weekly?

## Separation of concerns

- Keep **business logic** in your code, not buried in a giant prompt.
- Keep **policies** short and versioned.
- Keep **presentation** (UI copy) separate from model instructions when possible.

## Practice on this site

- [System Design for LLM Apps](../course-viewer.html?path=languages/ai/advanced/modules/01-system-design-for-llm-apps.md)
- Related: [RAG Guide](guide-viewer.html?path=guides/rag-guide.md), [Reliability & Fallbacks](guide-viewer.html?path=guides/reliability-fallbacks.md)
