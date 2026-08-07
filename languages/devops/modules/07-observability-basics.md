# Observability basics

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 7 of 10

## Learning goals

By the end of this lesson you will be able to:

- Separate logs, metrics, and traces
- Add structured logs and a basic RED/USE style check
- Define one SLO-ish symptom for your service

## Why this matters

You cannot improve what you cannot see. Guessing during incidents wastes customers’ time.

## Core ideas

1. **Logs** — events; prefer structured JSON.
2. **Metrics** — aggregates for dashboards/alerts.
3. **Traces** — request path across services.
4. **Alert on symptoms** — user pain, not every CPU blip.

## Worked example

### Lab: structured log + simple metric

```js
// example: log one request
console.log(JSON.stringify({
  level: "info",
  msg: "request",
  route: "/checkout",
  status: 200,
  latency_ms: 42,
  request_id: "abc123"
}));
```

Pick one alert idea: “5xx rate > 2% for 5 minutes” or “p95 latency > 800ms”.


## Practice

1. Add `request_id` to logs for one endpoint.
2. List three signals you would graph for your API.
3. Write one alert in plain language tied to user impact.

## Common mistakes

- Logging secrets or full card numbers
- Alert fatigue from noisy low-value pages
- No correlation IDs across services

## Stretch goal

Sketch a tiny dashboard: traffic, errors, latency.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
