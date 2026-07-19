# AI — Module 05: Guardrails and Safety Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Output controls in RAG should…
**Checks outcome 1:** Enforce input/output controls including source-only and refusal rules.

A) Allow answers without evidence  
B) Require evidence or refuse/abstain  
C) Strip all citations  
D) Log raw secrets  

**Your answer:** _______________

---

### Question 2: Input controls typically…
**Checks outcome 1:** Enforce input/output controls including source-only and refusal rules.

A) Trust all user text as system policy  
B) Detect/block injection and disallowed content before tools run  
C) Disable AuthZ  
D) Skip evals  

**Your answer:** _______________

---

### Question 3: Least-privilege tools mean…
**Checks outcome 2:** Constrain tools with least privilege and verify via tests.

A) Every agent can drop production tables  
B) Only tools needed for the task are exposed, with arg limits  
C) No tools ever  
D) Tools without contracts  

**Your answer:** _______________

---

### Question 4: Tests should try to make the agent…
**Checks outcome 2:** Constrain tools with least privilege and verify via tests.

A) Only summarize kindly  
B) Call disallowed tools or exfiltrate secrets — and verify denial  
C) Skip audit logs  
D) Disable refusals  

**Your answer:** _______________

---

### Question 5: Red-team suites focus on…
**Checks outcome 3:** Build red-team suites that target top abuse paths.

A) Happy-path UX copy  
B) Highest-impact abuse and bypass attempts  
C) Font kerning  
D) CDN purge times  

**Your answer:** _______________

---

### Question 6: Prompt injection into tool args is dangerous because…
**Checks outcome 3:** Build red-team suites that target top abuse paths.

A) Args are never executed  
B) It can trigger unintended side effects  
C) It only affects CSS  
D) It improves grounding  

**Your answer:** _______________

---

### Question 7: A CI safety gate should…
**Checks outcome 4:** Add safety gates in CI that fail on safety regressions.

A) Be optional forever  
B) Fail the build when safety evals regress beyond threshold  
C) Only run on Fridays  
D) Store production keys in artifacts  

**Your answer:** _______________

---

### Question 8: Safety tests belong in the harness so…
**Checks outcome 4:** Add safety gates in CI that fail on safety regressions.

A) They are forgotten  
B) Every prompt change re-checks policy behavior  
C) Latency is ignored  
D) Schemas are deleted  

**Your answer:** _______________

---

### Question 9: Escalation for high-risk outputs may include…
**Checks outcome 5:** Design escalation paths for high-risk model outputs.

A) Auto-publish always  
B) Human review, block, or safe-complete paths  
C) Higher temperature  
D) Disabling logs  

**Your answer:** _______________

---

### Question 10: Audit-friendly logging for safety events should…
**Checks outcome 5:** Design escalation paths for high-risk model outputs.

A) Include full sensitive payloads always  
B) Record category and action taken without unnecessary secrets  
C) Be off in production  
D) Replace threat models  

**Your answer:** _______________

---

## Check Your Answers

Once you finish, check the answers file for explanations.

## How Did You Do?

- **10/10 correct:** Excellent — you can apply this module's outcomes.
- **8-9 correct:** Strong — review the missed outcome(s).
- **0-7 correct:** Revisit the lessons for those outcomes, then retry.

---

**Good luck!** Check your answers when you are ready.
