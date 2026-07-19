# AI — Module 07: Data Governance and Privacy Quiz Answers

## Question 1: A data handling policy should answer…
**Answer: B** — What is stored, purpose, retention, and who can access

**Outcome 1:** Write data-handling policies for what is stored, why, and how long.

**Explanation:** Concrete policy beats slogans.

---

## Question 2: Purpose limitation means…
**Answer: B** — Use collected data only for stated purposes

**Outcome 1:** Write data-handling policies for what is stored, why, and how long.

**Explanation:** Purpose binds processing.

---

## Question 3: Redaction tests should include…
**Answer: B** — Samples where PII must not appear in outputs/logs

**Outcome 2:** Implement and test PII redaction on inputs/outputs.

**Explanation:** Negative cases prove redaction.

---

## Question 4: Redacting in the UI but logging raw text…
**Answer: B** — Leaves a major leak channel

**Outcome 2:** Implement and test PII redaction on inputs/outputs.

**Explanation:** Protect all channels.

---

## Question 5: No-leakage tests for RAG verify…
**Answer: B** — Unauthorized docs never appear in context/answers

**Outcome 3:** Enforce permission-aware retrieval and no-leakage tests.

**Explanation:** AuthZ belongs in retrieval tests.

---

## Question 6: Permission metadata on chunks enables…
**Answer: B** — Filtering retrieval by caller rights

**Outcome 3:** Enforce permission-aware retrieval and no-leakage tests.

**Explanation:** Metadata drives ACL filters.

---

## Question 7: Safe logging schemas typically store…
**Answer: B** — IDs, categories, hashes/redacted snippets — not raw secrets

**Outcome 4:** Design safe logging schemas that avoid raw sensitive text.

**Explanation:** Minimize sensitive telemetry.

---

## Question 8: Audit queries (“who accessed what”) support…
**Answer: B** — Accountability and incident investigation

**Outcome 4:** Design safe logging schemas that avoid raw sensitive text.

**Explanation:** Governance needs auditability.

---

## Question 9: Privacy review in releases catches…
**Answer: B** — New data flows that expand retention or exposure

**Outcome 5:** Add privacy review checklists to release process.

**Explanation:** Ship checks for data risk.

---

## Question 10: “Data should not appear” negative tests are critical because…
**Answer: A** — Absence is hard to notice without assertions

**Outcome 5:** Add privacy review checklists to release process.

**Explanation:** Assert non-presence explicitly.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
