# S3 & storage

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 5 of 10

## Learning goals

By the end of this lesson you will be able to:

- Create a private bucket with Block Public Access on
- Explain versioning and lifecycle basics
- Generate a pre-signed URL mindset for temporary access

## Why this matters

S3 is everywhere — backups, static assets, data lakes. Public bucket mistakes make headlines.

## Core ideas

1. **Private by default** — Block Public Access.
2. **Versioning** — recover from overwrite/delete.
3. **Lifecycle** — transition/expire to control cost.
4. **Encryption** — SSE-S3/SSE-KMS; know which you chose.

## Worked example

### Lab: private bucket + versioning

```bash
aws s3 mb s3://YOUR-UNIQUE-LEARNING-BUCKET
aws s3api put-public-access-block --bucket YOUR-UNIQUE-LEARNING-BUCKET \
  --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
aws s3api put-bucket-versioning --bucket YOUR-UNIQUE-LEARNING-BUCKET \
  --versioning-configuration Status=Enabled
echo "hello" > note.txt
aws s3 cp note.txt s3://YOUR-UNIQUE-LEARNING-BUCKET/
```


## Practice

1. Create a private versioned bucket and upload a file.
2. Write a lifecycle rule idea (e.g. expire incomplete uploads).
3. Explain when static website hosting is OK vs CloudFront+OAC patterns.

## Common mistakes

- Public ACLs for “just a second”
- No versioning on important backups
- Leaving old incomplete multipart uploads forever

## Stretch goal

Enable access logging or server access logs to another bucket.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
