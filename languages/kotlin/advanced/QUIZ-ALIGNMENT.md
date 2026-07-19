# kotlin / advanced — Quiz Alignment Sheet

Codecademy-style mapping: each learning outcome is tested by at least one quiz item.

Track: `languages/kotlin/advanced/modules/`

## 01-system-design-foundations

| Outcome | Quiz questions |
|---|---|
| LO1: Turn vague product goals into requirements, constraints, and rough capacity estimates. | Q1, Q2, Q10 |
| LO2: Choose caching, load balancing, and data partitioning approaches for a given load pattern. | Q3, Q4, Q9 |
| LO3: Apply CAP/consistency tradeoffs to pick a consistency model for a use case. | Q5, Q6 |
| LO4: Design async workflows with queues or streams when synchronous request paths are insufficient. | Q7, Q8 |

## 02-architecture-patterns

| Outcome | Quiz questions |
|---|---|
| LO1: Compare layered, hexagonal, and clean architecture and place dependencies correctly. | Q1, Q2, Q9 |
| LO2: Model domain concepts with entities, value objects, and aggregates. | Q3, Q4, Q10 |
| LO3: Design event-driven flows and sagas for multi-step business processes. | Q5, Q6 |
| LO4: Decide when CQRS helps — and when it adds unjustified complexity. | Q7, Q8 |

## 03-concurrency-and-async

| Outcome | Quiz questions |
|---|---|
| LO1: Identify race conditions and choose safe synchronization or ownership patterns. | Q1, Q2 |
| LO2: Apply backpressure with bounded queues so producers cannot overwhelm consumers. | Q3, Q4, Q9 |
| LO3: Use timeouts, cancellation, and structured concurrency to bound work lifetimes. | Q5, Q6, Q10 |
| LO4: Design for at-least-once delivery and idempotent handlers — not mythical exactly-once. | Q7, Q8 |

## 04-performance-and-profiling

| Outcome | Quiz questions |
|---|---|
| LO1: Establish performance baselines before changing code. | Q1, Q2, Q10 |
| LO2: Run load tests and locate bottlenecks with evidence. | Q3, Q4, Q9 |
| LO3: Tune databases using indexes, query plans, and lock analysis. | Q5, Q6 |
| LO4: Choose cache invalidation strategies that match correctness needs. | Q7, Q8 |

## 05-reliability-and-resilience

| Outcome | Quiz questions |
|---|---|
| LO1: Configure retries with timeouts, budgets, and jitter for transient faults. | Q1, Q2, Q10 |
| LO2: Apply circuit breakers, bulkheads, and rate limits to contain failures. | Q3, Q4, Q9 |
| LO3: Use idempotency keys and dedupe to make retried writes safe. | Q5, Q6 |
| LO4: Write and follow runbooks for common incident classes. | Q7, Q8 |

## 06-security-advanced

| Outcome | Quiz questions |
|---|---|
| LO1: Threat-model a feature including abuse cases and prioritised mitigations. | Q1, Q2, Q9 |
| LO2: Apply encryption at rest/in transit with sound key management. | Q3, Q4, Q10 |
| LO3: Enforce supply-chain controls for dependencies and build artifacts. | Q5, Q6 |
| LO4: Execute a hardening checklist covering auth, config, and security tests. | Q7, Q8 |

## 07-observability-and-slos

| Outcome | Quiz questions |
|---|---|
| LO1: Define SLIs/SLOs and manage error budgets for a service. | Q1, Q2, Q9 |
| LO2: Apply RED/USE metrics while avoiding high-cardinality label explosions. | Q3, Q4, Q10 |
| LO3: Propagate trace context across services to diagnose latency. | Q5, Q6 |
| LO4: Design alerts that are actionable and kind to on-call. | Q7, Q8 |

## 08-ci-cd-and-release-strategies

| Outcome | Quiz questions |
|---|---|
| LO1: Choose canary, blue-green, or rolling releases for a risk profile. | Q1, Q2, Q9 |
| LO2: Use feature flags and safe config changes to control exposure. | Q3, Q4, Q10 |
| LO3: Plan production database migrations that avoid downtime and lockouts. | Q5, Q6 |
| LO4: Execute rollbacks with clear versioning and changelogs. | Q7, Q8 |

## system-design

| Outcome | Quiz questions |
|---|---|
| LO1: Design a service for expected scale with explicit bottlenecks and mitigations. | Q1, Q2, Q7 |
| LO2: Document architecture tradeoffs and rejected alternatives clearly. | Q3, Q4, Q8 |
| LO3: Define verification (tests, load checks, or probes) that match the design risks. | Q5, Q6 |
