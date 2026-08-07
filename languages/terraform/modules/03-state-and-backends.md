# State & backends

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 3 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain why Terraform state maps resource addresses to remote objects
- Configure a remote backend with locking, encryption, access control, and recovery
- Use supported state commands for moves, imports, and removals

## Why this matters

State is operationally sensitive and often contains secrets. A reliable backend prevents conflicting writes, enables team workflows, and makes recovery possible.

## Core ideas

1. **State is Terraform's ownership and identity record** — losing it does not delete infrastructure, but destroys Terraform's mapping.
2. **A backend stores state and may coordinate locking**; backend capabilities differ by implementation.
3. **State can expose sensitive values despite `sensitive = true`** — encrypt it and restrict read access.
4. **Refactors need address migration** through `moved` blocks or `terraform state mv` to avoid accidental replacement.

## Worked example

### Lab: migrate state to a protected backend

```hcl
terraform {
  backend "s3" {
    bucket       = "company-terraform-state"
    key          = "training/app/terraform.tfstate"
    region       = "eu-west-2"
    encrypt      = true
    use_lockfile = true
  }
}
```

```bash
terraform init -migrate-state
terraform state list
terraform state show terraform_data.course
terraform state pull > /tmp/state-backup.json
```

Protect the bucket with versioning, least-privilege IAM, public-access blocking, and tested recovery. Never commit the backup.

## Practice

1. Document backend encryption, locking, versioning, access, and disaster recovery.
2. Use a `moved` block to rename a resource address without recreation.
3. Practice importing a disposable object and reconciling configuration to a no-change plan.

## Common mistakes

- Sharing local state files through Git or chat
- Assuming `sensitive` prevents a value from existing in state
- Using `terraform state rm` as if it deletes the real cloud resource

## Stretch goal

Restore a prior backend object version in an isolated exercise and verify it against remote infrastructure.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
