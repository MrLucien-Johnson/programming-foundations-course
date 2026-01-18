# Security Rubric

Assesses basic security hygiene and risk awareness.

## Scoring guide
- 1 - Below: Obvious vulnerabilities or unsafe defaults.
- 2 - Meets: Reasonable safeguards and safe handling of data.
- 3 - Exceeds: Proactive threat thinking and documented mitigations.

## Criteria
### Input validation and sanitization
Meets:
- Validates user input and handles invalid values safely.
- Avoids unsafe string interpolation for queries or commands.
Exceeds:
- Centralized validation with reusable rules.
- Explicit threat modeling notes for inputs.

### Secrets and configuration
Meets:
- Secrets are not hard-coded in source files.
- Sensitive configuration is documented and externalized.
Exceeds:
- Uses environment-based configuration with clear rotation guidance.
- Adds checks to prevent accidental secret commits.

### Dependency and supply-chain hygiene
Meets:
- Uses maintained libraries and pins versions when needed.
- Avoids unnecessary dependencies.
Exceeds:
- Includes a lightweight dependency audit note.
- Documents known risks and upgrade cadence.

### Authorization and least privilege
Meets:
- Access controls are explicit where applicable.
- Data exposure is limited to required fields.
Exceeds:
- Documents permission boundaries and roles.
- Adds tests for unauthorized access paths.
