# GCP foundations & projects

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 1 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain the GCP resource hierarchy from organization and folders to projects and resources
- Select a region or zone based on availability, latency, residency, and service support
- Initialize `gcloud`, choose a project explicitly, and inspect enabled services

## Why this matters

Projects are GCP's central boundary for APIs, IAM, quotas, and billing. Deliberate project and location choices keep experiments isolated and production governable.

## Core ideas

1. **Organization → folders → projects → resources** provides inheritance for IAM and organization policies.
2. **Projects are durable isolation boundaries** — every project has a name, immutable project ID, and numeric project number.
3. **Regions contain zones** — regional services can survive zonal failure; multi-region services trade control for broader placement.
4. **APIs are enabled per project** — permission alone is insufficient when the service API is disabled.

## Worked example

### Lab: establish explicit GCP context

```bash
gcloud auth login
gcloud projects list
gcloud config configurations create cloud-course
gcloud config set project <project-id>
gcloud config set compute/region europe-west1
gcloud config set compute/zone europe-west1-b
gcloud services list --enabled
gcloud auth list
```

Confirm the project printed by `gcloud config list --format='text(core.project)'` before creating or deleting anything.

## Practice

1. Draw a folder and project hierarchy for platform, production, development, and sandbox teams.
2. Compare two regions for service availability and data-residency requirements.
3. Create a named CLI configuration and verify project, account, region, and zone.

## Common mistakes

- Confusing a project's display name with its globally unique project ID
- Running commands against the previously active project
- Assuming all services and machine types exist in every region or zone

## Stretch goal

Design a project-factory checklist covering billing attachment, APIs, labels, logging, and baseline IAM.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
