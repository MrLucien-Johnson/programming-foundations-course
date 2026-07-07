# Go Intermediate — Module 08: Deployment and CI Quiz: Test Your Understanding

## Instructions

Answer these questions about what you've learned. Try to answer from memory first!

## Questions

### Question 1: You need to run the test suite. Which command should you use?
A) `go test ./...`  
B) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.  
C) All work must be covered by **gofmt + lint + tests in CI**.  
D) Containers for local dev and CI (45 min)  

**Your answer:** _______________

---

### Question 2: You need to run lint checks. Which command should you use?
A) Run: `golangci-lint run`  
B) `golangci-lint run`  
C) Over-mocking (tests assert implementation details instead of outcomes).  
D) Document decisions and constraints clearly for reviewers.  

**Your answer:** _______________

---

### Question 3: You need to format the code. Which command should you use?
A) Introduce a quality gate (pre-commit hook or CI step) that prevents common regressions.  
B) Over-mocking (tests assert implementation details instead of outcomes).  
C) `gofmt -w .`  
D) Copy the starter pack from `languages/go/intermediate/starter-pack` into a new working folder.  

**Your answer:** _______________

---

### Question 4: Which action best satisfies the Core requirements?
A) Review the module goals and plan how you will ship safely with automation.  
B) Change multiple variables at once so you cannot compare outcomes.  
C) Implement a small feature tied to this module in an existing starter app.  
D) If the module involves a database, tests must run against an isolated schema/database.  

**Your answer:** _______________

---

### Question 5: Which action upgrades the work to the Better level?
A) Deployments: health checks + migrations + rollback plan (45 min)  
B) Containers for local dev and CI (45 min)  
C) Treat every request as safe without review.  
D) Add an integration test that hits a real boundary (HTTP, database, file system, or process).  

**Your answer:** _______________

---

### Question 6: Which action qualifies as a Beast Mode upgrade?
A) Add a performance or reliability improvement and **measure** the impact.  
B) Add a CI workflow or script that runs tests automatically.  
C) If the module involves a database, tests must run against an isolated schema/database.  
D) Run: `go test ./...`  

**Your answer:** _______________

---

### Question 7: Before submitting, which verification step must you complete?
A) Document decisions in a short README section (assumptions, tradeoffs, next steps).  
B) Add an integration test that hits a real boundary (HTTP, database, file system, or process).  
C) Run the module tests and confirm they pass.  
D) Treat every request as safe without review.  

**Your answer:** _______________

---

### Question 8: Which testing requirement must be satisfied to pass?
A) `golangci-lint run`  
B) Run: `gofmt -w .`  
C) `gofmt -w .`  
D) All work must be covered by **gofmt + lint + tests in CI**.  

**Your answer:** _______________

---

### Question 9: Which option would be a common mistake to avoid?
A) Ship changes without documentation.  
B) Tests must be deterministic (no flakes) and runnable by a reviewer.  
C) Run: `golangci-lint run`  
D) Shipping without an automated test run in CI.  

**Your answer:** _______________

---

### Question 10: A reviewer asks what capability you demonstrated. Which outcome matches?
A) Add a performance or reliability improvement and **measure** the impact.  
B) Explain the core concepts and tradeoffs for **Deployment and CI**.  
C) Add a CI workflow or script that runs tests automatically.  
D) Create a short write-up: what changed, why, and how you verified it.  

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