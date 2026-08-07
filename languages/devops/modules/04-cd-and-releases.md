# Continuous delivery & releases

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 4 of 10

## Learning goals

By the end of this lesson you will be able to:

- Distinguish continuous delivery from continuous deployment
- Describe blue/green or canary at a high level
- Write a release checklist with rollback

## Why this matters

Shipping is a product skill. Unplanned releases create outages; planned, reversible releases build trust.

## Core ideas

1. **Delivery vs deployment** — CD often means *always releasable*; auto-prod is optional.
2. **Same artefact** — staging and prod differ by config, not by mystery rebuilds.
3. **Progressive delivery** — canary/blue-green limit blast radius.
4. **Rollback is a feature** — practise it before you need it.

## Worked example

### Lab: release runbook (one page)

```markdown
# Release: api v1.4.2
## Pre
- [ ] CI green on tag
- [ ] Migrations backward compatible?
- [ ] Feature flag default?
## Deploy
- [ ] Deploy to staging; smoke /health and one critical path
- [ ] Deploy to prod (canary 5% → 25% → 100%)
## Verify
- [ ] Error rate, latency, one business metric
## Rollback
- [ ] Redeploy previous artefact / flip flag off
- [ ] Who to notify
```


## Practice

1. Write a release checklist for your sample API.
2. Decide: continuous delivery (manual prod click) vs continuous deployment.
3. Document one rollback method you could execute in under 15 minutes.

## Common mistakes

- Hotfixing production without a recorded change
- Forward-only migrations with no expand/contract plan
- No smoke tests after deploy

## Stretch goal

Add a feature flag for a risky change and practise toggling it.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
