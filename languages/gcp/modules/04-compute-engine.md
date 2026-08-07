# Compute Engine

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 4 of 10

## Learning goals

By the end of this lesson you will be able to:

- Create a hardened Compute Engine VM with suitable machine, disk, identity, and network settings
- Explain instance templates, managed instance groups, health checks, and autoscaling
- Choose Spot VMs only for interruption-tolerant work

## Why this matters

Compute Engine offers low-level flexibility, but that flexibility includes patching, image, identity, firewall, availability, and lifecycle responsibilities.

## Core ideas

1. **Machine families optimize different constraints** — general purpose, compute, memory, accelerator, and cost profiles differ.
2. **Instance templates make VM configuration repeatable** and underpin managed instance groups.
3. **Managed instance groups repair and scale identical instances** using health checks and autoscaling signals.
4. **Shielded VM, OS Login, and least-privilege service accounts improve the baseline** without embedded SSH keys or broad API scopes.

## Worked example

### Lab: create a private, low-cost VM

```bash
gcloud compute instances create vm-lab   --zone=europe-west1-b   --machine-type=e2-micro   --subnet=app-eu --no-address   --service-account=app-runtime@$(gcloud config get-value project).iam.gserviceaccount.com   --scopes=cloud-platform   --shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring   --labels=environment=lab,owner=student
gcloud compute instances describe vm-lab --zone=europe-west1-b   --format="yaml(status,networkInterfaces,serviceAccounts)"
gcloud compute instances stop vm-lab --zone=europe-west1-b
```

## Practice

1. Compare E2, N2, and memory-optimized machines for three workload profiles.
2. Create and inspect a private VM, then stop and delete it.
3. Sketch a regional managed instance group with health checks and an autoscaling target.

## Common mistakes

- Using the default service account with broad historical permissions
- Assigning external IPs and public SSH rules to every VM
- Running stateful or non-checkpointed work on Spot VMs

## Stretch goal

Build an instance template and rolling-update plan with canary percentage, surge, and unavailable limits.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
