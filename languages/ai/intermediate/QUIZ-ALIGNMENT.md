# ai / intermediate — Quiz Alignment Sheet

Codecademy-style mapping: each learning outcome is tested by at least one quiz item.

Track: `languages/ai/intermediate/modules/`

## 01-advanced-prompting-tool-use

| Outcome | Quiz questions |
|---|---|
| LO1: Write tool contracts with typed arguments and error cases. | Q1, Q2 |
| LO2: Choose among answer, clarify, or call-tool based on the request. | Q3, Q4 |
| LO3: Verify tool results against the user request before finalizing. | Q5, Q6 |
| LO4: Apply retry budgets and clear errors for tool failures. | Q7, Q8 |
| LO5: Log tool calls in an audit schema without leaking secrets. | Q9, Q10 |

## 02-structured-outputs-and-schemas

| Outcome | Quiz questions |
|---|---|
| LO1: Design schemas for task outputs with required and optional fields. | Q1, Q2 |
| LO2: Validate outputs and measure validity/completeness on a dataset. | Q3, Q4 |
| LO3: Add capped repair passes that fix structure without new facts. | Q5, Q6 |
| LO4: Version schemas and plan migrations for breaking changes. | Q7, Q8 |
| LO5: Fail closed with a fallback when strict validation fails. | Q9, Q10 |

## 03-rag-foundations

| Outcome | Quiz questions |
|---|---|
| LO1: Chunk documents and attach metadata for retrieval. | Q1, Q2 |
| LO2: Answer only from retrieved context with citations. | Q3, Q4, Q10 |
| LO3: Abstain when evidence is missing and measure hallucination drop. | Q5 |
| LO4: Separate retrieval failures from generation failures in evals. | Q6, Q7 |
| LO5: Improve hit-rate with query rewriting and simple offline metrics. | Q8, Q9 |

## 04-model-evaluation-and-testing

| Outcome | Quiz questions |
|---|---|
| LO1: Run a repeatable eval harness on a fixed case set. | Q1, Q2, Q10 |
| LO2: Set pass/fail thresholds for schema and rubric scores. | Q3, Q4 |
| LO3: Score adversarial cases separately from the main set. | Q5, Q6 |
| LO4: Produce regression reports with change impact and rollback criteria. | Q7, Q8 |
| LO5: Record cost and latency alongside quality metrics. | Q9 |

## 05-guardrails-and-safety

| Outcome | Quiz questions |
|---|---|
| LO1: Enforce input/output controls including source-only and refusal rules. | Q1, Q2 |
| LO2: Constrain tools with least privilege and verify via tests. | Q3, Q4 |
| LO3: Build red-team suites that target top abuse paths. | Q5, Q6 |
| LO4: Add safety gates in CI that fail on safety regressions. | Q7, Q8 |
| LO5: Design escalation paths for high-risk model outputs. | Q9, Q10 |

## 06-agentic-workflows

| Outcome | Quiz questions |
|---|---|
| LO1: Specify agent plans with tool boundaries and stop conditions. | Q1, Q2 |
| LO2: Insert verification steps that check claims against sources. | Q3, Q10 |
| LO3: Enforce tool budgets to prevent runaway loops. | Q4, Q5 |
| LO4: Require human approval for high-risk actions. | Q6, Q7 |
| LO5: Emit post-run reports covering actions, evidence, and uncertainties. | Q8, Q9 |

## 07-cost-latency-and-ops

| Outcome | Quiz questions |
|---|---|
| LO1: Set cost/latency budgets and enforce them in workflows. | Q1, Q2 |
| LO2: Design cache keys and reuse strategies that preserve correctness. | Q3, Q4 |
| LO3: Add early-exit/abstain rules when confidence is low. | Q5, Q6 |
| LO4: Monitor quality, cost, and latency with actionable alerts. | Q7, Q8 |
| LO5: Plan canary/rollback for prompt and model version changes. | Q9, Q10 |

## 08-deployment-basics

| Outcome | Quiz questions |
|---|---|
| LO1: Create a deployment checklist including eval and safety gates. | Q1, Q2 |
| LO2: Version prompts/schemas and keep a change log. | Q3, Q4 |
| LO3: Define rollback triggers from eval and user-impact signals. | Q5, Q6 |
| LO4: Run smoke tests on critical flows post-deploy. | Q7, Q8 |
| LO5: Use staged rollout with shadow evaluation where appropriate. | Q9, Q10 |

## evaluation-harness

| Outcome | Quiz questions |
|---|---|
| LO1: Assemble golden/test sets for automated or rubric scoring. | Q1, Q2, Q7 |
| LO2: Run the harness repeatedly and track regressions over time. | Q3, Q4, Q8 |
| LO3: Produce evaluation reports that drive go/no-go decisions. | Q5, Q6 |
