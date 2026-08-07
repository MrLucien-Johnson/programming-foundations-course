# Storage & persistent volumes

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 5 of 10

## Learning goals

By the end of this lesson you will be able to:

- Explain PersistentVolume, PersistentVolumeClaim, StorageClass, and CSI driver roles
- Select access mode, volume mode, capacity, reclaim policy, and binding behavior
- Protect stateful data during workload and namespace lifecycle changes

## Why this matters

Containers are disposable, but application data may not be. Kubernetes storage separates workload claims from infrastructure provisioning while preserving provider-specific constraints.

## Core ideas

1. **A PVC requests storage; a PV represents supplied storage** and binding connects compatible objects.
2. **StorageClasses define dynamic provisioning and policy** such as type, expansion, reclaim behavior, and binding mode.
3. **Access modes describe attachment semantics** but actual multi-writer support depends on the storage system.
4. **StatefulSet volumeClaimTemplates give each replica stable storage identity**; they do not create database replication.

## Worked example

### Lab: request and mount persistent storage

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata: {name: app-data, namespace: course}
spec:
  accessModes: [ReadWriteOnce]
  resources:
    requests: {storage: 1Gi}
---
apiVersion: v1
kind: Pod
metadata: {name: writer, namespace: course}
spec:
  containers:
    - name: writer
      image: busybox:1.36
      command: ["sh", "-c", "date >> /data/history; sleep 3600"]
      volumeMounts: [{name: data, mountPath: /data}]
  volumes:
    - name: data
      persistentVolumeClaim: {claimName: app-data}
```

```bash
kubectl apply -f storage-lab.yaml
kubectl get pvc,pv -n course
kubectl describe pvc app-data -n course
```

## Practice

1. Inspect the default StorageClass and its provisioner, reclaim policy, and binding mode.
2. Delete and recreate the pod, then verify persisted data.
3. Document snapshot, restore, and expansion procedures for the chosen CSI driver.

## Common mistakes

- Assuming ReadWriteOnce means only one pod under every topology
- Deleting a PVC without checking PV reclaim policy and backups
- Treating a single persistent disk as a highly available database

## Stretch goal

Deploy a StatefulSet with per-replica claims and test a CSI snapshot restore into a new claim.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
