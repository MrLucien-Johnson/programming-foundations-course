# AWS foundations & accounts

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 1 of 10

## Learning goals

By the end of this lesson you will be able to:

- Navigate regions, AZs, and the shared responsibility model
- Create a learning account habit (billing alarm first)
- Use AWS CLI or Console with an IAM user/role — not root daily

## Why this matters

AWS is huge. Foundations prevent surprise bills and root-key disasters before you touch fancy services.

## Core ideas

1. **Account = blast radius boundary** — prefer separate learning/prod later.
2. **Region choice** — latency, data residency, service availability.
3. **Shared responsibility** — AWS secures the cloud; you secure *in* the cloud.
4. **Billing alarm day one** — CloudWatch billing or Budgets.

## Worked example

### Lab: account hygiene

1. Enable MFA on root; create an admin IAM user/role for daily work.
2. Create a Budget alert (e.g. $10).
3. `aws sts get-caller-identity` and screenshot (redact account specifics if sharing).

```bash
aws sts get-caller-identity
aws configure list
```


## Practice

1. Set a billing alert.
2. Document your home region and why.
3. Write the shared responsibility split for EC2 vs Lambda in one paragraph.

## Common mistakes

- Using root access keys daily
- No billing alarm
- Leaving unused resources running

## Stretch goal

Enable Cost Explorer and identify the top cost category after a tiny lab.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
