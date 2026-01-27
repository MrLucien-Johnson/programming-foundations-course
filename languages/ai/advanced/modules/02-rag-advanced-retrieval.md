# AI — Module 02: RAG: Advanced Retrieval

## Overview
Improve retrieval quality: hybrid search, metadata filters, reranking, and freshness.

**Included examples (tool-agnostic):**
- RAG-based Q&A over docs (advanced retrieval + eval)

## Learning Outcomes
- Translate a vague request into a clear goal, constraints, and success criteria.
- Produce prompts/specs that are repeatable (not “one-off magic prompts”).
- Build a small evaluation loop: test cases, metrics, and iteration notes.
- Apply safety and policy basics: refuse/redirect, handle sensitive data, reduce hallucinations.
- Document and version changes so improvements are explainable.

## Prerequisites
- Comfort writing clear, structured English.
- Basic familiarity with APIs and JSON (helpful but not required in beginner).
- Willingness to iterate: you’ll run tests, record failures, and improve.

## Lessons
1) Retrieval quality signals: precision, recall, and failure modes (50 min)
2) Hybrid retrieval: keyword + semantic + filters (55 min)
3) Reranking and query rewriting (45 min)
4) Freshness and re-indexing strategies (45 min)

## Exercises
### Core
- Design a retrieval evaluation plan: hit-rate, groundedness, abstentions.
- Add a metadata strategy (document type, version, access controls).

### Better
- Compare two chunking strategies and record tradeoffs.
- Add reranking and measure improvement on a fixed question set.

### Beast Mode
- Add access-control-aware retrieval (no leakage across permissions).
- Add freshness tests: new doc appears and is retrievable within a target window.

## Mini-Project
### Brief
Upgrade a RAG design with hybrid retrieval + reranking + freshness plan.

### Acceptance Criteria
- Demonstrates measured improvement on a fixed question set.
- Includes access control and freshness considerations.

## Testing Requirements
- Eval harness separates retrieval vs generation metrics.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- Optimizing retrieval with changing datasets (no stable benchmark).
- Ignoring permissions/access control in retrieval.

## Stretch Resources
- (Placeholder) Add links to hybrid retrieval and reranking techniques.
