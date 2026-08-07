# Billing & cost control

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 9 of 10

## Learning goals

By the end of this lesson you will be able to:

- Relate billing accounts, projects, budgets, quotas, labels, and detailed exports
- Analyze cost before choosing rightsizing, scheduling, commitment, or storage actions
- Explain why budgets and quotas are guardrails rather than universal hard stops

## Why this matters

GCP costs follow architecture and usage. Attribution, exports, and accountable alerts make optimization evidence-based rather than a sequence of risky guesses.

## Core ideas

1. **A billing account pays for linked projects** while IAM on billing and projects remains separate.
2. **Budgets notify on actual or forecasted spend** but generally do not cap usage automatically.
3. **Billing export to BigQuery enables SKU-level analysis** and joins cost with labels and business metadata.
4. **Commit only after measuring stable demand** — committed use discounts exchange flexibility for a term commitment.

## Worked example

### Lab: inspect project billing and labelled resources

```bash
PROJECT_ID=$(gcloud config get-value project)
gcloud billing projects describe "$PROJECT_ID"
gcloud billing budgets list --billing-account=<billing-account-id>
gcloud compute instances list   --format='table(name,zone,machineType.basename(),status,labels)'
gcloud storage buckets list   --format='table(name,location,storageClass)'
```

Enable detailed billing export to BigQuery, then query cost by `project.id`, `service.description`, `sku.description`, and credits before recommending changes.

## Practice

1. Define budget thresholds for actual and forecasted spend with named recipients.
2. Identify idle VMs, unattached disks, stale snapshots, and oversized log retention.
3. Write a BigQuery billing-export query plan grouped by project, service, SKU, and label.

## Common mistakes

- Assuming a budget automatically shuts down resources
- Buying commitments from a short or highly variable usage sample
- Deleting resources based only on low CPU without checking memory, latency, or business schedule

## Stretch goal

Design a Pub/Sub budget-notification workflow with approvals and resource-specific safe actions.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
