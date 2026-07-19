# AI — Module 05: Safety and Policy Basics Quiz Answers

## Question 1: A safety checklist for a summarizer should cover…
**Answer: B** — Privacy, harmful content, and prompt injection

**Outcome 1:** Apply a safety checklist covering privacy, harm, and injection.

**Explanation:** Checklists make safety reviewable.

---

## Question 2: Treating user input as trusted instructions is dangerous because…
**Answer: B** — It enables prompt injection and policy bypass

**Outcome 1:** Apply a safety checklist covering privacy, harm, and injection.

**Explanation:** Untrusted input must not override policy.

---

## Question 3: Refuse/redirect is better than “refuse everything” when…
**Answer: A** — You can safely help within policy (e.g., point to allowed resources)

**Outcome 2:** Design refuse/redirect behaviors for unsafe requests.

**Explanation:** Proportionate safe completion beats blanket refusal.

---

## Question 4: Unsafe request handling should be…
**Answer: B** — Specified as explicit behaviors in the prompt/policy

**Outcome 2:** Design refuse/redirect behaviors for unsafe requests.

**Explanation:** Specified behavior is testable.

---

## Question 5: Source-only Q&A means…
**Answer: B** — Answer only with evidence from provided sources or abstain

**Outcome 3:** Use source-only answering to reduce hallucinations in doc Q&A.

**Explanation:** Grounding cuts hallucinations in RAG-like flows.

---

## Question 6: If sources lack the answer, prefer…
**Answer: B** — Abstain / say insufficient evidence

**Outcome 3:** Use source-only answering to reduce hallucinations in doc Q&A.

**Explanation:** Abstention is a safety feature.

---

## Question 7: Red-team sets should include…
**Answer: B** — Injection and data-exfiltration style attacks

**Outcome 4:** Red-team prompts for injection and exfiltration attempts.

**Explanation:** Adversarial coverage finds policy holes.

---

## Question 8: A prompt that says “ignore previous instructions” in user data tests…
**Answer: B** — Injection resistance

**Outcome 4:** Red-team prompts for injection and exfiltration attempts.

**Explanation:** Classic injection probe.

---

## Question 9: Severity models (low/med/high) drive…
**Answer: B** — Different required actions and escalations

**Outcome 5:** Define severity levels and escalation paths for high-risk cases.

**Explanation:** Severity maps to response playbooks.

---

## Question 10: High-risk cases often need…
**Answer: B** — Human handoff, logging, and/or blocks

**Outcome 5:** Define severity levels and escalation paths for high-risk cases.

**Explanation:** Escalation paths contain blast radius.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
