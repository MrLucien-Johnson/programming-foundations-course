# Quiz — Continuous integration pipelines

1. CI should primarily…
   - A. Deploy to production on every keystroke
   - B. Prove each change builds and passes automated checks
   - C. Replace code review entirely
   - D. Store production passwords in git

2. “Build once, promote many” means…
   - A. Rebuild with different flags per environment casually
   - B. Create one artefact and promote the same artefact
   - C. Never build artefacts
   - D. Only build on Fridays

3. Where should CI secrets live?
   - A. Committed as plain text
   - B. In the CI secret store / environment
   - C. In public screenshots
   - D. In the README title

4. A flaky test that fails randomly should be…
   - A. Ignored forever with no ticket
   - B. Quarantined/fixed so CI stays trustworthy
   - C. Used as the only gate to production
   - D. Deleted along with all tests

5. Fast CI feedback helps because…
   - A. People are less likely to bypass checks
   - B. It removes the need for any tests
   - C. It guarantees zero bugs
   - D. It replaces monitoring
