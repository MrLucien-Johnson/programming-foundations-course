# AGENTS.md

## Cursor Cloud specific instructions

This repository is an educational programming-course project. It is mostly Markdown
curriculum content plus a small static website. There are three runnable pieces:

### 1. Static docs site (the "application")
- Source lives in `docs/` (plain HTML/CSS/JS, no build step).
- Run in dev mode by serving the folder over HTTP, e.g. `python3 -m http.server 8000`
  from inside `docs/`, then open `http://localhost:8000/index.html`.
- It must be served over HTTP (not opened as `file://`) because pages use `fetch()`.
- Non-obvious: `docs/course-viewer.html` and `docs/quiz-viewer.html` fetch each lesson/quiz
  Markdown from `https://raw.githubusercontent.com/MrLucien-Johnson/programming-foundations-course/main/...`
  (the hard-coded `rawRoot`), NOT from local files. So lesson/quiz content requires internet
  access and reflects the published `main` branch, not local edits. `docs/courses.html` does
  load the local `docs/course-index.json`.

### 2. Curriculum lint (CI check)
- Run with `python3 scripts/curriculum_lint.py` (stdlib only, no dependencies).
- This is the same check run by `.github/workflows/curriculum-lint.yml`. It verifies the
  expected `languages/<lang>/<level>/{modules,projects}` structure and certification files.

### 3. Language starter packs (learner example projects)
- Python: `languages/python/{intermediate,advanced}/starter-pack` — test with
  `python3 -m pytest`, lint with `ruff check .`.
- Rust: `languages/rust/{intermediate,advanced}/starter-pack` — `cargo run` / `cargo build`
  (Rust `target/` and `Cargo.lock` are not gitignored here; don't commit them).
- C#: the C# course/starter material requires the .NET SDK (6.0+), which is NOT installed by
  default in this environment. Install it only if you need to run C# examples.

### Notes
- `pytest` and `ruff` are installed to `~/.local/bin`, which is not on `PATH` by default.
  Invoke ruff as `~/.local/bin/ruff` (or add the dir to `PATH`); pytest works via
  `python3 -m pytest`.
