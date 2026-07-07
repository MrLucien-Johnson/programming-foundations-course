# Go Intermediate — Module 06: Security Basics Quiz: Test Your Understanding

## Instructions

Answer these questions about what you've learned. Try to answer from memory first!

## Questions

### Question 1: You need to run the test suite. Which command should you use?
A) Change multiple variables at once so you cannot compare outcomes.  
B) Ship changes without documentation.  
C) `go test ./...`  
D) Over-mocking (tests assert implementation details instead of outcomes).  

**Your answer:** _______________

---

### Question 2: You need to run lint checks. Which command should you use?
A) Add at least **3 focused unit tests** that cover normal cases and edge cases.  
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.  
C) Use tooling to keep quality high: gofmt + golangci-lint.  
D) `golangci-lint run`  

**Your answer:** _______________

---

### Question 3: You need to format the code. Which command should you use?
A) `gofmt -w .`  
B) `go test ./...`  
C) Create a short write-up: what changed, why, and how you verified it.  
D) Write tests that prove correctness and prevent regressions.  

**Your answer:** _______________

---

### Question 4: Which action best satisfies the Core requirements?
A) Implement a small feature tied to this module in an existing starter app.  
B) Run: `go test ./...`  
C) `golangci-lint run`  
D) Run the module tests and confirm they pass.  

**Your answer:** _______________

---

### Question 5: Which action upgrades the work to the Better level?
A) Add an integration test that hits a real boundary (HTTP, database, file system, or process).  
B) Treat every request as safe without review.  
C) Write tests that prove correctness and prevent regressions.  
D) Run: `go test ./...`  

**Your answer:** _______________

---

### Question 6: Which action qualifies as a Beast Mode upgrade?
A) Add a performance or reliability improvement and **measure** the impact.  
B) Document decisions and constraints clearly for reviewers.  
C) Implement a small feature tied to this module in an existing starter app.  
D) Update the README with setup, run, and test commands.  

**Your answer:** _______________

---

### Question 7: Before submitting, which verification step must you complete?
A) Add or update documentation (README notes or ADR-style notes).  
B) Making performance claims without measurements.  
C) Shipping without an automated test run in CI.  
D) Run the module tests and confirm they pass.  

**Your answer:** _______________

---

### Question 8: Which testing requirement must be satisfied to pass?
A) Add a “failure mode” test (timeouts, invalid input, concurrency, or partial failure).  
B) AuthZ checks + least privilege (35 min)  
C) Jump to the next module without verifying results.  
D) All work must be covered by **gofmt + lint + tests in CI**.  

**Your answer:** _______________

---

### Question 9: Which option would be a common mistake to avoid?
A) Treat every request as safe without review.  
B) Shipping without an automated test run in CI.  
C) Add at least **3 focused unit tests** that cover normal cases and edge cases.  
D) Add or update documentation (README notes or ADR-style notes).  

**Your answer:** _______________

---

### Question 10: A reviewer asks what capability you demonstrated. Which outcome matches?
A) Update the README with setup, run, and test commands.  
B) Verify the primary feature works with normal and edge-case inputs.  
C) Run: `gofmt -w .`  
D) Explain the core concepts and tradeoffs for **Security Basics**.  

**Your answer:** _______________

---

## Check Your Answers

Once you finish, check the answers file for explanations.

## How Did You Do?

- **10/10 correct:** Excellent! You understand the module well.
- **8-9 correct:** Great work! Review what you missed.
- **0-7 correct:** Review the module and try again.

---

**Good luck!** Check your answers when you are ready.