# VPC & networking

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 3 of 10

## Learning goals

By the end of this lesson you will be able to:

- Draw public vs private subnets
- Explain route tables, IGW, and NAT at a high level
- Place a web tier and data tier thoughtfully

## Why this matters

Networking mistakes expose databases or block deploys. A simple VPC sketch prevents both.

## Core ideas

1. **Public subnet** — route to Internet Gateway for inbound public services.
2. **Private subnet** — no public IP; egress via NAT if needed.
3. **Security groups** — stateful allow-lists on ENIs.
4. **NACLs** — optional extra subnet-level filter (keep simple at first).

## Worked example

### Lab: napkin VPC

```text
VPC 10.0.0.0/16
  public-a  10.0.0.0/24  → IGW
  private-a 10.0.10.0/24 → NAT (egress)
SG-web: allow 443 from 0.0.0.0/0
SG-db:  allow 5432 from SG-web only
```

Never put the database in a public subnet for learning “convenience”.


## Practice

1. Draw your VPC with two subnets and two security groups.
2. Write which resources get public IPs and why.
3. Trace a packet from browser → ALB/instance → DB.

## Common mistakes

- 0.0.0.0/0 to SSH on 22 permanently
- Database in public subnet
- Overlapping CIDRs when peering later

## Stretch goal

Add a second AZ subnet pair for high availability sketch.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
