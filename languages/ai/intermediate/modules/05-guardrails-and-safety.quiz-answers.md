# AI — Module 05: Guardrails and Safety Quiz Answers

## Question 1: Output controls in RAG should…
**Answer: B** — Require evidence or refuse/abstain

**Outcome 1:** Enforce input/output controls including source-only and refusal rules.

**Explanation:** Source-only is an output guardrail.

---

## Question 2: Input controls typically…
**Answer: B** — Detect/block injection and disallowed content before tools run

**Outcome 1:** Enforce input/output controls including source-only and refusal rules.

**Explanation:** Filter early to reduce blast radius.

---

## Question 3: Least-privilege tools mean…
**Answer: B** — Only tools needed for the task are exposed, with arg limits

**Outcome 2:** Constrain tools with least privilege and verify via tests.

**Explanation:** Privilege minimization is a guardrail.

---

## Question 4: Tests should try to make the agent…
**Answer: B** — Call disallowed tools or exfiltrate secrets — and verify denial

**Outcome 2:** Constrain tools with least privilege and verify via tests.

**Explanation:** Negative tests prove constraints hold.

---

## Question 5: Red-team suites focus on…
**Answer: B** — Highest-impact abuse and bypass attempts

**Outcome 3:** Build red-team suites that target top abuse paths.

**Explanation:** Prioritize real threats.

---

## Question 6: Prompt injection into tool args is dangerous because…
**Answer: B** — It can trigger unintended side effects

**Outcome 3:** Build red-team suites that target top abuse paths.

**Explanation:** Tools turn text into actions.

---

## Question 7: A CI safety gate should…
**Answer: B** — Fail the build when safety evals regress beyond threshold

**Outcome 4:** Add safety gates in CI that fail on safety regressions.

**Explanation:** Automate the regression tripwire.

---

## Question 8: Safety tests belong in the harness so…
**Answer: B** — Every prompt change re-checks policy behavior

**Outcome 4:** Add safety gates in CI that fail on safety regressions.

**Explanation:** Safety is a continuous eval, not a one-off.

---

## Question 9: Escalation for high-risk outputs may include…
**Answer: B** — Human review, block, or safe-complete paths

**Outcome 5:** Design escalation paths for high-risk model outputs.

**Explanation:** Severity drives response path.

---

## Question 10: Audit-friendly logging for safety events should…
**Answer: B** — Record category and action taken without unnecessary secrets

**Outcome 5:** Design escalation paths for high-risk model outputs.

**Explanation:** Investigate without creating new leaks.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
