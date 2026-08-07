# Ops & Cloud Logging

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 8 of 10

## Learning goals

By the end of this lesson you will be able to:

- Use Cloud Logging, Cloud Monitoring, Error Reporting, and Trace for distinct questions
- Write Logs Explorer filters and log-based metrics
- Build an actionable alert and control telemetry routing and retention

## Why this matters

Google Cloud Observability turns distributed service behavior into searchable evidence, but useful signals require structured fields, correlation, retention, and response design.

## Core ideas

1. **Structured logs preserve severity and fields** so filters do not depend on brittle text parsing.
2. **Metrics describe trends; logs explain events; traces connect latency across calls** — incidents often need all three.
3. **Log sinks route matching entries** to buckets, BigQuery, Pub/Sub, or other supported destinations.
4. **SLO-based alerts favor user impact** over noisy infrastructure thresholds.

## Worked example

### Lab: query failures and inspect metrics

```bash
gcloud logging read   'resource.type="cloud_run_revision"
   resource.labels.service_name="hello-api"
   severity>=ERROR'   --freshness=1h --limit=20   --format='table(timestamp,severity,jsonPayload.message)'

gcloud monitoring metrics list   --filter='metric.type:run.googleapis.com/request_count' --limit=5
```

In Logs Explorer, refine with `httpRequest.status>=500`, then create a counter metric grouped by service and response code before alerting on a sustained rate.

## Practice

1. Emit a structured log with severity, request ID, release, and safe error code.
2. Create a logs filter for one service's 5xx responses in the last hour.
3. Design an alert policy with threshold, duration, notification channel, and runbook.

## Common mistakes

- Logging credentials, identity tokens, or full sensitive request bodies
- Alerting on one error instead of a sustained user-impact rate
- Exporting all logs without estimating destination storage and query cost

## Stretch goal

Define an availability SLO and burn-rate alerts for fast and slow budget consumption.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
