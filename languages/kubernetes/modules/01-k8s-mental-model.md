# Kubernetes mental model

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 1 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain desired-state reconciliation across the API server, controllers, scheduler, nodes, and kubelet
- Use declarative manifests and labels to inspect cluster objects
- Separate cluster, namespace, and workload responsibilities

## Why this matters

Kubernetes is a control system, not a collection of imperative container commands. Its reconciliation model explains both normal behavior and most troubleshooting paths.

## Core ideas

1. **The API server stores declared intent** and validates requests; etcd persists cluster state.
2. **Controllers reconcile actual state toward desired state** repeatedly rather than running a one-time script.
3. **The scheduler chooses a node; kubelet realizes pod state on that node** through the container runtime.
4. **Labels identify sets; namespaces scope names and policy** but are not complete security boundaries by themselves.

## Worked example

### Lab: observe reconciliation

```bash
kubectl cluster-info
kubectl create namespace course
kubectl create deployment web --image=nginx:1.27   --replicas=2 --namespace=course
kubectl get deployment,replicaset,pods -n course   --show-labels --watch
```

In another terminal, delete one pod:

```bash
kubectl delete pod -n course   $(kubectl get pod -n course -o jsonpath='{.items[0].metadata.name}')
```

The ReplicaSet controller creates a replacement because the Deployment still declares two replicas.

## Practice

1. Trace a Deployment request from `kubectl` to a running container.
2. Delete a managed pod and record the controller events that follow.
3. Label two objects and select them with `kubectl get ... -l key=value`.

## Common mistakes

- Editing containers inside pods as if they were durable servers
- Assuming a namespace alone provides strong tenant isolation
- Treating `kubectl` output as the source of truth instead of the API objects

## Stretch goal

Inspect owner references from Pod to ReplicaSet to Deployment and explain garbage collection.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
