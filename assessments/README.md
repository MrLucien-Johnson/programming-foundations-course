# Assessments and Certification

This folder defines how learner work is submitted, reviewed, and certified.
Use these documents for consistent evaluation across languages.

## How learners submit work
1. Create a branch named `submission/<learner>/<language>/<module-or-project>`.
2. Add work under `submissions/<learner>/<language>/<module-or-project>/`.
3. Include a short `README.md` with setup, run steps, and evidence.
4. Open a PR and link to the relevant checklist and rubric(s).

If `submissions/` does not exist, create it in the PR and keep edits
limited to that folder plus any required project files.

## How grading works using rubrics
Reviewers grade against the rubrics in `assessments/rubrics/`.
Each rubric provides criteria plus clear "Meets" and "Exceeds" examples.
Use the rubric scores to determine the certification level.

## How to run evaluation locally
- Follow the submission `README.md` to install dependencies and run tests.
- Verify all automated tests pass and record the outputs.
- Run the application or scripts to confirm behavior matches the prompt.
- Check for basic security hygiene and performance considerations.

## What a good submission looks like
- Clear folder structure and descriptive filenames.
- A concise `README.md` with setup, run, and test commands.
- Evidence artifacts: test logs, screenshots, and deployment proof if needed.
- Clean commits and a short PR summary explaining tradeoffs.

## How to use the tracking template
Use `assessments/certifications/TRACKING-TEMPLATE.md` to record:
- Learner info and target certification level.
- Module and project completion links.
- Rubric scores, reviewer notes, and final decision.
