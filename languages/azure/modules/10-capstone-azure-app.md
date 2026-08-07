# Capstone: host a small Azure app

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 10 of 10

## Learning goals

By the end of this lesson you will be able to:

- Deploy a small Azure web application with managed identity, private data, and telemetry
- Demonstrate a staged release, failure signal, rollback, and cleanup path
- Present architecture and operational evidence rather than only a successful URL

## Why this matters

A capstone proves that identity, compute, data, networking, monitoring, governance, and cost decisions work together as an operable service.

## Core ideas

1. **Build the smallest complete service** — App Service or Container Apps, Storage or Azure SQL, and Application Insights are enough.
2. **Identity replaces embedded secrets** — grant the app's managed identity only its required data role.
3. **Production readiness is observable** — health, failures, latency, deploy version, and cost ownership must be visible.
4. **A capstone includes teardown** — reproducible cleanup is part of responsible cloud engineering.

## Worked example

### Capstone: deploy, observe, and prove

```bash
az group create -n rg-capstone-web -l uksouth   --tags owner=student environment=capstone
az appservice plan create -g rg-capstone-web -n plan-capstone   --is-linux --sku B1
az webapp create -g rg-capstone-web -p plan-capstone   -n <unique-app-name> --runtime "NODE:20-lts"
PRINCIPAL_ID=$(az webapp identity assign -g rg-capstone-web   -n <unique-app-name> --query principalId -o tsv)
az webapp config appsettings set -g rg-capstone-web   -n <unique-app-name> --settings RELEASE_SHA="$(git rev-parse --short HEAD)"
```

Add private storage, assign `Storage Blob Data Contributor` at container or account scope, enable Application Insights, then capture a healthy request and a controlled failure. Document rollback and run `az group delete -n rg-capstone-web --yes --no-wait` after assessment.

## Practice

1. Create an architecture diagram showing trust boundaries, identities, ingress, and data flow.
2. Run a five-minute demonstration: deploy, health check, telemetry query, staged update, and rollback.
3. Record resource inventory, estimated cost, role assignments, and cleanup evidence.

## Common mistakes

- Using Owner permissions or storage keys to make the demo work quickly
- Showing only the happy-path homepage with no operational evidence
- Leaving paid resources, public endpoints, or test data after the capstone

## Stretch goal

Provision the capstone declaratively with Bicep or Terraform and add a private endpoint plus custom-domain TLS.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
