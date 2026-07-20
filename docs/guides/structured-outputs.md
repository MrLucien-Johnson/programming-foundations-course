# Structured Outputs & Schemas

Make model output machine-readable so your app can use it without fragile parsing.

## Why schemas matter

Free-form text is fine for reading. Apps need **predictable fields**: IDs, enums, lists, and nested objects.

## Practical approach

1. Define the JSON shape you need (or a markdown template with fixed headings).
2. Put the schema **in the prompt** and show one short example.
3. Validate the response in code.
4. On validation failure: retry once with the error message, then fall back.

### Minimal schema example

```json
{
  "issue": "string",
  "urgency": "low | medium | high",
  "next_steps": ["string"]
}
```

### Prompt fragment

```text
Return ONLY valid JSON matching this schema.
No markdown fences. No commentary.
If a field is unknown, use null.
```

## Tips that improve reliability

- Prefer enums over free text when choices are limited.
- Cap list lengths (“1–5 items”).
- Separate “reasoning” from “final JSON” if you need both — or ask for JSON only.
- Version your schema; log which version produced each result.

## Testing

- Good cases: normal inputs that should fill every field.
- Bad cases: empty input, contradictory instructions, missing fields.
- Ambiguous cases: two possible urgencies — define the rule.

## Next on this site

- Module: [Structured Outputs & Schemas](../course-viewer.html?path=languages/ai/intermediate/modules/02-structured-outputs-and-schemas.md)
- Related: [Evaluation Guide](guide-viewer.html?path=guides/evaluation-guide.md)
