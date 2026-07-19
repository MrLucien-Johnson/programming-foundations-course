# AI — Module 02: Prompting Basics Quiz Answers

## Question 1: “Be helpful” alone is a weak prompt because…
**Answer: B** — It lacks constraints and a checkable output shape

**Outcome 1:** Write prompts with explicit constraints and output format.

**Explanation:** Constraints and format make behavior repeatable.

---

## Question 2: Asking for bullet summaries with “no invented policies” is an example of…
**Answer: B** — An explicit behavioral constraint

**Outcome 1:** Write prompts with explicit constraints and output format.

**Explanation:** Constraints bound what the model may say.

---

## Question 3: Why delimit user content from instructions?
**Answer: B** — To reduce instruction/data mix-ups and injection success

**Outcome 2:** Separate instructions from user content with clear delimiters.

**Explanation:** Delimiters clarify what is data vs policy.

---

## Question 4: Putting untrusted ticket text in the same blob as rules without markers risks…
**Answer: B** — The model treating user text as new instructions

**Outcome 2:** Separate instructions from user content with clear delimiters.

**Explanation:** Injection thrives when data and instructions blur.

---

## Question 5: Few-shot examples help most when they…
**Answer: B** — Show the exact format and edge-case handling you want

**Outcome 3:** Add few-shot examples that demonstrate the desired behavior.

**Explanation:** Examples teach shape and judgment better than adjectives.

---

## Question 6: Three short diverse examples usually beat…
**Answer: A** — One huge contradictory dump

**Outcome 3:** Add few-shot examples that demonstrate the desired behavior.

**Explanation:** Contradictory or bloated examples hide the rule.

---

## Question 7: Notes missing an owner — preferred behavior?
**Answer: B** — Clarify or refuse per the rule

**Outcome 4:** Handle missing info with clarify-or-refuse rules.

**Explanation:** Clarify/refuse beats fabrication for missing keys.

---

## Question 8: A negative test for prompting checks that…
**Answer: B** — The model asks/refuses when required info is absent

**Outcome 4:** Handle missing info with clarify-or-refuse rules.

**Explanation:** Negative tests lock safe behavior.

---

## Question 9: A scorecard with format/factuality/helpfulness lets you…
**Answer: B** — Track regressions across prompt versions

**Outcome 5:** Score outputs on format, factuality, and helpfulness.

**Explanation:** Multi-axis scores catch format wins that hurt factuality.

---

## Question 10: Structured output requests (headings/JSON fields) mainly improve…
**Answer: B** — Downstream parsing and consistent evaluation

**Outcome 1:** Write prompts with explicit constraints and output format.

**Explanation:** Structure makes outputs usable and testable.

---

## How Did You Do?

- **10/10 correct:** Excellent! You are ready to move on.
- **8-9 correct:** Great work — review the missed outcomes.
- **0-7 correct:** Revisit the module lessons, then try again.
