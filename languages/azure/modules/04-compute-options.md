# Compute options

**Course:** Azure Cloud Course (donor / allowlist access)  
**Module:** 4 of 10

## Learning goals

By the end of this lesson you will be able to:

- Select among Virtual Machines, VM Scale Sets, Container Apps, Functions, and AKS
- Recognize the operational trade-off between control and managed abstractions
- Create and inspect a minimal VM while controlling access and cost

## Why this matters

Azure offers multiple valid compute models. Choosing the least operationally demanding model that satisfies workload constraints keeps teams focused on application value.

## Core ideas

1. **VMs maximize control and responsibility** — you patch the OS, harden access, and plan availability.
2. **Scale Sets provide a uniform VM fleet** — instances scale from an image and health model.
3. **Container Apps and Functions reduce infrastructure work** — they suit HTTP, event, and job workloads with platform constraints.
4. **AKS is justified by Kubernetes needs** — it adds cluster, networking, and workload operational complexity.

## Worked example

### Lab: create an inexpensive Linux VM without public inbound access

```bash
az vm create -g rg-learning-web -n vm-lab   --image Ubuntu2204 --size Standard_B1s   --admin-username azureuser --generate-ssh-keys   --public-ip-address '""'
az vm show -g rg-learning-web -n vm-lab   --show-details --query "{state:powerState,privateIp:privateIps}" -o yaml
az vm deallocate -g rg-learning-web -n vm-lab
```

Use Bastion, VPN, or a controlled run-command path rather than adding a broad public SSH rule.

## Practice

1. Create a decision table for VM, Functions, Container Apps, and AKS using control, scaling, and operations.
2. Deploy, inspect, deallocate, and delete a lab VM.
3. Estimate whether a steady service or bursty event handler benefits from consumption pricing.

## Common mistakes

- Selecting AKS merely because the application ships as a container
- Leaving lab VMs allocated after use
- Treating automatic scaling as a substitute for load testing and resource limits

## Stretch goal

Draft a VM Scale Set design with health probes, zone distribution, and immutable image rollout.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](azure-course.html) for the full path.
