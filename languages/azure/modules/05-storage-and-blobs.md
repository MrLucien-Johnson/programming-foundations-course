# Storage & blobs

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 5 of 10

## Learning goals

By the end of this lesson you will be able to:

- Choose Blob, Files, Queue, or Table storage for a workload
- Configure redundancy, access tiers, lifecycle rules, and public-access controls
- Upload and verify a blob using identity-based authorization

## Why this matters

Storage choices affect durability, recovery, performance, security, and recurring cost. Secure defaults matter because a single anonymous container can expose an entire dataset.

## Core ideas

1. **A storage account is the namespace and policy boundary** for Blob, Files, Queues, and Tables.
2. **Redundancy matches failure tolerance** — LRS, ZRS, GRS, and GZRS protect against different scopes at different prices.
3. **Blob tiers and lifecycle policies manage economics** — hot, cool, cold, and archive trade access cost for storage cost.
4. **Use Entra ID and RBAC for data operations** instead of long-lived account keys where possible.

## Worked example

### Lab: create private Blob storage and upload with Entra credentials

```bash
ACCOUNT="stlab$RANDOM$RANDOM"
az storage account create -g rg-learning-web -n "$ACCOUNT"   -l uksouth --sku Standard_ZRS --kind StorageV2   --allow-blob-public-access false --min-tls-version TLS1_2
az storage container create --account-name "$ACCOUNT"   --name uploads --auth-mode login
printf 'hello azure
' > /tmp/azure-lab.txt
az storage blob upload --account-name "$ACCOUNT"   --container-name uploads --name hello.txt   --file /tmp/azure-lab.txt --auth-mode login
az storage blob list --account-name "$ACCOUNT"   --container-name uploads --auth-mode login -o table
```

## Practice

1. Match object, shared-file, message, and key-value needs to Azure Storage services.
2. Create a private container and prove anonymous access is unavailable.
3. Write a lifecycle policy that moves old logs to cool storage and later deletes them.

## Common mistakes

- Sharing storage account keys as application configuration
- Choosing geo-redundancy without understanding failover and data residency
- Moving frequently read objects to archive and incurring retrieval delay and cost

## Stretch goal

Add soft delete, versioning, and a private endpoint, then document the restore and DNS paths.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
