# CI for Terraform

**Course:** Terraform & IaC Course (donor / allowlist access)  
**Module:** 9 of 10

## Learning goals

By the end of this lesson you will be able to:

- Build a CI workflow for format, validation, tests, plan review, and controlled apply
- Use workload identity federation and protected environments instead of static cloud keys
- Prevent concurrent state writes and preserve auditable plan evidence

## Why this matters

CI turns Terraform from a developer command into a controlled team delivery process. Identity, plan integrity, serialization, and approvals determine whether automation is safer than laptops.

## Core ideas

1. **Pull requests should produce readable plans without applying production changes**.
2. **Apply from a trusted branch and protected environment** using the reviewed commit and controlled approval.
3. **OIDC federation exchanges CI identity for short-lived cloud credentials** instead of storing long-lived secrets.
4. **Concurrency controls complement backend locking** by preventing avoidable competing runs for the same environment.

## Worked example

### Lab: shape a safe GitHub Actions plan job

```yaml
permissions:
  contents: read
  id-token: write
  pull-requests: write
concurrency:
  group: terraform-production
  cancel-in-progress: false
steps:
  - uses: actions/checkout@v4
  - uses: hashicorp/setup-terraform@v3
  - run: terraform fmt -check -recursive
  - run: terraform init -input=false
  - run: terraform validate
  - run: terraform test
  - run: terraform plan -input=false -out=tfplan
  - run: terraform show -no-color tfplan > plan.txt
```

Configure the cloud's OIDC trust outside this snippet. Store the plan as a restricted, short-retention artifact and apply only after verifying the commit and environment approval.

## Practice

1. Create separate PR plan and protected-branch apply workflows.
2. Configure or diagram OIDC trust claims restricted to repository, branch, and environment.
3. Test two queued runs and confirm concurrency plus backend locking prevent overlap.

## Common mistakes

- Storing cloud access keys as long-lived repository secrets
- Applying after merge by generating a different unreviewed plan with changed inputs
- Posting plans publicly even though values and structure may be sensitive

## Stretch goal

Add drift detection that opens a review signal without automatically overwriting intentional emergency changes.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](terraform-course.html) for the full path.
