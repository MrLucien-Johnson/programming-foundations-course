# AI — Module 06: Workflows and Automation Quiz Answers

## Question 1: A 3-step notes workflow should define…
**Answer: B** — Input/output contracts per step (extract → verify → finalize)

**Outcome 1:** Design multi-step workflows with explicit step I/O contracts.

**Explanation:** Contracts make steps testable and composable.

---

## Question 2: Why split extract vs verify?
**Answer: B** — To catch missing/invalid actions before delivery

**Outcome 1:** Design multi-step workflows with explicit step I/O contracts.

**Explanation:** Verification reduces bad outputs shipping.

---

## Question 3: Verification against sources prevents…
**Answer: B** — Unfounded claims in later steps

**Outcome 2:** Add verification steps before accepting intermediate outputs.

**Explanation:** Check facts before acting.

---

## Question 4: A retry budget exists to…
**Answer: B** — Bound cost/latency when steps fail or are uncertain

**Outcome 3:** Set retry budgets and stop conditions for uncertain results.

**Explanation:** Budgets prevent runaway automation.

---

## Question 5: Stop-if-uncertain rules protect…
**Answer: B** — Users from automated wrong actions

**Outcome 3:** Set retry budgets and stop conditions for uncertain results.

**Explanation:** Uncertainty should halt side effects.

---

## Question 6: Audit logs should include…
**Answer: B** — Run id, prompt version, result category, and redacted context

**Outcome 4:** Log privacy-safe audit fields for each run.

**Explanation:** Privacy-safe provenance beats dumping secrets.

---

## Question 7: Redaction before logging is important because…
**Answer: B** — Logs are a common leak channel for sensitive data

**Outcome 4:** Log privacy-safe audit fields for each run.

**Explanation:** Minimize sensitive retention in telemetry.

---

## Question 8: When a step fails, a fallback might…
**Answer: B** — Ask a human, abstain, or return a safe degraded result

**Outcome 5:** Define fallbacks when a step fails or confidence is low.

**Explanation:** Explicit fallbacks beat silent failure.

---

## Question 9: Agentic multi-step flows need stop conditions because…
**Answer: B** — Unbounded tool loops can runaway in cost and harm

**Outcome 5:** Define fallbacks when a step fails or confidence is low.

**Explanation:** Bounds are a core automation control.

---

## Question 10: End-to-end testing a workflow on 10 cases mainly checks…
**Answer: B** — Contracts, verification, and fallbacks under realistic inputs

**Outcome 2:** Add verification steps before accepting intermediate outputs.

**Explanation:** E2E proves the pipeline, not just prompts in isolation.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
