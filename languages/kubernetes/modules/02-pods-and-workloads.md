# Pods & workloads

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 2 of 10

## Learning goals

By the end of this lesson you will be able to:

- Describe pods as co-scheduled containers sharing network and selected volumes
- Choose Deployment, StatefulSet, DaemonSet, Job, or CronJob by workload behavior
- Configure resource requests, limits, probes, and restart behavior

## Why this matters

A pod is Kubernetes' scheduling unit, but controllers make applications resilient. Correct workload type and runtime contract determine whether recovery and scaling behave safely.

## Core ideas

1. **Containers in one pod share an IP and localhost** and should have a tight lifecycle reason to be co-located.
2. **Deployments suit replaceable replicas; StatefulSets add stable identity; DaemonSets place per-node agents**.
3. **Jobs finish; CronJobs schedule Jobs** — they are better than keeping a server alive for batch work.
4. **Requests guide scheduling, limits constrain use, and probes communicate health stages**.

## Worked example

### Lab: create a resource-aware Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: api, namespace: course}
spec:
  replicas: 2
  selector: {matchLabels: {app: api}}
  template:
    metadata: {labels: {app: api}}
    spec:
      containers:
        - name: api
          image: nginx:1.27
          resources:
            requests: {cpu: 100m, memory: 128Mi}
            limits: {cpu: 500m, memory: 256Mi}
          readinessProbe:
            httpGet: {path: /, port: 80}
            initialDelaySeconds: 2
```

```bash
kubectl apply -f deployment.yaml
kubectl describe pod -n course -l app=api
```

## Practice

1. Match five sample workloads to Deployment, StatefulSet, DaemonSet, Job, or CronJob.
2. Add startup, readiness, and liveness probes with different purposes.
3. Cause an OOM limit failure in a disposable lab and inspect status and events.

## Common mistakes

- Running unrelated processes in one pod
- Omitting requests and making scheduling and capacity unpredictable
- Using a liveness probe that restarts a healthy but temporarily unready application

## Stretch goal

Add topology spread constraints so replicas distribute across zones without making scheduling impossible.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
