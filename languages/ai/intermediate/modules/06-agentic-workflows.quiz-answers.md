# AI — Module 06: Agentic Workflows Quiz Answers

## Question 1: An agent workflow spec should state…
**Answer: B** — Steps, allowed tools, stop conditions, and outputs

**Outcome 1:** Specify agent plans with tool boundaries and stop conditions.

**Explanation:** Specs bound autonomy.

---

## Question 2: Tool boundaries exist to…
**Answer: B** — Prevent actions outside the task’s privilege set

**Outcome 1:** Specify agent plans with tool boundaries and stop conditions.

**Explanation:** Boundaries are safety and product constraints.

---

## Question 3: Verification before deliver means…
**Answer: B** — Checking facts against provided sources

**Outcome 2:** Insert verification steps that check claims against sources.

**Explanation:** Verify reduces hallucinated actions.

---

## Question 4: A tool budget of N calls stops…
**Answer: B** — Runaway loops that burn cost and time

**Outcome 3:** Enforce tool budgets to prevent runaway loops.

**Explanation:** Budgets are circuit breakers for agents.

---

## Question 5: Missing stop conditions typically cause…
**Answer: B** — Endless plan/execute cycles

**Outcome 3:** Enforce tool budgets to prevent runaway loops.

**Explanation:** Agents need explicit halting rules.

---

## Question 6: Human approval checkpoints belong on…
**Answer: B** — High-risk side effects (refunds, emails, deletes)

**Outcome 4:** Require human approval for high-risk actions.

**Explanation:** Match human gates to blast radius.

---

## Question 7: Adversarial cases that push secret leakage should…
**Answer: B** — Be in the eval set with expected denials

**Outcome 4:** Require human approval for high-risk actions.

**Explanation:** Agents need red-team coverage.

---

## Question 8: A post-run report should include…
**Answer: B** — Actions taken, evidence, and remaining uncertainties

**Outcome 5:** Emit post-run reports covering actions, evidence, and uncertainties.

**Explanation:** Reports make autonomy reviewable.

---

## Question 9: Listing uncertainties helps operators…
**Answer: B** — Decide what needs human follow-up

**Outcome 5:** Emit post-run reports covering actions, evidence, and uncertainties.

**Explanation:** Uncertainty is an operational signal.

---

## Question 10: Simulating tool-down failures in tests checks…
**Answer: B** — Whether the agent degrades safely (retry/stop/escalate)

**Outcome 2:** Insert verification steps that check claims against sources.

**Explanation:** Failure injection validates agent resilience.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
