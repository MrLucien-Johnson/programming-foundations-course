# Capstone: deploy an app to a cluster

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 10 of 10

## Learning goals

By the end of this lesson you will be able to:

- Deploy a production-shaped application with declarative workload, service, config, security, and availability controls
- Demonstrate rollout, autoscaling or capacity behavior, diagnostics, and rollback
- Package manifests and operational evidence for repeatable review

## Why this matters

The capstone proves that individual Kubernetes objects form a resilient and diagnosable application contract rather than an assortment of YAML files.

## Core ideas

1. **Start from an application contract** — image, ports, configuration, health, resources, identity, storage, and traffic.
2. **Safe delivery needs readiness and immutable artifacts** before replicas can protect availability.
3. **Secure defaults are visible in manifests** — non-root, restricted capabilities, scoped identity, and allowed network paths.
4. **Operations are part of done** — dashboards, failure triage, rollback, backup if stateful, and cleanup.

## Worked example

### Capstone: apply and verify an application bundle

```bash
kubectl create namespace capstone
kubectl label namespace capstone   pod-security.kubernetes.io/enforce=restricted
kubectl apply -n capstone -f k8s/
kubectl rollout status deployment/api -n capstone --timeout=3m
kubectl get deploy,pod,service,endpointslice,hpa,pvc -n capstone
kubectl wait -n capstone --for=condition=Ready pod   -l app=api --timeout=2m
kubectl run smoke -n capstone --rm -i --restart=Never   --image=curlimages/curl -- http://api/health
```

Deploy a bad revision in the lab, identify it through readiness and logs, roll it back, and preserve the command output as evidence.

## Practice

1. Submit manifests for Namespace, Deployment, Service, configuration, identity, policy, and optional storage/ingress.
2. Demonstrate healthy traffic, failed rollout diagnosis, and successful rollback.
3. Run server-side dry-run, manifest validation, access checks, and namespace cleanup.

## Common mistakes

- Submitting generated YAML that cannot be applied in dependency order
- Leaving probes, requests, limits, security context, and image version unspecified
- Calling the capstone complete without a controlled failure and recovery demonstration

## Stretch goal

Package the application as a Helm chart or Kustomize bases/overlays and test it in a second namespace.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
