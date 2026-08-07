# Quiz — Capstone: deploy an app to a cluster

1. What should gate Service traffic during a rollout?
   - A. Readiness
   - B. Image size
   - C. Namespace age
   - D. PVC name

2. What proves manifests are operable?
   - A. Apply, smoke test, failure diagnosis, and rollback evidence
   - B. YAML syntax alone
   - C. A public NodePort
   - D. Cluster-admin access

3. Why include requests and limits?
   - A. For scheduling, capacity, and containment
   - B. To create DNS
   - C. To configure RBAC
   - D. To encrypt etcd

4. What should identify the deployed artifact?
   - A. An immutable image tag or digest
   - B. `latest` only
   - C. A pod name
   - D. A node IP

5. What closes a temporary capstone environment?
   - A. Verified cleanup
   - B. Leaving the namespace
   - C. Disabling probes
   - D. Deleting logs first
