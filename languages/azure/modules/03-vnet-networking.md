# VNet & networking

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 3 of 10

## Learning goals

By the end of this lesson you will be able to:

- Plan non-overlapping VNet and subnet CIDR ranges
- Explain routes, network security groups, private endpoints, and Azure DNS roles
- Test network reachability without assuming that a public IP is required

## Why this matters

A VNet is the connectivity and isolation foundation for Azure workloads. Address mistakes and permissive rules become difficult to repair after environments are connected.

## Core ideas

1. **VNets are regional private networks** — subnets divide address space; peering connects VNets without transitive routing by default.
2. **NSGs are stateful filters** — inbound and outbound rules apply by priority to subnets or network interfaces.
3. **Routes choose paths; NSGs permit traffic** — a valid route does not imply authorization.
4. **Private endpoints bring PaaS privately into a VNet** — private DNS must resolve the service name to the endpoint address.

## Worked example

### Lab: create a VNet and restricted application subnet

```bash
az network vnet create -g rg-learning-web -n vnet-web   --address-prefix 10.40.0.0/16   --subnet-name snet-app --subnet-prefix 10.40.1.0/24
az network nsg create -g rg-learning-web -n nsg-app
az network nsg rule create -g rg-learning-web --nsg-name nsg-app   -n allow-https --priority 100 --direction Inbound   --protocol Tcp --destination-port-ranges 443   --source-address-prefixes 10.40.0.0/16 --access Allow
az network vnet subnet update -g rg-learning-web --vnet-name vnet-web   -n snet-app --network-security-group nsg-app
```

Inspect effective rules before troubleshooting the application: `az network nsg rule list -g rg-learning-web --nsg-name nsg-app -o table`.

## Practice

1. Allocate three non-overlapping `/24` subnets inside a `/16` VNet.
2. Write an NSG rule set that allows HTTPS from a trusted source and denies unnecessary administration ports.
3. Draw DNS resolution for a Storage private endpoint.

## Common mistakes

- Using overlapping CIDRs that later block peering or VPN connectivity
- Opening SSH or RDP to the entire internet
- Creating a private endpoint without configuring or linking private DNS

## Stretch goal

Design a hub-and-spoke topology with Azure Firewall, shared DNS, and explicit spoke routes.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
