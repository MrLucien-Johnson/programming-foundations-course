# Entra ID & RBAC

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 2 of 10

## Learning goals

By the end of this lesson you will be able to:

- Distinguish Entra authentication from Azure RBAC authorization
- Assign a least-privilege role at the narrowest practical scope
- Prefer managed identities over application secrets for Azure-hosted workloads

## Why this matters

Most damaging cloud incidents begin with excessive or persistent credentials. Entra ID and Azure RBAC let teams prove identity and constrain what that identity can do.

## Core ideas

1. **Authentication is who; authorization is what** — Entra verifies identities, while RBAC role assignments grant actions at a scope.
2. **A role assignment has three parts** — security principal, role definition, and scope.
3. **Inheritance expands reach** — subscription-level access flows into every child resource group unless constrained.
4. **Managed identity removes secret distribution** — Azure issues and rotates workload credentials for supported services.

## Worked example

### Lab: grant read-only access to one resource group

```bash
RG_ID=$(az group show -n rg-learning-web --query id -o tsv)
USER_ID=$(az ad signed-in-user show --query id -o tsv)
az role assignment create   --assignee-object-id "$USER_ID"   --assignee-principal-type User   --role Reader --scope "$RG_ID"
az role assignment list --scope "$RG_ID" --all --output table
```

Use `az role assignment delete` after the exercise. For an App Service, enable a workload identity with `az webapp identity assign --resource-group rg-learning-web --name <app-name>`.

## Practice

1. Map Reader, Contributor, and User Access Administrator to concrete allowed and denied tasks.
2. Create a Reader assignment at resource-group scope and verify it with the CLI.
3. Explain how a managed identity reaches Key Vault without embedding a client secret.

## Common mistakes

- Granting Owner when a data-plane or Reader role is enough
- Confusing an Entra directory role with an Azure resource role
- Putting service-principal secrets in source code or pipeline logs

## Stretch goal

Create a custom-role design that permits restart and status checks but not deletion or role assignment.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
