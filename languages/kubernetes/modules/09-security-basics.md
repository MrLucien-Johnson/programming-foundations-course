# Kubernetes security basics

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 9 of 10

## Learning goals

By the end of this lesson you will be able to:

- Apply least-privilege RBAC, service accounts, and namespace policy
- Use Pod Security Standards, security contexts, and NetworkPolicies
- Reduce supply-chain risk with immutable, scanned, and verifiable images

## Why this matters

A Kubernetes cluster combines powerful APIs, shared nodes, network reachability, and software supply chains. Security must constrain identities, workloads, traffic, and artifacts together.

## Core ideas

1. **RBAC controls API verbs on resources** — test effective access and avoid wildcard cluster roles.
2. **Pod Security Standards restrict risky workload settings** such as privilege, host namespaces, root, and added capabilities.
3. **NetworkPolicy changes pod traffic from broadly reachable toward explicit allowance** when the CNI enforces it.
4. **Image security starts before admission** — pin digests, scan dependencies, sign artifacts, and enforce trusted sources.

## Worked example

### Lab: create a read-only workload identity

```bash
kubectl create serviceaccount viewer -n course
kubectl create role pod-reader -n course   --verb=get,list,watch --resource=pods
kubectl create rolebinding viewer-reads-pods -n course   --role=pod-reader --serviceaccount=course:viewer
kubectl auth can-i list pods   --as=system:serviceaccount:course:viewer -n course
kubectl auth can-i delete pods   --as=system:serviceaccount:course:viewer -n course
kubectl label namespace course   pod-security.kubernetes.io/enforce=restricted --overwrite
```

## Practice

1. Create a Role that can read ConfigMaps but cannot read Secrets.
2. Harden a pod with non-root user, read-only root filesystem, dropped capabilities, and seccomp.
3. Apply default-deny ingress and egress, then add only required DNS and service flows.

## Common mistakes

- Binding workloads or developers to `cluster-admin`
- Assuming a NetworkPolicy works without CNI enforcement
- Running unpinned images as root with privilege or host mounts

## Stretch goal

Enforce signed images from an approved registry with an admission policy and document the break-glass process.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
