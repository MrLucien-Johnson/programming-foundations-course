# Monitoring with CloudWatch

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 8 of 10

## Learning goals

By the end of this lesson you will be able to:

- Find default metrics for a service you used
- Create an alarm idea with a threshold
- Use logs insights mindset for one query

## Why this matters

Without CloudWatch (or equivalent), you learn about outages from Twitter.

## Core ideas

1. **Metrics → Alarms → Actions** (SNS/email).
2. **Dashboards** for a service overview.
3. **Logs retention** — cost vs need.
4. **Alarms on symptoms** tied to user impact.

## Worked example

### Lab: alarm sketch

Metric: `5XXError` on ALB or `Errors` on Lambda  
Threshold: > 1% of requests for 5 minutes  
Action: email SNS topic  

Write the plain-English symptom: “Users cannot complete checkout.”


## Practice

1. Create or sketch one alarm + SNS email.
2. Set log retention intentionally on a log group.
3. Write one Logs Insights style question you care about.

## Common mistakes

- No alarms at all
- Alarm on noisy metrics with no runbook
- Infinite log retention on debug noise

## Stretch goal

Composite alarm or anomaly detection note.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
