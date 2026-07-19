# Optimization and Safety (Advanced) Quiz Answers

## Question 1: Cutting tokens by removing safety instructions is…
**Answer: B** — Unsafe — keep required policy checks even under budget pressure

**Outcome 1:** Budget cost and latency without sacrificing required safety checks.

**Explanation:** Do not optimize away safety.

---

## Question 2: A cost plan should state…
**Answer: B** — Budgets, enforcement, and what quality/safety must not regress

**Outcome 1:** Budget cost and latency without sacrificing required safety checks.

**Explanation:** Budgets need hard constraints and non-negotiables.

---

## Question 3: Caching model outputs is inappropriate when…
**Answer: B** — Outputs are user-specific/sensitive or must reflect fresh private data

**Outcome 2:** Apply caching/reuse only when correctness and privacy allow.

**Explanation:** Privacy and freshness gate caching.

---

## Question 4: Reuse strategies should document…
**Answer: B** — Cache keys, invalidation, and sensitivity rules

**Outcome 2:** Apply caching/reuse only when correctness and privacy allow.

**Explanation:** Operationalize safe reuse.

---

## Question 5: Performance work without safety evals risks…
**Answer: B** — Faster, cheaper, more dangerous systems

**Outcome 3:** Plan safety evaluations and red-teaming alongside performance work.

**Explanation:** Optimize with red-team gates.

---

## Question 6: A safety assessment summary for optimization should include…
**Answer: B** — What was changed, residual risks, and eval evidence

**Outcome 3:** Plan safety evaluations and red-teaming alongside performance work.

**Explanation:** Evidence that safety still holds.

---

## Question 7: Latency wins that increase jailbreak success should…
**Answer: B** — Be rejected or redesigned until safety gates pass

**Outcome 1:** Budget cost and latency without sacrificing required safety checks.

**Explanation:** Safety is a release constraint.

---

## Question 8: Shared caches across tenants without isolation…
**Answer: B** — Risk cross-tenant data leakage

**Outcome 2:** Apply caching/reuse only when correctness and privacy allow.

**Explanation:** Isolation is a caching safety rule.

---

## How Did You Do?

- **8/8 correct:** Excellent! You are ready to move on.
- **6-7 correct:** Great work — review the missed outcomes.
- **0-5 correct:** Revisit the module lessons, then try again.
