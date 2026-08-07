# Providers & resources

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 2 of 10

## Learning goals

By the end of this lesson you will be able to:

- Declare providers with explicit source and compatible version constraints
- Configure resources and data sources without hard-coded credentials
- Reason about references, dependency graph, aliases, and replacement behavior

## Why this matters

Providers are executable plugins that control real infrastructure. Their versions, credentials, regions, schemas, and dependency relationships must be deliberate and reviewable.

## Core ideas

1. **`required_providers` records source and version compatibility** while the lock file selects checksummed versions.
2. **Resources manage lifecycle; data sources read existing information** without owning it.
3. **References create implicit dependencies**; `depends_on` is for hidden behavioral dependencies, not routine ordering.
4. **Provider aliases support multiple regions or accounts** and must be passed explicitly into modules.

## Worked example

### Lab: declare and inspect a provider

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "lab" {
  name     = "rg-tf-course"
  location = "UK South"
}
```

```bash
az login
terraform init
terraform providers
terraform validate
terraform plan
```

Use ambient CLI, workload identity, or CI federation; do not put client secrets in provider blocks.

## Practice

1. Pin a provider compatibility range and inspect `.terraform.lock.hcl`.
2. Reference a resource attribute from another resource to create an implicit dependency.
3. Create an aliased second-region provider and pass it to a small module.

## Common mistakes

- Leaving provider origin or version unconstrained
- Hard-coding cloud credentials in `.tf` files
- Adding `depends_on` everywhere instead of using attribute references

## Stretch goal

Upgrade one provider with `terraform init -upgrade`, review schema-driven plan changes, and document the lock-file diff.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
