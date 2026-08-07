# Quiz — Containers basics

1. An image is best thought of as…
   - A. A running process only
   - B. An immutable filesystem snapshot + metadata
   - C. A VPN tunnel
   - D. A git branch

2. Why avoid relying on `:latest` in production?
   - A. It is always slower
   - B. It is ambiguous and can change underneath you
   - C. Docker forbids it
   - D. It disables networking

3. Secrets should be…
   - A. COPY’d into the Dockerfile permanently
   - B. Injected at runtime via env/secret stores
   - C. Printed in build logs on purpose
   - D. Committed next to the Dockerfile

4. Pinning a base image helps…
   - A. Reproducible builds
   - B. Random breakage as a feature
   - C. Skipping tests
   - D. Hiding CVEs forever

5. `docker run` starts…
   - A. A container from an image
   - B. A new cloud region
   - C. A Terraform backend
   - D. A DNS zone
