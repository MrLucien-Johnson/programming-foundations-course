# Quiz — EC2 & compute choices

1. Stopping an EC2 instance…
   - A. Usually stops compute charges (EBS may still cost)
   - B. Deletes the VPC
   - C. Removes IAM
   - D. Is identical to terminating always

2. Why prefer SSM Session Manager?
   - A. Avoid opening SSH to the world
   - B. It replaces all security groups
   - C. It is a database
   - D. It disables CloudTrail

3. Tags help with…
   - A. Cost allocation and ownership
   - B. Faster CPUs magically
   - C. Skipping patches
   - D. Public access

4. User data scripts should…
   - A. Be treated carefully — prefer immutable images for prod
   - B. Contain production secrets always
   - C. Never be reviewed
   - D. Replace IAM policies

5. Pick EC2 when you need…
   - A. Full OS control / long-running custom runtimes
   - B. Only a single SQL query forever
   - C. DNS only
   - D. Object storage only
