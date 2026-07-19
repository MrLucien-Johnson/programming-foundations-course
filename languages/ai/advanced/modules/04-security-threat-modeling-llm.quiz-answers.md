# AI — Module 04: Security Threat Modeling for LLM Apps Quiz Answers

## Question 1: Threat modeling an agent should list…
**Answer: B** — Assets, attackers, abuse paths, and mitigations

**Outcome 1:** Produce a threat model with mitigations for an LLM app.

**Explanation:** Structured threats → prioritized controls.

---

## Question 2: Tool abuse as a threat means…
**Answer: B** — Attackers coerce the agent into harmful side effects

**Outcome 1:** Produce a threat model with mitigations for an LLM app.

**Explanation:** Agents + tools = actionable attack surface.

---

## Question 3: Red-team suites should map to…
**Answer: B** — Top threats from the model

**Outcome 2:** Build red-team suites targeting top threats (injection, tool abuse).

**Explanation:** Tests follow the threat model.

---

## Question 4: Injection that tries to exfiltrate secrets should expect…
**Answer: B** — Containment/refusal and no secret leakage

**Outcome 2:** Build red-team suites targeting top threats (injection, tool abuse).

**Explanation:** Security tests assert negative outcomes.

---

## Question 5: Least-privilege tool policy is verified by…
**Answer: B** — Tests that attempt disallowed tools/args and expect denial

**Outcome 3:** Enforce least-privilege tool policies verified by tests.

**Explanation:** Prove the policy holds.

---

## Question 6: Over-broad tools increase…
**Answer: B** — Blast radius when injection succeeds

**Outcome 3:** Enforce least-privilege tool policies verified by tests.

**Explanation:** Privilege amplifies compromise.

---

## Question 7: Retention rules for prompts/outputs reduce…
**Answer: B** — Long-term exposure of sensitive content

**Outcome 4:** Apply data minimization and retention to prompts/outputs.

**Explanation:** Minimize how long risk lives.

---

## Question 8: Data minimization says…
**Answer: B** — Collect/process only what the task needs

**Outcome 4:** Apply data minimization and retention to prompts/outputs.

**Explanation:** Less data → less breach impact.

---

## Question 9: Supply-chain policy for prompts/evals covers…
**Answer: B** — Integrity/ownership of prompt packs, datasets, and scorers

**Outcome 5:** Plan incident response and supply-chain controls for AI artifacts.

**Explanation:** AI artifacts are part of the trusted compute base.

---

## Question 10: Incident response for a prompt-injection breach should include…
**Answer: B** — Triage, containment (flags/tool lockdown), and follow-up hardening

**Outcome 5:** Plan incident response and supply-chain controls for AI artifacts.

**Explanation:** Security IR applies to LLM apps too.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
