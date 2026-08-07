# Azure foundations & subscriptions

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 1 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain the relationship among an Entra tenant, management groups, subscriptions, resource groups, and resources
- Choose an Azure region and paired-region strategy using latency, compliance, and service availability
- Create and inspect a resource group safely with Azure CLI

## Why this matters

Azure's hierarchy determines ownership, policy scope, billing, and blast radius. Getting it right before deployment prevents tangled permissions and expensive cleanup.

## Core ideas

1. **Scope hierarchy** — management group → subscription → resource group → resource; settings commonly inherit downward.
2. **Resource groups are lifecycle boundaries** — group resources that are deployed, owned, and removed together.
3. **Regions and availability zones solve different failures** — zones isolate datacentres within a region; paired regions support regional recovery planning.
4. **Shared responsibility remains workload-specific** — Microsoft secures the cloud; you still secure identities, data, configuration, and code.

## Worked example

### Lab: establish a safe Azure scope

```bash
az login
az account list --output table
az account set --subscription "<subscription-id>"
az group create --name rg-learning-web --location uksouth   --tags owner=student environment=lab
az group show --name rg-learning-web --output table
```

Record the selected tenant, subscription, region, tags, and cleanup owner. Remove the lab when finished with `az group delete --name rg-learning-web --yes --no-wait`.

## Practice

1. Draw the Azure hierarchy for a company with production and sandbox subscriptions.
2. Compare two candidate regions with `az account list-locations --output table` and document the decision.
3. Create a tagged lab resource group, inspect its resource ID, then delete it.

## Common mistakes

- Treating a resource group as a network or identity security boundary
- Deploying before confirming the active subscription and tenant
- Choosing a region without checking required service and SKU availability

## Stretch goal

Design a management-group hierarchy that separates platform, production, and sandbox policy scope.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
