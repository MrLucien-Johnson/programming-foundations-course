# AI — Module 03: RAG Foundations

## Overview
Build retrieval-augmented generation (RAG) systems: chunking, embeddings, retrieval, and grounded answering.

**Included examples (tool-agnostic):**
- RAG-based Q&A over docs (answer with citations to provided excerpts)

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
1) RAG mental model: retrieve → read → answer (45 min)
2) Document prep: chunking, metadata, and updates (50 min)
3) Retrieval: top-k, filters, and re-ranking basics (45 min)
4) Grounded answers: cite sources and abstain when missing (45 min)

## Exercises
### Core
- Create a doc set (10–30 pages) and define a question set (30 questions).
- Design prompts that answer only using retrieved context and cite excerpts.

### Better
- Add a “no evidence → abstain” rule and test hallucination reduction.
- Track retrieval failures separately from generation failures.

### Beast Mode
- Add query rewriting and compare retrieval hit-rate.
- Design an offline evaluation for retrieval quality (precision@k proxy).

## Mini-Project
### Brief
Build a small RAG Q&A prototype spec with dataset, grounded answering, and eval plan.

### Acceptance Criteria
- Includes chunking strategy, metadata plan, and grounding rules.
- Includes a question set and a scoring rubric.

## Testing Requirements
- At minimum: manual scoring with a rubric; better: scripted scoring of citations/abstentions.

## Rubric
| Criteria | Meets | Exceeds |
|---|---|---|
| Correctness | Output meets the stated goal | Handles edge cases and constraints reliably |
| Evaluation | Basic checks exist | Repeatable eval harness with clear metrics/targets |
| Safety | Obvious risks addressed | Explicit safety checklist + red-team prompts + mitigations |
| Maintainability | Clear structure and docs | Modular prompts, versioning, and change notes |
| Cost/Latency | Reasonable defaults | Measured costs/latency + optimizations + budgets |


## Common Mistakes
- No citation requirement, leading to confident hallucinations.
- Chunking without metadata, making filtering impossible.
- Not separating retrieval vs generation issues.

## Stretch Resources
- (Placeholder) Add links to RAG evaluation and retrieval strategies.
