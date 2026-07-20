# Incident Playbooks for AI Systems

When an AI feature breaks or behaves badly in production, follow a clear playbook.

## Severity guide

| Level | Examples |
|---|---|
| SEV1 | Data leak, unsafe actions executed, widespread wrong answers on critical path |
| SEV2 | Major quality drop, high error rate, cost spike |
| SEV3 | Minor regressions, single-region latency |

## First 15 minutes

1. **Acknowledge** — who is incident lead?
2. **Contain** — feature flag off, force fallback, or block the bad prompt version.
3. **Preserve evidence** — prompt version, sample traces, error rates (watch privacy).
4. **Communicate** — status note to stakeholders; user-facing banner if needed.

## Investigate

- Which prompt / model / retrieval index changed recently?
- Do evals still pass offline?
- Is a vendor outage involved?
- Any prompt-injection or abuse pattern in inputs?

## Recover

- Roll back to last known good config
- Hotfix validators or filters if needed
- Re-enable gradually (canary)

## Post-incident

Write a short postmortem:

- What happened and user impact
- Timeline
- Root cause
- What went well / poorly
- Action items with owners and dates

Blameless tone; focus on systems.

## Practice on this site

- [Production Incident Playbooks](../course-viewer.html?path=languages/ai/advanced/modules/08-production-incident-playbooks.md)
- Related: [Deployment & CI](guide-viewer.html?path=guides/deployment-ci.md), [Reliability & Fallbacks](guide-viewer.html?path=guides/reliability-fallbacks.md)
