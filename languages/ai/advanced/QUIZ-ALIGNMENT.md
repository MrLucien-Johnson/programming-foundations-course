# ai / advanced — Quiz Alignment Sheet

Codecademy-style mapping: each learning outcome is tested by at least one quiz item.

Track: `languages/ai/advanced/modules/`

## 01-system-design-for-llm-apps

| Outcome | Quiz questions |
|---|---|
| LO1: Draw architecture and data flow for an LLM feature including failure modes. | Q1, Q2 |
| LO2: Plan scaling with caches, queues, and backpressure for model/tool workloads. | Q3, Q4 |
| LO3: Define latency/quality SLOs and error budgets for the feature. | Q5, Q6 |
| LO4: Design prompt/schema migrations with backward compatibility. | Q7, Q8 |
| LO5: Apply privacy-by-design (minimization, retention, access control). | Q9, Q10 |

## 02-rag-advanced-retrieval

| Outcome | Quiz questions |
|---|---|
| LO1: Evaluate retrieval with hit-rate, groundedness, and abstention metrics. | Q1, Q2, Q10 |
| LO2: Compare chunking strategies with measured tradeoffs. | Q3, Q4 |
| LO3: Add reranking and quantify lift on a fixed question set. | Q5, Q6 |
| LO4: Enforce access-control-aware retrieval to prevent leakage. | Q7, Q8 |
| LO5: Test freshness so new docs become retrievable within a target window. | Q9 |

## 03-evals-at-scale

| Outcome | Quiz questions |
|---|---|
| LO1: Design batch eval runners with retries, budgets, and reproducibility. | Q1, Q2 |
| LO2: Detect quality drift with stratified sampling and cadence. | Q3, Q4 |
| LO3: Define stop-the-line criteria for regressions. | Q5, Q6 |
| LO4: Run privacy-safe shadow evaluation on live traffic. | Q7, Q8 |
| LO5: Operate human labeling with calibration across raters. | Q9, Q10 |

## 04-security-threat-modeling-llm

| Outcome | Quiz questions |
|---|---|
| LO1: Produce a threat model with mitigations for an LLM app. | Q1, Q2 |
| LO2: Build red-team suites targeting top threats (injection, tool abuse). | Q3, Q4 |
| LO3: Enforce least-privilege tool policies verified by tests. | Q5, Q6 |
| LO4: Apply data minimization and retention to prompts/outputs. | Q7, Q8 |
| LO5: Plan incident response and supply-chain controls for AI artifacts. | Q9, Q10 |

## 05-observability-and-monitoring-llm

| Outcome | Quiz questions |
|---|---|
| LO1: Define SLIs/SLOs for quality, safety, cost, and latency. | Q1, Q2 |
| LO2: Design dashboards and alert thresholds operators can act on. | Q3, Q4 |
| LO3: Trace multi-step LLM flows (retrieval, generation, tools). | Q5, Q6 |
| LO4: Sample quality safely (privacy-preserving) with escalation paths. | Q7, Q8 |
| LO5: Run continuous canary evaluation in production. | Q9, Q10 |

## 06-reliability-and-fallbacks

| Outcome | Quiz questions |
|---|---|
| LO1: Define fallbacks per top failure mode (model, retrieval, tools). | Q1, Q2 |
| LO2: Set retry budgets and stop conditions for degraded paths. | Q3, Q4 |
| LO3: Failure-inject outages/timeouts in the harness. | Q5, Q6 |
| LO4: Specify degraded modes: abstain, ask, cached answer, human queue. | Q7, Q8 |
| LO5: Run post-incident reviews that harden evals and guardrails. | Q9, Q10 |

## 07-data-governance-and-privacy

| Outcome | Quiz questions |
|---|---|
| LO1: Write data-handling policies for what is stored, why, and how long. | Q1, Q2 |
| LO2: Implement and test PII redaction on inputs/outputs. | Q3, Q4 |
| LO3: Enforce permission-aware retrieval and no-leakage tests. | Q5, Q6 |
| LO4: Design safe logging schemas that avoid raw sensitive text. | Q7, Q8 |
| LO5: Add privacy review checklists to release process. | Q9, Q10 |

## 08-production-incident-playbooks

| Outcome | Quiz questions |
|---|---|
| LO1: Write playbooks for cost spikes, safety regressions, and quality drops. | Q1, Q2 |
| LO2: Define immediate mitigations: flags, degrade modes, stricter filters. | Q3, Q4 |
| LO3: Run incident drills that exercise detection and response. | Q5, Q6 |
| LO4: Prepare internal and user-facing communication templates. | Q7, Q8 |
| LO5: Close the loop by updating evals and guardrails after incidents. | Q9, Q10 |

## optimization-safety

| Outcome | Quiz questions |
|---|---|
| LO1: Budget cost and latency without sacrificing required safety checks. | Q1, Q2, Q7 |
| LO2: Apply caching/reuse only when correctness and privacy allow. | Q3, Q4, Q8 |
| LO3: Plan safety evaluations and red-teaming alongside performance work. | Q5, Q6 |
