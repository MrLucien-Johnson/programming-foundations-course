# AI — Module 01: Advanced Prompting: Tool Use Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: A tool contract should specify…
**Checks outcome 1:** Write tool contracts with typed arguments and error cases.

A) Only a friendly name  
B) Args, types, side effects, and error modes  
C) The model’s favorite color  
D) Unlimited privileges  

**Your answer:** _______________

---

### Question 2: create_task(title, owner, due_date) without types risks…
**Checks outcome 1:** Write tool contracts with typed arguments and error cases.

A) Perfect validation  
B) Ambiguous/invalid calls the model invents  
C) Faster audits  
D) No side effects  

**Your answer:** _______________

---

### Question 3: When required fields are missing, prefer…
**Checks outcome 2:** Choose among answer, clarify, or call-tool based on the request.

A) Calling the tool with guesses  
B) Asking a clarifying question  
C) Ignoring the user  
D) Disabling the tool forever  

**Your answer:** _______________

---

### Question 4: If the question is answerable without tools…
**Checks outcome 2:** Choose among answer, clarify, or call-tool based on the request.

A) Always call every tool  
B) Answer directly per policy  
C) Refuse always  
D) Invent a tool result  

**Your answer:** _______________

---

### Question 5: Verification after a tool call checks…
**Checks outcome 3:** Verify tool results against the user request before finalizing.

A) That any JSON returned is celebrated  
B) That the result matches the requested action/constraints  
C) Only latency  
D) The CDN  

**Your answer:** _______________

---

### Question 6: Tool returns a due date in the past vs request. You should…
**Checks outcome 3:** Verify tool results against the user request before finalizing.

A) Ship it anyway  
B) Flag/repair or ask before confirming to the user  
C) Hide the field  
D) Raise temperature  

**Your answer:** _______________

---

### Question 7: Tool timeouts should be handled with…
**Checks outcome 4:** Apply retry budgets and clear errors for tool failures.

A) Infinite silent waits  
B) Budgeted retries and explicit user-visible errors  
C) Pretend success  
D) Deleting the audit log  

**Your answer:** _______________

---

### Question 8: Adversarial “call admin tools” prompts should…
**Checks outcome 4:** Apply retry budgets and clear errors for tool failures.

A) Bypass contracts  
B) Be refused when outside allowed tool policy  
C) Auto-approve  
D) Disable verification  

**Your answer:** _______________

---

### Question 9: Audit logs for tools should capture…
**Checks outcome 5:** Log tool calls in an audit schema without leaking secrets.

A) Raw secrets in arguments  
B) Who/what/when/why with redaction  
C) Nothing  
D) Only emoji reactions  

**Your answer:** _______________

---

### Question 10: Why log tool failures as well as successes?
**Checks outcome 5:** Log tool calls in an audit schema without leaking secrets.

A) To inflate metrics  
B) To diagnose retries, abuse, and reliability issues  
C) Because successes do not matter  
D) To store PII longer  

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
