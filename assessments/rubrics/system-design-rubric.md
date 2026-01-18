# System Design Rubric

Assesses architecture clarity and advanced design decisions.

## Scoring guide
- 1 - Below: Design is unclear or mismatched to requirements.
- 2 - Meets: Design is coherent and supports the use cases.
- 3 - Exceeds: Design is well-justified with tradeoffs explained.

## Criteria
### Architecture and component boundaries
Meets:
- Components and responsibilities are clearly defined.
- Data flow is easy to trace across layers.
Exceeds:
- Includes diagrams or structured docs for clarity.
- Highlights alternative designs and rationale.

### Scalability and reliability
Meets:
- Identifies likely bottlenecks and basic mitigations.
- Handles failure modes with graceful degradation.
Exceeds:
- Includes scaling assumptions and capacity reasoning.
- Describes retry, caching, or resilience strategies.

### Observability and operations
Meets:
- Logs and errors are structured for debugging.
- Key metrics are identified, even if not implemented.
Exceeds:
- Proposes alerting thresholds and dashboards.
- Includes runbook notes for operations.

### Profiling and performance evidence (advanced)
Meets:
- Discusses expected performance constraints.
- Avoids unbounded complexity in critical paths.
Exceeds:
- Provides profiling or benchmark output.
- Documents performance improvements backed by data.
