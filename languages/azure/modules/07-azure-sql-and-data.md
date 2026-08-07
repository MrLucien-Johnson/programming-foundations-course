# Azure SQL & data

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 7 of 10

## Learning goals

By the end of this lesson you will be able to:

- Differentiate Azure SQL Database, Managed Instance, and SQL on Azure VMs
- Configure identity, network access, backups, and service tiers for a database
- Test connectivity without exposing the server broadly

## Why this matters

Managed databases remove much routine infrastructure work, but schema, identity, query performance, network exposure, and recovery objectives remain application responsibilities.

## Core ideas

1. **Choose the least infrastructure needed** — SQL Database suits cloud applications; Managed Instance adds broader SQL Server compatibility; VMs retain OS control.
2. **Logical servers are management endpoints** — databases have independent compute and storage characteristics.
3. **Private connectivity and Entra authentication reduce exposure** — firewall exceptions should be narrow and temporary.
4. **Backups are useful only with recovery objectives** — understand point-in-time retention, geo-restore, and restore testing.

## Worked example

### Lab: create a small Azure SQL database

```bash
az sql server create -g rg-learning-web -n <unique-sql-server>   -l uksouth -u sqladmin -p '<strong-temporary-password>'
az sql db create -g rg-learning-web -s <unique-sql-server>   -n appdb --service-objective Basic --backup-storage-redundancy Local
az sql db show -g rg-learning-web -s <unique-sql-server>   -n appdb --query "{status:status,tier:currentServiceObjectiveName}" -o yaml
az sql db list-usages -g rg-learning-web -s <unique-sql-server>   -n appdb -o table
```

For a real workload, configure an Entra administrator, private endpoint, and private DNS rather than leaving broad public firewall rules.

## Practice

1. Compare managed database options for a new API and a lift-and-shift SQL Server application.
2. Write RPO and RTO targets, then map them to a restore strategy.
3. Inspect query performance recommendations and identify one index or query hypothesis.

## Common mistakes

- Adding a `0.0.0.0/0`-style broad firewall range for convenience
- Assuming platform backups eliminate the need to test restores
- Scaling compute before investigating slow queries and indexes

## Stretch goal

Design failover-group behavior for two regions, including connection endpoints and failover criteria.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
