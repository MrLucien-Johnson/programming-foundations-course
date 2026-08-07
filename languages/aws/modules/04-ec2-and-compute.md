# EC2 & compute choices

**Course:** AWS Cloud Course (donor / allowlist access)  
**Module:** 4 of 10

## Learning goals

By the end of this lesson you will be able to:

- Launch a tiny EC2 (or use CloudShell) safely
- Choose instance sizing with cost in mind
- Connect via SSM Session Manager mindset (prefer over open SSH)

## Why this matters

EC2 is the classic compute primitive. Learning it teaches AMIs, disks, and networking that other services abstract.

## Core ideas

1. **AMI + instance type + storage + SG** — the four knobs.
2. **Stop vs terminate** — cost and data implications.
3. **User data** — bootstrap carefully; prefer images/CI later.
4. **SSM over bastion** when possible.

## Worked example

### Lab: free-tier minded instance

1. Amazon Linux in your home region, t2/t3.micro if eligible.
2. SG: no 22 from the world; prefer SSM role + `AmazonSSMManagedInstanceCore`.
3. Tag `Project=learning`, `KeepUntil=YYYY-MM-DD`.
4. Stop or terminate when done; verify billing.

```bash
# from CloudShell / your laptop with rights:
aws ec2 describe-instances --query 'Reservations[].Instances[].InstanceId'
```


## Practice

1. Launch, tag, connect (SSM or tightly scoped SSH), install nothing unnecessary, stop.
2. Write when you’d pick EC2 vs Lambda vs containers.
3. Document disk: root volume size and whether data must persist.

## Common mistakes

- Forgetting to stop instances
- Wide-open SSH
- Storing unique data only on ephemeral instance store without backup

## Stretch goal

Create a simple launch template or note why you’d want one.

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub](aws-course.html) for the full path.
