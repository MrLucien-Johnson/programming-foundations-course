# AI — Module 04: Model Evaluation and Testing Quiz Answers

## Question 1: A harness is “repeatable” when…
**Answer: A** — Inputs, prompt version, and scoring rules are fixed/logged

**Outcome 1:** Run a repeatable eval harness on a fixed case set.

**Explanation:** Reproducibility needs versioned inputs and scorers.

---

## Question 2: Fifty labeled cases beat five anecdotes because…
**Answer: B** — Variance and coverage become visible

**Outcome 1:** Run a repeatable eval harness on a fixed case set.

**Explanation:** More cases → stabler decisions.

---

## Question 3: Thresholds like “90% schema validity” act as…
**Answer: B** — Release gates for quality

**Outcome 2:** Set pass/fail thresholds for schema and rubric scores.

**Explanation:** Gates turn metrics into go/no-go.

---

## Question 4: Failing a threshold should…
**Answer: B** — Block or roll back per policy

**Outcome 2:** Set pass/fail thresholds for schema and rubric scores.

**Explanation:** Gates without enforcement are theater.

---

## Question 5: Separate adversarial scores prevent…
**Answer: B** — Happy-path averages from hiding injection failures

**Outcome 3:** Score adversarial cases separately from the main set.

**Explanation:** Safety regressions must not be averaged away.

---

## Question 6: Injection cases in evals are…
**Answer: B** — First-class tests for policy robustness

**Outcome 3:** Score adversarial cases separately from the main set.

**Explanation:** Adversarial coverage is required.

---

## Question 7: A regression report should state…
**Answer: B** — What changed, what broke, metrics deltas, and rollback decision

**Outcome 4:** Produce regression reports with change impact and rollback criteria.

**Explanation:** Reports make A/B prompt decisions auditable.

---

## Question 8: A/B prompt versions need rollback criteria so…
**Answer: B** — You know when to switch back on quality/safety drops

**Outcome 4:** Produce regression reports with change impact and rollback criteria.

**Explanation:** Predeclare failure → action.

---

## Question 9: Logging cost/latency per eval run helps…
**Answer: B** — Catch quality wins that are operationally unaffordable

**Outcome 5:** Record cost and latency alongside quality metrics.

**Explanation:** Ops metrics belong next to quality.

---

## Question 10: Deterministic eval settings (fixed seed/temp where possible) reduce…
**Answer: B** — Noise that confuses regression interpretation

**Outcome 1:** Run a repeatable eval harness on a fixed case set.

**Explanation:** Control what you can when comparing versions.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
