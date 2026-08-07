# App Service

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 6 of 10

## Learning goals

By the end of this lesson you will be able to:

- Deploy a web application to an App Service plan
- Use deployment slots and application settings for safer releases
- Configure health checks, logs, managed identity, and scale intentionally

## Why this matters

App Service provides managed web hosting without requiring VM or cluster administration, while still supporting release, networking, identity, and observability controls.

## Core ideas

1. **The plan supplies compute; the app supplies runtime configuration** — plan tier determines scaling and feature availability.
2. **Deployment slots separate validation from production** — mark environment-specific settings as slot settings before swap.
3. **Application settings become environment variables** — secrets should be Key Vault references, not literal values in source.
4. **Health checks and autoscale need meaningful signals** — a process being alive is weaker than a dependency-aware readiness check.

## Worked example

### Lab: deploy and inspect a Linux web app

```bash
az appservice plan create -g rg-learning-web -n plan-web   --is-linux --sku B1
az webapp create -g rg-learning-web -p plan-web -n <globally-unique-app>   --runtime "PYTHON:3.12"
az webapp config appsettings set -g rg-learning-web -n <app-name>   --settings APP_ENV=lab
az webapp log config -g rg-learning-web -n <app-name>   --application-logging filesystem --level information
az webapp log tail -g rg-learning-web -n <app-name>
```

On tiers supporting slots, create one with `az webapp deployment slot create ... --slot staging`, validate it, then swap deliberately.

## Practice

1. Deploy a hello application and locate its default hostname and outbound addresses.
2. Create a staging-slot checklist covering migrations, settings, health, and rollback.
3. Enable a managed identity and describe a Key Vault reference flow.

## Common mistakes

- Swapping a slot before marking environment-specific settings as sticky
- Storing production secrets directly in application settings or source
- Scaling instances without checking database, connection, and session behavior

## Stretch goal

Add VNet integration for outbound private access and explain how it differs from a private endpoint for inbound access.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
