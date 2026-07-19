# Rust Advanced — Module 06: Security (Advanced) Quiz Answers

## Question 1: Threat modeling starts by…
**Answer: B** — Listing assets, entry points, threats, and mitigations for the feature

**Outcome 1:** Threat-model a feature including abuse cases and prioritised mitigations.

**Explanation:** Structured threat models drive prioritized defenses.

---

## Question 2: An “abuse case” focuses on…
**Answer: B** — How a motivated attacker or abusive user misuses the system

**Outcome 1:** Threat-model a feature including abuse cases and prioritised mitigations.

**Explanation:** Abuse cases complement functional requirements.

---

## Question 3: TLS primarily protects…
**Answer: A** — Data in transit from eavesdropping/tampering

**Outcome 2:** Apply encryption at rest/in transit with sound key management.

**Explanation:** In-transit encryption ≠ at-rest encryption.

---

## Question 4: Where should encryption keys live?
**Answer: B** — In a managed KMS/HSM with rotation and access control

**Outcome 2:** Apply encryption at rest/in transit with sound key management.

**Explanation:** Key management is the hard part of encryption.

---

## Question 5: Pinning dependency versions and verifying checksums helps against…
**Answer: B** — Malicious or swapped packages in the supply chain

**Outcome 3:** Enforce supply-chain controls for dependencies and build artifacts.

**Explanation:** Supply-chain controls reduce dependency compromise risk.

---

## Question 6: A compromised build pipeline can…
**Answer: B** — Inject malicious artifacts into what you ship

**Outcome 3:** Enforce supply-chain controls for dependencies and build artifacts.

**Explanation:** Protect CI/CD like production — it produces production.

---

## Question 7: A hardening checklist should include…
**Answer: B** — AuthZ reviews, secret hygiene, dependency updates, and security test gates

**Outcome 4:** Execute a hardening checklist covering auth, config, and security tests.

**Explanation:** Hardening is a repeatable checklist, not a one-off slogan.

---

## Question 8: Security tests in CI are valuable because they…
**Answer: B** — Catch regressions in injection, authz, and dependency policy before release

**Outcome 4:** Execute a hardening checklist covering auth, config, and security tests.

**Explanation:** Automate what you can; still model new threats.

---

## Question 9: Prioritising mitigations should weigh…
**Answer: B** — Likelihood × impact and exploitability of each threat

**Outcome 1:** Threat-model a feature including abuse cases and prioritised mitigations.

**Explanation:** Risk-based prioritization beats checkbox theater.

---

## Question 10: Encrypting a database volume but logging raw PAN data means…
**Answer: B** — Sensitive data still leaks via another channel

**Outcome 2:** Apply encryption at rest/in transit with sound key management.

**Explanation:** Encryption must cover actual sensitive data paths end-to-end.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
