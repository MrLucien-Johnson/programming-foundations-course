# Deployment & CI for AI Features

Treat prompts and AI configs like code: version them, test them, and release carefully.

## What belongs in version control

- Prompt templates and system instructions
- Schemas and output validators
- Eval sets and scoring scripts
- Tool allow-lists and safety policies
- Feature flags for model choice

## CI checks that catch real bugs

1. **Schema validation** on sample outputs
2. **Eval smoke suite** (fast subset of your full eval set)
3. **Safety probes** (injection / leakage red-team cases)
4. **Config lint** — required fields present, versions labeled

Fail the build if smoke evals regress beyond a threshold.

## Release strategy

| Stage | Purpose |
|---|---|
| Dev | Iterate on prompts freely |
| Staging | Run fuller evals against production-like data |
| Canary | Ship to a small % of traffic |
| Full | Promote when metrics hold |

Keep a one-click rollback to the previous prompt version.

## Production practices

- Separate secrets from prompts
- Rate-limit public endpoints
- Log prompt version with every response
- Document owners for each AI feature

## Practice on this site

- [Deployment Basics](../course-viewer.html?path=languages/ai/intermediate/modules/08-deployment-basics.md)
- Related: [Evaluation Guide](guide-viewer.html?path=guides/evaluation-guide.md), [Incident Playbooks](guide-viewer.html?path=guides/incident-playbooks.md)
