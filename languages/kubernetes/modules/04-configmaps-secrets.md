# ConfigMaps & Secrets

**Course:** Kubernetes Course (donor / allowlist access)  
**Module:** 4 of 10

## Learning goals

By the end of this lesson you will be able to:

- Inject non-sensitive and sensitive configuration into pods
- Explain ConfigMap and Secret update behavior for volumes and environment variables
- Protect secrets with encryption, RBAC, external stores, and safe delivery practices

## Why this matters

Separating configuration from images enables repeatable promotion. Kubernetes Secret objects improve handling conventions, but base64 encoding alone does not make secret data secure.

## Core ideas

1. **ConfigMaps hold non-secret configuration; Secrets mark sensitive values** for stricter access and tooling.
2. **Environment variable values are captured at process start**; projected volumes can update eventually, but applications must reload them.
3. **Base64 is encoding, not encryption** — protect etcd, transport, RBAC, backups, and operator access.
4. **External secret managers reduce secret sprawl** when integrated with workload identity and rotation.

## Worked example

### Lab: mount configuration and reference a Secret

```bash
kubectl create configmap api-config -n course   --from-literal=LOG_LEVEL=info
kubectl create secret generic api-secret -n course   --from-literal=DATABASE_PASSWORD='replace-in-a-real-secret-manager'
kubectl set env deployment/api -n course   --from=configmap/api-config
kubectl set env deployment/api -n course   --from=secret/api-secret
kubectl rollout status deployment/api -n course
```

Avoid putting literal secrets in shell history for real systems; use a secrets operator, encrypted Git workflow, or secure stdin/file process.

## Practice

1. Mount a ConfigMap as files and observe update behavior.
2. Rotate a disposable Secret and deliberately restart the consuming Deployment.
3. Use `kubectl auth can-i get secrets --as=<identity> -n course` to review access.

## Common mistakes

- Committing plaintext Secret manifests or literal creation commands to shared history
- Assuming base64-encoded Secret data is encrypted
- Expecting an environment variable to change inside an already running process

## Stretch goal

Integrate an external secret manager with workload identity and demonstrate rotation without storing secret material in Git.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](kubernetes-course.html) for the full path.
