# Answers — CI for Terraform

## Question 1: What should a pull-request Terraform job normally produce?
**Answer: A** — Checks and a reviewable plan

**Explanation:** Prefer the option that shrinks blast radius, clarifies ownership, or matches the lab outcome for this module.

---

## Question 2: Why use OIDC federation in CI?
**Answer: A** — To obtain short-lived scoped credentials

**Explanation:** Prefer the option that shrinks blast radius, clarifies ownership, or matches the lab outcome for this module.

---

## Question 3: What does CI concurrency reduce?
**Answer: A** — Competing runs against one environment

**Explanation:** Prefer the option that shrinks blast radius, clarifies ownership, or matches the lab outcome for this module.

---

## Question 4: Why restrict plan artifacts?
**Answer: A** — They can contain sensitive infrastructure data

**Explanation:** Prefer the option that shrinks blast radius, clarifies ownership, or matches the lab outcome for this module.

---

## Question 5: What should gate production apply?
**Answer: A** — Trusted branch, reviewed plan/commit, and protected approval

**Explanation:** Prefer the option that shrinks blast radius, clarifies ownership, or matches the lab outcome for this module.

---

**Teaching note:** Prefer reasoning about outcomes, blast radius, and evidence over trivia.
