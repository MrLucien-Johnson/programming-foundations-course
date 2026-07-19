# Swift Advanced — Module 08: CI/CD and Release Strategies Quiz Answers

## Question 1: A canary release primarily…
**Answer: B** — Exposes a new version to a small slice of traffic first

**Outcome 1:** Choose canary, blue-green, or rolling releases for a risk profile.

**Explanation:** Canaries limit blast radius while you watch metrics.

---

## Question 2: Blue-green deployment keeps…
**Answer: A** — Two environments so you can switch traffic atomically and roll back fast

**Outcome 1:** Choose canary, blue-green, or rolling releases for a risk profile.

**Explanation:** Blue-green trades cost for fast switch/rollback.

---

## Question 3: Feature flags help you…
**Answer: B** — Decouple deploy from release and kill-switch bad behavior

**Outcome 2:** Use feature flags and safe config changes to control exposure.

**Explanation:** Flags control exposure without redeploying binaries every time.

---

## Question 4: A risky config change should be…
**Answer: B** — Rolled out gradually with monitoring and a fast revert path

**Outcome 2:** Use feature flags and safe config changes to control exposure.

**Explanation:** Treat config like code: staged, observable, reversible.

---

## Question 5: Expand/contract migrations reduce risk by…
**Answer: B** — Adding new schema first, dual-writing/reading, then removing old later

**Outcome 3:** Plan production database migrations that avoid downtime and lockouts.

**Explanation:** Online migrations are multi-phase and backwards compatible.

---

## Question 6: Taking a long ACCESS EXCLUSIVE lock on a hot table during peak…
**Answer: B** — Can stall writes/reads and cause an outage

**Outcome 3:** Plan production database migrations that avoid downtime and lockouts.

**Explanation:** Plan locks and backfills carefully in production.

---

## Question 7: A rollback plan needs…
**Answer: B** — A known-good version, data compatibility rules, and a practiced switch

**Outcome 4:** Execute rollbacks with clear versioning and changelogs.

**Explanation:** Rollbacks fail when versions/data are incompatible or unpracticed.

---

## Question 8: Changelogs/versioning help incidents by…
**Answer: B** — Making it obvious what changed when symptoms started

**Outcome 4:** Execute rollbacks with clear versioning and changelogs.

**Explanation:** Version clarity speeds bisect and rollback decisions.

---

## Question 9: Rolling deploys gradually replace instances. Main risk to watch?
**Answer: A** — Mixed versions briefly serving traffic

**Outcome 1:** Choose canary, blue-green, or rolling releases for a risk profile.

**Explanation:** Ensure mixed-version compatibility during the roll.

---

## Question 10: Turning a flag on for 5% of users is similar in spirit to…
**Answer: B** — A canary / progressive delivery of a behavior

**Outcome 2:** Use feature flags and safe config changes to control exposure.

**Explanation:** Flags enable progressive delivery of features.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
