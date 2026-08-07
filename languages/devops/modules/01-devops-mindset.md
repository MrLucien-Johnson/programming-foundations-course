# DevOps mindset & value stream

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 1 of 10

## Learning goals

By the end of this lesson you will be able to:

- Define DevOps as a delivery system (not a job title or a tool list)
- Sketch a value stream from commit to production for a small API
- Name lead time, deploy frequency, change failure rate, and MTTR in plain words

## Why this matters

Teams that only add tools without fixing handoffs still ship slowly. A clear value stream shows where time and risk actually hide.

## Core ideas

1. **Flow over heroics** — frequent small changes beat rare big releases.
2. **You build it, you run it (shared)** — developers and ops share outcomes, not blame.
3. **Feedback loops** — telemetry and incidents must reach the people who can change the code.
4. **Constraints first** — map the bottleneck before buying another platform.

## Worked example

### Lab: map a value stream (45 minutes)

Pick a real or sample web API. Draw four boxes: **Commit → Build → Deploy → Observe**.

For each box write: owner, typical wait time, and one failure mode.

Then answer:
1. Where does work sit idle the longest?
2. Which step needs a human every time?
3. What is the smallest automation that would cut wait time this week?

```text
Example (fill yours in):
Commit  → PR review (owner: team, wait: 1d, fail: flaky tests)
Build   → CI (owner: platform, wait: 12m, fail: secret missing)
Deploy  → manual SSH (owner: ops, wait: 2h, fail: wrong host)
Observe → none (owner: ?, wait: ?, fail: users report first)
```


## Practice

1. Write a one-page value-stream note for your sample service.
2. List the four DORA-style metrics and invent honest baseline guesses.
3. Propose one change that improves *flow*, not just tooling.

## Common mistakes

- Renaming the ops team “DevOps” without changing the release process
- Buying a CI product before fixing branch and review habits
- Optimising a step that is not the bottleneck

## Stretch goal

Interview one teammate (or invent a persona) and update the stream with their wait times.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
