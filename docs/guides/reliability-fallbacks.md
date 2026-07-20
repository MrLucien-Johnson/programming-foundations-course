# Reliability & Fallbacks

AI calls fail. Design for timeouts, bad outputs, and provider outages.

## Failure modes

- Provider timeout or 5xx
- Rate limits
- Invalid JSON / schema mismatch
- Empty or low-quality retrieval
- Safety filter blocks a valid request
- Model returns confident nonsense

## Patterns that help

| Pattern | Idea |
|---|---|
| Timeouts | Fail fast; show a useful message |
| Retries | Retry transient errors with backoff; do not blindly retry unsafe side effects |
| Fallback model | Smaller/cheaper model or template response |
| Cached answer | Serve last known good for identical queries |
| Degraded mode | Skip fancy RAG; answer with a form or FAQ link |
| Queue | Defer non-interactive jobs |

## Validator-first flow

```text
call model → validate → if fail, repair prompt once → if still fail, fallback
```

Never show raw invalid JSON to end users.

## SLOs for AI features

Pick simple targets, for example:

- 99% of requests return within 8 seconds
- <2% validation failure after retries
- Availability matching your API’s overall SLO

## Practice on this site

- [Reliability & Fallbacks](../course-viewer.html?path=languages/ai/advanced/modules/06-reliability-and-fallbacks.md)
- Related: [Cost, Latency & Ops](guide-viewer.html?path=guides/cost-latency-ops.md)
