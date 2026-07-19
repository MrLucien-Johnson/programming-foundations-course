# Quiz Alignment Standard (Codecademy-style)

Purpose: every quiz item must **exercise a skill** from that module’s learning outcomes — not scavenger-hunt the module’s process text (pytest commands, Core/Better/Beast labels, or “which outcome is listed?”).

## Rules

1. **Outcomes first** — 4–8 observable skills (“you will be able to…”), derived from the module’s lesson titles.
2. **One skill per outcome** — no boilerplate like “Explain the core concepts and tradeoffs for **{Topic}**.”
3. **Map every outcome** — each outcome appears on at least one quiz question.
4. **Tag questions** — under each stem, include:
   `**Checks outcome N:** <outcome text>`
5. **Plausible distractors** — wrong answers must be believable misconceptions, not random lines copied from the README.
6. **Explain the why** — answer keys name the outcome and explain the reasoning (with a short code/concept rationale when useful).
7. **Keep exercise levels separate** — Core / Better / Beast Mode stay in the lesson exercises; they are not quiz content unless tooling itself is an outcome.

## Template (quiz item)

```markdown
### Question 3: <skill-focused stem>
**Checks outcome 2:** <exact outcome text>

A) ...
B) ...
C) ...
D) ...

**Your answer:** _______________
```

## Template (answer item)

```markdown
## Question 3: <stem>
**Answer: B** — <choice text>

**Outcome 2:** <exact outcome text>

**Explanation:** <why B is right and why common wrong answers fail>
```

## Reference implementation

- Beginner workbook gold pattern: `python-beginner-workbook/module-02-basics/`
- Full language rollout: `languages/{python,csharp,go,java,kotlin,rust,sql,swift,typescript,ai}/`
  — each level has skill outcomes, tagged quizzes, answer keys, and `QUIZ-ALIGNMENT.md`
- Generators: `scripts/quiz_skill_banks.py` + `scripts/align_all_language_quizzes.py`

## Rollout

1. Rewrite outcomes from lesson titles.
2. Replace template quizzes with skill questions.
3. Add/update the per-track `QUIZ-ALIGNMENT.md` sheet.
4. Repeat per language / level.
