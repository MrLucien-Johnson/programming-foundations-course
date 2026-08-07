# IAM & org policy

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 2 of 10

## Learning goals

By the end of this lesson you will be able to:

- Model GCP IAM as principal, role, resource, and inherited policy
- Use predefined roles and service-account impersonation instead of broad basic roles and keys
- Explain how organization policies constrain configurations independently of IAM

## Why this matters

GCP IAM controls who can act, while organization policy constrains which configurations are allowed. Both are needed to reduce privilege and enforce guardrails at scale.

## Core ideas

1. **Allow policies bind principals to roles on resources** and inherit down the resource hierarchy.
2. **Predefined roles are usually safer than basic Owner/Editor/Viewer roles** because they express narrower service permissions.
3. **Service accounts are workload identities** — short-lived tokens and impersonation avoid downloadable keys.
4. **Organization policies set constraints** such as allowed regions or disabled service-account key creation; they do not grant API permissions.

## Worked example

### Lab: grant a service account a narrow project role

```bash
PROJECT_ID=$(gcloud config get-value project)
gcloud iam service-accounts create app-runtime   --display-name="Application runtime"
gcloud projects add-iam-policy-binding "$PROJECT_ID"   --member="serviceAccount:app-runtime@${PROJECT_ID}.iam.gserviceaccount.com"   --role="roles/logging.logWriter"
gcloud projects get-iam-policy "$PROJECT_ID"   --flatten="bindings[].members"   --filter="bindings.members:app-runtime"   --format="table(bindings.role)"
```

For administration, test impersonation with `gcloud ... --impersonate-service-account=<service-account-email>` rather than creating a JSON key.

## Practice

1. Translate three job tasks into predefined roles at project or resource scope.
2. Inspect inherited and direct IAM bindings for a project.
3. Compare an IAM denial with an organization-policy constraint in a troubleshooting note.

## Common mistakes

- Granting `roles/editor` to every human or workload
- Creating long-lived service-account keys when attached identity or impersonation works
- Expecting organization policy to grant a caller missing IAM permission

## Stretch goal

Design a conditional IAM binding that expires or applies only to a named resource.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
