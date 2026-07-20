# Data Privacy & Governance

Handle prompts, documents, and logs like sensitive product data.

## What often gets overlooked

- User messages stored in provider logs
- Retrieved documents that include PII
- Traces that capture secrets in tool arguments
- Training or “improve the product” toggles on vendor dashboards
- Long retention of chat history without a policy

## Practical rules

1. **Minimize** — send only the fields the task needs.
2. **Redact** — strip secrets, tokens, and unnecessary PII before calling a model.
3. **Access control** — RAG must respect document permissions.
4. **Retention** — define how long prompts and outputs are kept.
5. **Purpose limit** — do not reuse chat data for unrelated analytics without a decision.
6. **Vendor settings** — disable training on your data when the product requires it.

## Governance checklist for a new AI feature

- [ ] Data inventory (what goes in / what comes out)
- [ ] Legal / policy review for the use case
- [ ] Retention and deletion path
- [ ] Access who can view logs
- [ ] Incident contact if data leaks

## User-facing transparency

Tell users when AI is used, what data is processed, and how to get help if something looks wrong.

## Practice on this site

- [Data Governance & Privacy](../course-viewer.html?path=languages/ai/advanced/modules/07-data-governance-and-privacy.md)
- Related: [AI Safety & Security](guide-viewer.html?path=guides/ai-safety-security.md)
