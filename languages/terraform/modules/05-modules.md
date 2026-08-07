# Modules

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 5 of 10

## Learning goals

By the end of this lesson you will be able to:

- Build a focused reusable module with a stable input and output contract
- Call and version local or registry modules safely
- Refactor resources into a module without unintended destruction

## Why this matters

Modules encode an infrastructure capability and its safe defaults. Good modules reduce repetition without hiding critical decisions or creating a universal abstraction.

## Core ideas

1. **The root module composes; child modules encapsulate a coherent capability** such as a network or service.
2. **A module interface should be small, typed, documented, and opinionated** while exposing necessary decisions.
3. **Module sources should be versioned or pinned** so reviewed code cannot change silently.
4. **Moving existing resources into modules requires state-address migration** with `moved` blocks.

## Worked example

### Lab: call a small local module

```hcl
module "labels" {
  source = "./modules/labels"

  application = "payments"
  environment = "dev"
  extra_tags  = { owner = "platform" }
}

output "labels" {
  value = module.labels.values
}
```

```bash
terraform fmt -recursive
terraform init
terraform validate
terraform plan
terraform providers
```

Inside `modules/labels`, include `variables.tf`, `main.tf`, `outputs.tf`, and a README with examples and compatibility requirements.

## Practice

1. Extract one cohesive resource group into a child module with typed inputs.
2. Add a `moved` block from the old root address to the module address and confirm no replacement.
3. Write a minimal example that exercises the module's default and optional behavior.

## Common mistakes

- Building one giant module that exposes every provider argument
- Using an unpinned Git branch as a production module source
- Copying resources into a module without moving their state addresses

## Stretch goal

Publish the module contract with semantic versioning and a migration note for one intentional breaking change.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
