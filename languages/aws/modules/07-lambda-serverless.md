# Lambda & serverless

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 7 of 10

## Learning goals

By the end of this lesson you will be able to:

- Describe event-driven Lambda use cases
- Package a tiny function and think about IAM role
- Watch cold starts, timeouts, and cost dimensions

## Why this matters

Serverless removes server babysitting for spiky or event workloads — if you design events and IAM well.

## Core ideas

1. **Function + trigger + role** — the core trio.
2. **Stateless** — put state in DB/S3.
3. **Timeouts & memory** — affect CPU and cost.
4. **Least privilege role** — only needed AWS actions.

## Worked example

### Lab: hello function mindset

```python
def handler(event, context):
    return {"statusCode": 200, "body": "ok"}
```

Triggers to know: API Gateway/Function URL, S3 event, SQS.
IAM: permission to write logs to CloudWatch; nothing else until needed.


## Practice

1. Deploy or sketch a hello function with logs.
2. List three good and three bad Lambda use cases.
3. Set timeout intentionally (not max by default).

## Common mistakes

- VPC-attached Lambda without understanding ENI cold starts (when applicable)
- Huge deployment packages
- Admin role on the function

## Stretch goal

Add an S3 trigger that processes an uploaded object key (name only).

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
