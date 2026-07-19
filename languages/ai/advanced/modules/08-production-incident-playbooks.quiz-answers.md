# AI — Module 08: Production Incident Playbooks Quiz Answers

## Question 1: A cost-spike playbook’s first mitigations often include…
**Answer: B** — Rate limits, disabling expensive paths, or rolling back a canary

**Outcome 1:** Write playbooks for cost spikes, safety regressions, and quality drops.

**Explanation:** Stop the bleeding on spend.

---

## Question 2: A safety-regression playbook should prioritize…
**Answer: B** — Containment (stricter filters/flags off) before deep debugging

**Outcome 1:** Write playbooks for cost spikes, safety regressions, and quality drops.

**Explanation:** Safety first, then root cause.

---

## Question 3: Feature flags in incidents enable…
**Answer: B** — Fast disable of risky behavior without full redeploy

**Outcome 2:** Define immediate mitigations: flags, degrade modes, stricter filters.

**Explanation:** Flags are kill switches.

---

## Question 4: Degraded mode during an incident should be…
**Answer: B** — Predeclared so operators know the safe subset of behavior

**Outcome 2:** Define immediate mitigations: flags, degrade modes, stricter filters.

**Explanation:** Know the safe subset in advance.

---

## Question 5: Incident drills matter because…
**Answer: B** — Practice reveals gaps in detection and steps under time pressure

**Outcome 3:** Run incident drills that exercise detection and response.

**Explanation:** Drill → improve playbooks.

---

## Question 6: A drill that never triggers alerts shows…
**Answer: B** — A detection gap to fix

**Outcome 3:** Run incident drills that exercise detection and response.

**Explanation:** Detection is part of the playbook.

---

## Question 7: Communication templates reduce…
**Answer: B** — Ad-hoc conflicting messages during stress

**Outcome 4:** Prepare internal and user-facing communication templates.

**Explanation:** Say the right thing quickly.

---

## Question 8: User-facing incident notes should…
**Answer: B** — Be accurate, calm, and actionable without oversharing

**Outcome 4:** Prepare internal and user-facing communication templates.

**Explanation:** Honest, careful communication.

---

## Question 9: After action items should include…
**Answer: B** — New eval cases and tighter guardrails for the failure mode

**Outcome 5:** Close the loop by updating evals and guardrails after incidents.

**Explanation:** Turn incidents into permanent controls.

---

## Question 10: Updating evals post-incident prevents…
**Answer: B** — The same failure class from shipping unnoticed again

**Outcome 5:** Close the loop by updating evals and guardrails after incidents.

**Explanation:** Regression tests for production pain.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
