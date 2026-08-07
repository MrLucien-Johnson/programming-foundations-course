# Variables & outputs

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 4 of 10

## Learning goals

By the end of this lesson you will be able to:

- Design typed, validated input variables with safe defaults
- Use locals to name transformations and outputs as module interfaces
- Pass secrets without exposing them in source, plans, logs, or state unnecessarily

## Why this matters

Inputs and outputs are Terraform's public interface. Strong types and validation catch mistakes early, while disciplined secret handling limits accidental disclosure.

## Core ideas

1. **Type constraints define shape, not just documentation** — objects and collections make module contracts explicit.
2. **Validation rejects invalid intent before provider calls** and preconditions can assert relationships using resource context.
3. **Locals reduce repetition but do not create configurable inputs**.
4. **`sensitive` redacts common CLI display; it does not encrypt values or remove them from state**.

## Worked example

### Lab: create a validated module interface

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
  validation {
    condition     = contains(["dev", "stage", "prod"], var.environment)
    error_message = "environment must be dev, stage, or prod."
  }
}

variable "tags" {
  type    = map(string)
  default = {}
}

locals {
  common_tags = merge(var.tags, { environment = var.environment })
}

output "resource_id" {
  value       = terraform_data.course.id
  description = "Stable identifier for downstream automation"
}
```

```bash
terraform plan -var='environment=dev'
terraform output -json
```

## Practice

1. Add numeric range and allowed-value validations to two variables.
2. Replace duplicated naming and tags with readable locals.
3. Mark a disposable value sensitive and inspect plan, state implications, and JSON output handling.

## Common mistakes

- Using `type = any` when a stable object contract is known
- Putting production secrets in committed `.tfvars` files
- Changing an output casually when downstream automation depends on its name and type

## Stretch goal

Build an object variable with optional attributes and cross-field validation for a service configuration.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
