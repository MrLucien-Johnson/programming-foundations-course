# Git branching for teams

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 2 of 10

## Learning goals

By the end of this lesson you will be able to:

- Choose a simple trunk-based or short-lived branch workflow
- Write a PR description that helps reviewers and future you
- Use protected branches and required checks without drama

## Why this matters

Most delivery pain starts in Git habits: long-lived branches, unclear ownership, and merges that nobody can reverse.

## Core ideas

1. **Short-lived branches** — merge within a day or two when you can.
2. **Main stays releasable** — broken main blocks everyone.
3. **PR as a design note** — why, what, how to test, how to roll back.
4. **Protect main** — require reviews + CI; avoid force-push on shared branches.

## Worked example

### Lab: branch, commit, open a PR shape

```bash
git switch -c feat/health-endpoint
# …edit…
git add -A
git commit -m "feat: add /health for load balancer checks"
git push -u origin HEAD
```

Draft a PR body with these headings:

```markdown
## Why
## What changed
## How to test
## Rollback
```


## Practice

1. Create a short-lived branch and a PR template note in your lab repo.
2. List which checks should be required on `main`.
3. Practise a revert plan: `git revert` vs redeploy previous artefact.

## Common mistakes

- Week-long feature branches with no sync from main
- Committing secrets or huge binaries
- Force-pushing shared branches

## Stretch goal

Add a CODEOWNERS file for one critical path.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
