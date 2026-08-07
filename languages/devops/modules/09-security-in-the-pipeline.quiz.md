# Quiz — Security in the pipeline

1. Least privilege for deploy credentials means…
   - A. CI can do anything in the cloud account
   - B. CI can only perform required deploy actions
   - C. Developers email passwords around
   - D. Secrets live in the frontend bundle

2. Dependency scanning helps you…
   - A. Know vulnerable libraries you ship
   - B. Skip tests
   - C. Avoid version control
   - D. Disable TLS

3. Secret scanning on PRs is valuable because…
   - A. It catches accidental key commits early
   - B. It replaces IAM
   - C. It makes builds slower for fun
   - D. It encrypts the database automatically

4. Why separate prod and non-prod credentials?
   - A. To limit blast radius of leaks
   - B. To confuse newcomers
   - C. Clouds require identical keys
   - D. So rollbacks are impossible

5. Rotating a secret means…
   - A. Issuing a new value and retiring the old one safely
   - B. Printing it in Slack
   - C. Never changing it
   - D. Storing it in the README
