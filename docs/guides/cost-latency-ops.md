# Cost, Latency & Ops

Keep AI features fast enough and cheap enough to run. Measure before you optimize.

## What to track

| Signal | Why it matters |
|---|---|
| Tokens in / out | Direct cost driver |
| Latency (p50 / p95) | User experience |
| Error rate | Timeouts, validation failures |
| Cache hit rate | Savings from reuse |
| Cost per successful task | Business metric |

## Practical optimizations

1. **Shorter prompts** — remove unused instructions; put critical rules first.
2. **Smaller models** for easy tasks; reserve larger models for hard ones.
3. **Cache** repeated system prompts and frequent retrieval results.
4. **Batch** non-interactive work.
5. **Stream** responses when users are waiting on long answers.
6. **Cap** max output tokens to stop runaway completions.

## Monitoring basics

Log for each request (with privacy in mind):

- Feature / prompt version
- Latency and token counts
- Success vs validation failure
- Tool call count

Alert when p95 latency or error rate crosses a threshold you choose.

## Budgets

Set a soft budget per user or per day. When exceeded: degrade gracefully (smaller model, fewer retrievals) instead of failing silently.

## Practice on this site

- [Cost, Latency & Ops](../course-viewer.html?path=languages/ai/intermediate/modules/07-cost-latency-and-ops.md)
- [Observability for LLMs](../course-viewer.html?path=languages/ai/advanced/modules/05-observability-and-monitoring-llm.md)
