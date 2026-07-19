# ai / beginner — Quiz Alignment Sheet

Codecademy-style mapping: each learning outcome is tested by at least one quiz item.

Track: `languages/ai/beginner/modules/`

## 01-ai-foundations

| Outcome | Quiz questions |
|---|---|
| LO1: Translate a vague request into goal, constraints, and success criteria. | Q1, Q2 |
| LO2: Write a one-page task spec with inputs, outputs, and failure modes. | Q3, Q4 |
| LO3: Build a small eval set covering good, bad, and ambiguous cases. | Q5, Q6 |
| LO4: Add grounding/fallback rules and measure their effect on failures. | Q7, Q8 |
| LO5: Version prompt/spec changes with an iteration log. | Q9, Q10 |

## 02-prompting-basics

| Outcome | Quiz questions |
|---|---|
| LO1: Write prompts with explicit constraints and output format. | Q1, Q2, Q10 |
| LO2: Separate instructions from user content with clear delimiters. | Q3, Q4 |
| LO3: Add few-shot examples that demonstrate the desired behavior. | Q5, Q6 |
| LO4: Handle missing info with clarify-or-refuse rules. | Q7, Q8 |
| LO5: Score outputs on format, factuality, and helpfulness. | Q9 |

## 03-prompt-patterns

| Outcome | Quiz questions |
|---|---|
| LO1: Design extraction prompts that emit valid structured fields. | Q1, Q2, Q10 |
| LO2: Specify required-field checklists and missing-data behavior. | Q3, Q4 |
| LO3: Add a review/repair pass that fixes structure without inventing facts. | Q5, Q6 |
| LO4: Build an error taxonomy and track reductions across iterations. | Q7, Q8 |
| LO5: Cover tricky cases with targeted few-shot examples. | Q9 |

## 04-evaluation-and-iteration

| Outcome | Quiz questions |
|---|---|
| LO1: Create a rubric scorers can apply consistently. | Q1, Q2 |
| LO2: Build a regression set and compare baseline vs improved prompts. | Q3, Q4, Q10 |
| LO3: Use golden answers for qualitative spot checks. | Q5 |
| LO4: Prioritize fixes by failure-category frequency. | Q6, Q7 |
| LO5: Add abstain/fallback rules tied to confidence thresholds. | Q8, Q9 |

## 05-safety-and-policy-basics

| Outcome | Quiz questions |
|---|---|
| LO1: Apply a safety checklist covering privacy, harm, and injection. | Q1, Q2 |
| LO2: Design refuse/redirect behaviors for unsafe requests. | Q3, Q4 |
| LO3: Use source-only answering to reduce hallucinations in doc Q&A. | Q5, Q6 |
| LO4: Red-team prompts for injection and exfiltration attempts. | Q7, Q8 |
| LO5: Define severity levels and escalation paths for high-risk cases. | Q9, Q10 |

## 06-workflows-and-automation

| Outcome | Quiz questions |
|---|---|
| LO1: Design multi-step workflows with explicit step I/O contracts. | Q1, Q2 |
| LO2: Add verification steps before accepting intermediate outputs. | Q3, Q10 |
| LO3: Set retry budgets and stop conditions for uncertain results. | Q4, Q5 |
| LO4: Log privacy-safe audit fields for each run. | Q6, Q7 |
| LO5: Define fallbacks when a step fails or confidence is low. | Q8, Q9 |

## foundations

| Outcome | Quiz questions |
|---|---|
| LO1: Structure prompts with roles, constraints, and iteration notes. | Q1, Q2, Q7 |
| LO2: Demonstrate safe refuse/redirect behavior on risky inputs. | Q3, Q4, Q8 |
| LO3: Keep a prompt journal showing what improved and what did not. | Q5, Q6 |
