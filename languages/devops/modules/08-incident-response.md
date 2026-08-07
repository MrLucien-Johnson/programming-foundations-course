# Incident response habits

**Course:** DevOps Foundations Course (donor / allowlist access)  
**Module:** 8 of 10

## Learning goals

By the end of this lesson you will be able to:

- Follow a simple incident timeline: detect → mitigate → resolve → learn
- Communicate status without blame
- Write a short blameless postmortem outline

## Why this matters

Incidents are inevitable. Mature teams minimise impact and learn; immature teams panic and hide.

## Core ideas

1. **Mitigate first** — stop the bleeding before root-causing forever.
2. **Single incident lead** — clear roles beat chaos.
3. **Status updates** — what we know, what we’re doing, next update time.
4. **Blameless learning** — fix systems, not people.

## Worked example

### Lab: tabletop incident (30 minutes)

Scenario: checkout returns 500s after a deploy.

1. Who is incident lead?
2. First mitigate action (rollback vs flag)?
3. What do you tell support/status page in one paragraph?
4. What evidence do you capture (deploy id, graphs, recent changes)?

Postmortem outline:

```markdown
## Summary
## Impact
## Timeline
## Root causes (systems)
## Action items (owner + date)
```


## Practice

1. Run the tabletop with a friend or aloud to yourself.
2. Draft a status update template.
3. List three action items that would prevent a repeat.

## Common mistakes

- Debating root cause while customers are still down
- Blaming individuals in the write-up
- No follow-up actions with owners

## Stretch goal

Add a “break glass” access note: who can roll back prod.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](devops-course.html) for the full path.
