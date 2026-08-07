# VPC networking

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 3 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain GCP's global VPC and regional subnet model
- Configure routes, hierarchical or VPC firewall rules, Cloud NAT, and private service access appropriately
- Use GCP flow and connectivity tools to diagnose a path

## Why this matters

Unlike many cloud networks, a GCP VPC is global while its subnets are regional. Understanding this model prevents accidental exposure and incorrect multi-region designs.

## Core ideas

1. **A GCP VPC is global; subnets are regional** — one VPC can contain non-overlapping subnets in many regions.
2. **Firewall rules are stateful and apply to VM network interfaces** using targets such as service accounts or secure network tags.
3. **Routes select next hops** — system-generated subnet routes, custom static routes, and dynamic Cloud Router routes can coexist.
4. **Cloud NAT gives outbound internet access without inbound public IPs**; Private Google Access reaches Google APIs from private addresses.

## Worked example

### Lab: custom-mode VPC with private VM egress design

```bash
gcloud compute networks create app-vpc --subnet-mode=custom
gcloud compute networks subnets create app-eu   --network=app-vpc --region=europe-west1   --range=10.60.0.0/20 --enable-private-ip-google-access
gcloud compute firewall-rules create allow-internal-app   --network=app-vpc --direction=INGRESS --action=ALLOW   --rules=tcp:8080 --source-ranges=10.60.0.0/20   --target-service-accounts=app-runtime@$(gcloud config get-value project).iam.gserviceaccount.com
gcloud compute routes list --filter="network:app-vpc"
```

Add Cloud Router and Cloud NAT for controlled outbound access; do not assign public VM addresses merely for package downloads.

## Practice

1. Plan two regional subnets in one global custom-mode VPC without overlap.
2. Create a firewall rule targeted to a service account rather than all instances.
3. Trace private VM access to Google APIs, the internet through Cloud NAT, and another region.

## Common mistakes

- Describing a GCP VPC as regional or creating one VPC per zone by habit
- Using broad `0.0.0.0/0` SSH rules and mutable network tags
- Assuming Cloud NAT accepts unsolicited inbound internet connections

## Stretch goal

Design Shared VPC host and service projects with centrally managed subnets and delegated workload administration.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
