# Plan, apply, destroy

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 7 of 10

## Learning goals

By the end of this lesson you will be able to:

- Read plan actions, replacements, unknown values, and dependency effects
- Apply the exact reviewed saved plan
- Use lifecycle and destroy operations without masking unsafe design

## Why this matters

Terraform's safety comes from understanding and approving a concrete change set. Automatic apply without plan integrity can turn a small configuration edit into a large outage.

## Core ideas

1. **Plan symbols communicate lifecycle** — create, update, destroy, and replace must be reviewed with context.
2. **A saved plan binds the reviewed actions and variable values** but may contain sensitive information and can become stale.
3. **Replacement can cascade through references** and create downtime when names, quotas, or lifecycle do not allow overlap.
4. **Destroy is an intentional graph operation** — production protection needs policy, access control, backups, and lifecycle safeguards.

## Worked example

### Lab: save, inspect, and apply one plan

```bash
terraform fmt -check
terraform validate
terraform plan -out=tfplan -detailed-exitcode
# exit 0: no changes, 1: error, 2: changes
terraform show -no-color tfplan
terraform apply tfplan
terraform plan -detailed-exitcode
```

For a disposable lab only:

```bash
terraform plan -destroy -out=destroy.tfplan
terraform show destroy.tfplan
terraform apply destroy.tfplan
```

Treat plan files as sensitive artifacts and never reuse them after unrelated remote changes.

## Practice

1. Identify create, in-place update, replacement, and delete actions in sample plans.
2. Trigger a safe replacement in a lab and note ordering and downtime implications.
3. Add `prevent_destroy` to a critical sample resource and test the resulting plan failure.

## Common mistakes

- Piping an unreviewed plan directly into automatic production apply
- Assuming `create_before_destroy` always works despite unique names or quotas
- Using `-target` as a normal deployment workflow and leaving an incomplete graph

## Stretch goal

Write a plan-review checklist that flags deletes, replacements, IAM, public exposure, cost, and unknown values.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
