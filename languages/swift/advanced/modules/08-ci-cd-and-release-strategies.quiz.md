# Swift Advanced — Module 08: CI/CD and Release Strategies Quiz: Test Your Understanding

## Instructions

Answer these questions about the skills in this module's learning outcomes.
Try from memory first — then check the answers file for explanations.

## Questions

### Question 1: A canary release primarily…
**Checks outcome 1:** Choose canary, blue-green, or rolling releases for a risk profile.

A) Ships to 100% instantly  
B) Exposes a new version to a small slice of traffic first  
C) Deletes the old version immediately  
D) Skips health checks  

**Your answer:** _______________

---

### Question 2: Blue-green deployment keeps…
**Checks outcome 1:** Choose canary, blue-green, or rolling releases for a risk profile.

A) Two environments so you can switch traffic atomically and roll back fast  
B) No way to roll back  
C) Only canary pods forever  
D) Secrets in the image  

**Your answer:** _______________

---

### Question 3: Feature flags help you…
**Checks outcome 2:** Use feature flags and safe config changes to control exposure.

A) Avoid all testing  
B) Decouple deploy from release and kill-switch bad behavior  
C) Skip AuthZ  
D) Ignore migrations  

**Your answer:** _______________

---

### Question 4: A risky config change should be…
**Checks outcome 2:** Use feature flags and safe config changes to control exposure.

A) Pushed globally with no kill switch  
B) Rolled out gradually with monitoring and a fast revert path  
C) Stored only in chat history  
D) Applied by editing production DB by hand mid-flight  

**Your answer:** _______________

---

### Question 5: Expand/contract migrations reduce risk by…
**Checks outcome 3:** Plan production database migrations that avoid downtime and lockouts.

A) Dropping columns in the same deploy that removes all readers  
B) Adding new schema first, dual-writing/reading, then removing old later  
C) Rewriting applied migration files in place  
D) Skipping backups  

**Your answer:** _______________

---

### Question 6: Taking a long ACCESS EXCLUSIVE lock on a hot table during peak…
**Checks outcome 3:** Plan production database migrations that avoid downtime and lockouts.

A) Is ideal for UX  
B) Can stall writes/reads and cause an outage  
C) Improves canaries  
D) Replaces feature flags  

**Your answer:** _______________

---

### Question 7: A rollback plan needs…
**Checks outcome 4:** Execute rollbacks with clear versioning and changelogs.

A) Hope  
B) A known-good version, data compatibility rules, and a practiced switch  
C) Deleting metrics first  
D) Force-pushing secrets  

**Your answer:** _______________

---

### Question 8: Changelogs/versioning help incidents by…
**Checks outcome 4:** Execute rollbacks with clear versioning and changelogs.

A) Hiding what shipped  
B) Making it obvious what changed when symptoms started  
C) Replacing monitoring  
D) Guaranteeing zero bugs  

**Your answer:** _______________

---

### Question 9: Rolling deploys gradually replace instances. Main risk to watch?
**Checks outcome 1:** Choose canary, blue-green, or rolling releases for a risk profile.

A) Mixed versions briefly serving traffic  
B) Instant dual environments for free  
C) Automatic schema expand/contract  
D) Feature flags becoming unnecessary  

**Your answer:** _______________

---

### Question 10: Turning a flag on for 5% of users is similar in spirit to…
**Checks outcome 2:** Use feature flags and safe config changes to control exposure.

A) A full blue-green cutover with no metrics  
B) A canary / progressive delivery of a behavior  
C) Deleting the old code path immediately in DB  
D) Skipping CI  

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
