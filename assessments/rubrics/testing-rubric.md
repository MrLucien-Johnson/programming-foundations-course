# Testing Rubric

Assesses test strategy, coverage, and reliability.

## Scoring guide
- 1 - Below: Tests are missing or do not validate requirements.
- 2 - Meets: Tests validate key behavior with stable results.
- 3 - Exceeds: Tests are thorough, maintainable, and insightful.

## Criteria
### Coverage of requirements
Meets:
- Critical user flows are tested.
- Failure cases are represented.
Exceeds:
- Covers edge cases and alternative paths.
- Maps tests to requirements in the README.

### Test quality and clarity
Meets:
- Tests have clear names and assertions.
- Setup and teardown are straightforward.
Exceeds:
- Tests document intent and reduce ambiguity.
- Uses fixtures or helpers to keep tests DRY.

### Reliability and determinism
Meets:
- Tests are repeatable and not flaky.
- Avoids time-based or network-dependent failures.
Exceeds:
- Isolates external dependencies with mocks or stubs.
- Uses deterministic data and seeded randomness.

### Tooling and automation
Meets:
- A single command runs the full test suite.
- Test instructions are documented.
Exceeds:
- Includes CI or pre-commit guidance.
- Reports coverage or test summaries clearly.
