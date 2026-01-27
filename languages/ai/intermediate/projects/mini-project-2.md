# AI Intermediate — Mini Project 2: RAG Q&A Prototype (Grounded)

## Overview
- **Goal**: Build a doc Q&A system that answers only from retrieved context with citations and abstention.
- **Expected effort**: 2–3 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- Chunking + metadata strategy documented.
- Grounded answering: citations and abstain-with-reason when no evidence.
- Evaluation harness: groundedness + retrieval hit-rate proxy + abstention accuracy.
- Safety checklist: permissions-aware retrieval concept + injection defenses.
- Cost/latency plan: context trimming, caching, and budgets.
- Fallback strategy when retrieval fails or context is insufficient.

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- Harness must separate retrieval vs generation failures.
- Include adversarial questions attempting to override “source-only” rules.

## Deliverables
- `docs/` sample corpus + indexing notes.
- `eval/` question set (≥50) + scoring rubric + results.
- Write-up: top failure modes and mitigations.

## Suggested Run Steps
- Run the harness; show measurable improvement after at least one retrieval or prompt change.
