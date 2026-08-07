# Continuous integration pipelines

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 3 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain what CI must prove on every push
- Sketch a pipeline: lint → test → build artefact
- Separate flaky tests from real failures

## Why this matters

CI is the team’s shared safety net. If it is slow or flaky, people bypass it — and production pays.

## Core ideas

1. **Fast feedback** — fail in minutes, not hours.
2. **Deterministic builds** — lock dependencies; avoid “works on my machine”.
3. **Artefacts** — build once; promote the same binary/image.
4. **Secrets in the runner** — never in the repo.

## Worked example

### Lab: minimal GitHub Actions shape

```yaml
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm ci
      - run: npm test
      - run: npm run build
```

Extend later with lint, caching, and uploading a build artefact.


## Practice

1. Add a CI workflow that runs tests on every PR.
2. Time a green run; write a goal to keep it under a threshold you choose.
3. Document where secrets live (CI settings), not in markdown.

## Common mistakes

- Only testing on developer laptops
- Rebuilding differently for staging vs production
- Ignoring flaky tests until nobody trusts CI

## Stretch goal

Cache dependencies and measure the time saved.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
