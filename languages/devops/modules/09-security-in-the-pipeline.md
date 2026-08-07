# Security in the pipeline

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 9 of 10

## Learning goals

By the end of this lesson you will be able to:

- List SAST/dependency/scan checkpoints in CI
- Explain least privilege for deploy credentials
- Handle secrets with rotation in mind

## Why this matters

Security bolted on at the end fails. Shifting checks left catches issues when fixes are cheap.

## Core ideas

1. **Dependency scanning** — know what you ship.
2. **Least privilege CI roles** — deploy credentials are crown jewels.
3. **Signed/verified artefacts** when you can.
4. **Secrets scanning** on PRs — stop leaks early.

## Worked example

### Lab: pipeline security checklist

- [ ] `npm audit` / equivalent in CI (or Dependabot)
- [ ] Secret scan on PR
- [ ] Container scan on image build
- [ ] Deploy role can only push to intended environment
- [ ] No long-lived access keys in developer laptops for prod

Document where production secrets live (vault / cloud secret manager).


## Practice

1. Enable a dependency update bot or weekly audit note.
2. List every credential your pipeline needs and why.
3. Practise rotating one non-prod secret end-to-end.

## Common mistakes

- Admin credentials in CI “for convenience”
- Ignoring critical CVEs in base images
- Sharing one cloud key across all environments

## Stretch goal

Add an OIDC-style cloud login from CI instead of static keys (where supported).

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
