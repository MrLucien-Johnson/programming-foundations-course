# Autoscaling basics

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 7 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain Horizontal Pod Autoscaler, Vertical Pod Autoscaler, and node autoscaler responsibilities
- Configure an HPA using meaningful requests and metrics
- Recognize stabilization, startup, capacity, and downstream bottlenecks

## Why this matters

Autoscaling turns demand signals into capacity changes, but missing requests, lagging metrics, slow startup, and constrained dependencies can make scaling unstable or ineffective.

## Core ideas

1. **HPA changes replica count from observed metrics**; CPU utilization is measured relative to container requests.
2. **VPA recommends or changes pod resources** and can conflict with HPA when both act on the same CPU or memory signal.
3. **Node autoscaling supplies schedulable infrastructure** when pods remain pending for supported capacity reasons.
4. **Scaling is a feedback loop** — tolerance, stabilization windows, startup delay, quotas, and maximums prevent runaway behavior.

## Worked example

### Lab: create and inspect an HPA

```bash
kubectl set resources deployment/api -n course   --requests=cpu=100m,memory=128Mi   --limits=cpu=500m,memory=256Mi
kubectl autoscale deployment api -n course   --cpu-percent=60 --min=2 --max=10
kubectl get hpa -n course --watch
kubectl describe hpa api -n course
```

This requires a functioning resource metrics pipeline such as Metrics Server. Generate controlled load and observe replicas, pending pods, latency, and dependency saturation together.

## Practice

1. Create an HPA and explain how a 100m request affects displayed CPU utilization.
2. Load test until replicas increase, then observe scale-down stabilization.
3. List reasons pods can remain Pending even when an HPA asks for more replicas.

## Common mistakes

- Enabling CPU HPA without CPU requests
- Setting a high maximum that overwhelms a fixed-size database
- Expecting HPA to add cluster nodes or fix a slow-starting application by itself

## Stretch goal

Scale on a custom queue-depth metric and derive a target from per-replica processing capacity.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
