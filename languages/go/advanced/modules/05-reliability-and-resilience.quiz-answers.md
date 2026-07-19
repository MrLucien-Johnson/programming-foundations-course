# Go Advanced — Module 05: Reliability and Resilience Quiz Answers

## Question 1: Retrying immediately forever without jitter tends to…
**Answer: B** — Create synchronized retry storms that worsen outages

**Outcome 1:** Configure retries with timeouts, budgets, and jitter for transient faults.

**Explanation:** Backoff + jitter spreads retries; budgets cap total attempts.

---

## Question 2: A timeout without a retry budget means…
**Answer: A** — You may still hammer a sick dependency indefinitely via client loops

**Outcome 1:** Configure retries with timeouts, budgets, and jitter for transient faults.

**Explanation:** Pair timeouts with limited retries and overall deadlines.

---

## Question 3: A circuit breaker opens when…
**Answer: A** — Error rates/latency cross a threshold, failing fast instead of calling the dependency

**Outcome 2:** Apply circuit breakers, bulkheads, and rate limits to contain failures.

**Explanation:** Open circuits shed load from unhealthy dependencies.

---

## Question 4: Bulkheads help by…
**Answer: B** — Isolating resources so one failure domain cannot exhaust another

**Outcome 2:** Apply circuit breakers, bulkheads, and rate limits to contain failures.

**Explanation:** Bulkheads compartmentalize blast radius.

---

## Question 5: Idempotency keys are most critical for…
**Answer: B** — Create/payment operations that clients may retry

**Outcome 3:** Use idempotency keys and dedupe to make retried writes safe.

**Explanation:** Retried side-effecting writes need dedupe.

---

## Question 6: Deduping consumer messages by event ID prevents…
**Answer: B** — Double-applying the same business effect after redelivery

**Outcome 3:** Use idempotency keys and dedupe to make retried writes safe.

**Explanation:** At-least-once delivery + dedupe ≈ safe processing.

---

## Question 7: A runbook should primarily contain…
**Answer: B** — Detection signals, mitigation steps, owners, and escalation paths

**Outcome 4:** Write and follow runbooks for common incident classes.

**Explanation:** Runbooks make incidents executable under pressure.

---

## Question 8: During an incident, the first reliability move is often…
**Answer: B** — Mitigate user impact (rollback, feature flag, degrade) then diagnose

**Outcome 4:** Write and follow runbooks for common incident classes.

**Explanation:** Stop the bleeding, then find root cause.

---

## Question 9: Rate limiting a dependency client protects…
**Answer: B** — Both your service and the dependency from overload

**Outcome 2:** Apply circuit breakers, bulkheads, and rate limits to contain failures.

**Explanation:** Client-side limits are part of being a good citizen under stress.

---

## Question 10: Which retry policy is safest for non-idempotent POSTs without keys?
**Answer: B** — Fail clearly / get an idempotency key before retrying side effects

**Outcome 1:** Configure retries with timeouts, budgets, and jitter for transient faults.

**Explanation:** Do not blindly retry unsafe side effects.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
