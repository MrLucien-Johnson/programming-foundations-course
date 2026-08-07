# Why IaC & Terraform

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 1 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain infrastructure as code as a reviewed desired-state workflow
- Describe Terraform configuration, state, planning, and provider APIs
- Import or recreate infrastructure without treating generated code as unquestioned truth

## Why this matters

Infrastructure as code makes changes reviewable, repeatable, and auditable. Terraform adds dependency-aware planning, but safe use still depends on state discipline and human review.

## Core ideas

1. **Configuration declares desired infrastructure** while providers translate resource operations to platform APIs.
2. **Terraform compares configuration, prior state, and refreshed remote objects** to propose a plan.
3. **Idempotent convergence is the goal** — repeated applies should settle with no changes when inputs and remote systems are stable.
4. **IaC is a team process** — version control, review, testing, promotion, and recovery matter more than syntax alone.

## Worked example

### Lab: inspect the Terraform workflow locally

```hcl
terraform {
  required_version = ">= 1.8"
}

resource "terraform_data" "course" {
  input = {
    owner       = "student"
    environment = "lab"
  }
}
```

```bash
terraform fmt -check
terraform init
terraform validate
terraform plan -out=tfplan
terraform show tfplan
terraform apply tfplan
terraform plan -detailed-exitcode
```

A final exit code of `0` means no diff; `2` means a non-empty plan; `1` means an error.

## Practice

1. Explain each workflow step from configuration change through reviewed apply.
2. Create a local `terraform_data` resource and reach a no-change second plan.
3. Compare Terraform with an imperative provisioning script for rollback, drift, and review.

## Common mistakes

- Treating an approved plan as optional before production apply
- Editing state by hand or committing it to Git
- Assuming declarative configuration makes every change nondestructive

## Stretch goal

Import a disposable existing resource into a resource block and verify a no-change plan.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
