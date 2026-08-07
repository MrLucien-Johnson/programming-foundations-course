# Deployments & rollouts

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 6 of 10

## Learning goals

By the end of this lesson you will be able to:

- Perform and observe a rolling Deployment update
- Tune surge, unavailable, readiness, and progress-deadline settings
- Pause, resume, and roll back using revision evidence

## Why this matters

A Deployment makes replacement automated, but safe release behavior depends on capacity, readiness, application compatibility, and an observable rollback decision.

## Core ideas

1. **A Deployment manages ReplicaSets** and gradually shifts desired replicas during a rolling update.
2. **`maxSurge` and `maxUnavailable` trade temporary capacity for availability**.
3. **Readiness gates traffic, while `minReadySeconds` and progress deadlines detect unhealthy rollout behavior**.
4. **Rollback restores a pod template revision** but cannot automatically reverse incompatible database or external changes.

## Worked example

### Lab: update, observe, and undo

```bash
kubectl set image deployment/api -n course   api=ghcr.io/example/api:2.0.0 --record
kubectl rollout status deployment/api -n course --timeout=2m
kubectl rollout history deployment/api -n course
kubectl get rs,pods -n course -l app=api

# If health or error signals regress:
kubectl rollout undo deployment/api -n course
kubectl rollout status deployment/api -n course
```

Use immutable image digests in production and record the change reason through your delivery system.

## Practice

1. Set `maxSurge: 1` and `maxUnavailable: 0`, then watch pod replacement.
2. Deploy an intentionally failing readiness probe and inspect rollout status and events.
3. Rollback and verify both Kubernetes state and an application-level request.

## Common mistakes

- Using the mutable `latest` tag and losing artifact identity
- Calling a rollout successful before readiness and service metrics stabilize
- Assuming pod rollback reverses a destructive database migration

## Stretch goal

Implement a canary with a second Deployment and weighted traffic through a capable gateway or service mesh.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
