# Capstone: ship a reusable module

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 10 of 10

## Learning goals

By the end of this lesson you will be able to:

- Deliver a reusable Terraform module with documentation, tests, examples, and version constraints
- Consume the module from a separate root with remote state and a reviewed plan
- Demonstrate safe update, drift handling, and cleanup

## Why this matters

The capstone proves not only HCL fluency but the full infrastructure product lifecycle: interface design, validation, state, testing, delivery, operations, and consumer experience.

## Core ideas

1. **Choose one bounded capability** such as a secure storage bucket, network, or small web-service foundation.
2. **The module is a product** — inputs, outputs, defaults, compatibility, examples, tests, and upgrade notes form its contract.
3. **The consumer root owns environment concerns** including backend, credentials, provider configuration, and promotion.
4. **Evidence matters** — show clean checks, reviewed plan, apply, functional verification, no-change plan, and destroy or retention decision.

## Worked example

### Capstone: verify a reusable module and consumer

```bash
terraform fmt -check -recursive
terraform -chdir=modules/secure-storage init -backend=false
terraform -chdir=modules/secure-storage validate
terraform -chdir=modules/secure-storage test

terraform -chdir=examples/basic init
terraform -chdir=examples/basic plan -out=tfplan
terraform -chdir=examples/basic show -no-color tfplan
terraform -chdir=examples/basic apply tfplan
terraform -chdir=examples/basic plan -detailed-exitcode
```

The module should enforce private access and encryption, emit useful identifiers, and document migration and destruction behavior. Run a reviewed destroy for disposable infrastructure.

## Practice

1. Publish module files, README, example, tests, changelog, and compatibility constraints.
2. Use a separate consumer root and remote backend to prove real composition.
3. Demonstrate invalid-input failure, successful apply, functional check, no-change plan, and cleanup.

## Common mistakes

- Embedding backend configuration or environment credentials inside the child module
- Claiming reusability without a second consumer example or tests
- Destroying retained data during demonstration without backup and explicit approval

## Stretch goal

Tag a semantic release, consume that exact version from another repository, and complete a backward-compatible upgrade.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
