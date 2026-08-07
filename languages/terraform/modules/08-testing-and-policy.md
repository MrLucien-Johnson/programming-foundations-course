# Testing & policy

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 8 of 10

## Learning goals

By the end of this lesson you will be able to:

- Layer formatting, validation, linting, native tests, plans, and integration checks
- Write a Terraform test with assertions
- Use policy as code to block dangerous plan characteristics

## Why this matters

Syntax-valid infrastructure can still be insecure, expensive, or functionally wrong. Layered tests and policy catch different defect classes before or after real APIs are touched.

## Core ideas

1. **Static checks are fast and broad** — formatting, validation, linting, and security scanning should run before cloud tests.
2. **`terraform test` executes run blocks and assertions** using plan or apply modes according to the test design.
3. **Plan inspection tests proposed values and actions** without pretending every unknown value is final.
4. **Policy as code enforces organizational boundaries** such as allowed regions, encryption, tags, and prohibited public exposure.

## Worked example

### Lab: assert a module contract

```hcl
# tests/defaults.tftest.hcl
run "plan_defaults" {
  command = plan

  variables {
    environment = "dev"
  }

  assert {
    condition     = output.labels["environment"] == "dev"
    error_message = "The environment label must match the input."
  }
}
```

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
terraform test
```

Add a policy/scanner check that rejects public access or missing encryption, and maintain explicit, reviewed exceptions.

## Practice

1. Write tests for a default, an override, and an invalid input.
2. Run a linter and security scanner, then classify findings rather than blindly suppressing them.
3. Draft a policy rule that denies public storage unless an approved exception exists.

## Common mistakes

- Treating `terraform validate` as proof that infrastructure is secure
- Writing only apply-based tests and leaking costly fixtures after failures
- Adding broad policy suppressions with no owner, reason, or expiry

## Stretch goal

Create an ephemeral integration test that applies, probes a real endpoint, and always destroys through a controlled cleanup job.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
