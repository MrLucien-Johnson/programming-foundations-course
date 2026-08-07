# Cloud Run

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 6 of 10

## Learning goals

By the end of this lesson you will be able to:

- Deploy a stateless container to Cloud Run with deliberate ingress and authentication
- Configure revisions, traffic splitting, concurrency, scaling, and resource limits
- Use a service identity and Secret Manager without embedding credentials

## Why this matters

Cloud Run turns a container into an autoscaling HTTPS service while preserving revision and identity controls. It is often a better fit than managing VMs or Kubernetes for stateless services.

## Core ideas

1. **A deployment creates an immutable revision** — configuration and image changes can receive percentages of traffic.
2. **Scale-to-zero and request-based autoscaling fit bursty services** — minimum instances trade cost for reduced cold starts.
3. **Ingress and IAM are separate controls** — network reachability does not automatically grant invocation.
4. **Concurrency and CPU/memory settings affect latency, throughput, and cost** — measure rather than relying on defaults.

## Worked example

### Lab: deploy an authenticated Cloud Run service

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
gcloud run deploy hello-api   --source=. --region=europe-west1   --service-account=app-runtime@$(gcloud config get-value project).iam.gserviceaccount.com   --no-allow-unauthenticated   --ingress=all --concurrency=40 --max-instances=5   --set-env-vars=APP_ENV=lab
URL=$(gcloud run services describe hello-api --region=europe-west1   --format='value(status.url)')
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" "$URL/health"
gcloud run revisions list --service=hello-api --region=europe-west1
```

## Practice

1. Deploy an authenticated service and invoke it with an identity token.
2. Create a new revision and shift 10% of traffic to it before full promotion.
3. Load test two concurrency settings and compare latency and instance count.

## Common mistakes

- Using `--allow-unauthenticated` without an explicit public API requirement
- Writing durable application state to the container filesystem
- Setting unlimited scaling without protecting downstream database capacity

## Stretch goal

Connect Cloud Run to a private database through Direct VPC egress and retrieve credentials from Secret Manager.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
