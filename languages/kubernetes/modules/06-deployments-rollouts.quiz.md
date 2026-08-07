# Quiz — Deployments & rollouts

1. What object stores a Deployment revision's pod template?
   - A. ReplicaSet
   - B. Service
   - C. ConfigMap
   - D. Node

2. What does `maxUnavailable: 0` require during rollout?
   - A. No desired replica may be unavailable
   - B. No surge is allowed
   - C. No image pull occurs
   - D. No probes run

3. What command restores a prior Deployment revision?
   - A. kubectl rollout undo
   - B. kubectl delete node
   - C. kubectl expose
   - D. kubectl auth reconcile

4. Does rollback reverse a database migration?
   - A. Always
   - B. No; it needs a compatible data strategy
   - C. Only for StatefulSets
   - D. Only if DNS is enabled

5. Why use an image digest?
   - A. It identifies immutable content
   - B. It increases replicas
   - C. It grants RBAC
   - D. It creates TLS
