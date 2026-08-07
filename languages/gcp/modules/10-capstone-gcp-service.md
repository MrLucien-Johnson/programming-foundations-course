# Capstone: ship on Cloud Run

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 10 of 10

## Learning goals

By the end of this lesson you will be able to:

- Ship a Cloud Run service using Artifact Registry, a dedicated identity, private data, and observability
- Demonstrate authenticated invocation, revision rollout, rollback, and cost controls
- Produce reproducible deployment and cleanup evidence

## Why this matters

The capstone validates that GCP projects, IAM, networking, managed compute, storage, operations, and billing controls form one secure service.

## Core ideas

1. **Use a dedicated project or clearly labelled lab scope** to isolate APIs, IAM, quotas, and billing.
2. **Build once and deploy an immutable image digest** so the tested artifact is the released artifact.
3. **The runtime service account receives only required roles** and humans deploy through auditable identities.
4. **Release evidence includes telemetry and rollback** rather than only an HTTP 200 response.

## Worked example

### Capstone: build and release a small API

```bash
REGION=europe-west1
PROJECT_ID=$(gcloud config get-value project)
gcloud artifacts repositories create capstone   --repository-format=docker --location="$REGION"
gcloud builds submit   --tag "$REGION-docker.pkg.dev/$PROJECT_ID/capstone/api:v1"
gcloud run deploy capstone-api   --image "$REGION-docker.pkg.dev/$PROJECT_ID/capstone/api:v1"   --region="$REGION"   --service-account="app-runtime@$PROJECT_ID.iam.gserviceaccount.com"   --no-allow-unauthenticated --max-instances=5
gcloud run services describe capstone-api --region="$REGION"   --format='yaml(status.url,status.traffic)'
```

Attach private Cloud Storage access, emit structured logs, deploy `v2` as a no-traffic revision, test it by tag, then shift traffic and demonstrate rollback.

## Practice

1. Present a diagram of project, caller, Cloud Run revision, service account, storage, and telemetry.
2. Prove denied anonymous invocation and successful identity-token invocation.
3. Capture release, error query, traffic rollback, billing alert, and cleanup output.

## Common mistakes

- Making the service or bucket public to bypass IAM troubleshooting
- Deploying mutable `latest` without recording the image digest
- Leaving Artifact Registry images, revisions, buckets, or billable resources unreviewed

## Stretch goal

Add a global external Application Load Balancer with managed TLS, a custom domain, and Cloud Armor policy.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
