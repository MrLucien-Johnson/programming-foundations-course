# Cloud Storage & data

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 5 of 10

## Learning goals

By the end of this lesson you will be able to:

- Create a secure Cloud Storage bucket with location, class, and protection features chosen intentionally
- Use uniform bucket-level access and IAM instead of object ACLs
- Select appropriate managed GCP data services for relational, analytical, and document workloads

## Why this matters

Cloud Storage is simple to start but its global namespace, IAM, lifecycle, retention, and egress choices have long-term security and cost consequences.

## Core ideas

1. **Bucket names are globally unique and bucket location is effectively permanent** — choose location before uploading data.
2. **Uniform bucket-level access centralizes authorization in IAM** and disables object ACL complexity.
3. **Storage classes reflect access patterns** — Standard, Nearline, Coldline, and Archive differ in minimum duration and retrieval economics.
4. **Choose data engines by access pattern** — Cloud SQL for relational transactions, Firestore for documents, and BigQuery for analytics.

## Worked example

### Lab: create a protected bucket and lifecycle rule

```bash
BUCKET="gs://$(gcloud config get-value project)-course-data"
gcloud storage buckets create "$BUCKET"   --location=europe-west1   --uniform-bucket-level-access   --public-access-prevention
printf 'event_id,value
1,42
' > /tmp/events.csv
gcloud storage cp /tmp/events.csv "$BUCKET/raw/events.csv"
gcloud storage ls --long "$BUCKET/raw/"
gcloud storage buckets describe "$BUCKET"   --format="yaml(location,storageClass,iamConfiguration)"
```

Add versioning with `gcloud storage buckets update "$BUCKET" --versioning` before testing overwrite recovery.

## Practice

1. Create a private bucket, upload an object, and verify public access prevention.
2. Design a lifecycle rule for temporary exports and a retention policy for regulated records.
3. Match an order database, event document store, and analytics warehouse to Cloud SQL, Firestore, and BigQuery.

## Common mistakes

- Using `allUsers` IAM bindings to solve application access
- Choosing a bucket location without considering compute location and egress
- Treating retention policies as ordinary lifecycle deletion rules

## Stretch goal

Configure a customer-managed encryption key design and document the impact if the KMS key is disabled.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
