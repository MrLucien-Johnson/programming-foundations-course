# Quiz — CI for Terraform

1. What should a pull-request Terraform job normally produce?
   - A. Checks and a reviewable plan
   - B. A production apply
   - C. A state deletion
   - D. A force unlock

2. Why use OIDC federation in CI?
   - A. To obtain short-lived scoped credentials
   - B. To make state public
   - C. To skip IAM
   - D. To remove audit logs

3. What does CI concurrency reduce?
   - A. Competing runs against one environment
   - B. Provider checksums
   - C. Variable validation
   - D. Output values

4. Why restrict plan artifacts?
   - A. They can contain sensitive infrastructure data
   - B. They are executable cloud accounts
   - C. They replace state
   - D. They create users

5. What should gate production apply?
   - A. Trusted branch, reviewed plan/commit, and protected approval
   - B. Any fork pull request
   - C. A formatting failure
   - D. A public secret
