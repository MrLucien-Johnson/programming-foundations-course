# GKE introduction

**Course:** GCP Cloud Course (donor / allowlist access)  
**Module:** 7 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain the GKE control plane, node, and Kubernetes workload responsibility split
- Create credentials for a cluster and deploy a minimal workload
- Choose Autopilot or Standard based on required control and operations

## Why this matters

GKE provides managed Kubernetes, not operation-free Kubernetes. Teams still own workloads, policy, access, observability, upgrades, and often parts of node and network management.

## Core ideas

1. **Google manages the GKE control plane; responsibility for workloads remains yours** and differs between Autopilot and Standard.
2. **Autopilot manages nodes and enforces workload resource expectations**; Standard provides deeper node and system control.
3. **Workload Identity Federation for GKE maps Kubernetes service accounts to Google identities** without node-wide keys.
4. **Regional clusters and maintenance policies improve availability and upgrade control** but do not fix unhealthy applications.

## Worked example

### Lab: deploy to an Autopilot cluster

```bash
gcloud container clusters create-auto course-cluster   --region=europe-west1 --release-channel=regular
gcloud container clusters get-credentials course-cluster   --region=europe-west1
kubectl create deployment web --image=nginx:1.27
kubectl set resources deployment web   --requests=cpu=100m,memory=128Mi   --limits=cpu=250m,memory=256Mi
kubectl expose deployment web --port=80 --type=ClusterIP
kubectl get pods,service -o wide
```

Delete the cluster after the lab with `gcloud container clusters delete course-cluster --region=europe-west1`.

## Practice

1. Compare GKE Autopilot and Standard for a stateless API and a privileged node agent.
2. Deploy a resource-bounded workload and inspect its events and assigned node.
3. Describe how a Kubernetes service account obtains a Google API identity.

## Common mistakes

- Creating a cluster when Cloud Run would satisfy the workload
- Using node service-account permissions for every pod
- Ignoring release channels, maintenance windows, and version skew

## Stretch goal

Configure Workload Identity Federation for one pod and prove it can access one bucket but not list all projects.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](gcp-course.html) for the full path.
