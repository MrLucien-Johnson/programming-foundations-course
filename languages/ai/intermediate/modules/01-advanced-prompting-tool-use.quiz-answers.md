# AI — Module 01: Advanced Prompting: Tool Use Quiz Answers

## Question 1: A tool contract should specify…
**Answer: B** — Args, types, side effects, and error modes

**Outcome 1:** Write tool contracts with typed arguments and error cases.

**Explanation:** Contracts make tool use testable and safe.

---

## Question 2: create_task(title, owner, due_date) without types risks…
**Answer: B** — Ambiguous/invalid calls the model invents

**Outcome 1:** Write tool contracts with typed arguments and error cases.

**Explanation:** Typed args reduce malformed calls.

---

## Question 3: When required fields are missing, prefer…
**Answer: B** — Asking a clarifying question

**Outcome 2:** Choose among answer, clarify, or call-tool based on the request.

**Explanation:** Clarify before side-effecting tools.

---

## Question 4: If the question is answerable without tools…
**Answer: B** — Answer directly per policy

**Outcome 2:** Choose among answer, clarify, or call-tool based on the request.

**Explanation:** Tool use is optional — not a reflex.

---

## Question 5: Verification after a tool call checks…
**Answer: B** — That the result matches the requested action/constraints

**Outcome 3:** Verify tool results against the user request before finalizing.

**Explanation:** Never trust tool output blindly.

---

## Question 6: Tool returns a due date in the past vs request. You should…
**Answer: B** — Flag/repair or ask before confirming to the user

**Outcome 3:** Verify tool results against the user request before finalizing.

**Explanation:** Verify semantic fit, not only parse success.

---

## Question 7: Tool timeouts should be handled with…
**Answer: B** — Budgeted retries and explicit user-visible errors

**Outcome 4:** Apply retry budgets and clear errors for tool failures.

**Explanation:** Failures need budgets and clear messaging.

---

## Question 8: Adversarial “call admin tools” prompts should…
**Answer: B** — Be refused when outside allowed tool policy

**Outcome 4:** Apply retry budgets and clear errors for tool failures.

**Explanation:** Tool policy is a safety boundary.

---

## Question 9: Audit logs for tools should capture…
**Answer: B** — Who/what/when/why with redaction

**Outcome 5:** Log tool calls in an audit schema without leaking secrets.

**Explanation:** Provenance without sensitive dumps.

---

## Question 10: Why log tool failures as well as successes?
**Answer: B** — To diagnose retries, abuse, and reliability issues

**Outcome 5:** Log tool calls in an audit schema without leaking secrets.

**Explanation:** Failure telemetry improves ops and safety.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
