# Monitor & Application Insights

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 8 of 10

## Learning goals

By the end of this lesson you will be able to:

- Distinguish Azure Monitor metrics, Log Analytics logs, Application Insights telemetry, and alerts
- Write a useful KQL query for an application symptom
- Create an actionable alert with an owner and response note

## Why this matters

Telemetry shortens the time from user impact to diagnosis. Azure Monitor is most valuable when signals are tied to service objectives and a clear response.

## Core ideas

1. **Metrics are numeric time series; logs are rich records** — use each according to the question.
2. **Application Insights correlates requests, dependencies, exceptions, and traces** through distributed operation identifiers.
3. **KQL transforms evidence into answers** — filter early, summarize deliberately, and preserve timestamps and dimensions.
4. **Actionable alerts need symptom, threshold, duration, recipient, and runbook** — otherwise they become noise.

## Worked example

### Lab: query failed requests and inspect resource metrics

```kusto
requests
| where timestamp > ago(30m)
| where success == false
| summarize failures=count(), p95=percentile(duration, 95)
    by operation_Name, bin(timestamp, 5m)
| order by timestamp desc
```

```bash
RESOURCE_ID=$(az webapp show -g rg-learning-web -n <app-name> --query id -o tsv)
az monitor metrics list --resource "$RESOURCE_ID"   --metric Http5xx --interval PT5M --output table
az monitor app-insights component show -g rg-learning-web   --app <insights-name> -o table
```

## Practice

1. Write KQL that finds the most common exception type in the last hour.
2. Define a latency or error-rate alert using a user-visible threshold and evaluation window.
3. Build a small incident dashboard with traffic, errors, latency, and saturation.

## Common mistakes

- Alerting on every individual error without rate, duration, or impact context
- Logging secrets, access tokens, or unnecessary personal data
- Keeping high-volume debug telemetry forever without sampling or retention policy

## Stretch goal

Add an availability test and correlate a failed probe to dependency telemetry and a deployment event.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
