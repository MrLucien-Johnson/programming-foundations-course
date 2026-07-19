# Swift Intermediate — Module 03: Git and Collaboration Quiz Answers

## Question 1: Which commit message is more useful in review history?
**Answer: C** — `Validate email before creating user to prevent duplicate accounts`

**Outcome 1:** Use a clear branching strategy and write commits that explain why a change happened.

**Explanation:** Good commits state intent/why, not just that something changed.

---

## Question 2: You are starting a feature on a shared repo using short-lived feature branches. Where should the work begin?
**Answer: B** — A feature branch off an up-to-date `main`

**Outcome 1:** Use a clear branching strategy and write commits that explain why a change happened.

**Explanation:** Feature branches keep `main` stable and make PRs reviewable.

---

## Question 3: What belongs on a PR review checklist?
**Answer: B** — Correctness, tests, risk, and clarity of the change

**Outcome 2:** Open and review pull requests using a practical checklist and actionable feedback.

**Explanation:** Reviews focus on behavior, tests, risk, and readability — not trivia.

---

## Question 4: Which review comment is more actionable?
**Answer: C** — `Can we extract the retry loop into a helper and add a test for the timeout path?`

**Outcome 2:** Open and review pull requests using a practical checklist and actionable feedback.

**Explanation:** Actionable feedback names the problem and a concrete next step.

---

## Question 5: You and a teammate both edited the same lines. Git stops with a conflict. What do you do?
**Answer: B** — Resolve the conflicting hunks, test, then continue the merge/rebase

**Outcome 3:** Resolve merge conflicts and rebase safely without rewriting shared history carelessly.

**Explanation:** Conflicts need intentional resolution and verification — never commit conflict markers.

---

## Question 6: When is rewriting history with rebase riskiest?
**Answer: B** — On a shared branch others already pulled

**Outcome 3:** Resolve merge conflicts and rebase safely without rewriting shared history carelessly.

**Explanation:** Rebasing shared history forces teammates to recover; prefer merge or coordinate carefully.

---

## Question 7: CI fails on your PR. Best next step?
**Answer: B** — Open the failing job logs, reproduce locally if possible, fix, and push

**Outcome 4:** Diagnose CI failures from logs and fix the underlying issue before merging.

**Explanation:** CI failures are signals — read logs, fix root cause, re-run.

---

## Question 8: A CI job fails with a flaky timeout only sometimes. What is a professional response?
**Answer: B** — Stabilize the test (determinism/timeouts/isolation) or quarantine with a tracked fix

**Outcome 4:** Diagnose CI failures from logs and fix the underlying issue before merging.

**Explanation:** Flakes erode trust. Fix isolation/timing or track quarantine with an owner.

---

## Question 9: Why keep commits focused (one logical change) when collaborating?
**Answer: B** — Reviewers can understand, revert, and bisect more easily

**Outcome 1:** Use a clear branching strategy and write commits that explain why a change happened.

**Explanation:** Small, purposeful commits improve review and recovery.

---

## Question 10: A PR description should mainly help reviewers by…
**Answer: B** — Explaining intent, risk, test plan, and how to verify

**Outcome 2:** Open and review pull requests using a practical checklist and actionable feedback.

**Explanation:** Good PR descriptions speed correct review and reduce back-and-forth.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
