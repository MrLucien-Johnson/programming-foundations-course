# Observability on Kubernetes

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 8 of 10

## Learning goals

By the end of this lesson you will be able to:

- Collect and correlate Kubernetes events, logs, metrics, and traces
- Use `kubectl` diagnostics without relying on interactive changes inside containers
- Define workload golden signals and alert from user impact

## Why this matters

Kubernetes adds scheduling and control-plane layers to application failures. Effective observability connects platform state to request behavior instead of collecting disconnected dashboards.

## Core ideas

1. **Events explain recent control-plane decisions** but have limited retention and are not a durable audit stream.
2. **Container logs should flow to a node-level collector** because local pod files disappear.
3. **Metrics expose trends and saturation; traces preserve request causality** across services.
4. **Labels enable correlation but unbounded values cause metric-cardinality and cost problems**.

## Worked example

### Lab: triage a failing workload

```bash
kubectl get pods -n course -o wide
kubectl describe pod -n course <pod-name>
kubectl logs -n course <pod-name> --all-containers --since=10m
kubectl logs -n course <pod-name> --previous
kubectl get events -n course   --sort-by=.metadata.creationTimestamp
kubectl top pods -n course
```

Start with the user symptom, then correlate pod restarts, readiness, resource saturation, recent revisions, application errors, and dependency traces.

## Practice

1. Diagnose CrashLoopBackOff, ImagePullBackOff, and Pending scenarios from evidence.
2. Define traffic, errors, latency, and saturation signals for one Service.
3. Propagate a request ID or trace context through two sample services.

## Common mistakes

- Using only `kubectl logs` and ignoring events, prior containers, and metrics
- Adding pod UID, request ID, or customer ID as an unbounded metric label
- Alerting on platform noise with no user impact or response action

## Stretch goal

Instrument an application with OpenTelemetry and correlate one trace with Kubernetes metadata and logs.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
