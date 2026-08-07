# Capstone: deploy a small AWS app

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 10 of 10

## Learning goals

By the end of this lesson you will be able to:

- Deploy a tiny architecture: compute + storage + IAM + monitoring note
- Prove private data placement and a billing alarm
- Package diagrams + commands as portfolio evidence

## Why this matters

Connecting IAM, network, compute, and storage is the real AWS skill — not memorising product logos.

## Core ideas

1. **Minimal viable cloud app** — static site on S3+CloudFront *or* API on managed compute.
2. **Diagram first** — boxes and trust boundaries.
3. **Cleanup script/notes** — leave no orphan spend.

## Worked example

### Capstone options (pick one)

**A.** Private S3 assets + CloudFront (or private bucket + pre-signed demo)  
**B.** Container/EC2/App behind SG + S3 for uploads + CloudWatch alarm  
**C.** Lambda + API Gateway + DynamoDB/S3 learning slice

Definition of done: diagram, IAM notes, deploy steps, alarm, cleanup steps.


## Practice

1. Complete one option end-to-end at learning scale.
2. Record cleanup commands/checklist.
3. Write a 5-minute demo script.

## Common mistakes

- Public databases
- No cleanup — surprise bill
- Admin IAM everywhere

## Stretch goal

Add HTTPS and a custom domain note (even if deferred).

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
