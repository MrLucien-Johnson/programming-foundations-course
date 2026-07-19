# AI — Module 03: Evals at Scale Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: A scalable eval runner should log…
**Checks outcome 1:** Design batch eval runners with retries, budgets, and reproducibility.

A) Nothing  
B) Dataset, prompt, scorer versions plus budgets/retries  
C) Only wall time  
D) Production passwords  

**Your answer:** _______________

---

### Question 2: Batching evals primarily helps…
**Checks outcome 1:** Design batch eval runners with retries, budgets, and reproducibility.

A) Hide failures  
B) Throughput and cost control for large sets  
C) Delete stratification  
D) Skip gates  

**Your answer:** _______________

---

### Question 3: Stratified sampling matters because…
**Checks outcome 2:** Detect quality drift with stratified sampling and cadence.

A) All users are identical  
B) Overall averages can hide regressions in a segment  
C) Drift cannot exist  
D) Labels are free  

**Your answer:** _______________

---

### Question 4: A drift metric without a cadence is weak because…
**Checks outcome 2:** Detect quality drift with stratified sampling and cadence.

A) Cadence is optional decoration  
B) You will not notice slow quality decay in time  
C) Shadow evals forbid cadence  
D) Budgets replace monitoring  

**Your answer:** _______________

---

### Question 5: Stop-the-line criteria should be…
**Checks outcome 3:** Define stop-the-line criteria for regressions.

A) Invented during the outage  
B) Predeclared thresholds that halt releases  
C) Secret from eng  
D) Only aesthetic  

**Your answer:** _______________

---

### Question 6: A sudden schema-validity collapse should…
**Checks outcome 3:** Define stop-the-line criteria for regressions.

A) Ship anyway  
B) Trip stop-the-line and rollback/investigate  
C) Raise temperature  
D) Delete the dataset  

**Your answer:** _______________

---

### Question 7: Shadow eval on live traffic must be…
**Checks outcome 4:** Run privacy-safe shadow evaluation on live traffic.

A) Logged with full sensitive payloads publicly  
B) Privacy-safe (minimize/redact) and non-user-impacting  
C) Allowed to change user answers  
D) Unversioned  

**Your answer:** _______________

---

### Question 8: Shadow scoring a new prompt helps you…
**Checks outcome 4:** Run privacy-safe shadow evaluation on live traffic.

A) Skip offline sets forever  
B) Estimate live impact before progressive delivery  
C) Avoid canaries  
D) Disable labeling  

**Your answer:** _______________

---

### Question 9: Rater calibration reduces…
**Checks outcome 5:** Operate human labeling with calibration across raters.

A) Dataset size needs  
B) Inconsistent human scores that muddy drift signals  
C) The need for automation  
D) Budgets  

**Your answer:** _______________

---

### Question 10: A labeling workflow should include…
**Checks outcome 5:** Operate human labeling with calibration across raters.

A) One rater forever with no guide  
B) Guidelines, examples, and periodic agreement checks  
C) Public posting of raw customer text  
D) No audit trail  

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
