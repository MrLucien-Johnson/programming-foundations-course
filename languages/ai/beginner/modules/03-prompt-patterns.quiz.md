# AI — Module 03: Prompt Patterns Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: Extraction prompts should define…
**Checks outcome 1:** Design extraction prompts that emit valid structured fields.

A) Only tone of voice  
B) Field names, types, and allowed empties  
C) The cloud vendor  
D) A canary percentage  

**Your answer:** _______________

---

### Question 2: Free text → JSON is brittle unless you…
**Checks outcome 1:** Design extraction prompts that emit valid structured fields.

A) Never validate  
B) Specify schema and validate outputs  
C) Raise temperature to max  
D) Skip examples  

**Your answer:** _______________

---

### Question 3: A required-field checklist tells the model…
**Checks outcome 2:** Specify required-field checklists and missing-data behavior.

A) To invent values for every field always  
B) Which fields must be present and what to do if absent  
C) To ignore urgency  
D) To output HTML only  

**Your answer:** _______________

---

### Question 4: If account ID is missing, a good pattern is…
**Checks outcome 2:** Specify required-field checklists and missing-data behavior.

A) Hallucinate an ID  
B) Leave null/omit per schema and flag incompleteness  
C) Crash the API key  
D) Retry infinitely  

**Your answer:** _______________

---

### Question 5: A repair prompt should…
**Checks outcome 3:** Add a review/repair pass that fixes structure without inventing facts.

A) Add new facts to “help”  
B) Fix invalid JSON/structure without changing meaning  
C) Remove all fields  
D) Translate to another language silently  

**Your answer:** _______________

---

### Question 6: A second review pass is useful to…
**Checks outcome 3:** Add a review/repair pass that fixes structure without inventing facts.

A) Increase cost only  
B) Flag missing fields or contradictions before finalizing  
C) Bypass safety  
D) Delete the taxonomy  

**Your answer:** _______________

---

### Question 7: An error taxonomy helps iteration by…
**Checks outcome 4:** Build an error taxonomy and track reductions across iterations.

A) Hiding failures  
B) Focusing fixes on the largest failure categories first  
C) Replacing the eval set  
D) Guaranteeing 100% validity  

**Your answer:** _______________

---

### Question 8: Tracking “invalid JSON” vs “wrong urgency” separately matters because…
**Checks outcome 4:** Build an error taxonomy and track reductions across iterations.

A) They need different mitigations  
B) They are the same bug  
C) Taxonomies are decorative  
D) Repair prompts fix urgency labels only  

**Your answer:** _______________

---

### Question 9: Few-shots for sarcasm/multiple issues help because…
**Checks outcome 5:** Cover tricky cases with targeted few-shot examples.

A) They waste tokens only  
B) They demonstrate judgment on hard cases the base rules under-specify  
C) They replace schemas  
D) They disable validation  

**Your answer:** _______________

---

### Question 10: Measuring % valid JSON on a fixed set proves…
**Checks outcome 1:** Design extraction prompts that emit valid structured fields.

A) Marketing copy quality  
B) Structural compliance of the extraction pattern  
C) Retrieval hit-rate  
D) TLS configuration  

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
