# IAM & security basics

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 2 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain users, groups, roles, and policies
- Write a least-privilege policy sketch for S3 read-only
- Prefer roles over long-lived access keys

## Why this matters

IAM mistakes are the #1 cloud self-own. Least privilege and roles beat shared access keys.

## Core ideas

1. **Identity vs permissions** — who you are vs what you can do.
2. **Roles for compute** — EC2/Lambda assume roles; avoid embedding keys.
3. **Deny by default** — grant only needed actions/resources.
4. **CloudTrail** — know who changed what.

## Worked example

### Lab: read-only S3 policy sketch

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:ListBucket"],
    "Resource": [
      "arn:aws:s3:::my-learning-bucket",
      "arn:aws:s3:::my-learning-bucket/*"
    ]
  }]
}
```

Attach to a role used by your learning EC2/CloudShell — not AdministratorAccess for everything.


## Practice

1. Create a least-privilege policy for one task.
2. List three actions that should never be `*` in learning accounts casually.
3. Enable CloudTrail (or confirm it) and find one event.

## Common mistakes

- `AdministratorAccess` on every principal
- Access keys in GitHub
- Public S3 ACLs “temporarily” forgotten

## Stretch goal

Use IAM Access Analyzer findings on one resource.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
