# Governance & cost

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 9 of 10

## Learning goals

By the end of this lesson you will be able to:

- Apply tags, Azure Policy, locks, budgets, and management groups at appropriate scopes
- Interpret Azure Cost Management data before optimizing
- Separate preventive governance from monitoring and financial alerts

## Why this matters

Cloud self-service scales only when guardrails make ownership, compliance, and cost visible without forcing every safe decision through a central team.

## Core ideas

1. **Policy evaluates resource state** — deny, audit, modify, or deploy-if-not-exists effects enforce standards.
2. **Tags describe ownership and allocation** — policy can require or inherit them, but tags are not access controls.
3. **Locks protect against accidental changes** — `CanNotDelete` and `ReadOnly` do not replace authorization.
4. **Budgets alert; they do not automatically stop spend** — pair alerts with accountable review and approved automation.

## Worked example

### Lab: inspect cost and add a deletion guard

```bash
SCOPE=$(az group show -n rg-learning-web --query id -o tsv)
az tag update --resource-id "$SCOPE" --operation merge   --tags owner=student cost-center=training environment=lab
az lock create --name protect-lab --lock-type CanNotDelete   --resource-group rg-learning-web   --notes "Remove only during documented cleanup"
az policy assignment list --scope "$SCOPE" --output table
az consumption usage list --start-date 2026-08-01   --end-date 2026-08-07 --output table
```

Remove the lock before intentional teardown: `az lock delete --name protect-lab --resource-group rg-learning-web`.

## Practice

1. Define required `owner`, `environment`, `service`, and `cost-center` tags.
2. Compare an Audit policy with a Deny policy and plan a safe rollout from compliance reporting.
3. Create a budget design with 50%, 80%, and forecasted-100% notifications.

## Common mistakes

- Rolling out Deny broadly before evaluating existing resources and exemptions
- Assuming a budget hard-caps or shuts down Azure services
- Using tags as if they prevent unauthorized resource access

## Stretch goal

Design a policy initiative for allowed regions, required tags, secure transport, and diagnostic settings.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
