# RDS & managed data

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 6 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain why managed databases exist
- Place RDS in private subnets
- Plan backups, multi-AZ idea, and credential storage

## Why this matters

Data loss ends careers. Managed DBs trade some control for backups, patching, and HA options.

## Core ideas

1. **Private placement** — no public accessibility for learning defaults.
2. **Automated backups + snapshots** — know RPO/RTO in plain words.
3. **Multi-AZ** — standby for failover (cost vs risk).
4. **Credentials in Secrets Manager** — not in app code.

## Worked example

### Lab: design note (even if you do not provision paid RDS)

Write a one-pager:

- Engine: Postgres
- Subnets: private
- PubliclyAccessible: false
- Backup retention: 7 days
- App connects via SG from app tier only
- Password: Secrets Manager rotation sketch


## Practice

1. Complete the design note.
2. Compare RDS vs self-managed Postgres on EC2 for your use case.
3. Define RPO/RTO targets in one sentence each.

## Common mistakes

- Publicly accessible database
- Single snapshot never tested
- Huge instance “just in case” without measuring

## Stretch goal

Sketch read replica use for reporting workloads.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
