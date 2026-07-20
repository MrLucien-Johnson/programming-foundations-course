# RAG & Retrieval

Retrieval-Augmented Generation (RAG) grounds answers in **your documents** so the model invents less and cites more.

## The basic pipeline

1. **Chunk** documents into searchable pieces.
2. **Index** them (keyword search, vectors, or both).
3. **Retrieve** the top passages for a user question.
4. **Prompt** the model with those passages and a grounding rule.
5. **Answer** with citations — or say you do not know.

## Grounding rule (copy/paste)

```text
Answer ONLY using the provided passages.
If the passages do not contain the answer, say "I don't know based on the provided documents."
Cite passage IDs for each claim.
```

## Design choices that matter

| Choice | Guidance |
|---|---|
| Chunk size | Start ~200–500 tokens; keep headings with chunks |
| Top-k | Start with 3–8 passages; measure precision |
| Hybrid search | Keyword + semantic often beats either alone |
| Freshness | Re-index when docs change |
| Permissions | Never retrieve docs the user cannot see |

## Evaluation for RAG

- **Faithfulness** — does the answer stick to retrieved text?
- **Relevance** — are the retrieved chunks the right ones?
- **Coverage** — does the answer miss required facts?

Build a small set of questions with known supporting passages and score retrieval and answers separately.

## Advanced directions

- Re-ranking retrieved results
- Query rewriting before search
- Multi-hop retrieval for questions that need two docs
- Caching frequent queries

## Practice on this site

- [RAG Foundations](../course-viewer.html?path=languages/ai/intermediate/modules/03-rag-foundations.md)
- [Advanced Retrieval](../course-viewer.html?path=languages/ai/advanced/modules/02-rag-advanced-retrieval.md)
