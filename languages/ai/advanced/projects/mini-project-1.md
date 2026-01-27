# AI Advanced — Mini Project 1: Retrieval Quality Upgrade

## Overview
- **Goal**: Improve retrieval with hybrid search/reranking and show measured impact on a fixed benchmark.
- **Expected effort**: 3–5 days

## Brief
Build a tool-agnostic AI workflow or app. You may use any LLM/provider, but your design must be portable: clear prompts/specs, versioning, evaluation, and safety.

## Requirements
- Benchmark question set and stable doc corpus with versions.
- Measured improvement (retrieval hit-rate proxy, groundedness, abstentions).
- Safety checklist (permissions, injection defenses).
- Cost/latency plan for retrieval + generation.
- Fallback strategy when retrieval confidence is low.

## Acceptance Criteria
- Reproducible run instructions (someone else can run it).
- Repeatable evaluation harness (even if simple).
- Safety checklist + red-team tests.
- Cost/latency plan + fallback strategy.

## Testing Requirements
- Eval harness must produce a reproducible report.

## Deliverables
- Benchmark report before/after changes.
- Design doc: chunking, metadata, and retrieval strategies.

## Suggested Run Steps
- Run benchmark and report improvements; include regression guardrails.
