# Code Review Rubric

Assesses code quality, readability, and maintainability.

## Scoring guide
- 1 - Below: Hard to read, inconsistent, or error-prone.
- 2 - Meets: Clear, consistent, and correct for the requirements.
- 3 - Exceeds: Clean, idiomatic, and thoughtfully engineered.

## Criteria
### Readability and naming
Meets:
- Names are descriptive and consistent with the language style.
- Control flow is easy to follow without hidden side effects.
Exceeds:
- Names encode intent and reduce the need for extra comments.
- File organization makes navigation effortless.

### Structure and maintainability
Meets:
- Functions and classes have single responsibilities.
- Reusable logic is extracted without over-abstraction.
Exceeds:
- Clear boundaries between modules and concerns.
- Extensibility is evident with minimal refactoring needed.

### Correctness and edge cases
Meets:
- Handles the required scenarios and basic edge cases.
- Input validation exists where needed.
Exceeds:
- Anticipates tricky edge cases with clear reasoning.
- Includes defensive checks and graceful failure paths.

### Documentation and comments
Meets:
- README or inline notes explain non-obvious decisions.
- Usage and configuration are described.
Exceeds:
- Documentation includes tradeoffs and alternatives considered.
- Examples and diagrams improve comprehension.

### Performance basics (intermediate)
Meets:
- Avoids obvious inefficiencies for the problem size.
- Uses appropriate data structures for lookups and iteration.
Exceeds:
- Identifies complexity hot spots and justifies choices.
- Includes small benchmarks or measurements when helpful.
