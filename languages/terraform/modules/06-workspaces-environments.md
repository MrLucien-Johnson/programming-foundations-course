# Workspaces & environments

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 6 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain what CLI workspaces isolate and what they do not
- Choose between workspaces, separate roots, and separate accounts or subscriptions
- Prevent accidental cross-environment credentials, state, and promotion

## Why this matters

Environment isolation is a state, identity, network, and ownership decision. CLI workspaces provide multiple state instances for one configuration but are not a complete security boundary.

## Core ideas

1. **A CLI workspace selects a separate state instance in the same backend configuration**.
2. **Workspaces share configuration and usually backend access** — they do not inherently isolate credentials or permissions.
3. **Separate root configurations and cloud accounts provide stronger blast-radius boundaries** for materially different environments.
4. **Promote reviewed code and immutable versions, not a mutated state file** between environments.

## Worked example

### Lab: observe workspace-specific state

```bash
terraform workspace new dev
terraform apply -auto-approve -var='environment=dev'
terraform workspace new stage
terraform plan -var='environment=stage'
terraform workspace list
terraform workspace show
```

In configuration, avoid silently deriving critical account selection from `terraform.workspace`. Make provider credentials and target account explicit in CI, and store production state under separately protected access where risk requires it.

## Practice

1. Create dev and stage workspaces for a local disposable resource and compare state lists.
2. Threat-model who can read and write each environment's backend and cloud account.
3. Choose an environment layout for sandbox, staging, and production and justify the isolation.

## Common mistakes

- Assuming a workspace creates a cloud account or permission boundary
- Applying while the wrong workspace or provider credentials are active
- Using many conditional expressions until environments no longer share one coherent design

## Stretch goal

Design separate production and non-production roots that consume the same versioned modules through independent pipelines.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
