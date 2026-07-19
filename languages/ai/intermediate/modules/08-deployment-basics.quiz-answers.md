# AI — Module 08: Deployment Basics Quiz Answers

## Question 1: Pre-deploy for an AI feature should include…
**Answer: B** — Eval harness + safety tests passing gates

**Outcome 1:** Create a deployment checklist including eval and safety gates.

**Explanation:** Gates before traffic.

---

## Question 2: A deployment checklist exists to…
**Answer: B** — Make release steps consistent and auditable

**Outcome 1:** Create a deployment checklist including eval and safety gates.

**Explanation:** Checklists catch skipped critical steps.

---

## Question 3: Prompt versioning enables…
**Answer: B** — Pinning, comparing, and rolling back specific behaviors

**Outcome 2:** Version prompts/schemas and keep a change log.

**Explanation:** Versions make releases reversible.

---

## Question 4: Schema version in a rollout matters when…
**Answer: A** — Clients parse structured outputs

**Outcome 2:** Version prompts/schemas and keep a change log.

**Explanation:** Breaking schemas break consumers.

---

## Question 5: Rollback triggers might include…
**Answer: B** — Eval score drops, safety failures, or user-impact spikes

**Outcome 3:** Define rollback triggers from eval and user-impact signals.

**Explanation:** Predefine what “bad” means.

---

## Question 6: User-impact signals complement offline evals because…
**Answer: B** — Production can reveal gaps offline missed

**Outcome 3:** Define rollback triggers from eval and user-impact signals.

**Explanation:** Online + offline together.

---

## Question 7: Smoke tests after deploy should hit…
**Answer: B** — The most important user flows quickly

**Outcome 4:** Run smoke tests on critical flows post-deploy.

**Explanation:** Fast confidence on critical paths.

---

## Question 8: A failed smoke test should…
**Answer: B** — Stop rollout / trigger rollback per playbook

**Outcome 4:** Run smoke tests on critical flows post-deploy.

**Explanation:** Smoke fails are stop-the-line signals.

---

## Question 9: Shadow evaluation means…
**Answer: B** — Scoring a new version on live inputs without affecting users

**Outcome 5:** Use staged rollout with shadow evaluation where appropriate.

**Explanation:** Shadow = observe before expose.

---

## Question 10: Staged rollout without a rollback plan is risky because…
**Answer: B** — You may lack a fast path back to known-good

**Outcome 5:** Use staged rollout with shadow evaluation where appropriate.

**Explanation:** Progressive delivery still needs an escape hatch.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
