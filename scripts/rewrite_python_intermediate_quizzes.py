#!/usr/bin/env python3
"""Rewrite Python Intermediate outcomes + quizzes for Codecademy-style skill alignment."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "languages" / "python" / "intermediate" / "modules"

MODULES: dict[str, dict] = {
    "01-dsa-practical": {
        "title": "DSA (Practical)",
        "outcomes": [
            "Choose list vs dict vs set for a given access pattern and justify the Big-O tradeoff.",
            "Apply stack/queue and BFS/DFS mental models to a small graph or tree-style problem.",
            "Decide when Python's built-in sort/search is enough versus writing a custom approach.",
            "Apply memoization or an LRU cache when recomputation is the bottleneck.",
            "Measure a change with a micro-benchmark and explain when profiling is the better tool.",
        ],
        "questions": [
            {
                "lo": 1,
                "q": "You need average O(1) lookup of a user record by `user_id`. Which structure fits best?",
                "choices": [
                    "A list you scan from the start each time",
                    "A dict keyed by `user_id`",
                    "A set of unsorted display names",
                    "A nested list of all fields without keys",
                ],
                "answer": "B",
                "explain": "Dicts give average O(1) keyed lookup. Scanning a list is O(n). Sets are for membership of values, not fielded records.",
            },
            {
                "lo": 1,
                "q": "You must enforce unique email addresses and only care whether an email already exists. Best choice?",
                "choices": [
                    "A list of emails",
                    "A dict mapping email → full user object (required even if unused)",
                    "A set of emails",
                    "A queue of emails",
                ],
                "answer": "C",
                "explain": "A set is ideal for unique membership checks. A dict works but stores unused values; a list makes uniqueness checks O(n).",
            },
            {
                "lo": 2,
                "q": "You need to explore a graph level-by-level (nearest neighbors first). Which approach matches?",
                "choices": [
                    "Depth-first search with a stack (or recursion)",
                    "Breadth-first search with a queue",
                    "Binary search on a sorted array",
                    "LRU eviction of the oldest key",
                ],
                "answer": "B",
                "explain": "BFS uses a queue and visits nodes by distance/level. DFS goes deep first. Binary search and LRU solve different problems.",
            },
            {
                "lo": 2,
                "q": "Undo/redo history in an editor is best modeled with which structure?",
                "choices": [
                    "A queue (FIFO)",
                    "A stack (LIFO)",
                    "A hash set",
                    "A priority queue ordered by timestamp only once at insert",
                ],
                "answer": "B",
                "explain": "Undo reverses the most recent action first — classic LIFO/stack behavior.",
            },
            {
                "lo": 3,
                "q": "You have a list of 50,000 comparable IDs and need them sorted once before a report. What should you do first?",
                "choices": [
                    "Write a custom quicksort from scratch",
                    "Use Python's built-in `sorted()` / `list.sort()` unless you have a measured reason not to",
                    "Always switch to a hand-rolled linked-list sort for clarity",
                    "Sort with bubble sort so Big-O stays obvious",
                ],
                "answer": "B",
                "explain": "CPython's Timsort is highly optimized. Custom sorts are rarely justified until profiling proves a need.",
            },
            {
                "lo": 4,
                "q": "A pure function is called repeatedly with the same arguments inside a hot loop. Which pattern helps first?",
                "choices": [
                    "Delete the function and inline random values",
                    "Memoization or `@functools.lru_cache` so repeated inputs reuse results",
                    "Replace the dict with a list scan",
                    "Disable tests to save time",
                ],
                "answer": "B",
                "explain": "Memoization/LRU caching avoids recomputing identical inputs — exactly this module's caching lesson.",
            },
            {
                "lo": 4,
                "q": "An LRU cache is full and a new key arrives. What happens to the least recently used entry?",
                "choices": [
                    "It stays forever",
                    "It is evicted to make room",
                    "It becomes the most recently used without eviction",
                    "All keys are wiped",
                ],
                "answer": "B",
                "explain": "LRU evicts the least recently used entry when capacity is exceeded.",
            },
            {
                "lo": 5,
                "q": "You want a quick before/after timing of one helper function. Best first tool?",
                "choices": [
                    "A full production distributed tracer only",
                    "A micro-benchmark / timing of that function",
                    "Guessing from code review alone",
                    "Turning off the GC permanently",
                ],
                "answer": "A",
                "explain": "WAIT - fix answer",
            },
        ],
    },
}


def fix_module_01() -> None:
    """Patch the intentional placeholder in module 01 question 8."""
    qs = MODULES["01-dsa-practical"]["questions"]
    qs[7] = {
        "lo": 5,
        "q": "You want a quick before/after timing of one helper function. Best first tool?",
        "choices": [
            "A micro-benchmark / timing of that function",
            "Only a full-cluster production profiler with no local measurement",
            "Guessing from code review alone",
            "Turning off tests so numbers look better",
        ],
        "answer": "A",
        "explain": "Micro-benchmarks answer “is this function faster?” Profiling answers “where does the whole program spend time?” Start local and measured.",
    }
    qs.append(
        {
            "lo": 5,
            "q": "When is profiling usually better than a micro-benchmark?",
            "choices": [
                "When you already know the one-line hotspot with certainty",
                "When you need to find where a whole program spends CPU or memory",
                "When you want to skip measurements entirely",
                "When sorting a 10-element list",
            ],
            "answer": "B",
            "explain": "Profilers locate hotspots across a running program. Micro-benchmarks compare a narrow slice you already suspect.",
        }
    )
    qs.append(
        {
            "lo": 1,
            "q": 'Looking up whether an id is in a large unsorted list of IDs is typically:',
            "choices": [
                "O(1) average",
                "O(n)",
                "O(log n) without sorting",
                "O(n²) always",
            ],
            "answer": "B",
            "explain": "Membership in an unsorted list scans elements — O(n). A set/dict membership check is average O(1).",
        }
    )


MODULES.update(
    {
        "02-testing-and-quality": {
            "title": "Testing and Quality",
            "outcomes": [
                "Place tests on the test pyramid and choose what to mock versus what to hit for real.",
                "Write deterministic unit tests using fixtures/factories and meaningful assertions.",
                "Add an integration test that crosses a real boundary (HTTP, DB, filesystem, or process).",
                "Interpret coverage as a signal — not a substitute for strong assertions.",
                "Use lint, format, and typecheck as automated quality gates.",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "On the test pyramid, which layer should usually be the largest (most numerous)?",
                    "choices": [
                        "Manual-only exploratory tests",
                        "Unit tests",
                        "Full production canaries only",
                        "UI screenshot tests for every line of code",
                    ],
                    "answer": "B",
                    "explain": "Unit tests are fast and numerous; integration/E2E are fewer and slower.",
                },
                {
                    "lo": 1,
                    "q": "You are unit-testing a pure pricing function. What should you usually avoid mocking?",
                    "choices": [
                        "The function's own arithmetic",
                        "An external payment HTTP API used by a different module",
                        "A clock if the function under test does not use time",
                        "Nothing — mock every name in scope",
                    ],
                    "answer": "A",
                    "explain": "Don't mock the behavior you are trying to prove. Mock slow/external boundaries, not the subject itself.",
                },
                {
                    "lo": 2,
                    "q": "A test fails only when run after another test. What is the likely problem?",
                    "choices": [
                        "The assertion is too meaningful",
                        "Shared mutable state — the suite is not deterministic/isolated",
                        "Coverage is above 90%",
                        "Ruff is too strict",
                    ],
                    "answer": "B",
                    "explain": "Order-dependent failures usually mean leaked global/DB/file state. Tests must isolate and reset fixtures.",
                },
                {
                    "lo": 2,
                    "q": "Which assertion is stronger for `create_user(email)`?",
                    "choices": [
                        "`assert result is not None`",
                        "`assert result.email == email and result.id is not None`",
                        "`assert True`",
                        "`assert result` with no further checks",
                    ],
                    "answer": "B",
                    "explain": "Meaningful assertions check observable outcomes, not merely “something happened.”",
                },
                {
                    "lo": 3,
                    "q": "Which example is an integration test?",
                    "choices": [
                        "Calling a pure function with mocked everything including its own logic",
                        "Hitting a real test database or HTTP endpoint and asserting the response",
                        "Reading the source code without running it",
                        "Formatting files with ruff",
                    ],
                    "answer": "B",
                    "explain": "Integration tests cross a real boundary (HTTP/DB/etc.), not just in-memory mocks of the unit.",
                },
                {
                    "lo": 4,
                    "q": "Coverage reports 100%, but a bug still ships. What lesson fits?",
                    "choices": [
                        "Coverage guarantees correctness",
                        "Coverage without meaningful assertions can still miss behavior",
                        "You should delete all unit tests",
                        "Only E2E tests ever matter",
                    ],
                    "answer": "B",
                    "explain": "Coverage shows what ran, not whether you asserted the right outcomes.",
                },
                {
                    "lo": 5,
                    "q": "Why run lint/format/typecheck in CI as quality gates?",
                    "choices": [
                        "To replace unit tests entirely",
                        "To catch style, bug-prone patterns, and type issues before merge",
                        "To slow developers with no signal",
                        "Only to generate prettier README screenshots",
                    ],
                    "answer": "B",
                    "explain": "Automated gates keep a consistent baseline so humans review design and behavior.",
                },
                {
                    "lo": 3,
                    "q": "Your feature writes to Postgres. Which test strategy best proves the boundary works?",
                    "choices": [
                        "Mock the DB away and never talk to SQL",
                        "An integration test against an isolated test schema/database",
                        "Print SQL in a comment and skip running it",
                        "Only type-check the ORM models",
                    ],
                    "answer": "B",
                    "explain": "DB behavior needs an isolated real (or close-to-real) boundary — not only mocks.",
                },
                {
                    "lo": 1,
                    "q": "When is mocking an HTTP client appropriate in a unit test?",
                    "choices": [
                        "Never",
                        "When the code under test calls an external service and you want a fast, deterministic unit test",
                        "When you want to avoid asserting anything",
                        "When replacing pytest itself",
                    ],
                    "answer": "B",
                    "explain": "Mock external I/O for unit speed/determinism; still keep some integration tests that hit real boundaries.",
                },
                {
                    "lo": 5,
                    "q": "In this course's Python tooling, which command runs lint checks?",
                    "choices": [
                        "`ruff check .`",
                        "`ruff format .`",
                        "`python -m pytest`",
                        "`git push --force`",
                    ],
                    "answer": "A",
                    "explain": "`ruff check .` lints; `ruff format .` formats; pytest runs tests. Tooling is an LO for this module.",
                },
            ],
        },
        "03-git-and-collaboration": {
            "title": "Git and Collaboration",
            "outcomes": [
                "Use a clear branching strategy and write commits that explain why a change happened.",
                "Open and review pull requests using a practical checklist and actionable feedback.",
                "Resolve merge conflicts and rebase safely without rewriting shared history carelessly.",
                "Diagnose CI failures from logs and fix the underlying issue before merging.",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "Which commit message is more useful in review history?",
                    "choices": [
                        "`fix`",
                        "`asdf`",
                        "`Validate email before creating user to prevent duplicate accounts`",
                        "`Update file`",
                    ],
                    "answer": "C",
                    "explain": "Good commits state intent/why, not just that something changed.",
                },
                {
                    "lo": 1,
                    "q": "You are starting a feature on a shared repo using short-lived feature branches. Where should the work begin?",
                    "choices": [
                        "Commit directly to `main` with no review",
                        "A feature branch off an up-to-date `main`",
                        "A random orphan branch with no base",
                        "Rewriting `main` history on every save",
                    ],
                    "answer": "B",
                    "explain": "Feature branches keep `main` stable and make PRs reviewable.",
                },
                {
                    "lo": 2,
                    "q": "What belongs on a PR review checklist?",
                    "choices": [
                        "Only whether the author used dark mode",
                        "Correctness, tests, risk, and clarity of the change",
                        "Rejecting any change that touches more than one file",
                        "Approving without reading if CI is green",
                    ],
                    "answer": "B",
                    "explain": "Reviews focus on behavior, tests, risk, and readability — not trivia.",
                },
                {
                    "lo": 2,
                    "q": "Which review comment is more actionable?",
                    "choices": [
                        "`This is bad.`",
                        "`Please fix.`",
                        "`Can we extract the retry loop into a helper and add a test for the timeout path?`",
                        "`👀`",
                    ],
                    "answer": "C",
                    "explain": "Actionable feedback names the problem and a concrete next step.",
                },
                {
                    "lo": 3,
                    "q": "You and a teammate both edited the same lines. Git stops with a conflict. What do you do?",
                    "choices": [
                        "Delete the repository",
                        "Resolve the conflicting hunks, test, then continue the merge/rebase",
                        "Force-push without looking",
                        "Ignore the conflict markers and commit them as-is",
                    ],
                    "answer": "B",
                    "explain": "Conflicts need intentional resolution and verification — never commit conflict markers.",
                },
                {
                    "lo": 3,
                    "q": "When is rewriting history with rebase riskiest?",
                    "choices": [
                        "On a local branch only you use",
                        "On a shared branch others already pulled",
                        "Before the first commit exists",
                        "On a scratch file outside git",
                    ],
                    "answer": "B",
                    "explain": "Rebasing shared history forces teammates to recover; prefer merge or coordinate carefully.",
                },
                {
                    "lo": 4,
                    "q": "CI fails on your PR. Best next step?",
                    "choices": [
                        "Merge anyway and hope",
                        "Open the failing job logs, reproduce locally if possible, fix, and push",
                        "Disable the workflow permanently",
                        "Blame the linter and skip review",
                    ],
                    "answer": "B",
                    "explain": "CI failures are signals — read logs, fix root cause, re-run.",
                },
                {
                    "lo": 4,
                    "q": "A CI job fails with a flaky timeout only sometimes. What is a professional response?",
                    "choices": [
                        "Ignore flakes forever",
                        "Stabilize the test (determinism/timeouts/isolation) or quarantine with a tracked fix",
                        "Delete all tests",
                        "Only run CI on Fridays",
                    ],
                    "answer": "B",
                    "explain": "Flakes erode trust. Fix isolation/timing or track quarantine with an owner.",
                },
                {
                    "lo": 1,
                    "q": "Why keep commits focused (one logical change) when collaborating?",
                    "choices": [
                        "Git requires exactly one file per commit",
                        "Reviewers can understand, revert, and bisect more easily",
                        "It makes CI slower on purpose",
                        "It hides the real diff",
                    ],
                    "answer": "B",
                    "explain": "Small, purposeful commits improve review and recovery.",
                },
                {
                    "lo": 2,
                    "q": "A PR description should mainly help reviewers by…",
                    "choices": [
                        "Listing every keystroke",
                        "Explaining intent, risk, test plan, and how to verify",
                        "Pasting unrelated stack traces only",
                        "Omitting context so review is a puzzle",
                    ],
                    "answer": "B",
                    "explain": "Good PR descriptions speed correct review and reduce back-and-forth.",
                },
            ],
        },
        "04-apis-and-auth": {
            "title": "APIs and Auth",
            "outcomes": [
                "Design REST endpoints with clear resources, status codes, and pagination.",
                "Validate input and return consistent error envelopes for clients.",
                "Distinguish authentication from authorization and apply sessions/JWT/roles appropriately.",
                "Add basic rate limiting / abuse protections to sensitive endpoints.",
                "Document the API with OpenAPI (or equivalent) including examples.",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "A client successfully creates a new resource. Which status code is most appropriate?",
                    "choices": [
                        "500",
                        "201 Created",
                        "404 Not Found",
                        "401 Unauthorized",
                    ],
                    "answer": "B",
                    "explain": "201 indicates a resource was created. 500 is server error; 404 missing; 401 auth failure.",
                },
                {
                    "lo": 1,
                    "q": "Why paginate list endpoints?",
                    "choices": [
                        "To hide errors from clients",
                        "To bound response size and keep latency predictable as data grows",
                        "Because REST forbids returning more than one item ever",
                        "To avoid using status codes",
                    ],
                    "answer": "B",
                    "explain": "Pagination protects performance and usability for large collections.",
                },
                {
                    "lo": 2,
                    "q": "A client sends an invalid email format. What should the API do?",
                    "choices": [
                        "Store it anyway",
                        "Reject with 4xx and a clear, consistent error body",
                        "Return 200 with empty data and no message",
                        "Crash the worker process",
                    ],
                    "answer": "B",
                    "explain": "Validate input and return a predictable error envelope clients can handle.",
                },
                {
                    "lo": 3,
                    "q": "Authentication answers which question?",
                    "choices": [
                        "What is this user allowed to do?",
                        "Who is this user / is the identity proven?",
                        "How fast is the database?",
                        "Which CSS theme to use?",
                    ],
                    "answer": "B",
                    "explain": "AuthN = identity. AuthZ = permissions/roles after identity is known.",
                },
                {
                    "lo": 3,
                    "q": "A logged-in user tries to delete another user's private document. Which check failed if they are blocked?",
                    "choices": [
                        "Only DNS",
                        "Authorization (AuthZ) / permissions",
                        "Pagination",
                        "OpenAPI formatting",
                    ],
                    "answer": "B",
                    "explain": "They may be authenticated but not authorized for that resource action.",
                },
                {
                    "lo": 3,
                    "q": "JWTs are commonly used to…",
                    "choices": [
                        "Replace HTTPS",
                        "Carry a signed identity/claims token the API can verify without a server session store (depending on design)",
                        "Encrypt the entire database at rest by themselves",
                        "Format Python code",
                    ],
                    "answer": "B",
                    "explain": "JWTs are a common AuthN token format; they do not replace transport security or AuthZ design.",
                },
                {
                    "lo": 4,
                    "q": "Why rate-limit a login endpoint?",
                    "choices": [
                        "To make UX worse for no reason",
                        "To slow brute-force and abuse attempts",
                        "Because HTTP forbids retries",
                        "To increase 500 errors intentionally",
                    ],
                    "answer": "B",
                    "explain": "Rate limits are a basic abuse protection on sensitive endpoints.",
                },
                {
                    "lo": 5,
                    "q": "What does OpenAPI documentation help API consumers do?",
                    "choices": [
                        "Guess endpoints from production outages only",
                        "See routes, schemas, status codes, and examples in one contract",
                        "Bypass authentication permanently",
                        "Avoid writing any server code",
                    ],
                    "answer": "B",
                    "explain": "OpenAPI is the machine/human-readable contract for the API surface.",
                },
                {
                    "lo": 2,
                    "q": "Which error response style is more client-friendly?",
                    "choices": [
                        "Random HTML stack traces with no structure",
                        "A consistent JSON envelope like `{ \"error\": { \"code\": \"validation_error\", \"message\": \"...\" } }`",
                        "Empty 200 OK for failures",
                        "Closing the TCP connection silently",
                    ],
                    "answer": "B",
                    "explain": "Consistent envelopes let clients branch on `code` and show `message` safely.",
                },
                {
                    "lo": 1,
                    "q": "`GET /users/{id}` when the user does not exist should typically return:",
                    "choices": [
                        "201 Created",
                        "404 Not Found",
                        "100 Continue forever",
                        "302 to a random site",
                    ],
                    "answer": "B",
                    "explain": "Missing resources map to 404 in common REST practice.",
                },
            ],
        },
        "05-databases": {
            "title": "Databases",
            "outcomes": [
                "Design schemas with constraints that protect data integrity.",
                "Write forward/backwards-safe migrations and apply them carefully.",
                "Use transactions and reason about basic isolation needs.",
                "Choose indexes and read query plans to fix slow queries.",
                "Avoid common ORM/query-builder pitfalls (N+1, lazy loads, unbounded queries).",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "You need emails to be unique per user. Where should that rule live primarily?",
                    "choices": [
                        "Only in a comment in the README",
                        "As a database unique constraint (and validated in the app)",
                        "Only in the UI's placeholder text",
                        "In a spreadsheet outside the repo",
                    ],
                    "answer": "B",
                    "explain": "Integrity constraints in the DB enforce rules even if app code misses a check.",
                },
                {
                    "lo": 1,
                    "q": "A foreign key constraint helps by…",
                    "choices": [
                        "Speeding up CSS",
                        "Preventing orphan rows that reference missing parents",
                        "Removing the need for indexes forever",
                        "Encrypting backups automatically",
                    ],
                    "answer": "B",
                    "explain": "FKs preserve referential integrity between tables.",
                },
                {
                    "lo": 2,
                    "q": "What makes a migration safer to ship?",
                    "choices": [
                        "Editing production data by hand with no script",
                        "A reviewed migration that is expandable/rollback-aware and tested on a copy first",
                        "Dropping columns in peak traffic without a plan",
                        "Storing the SQL only in chat history",
                    ],
                    "answer": "B",
                    "explain": "Migrations should be reviewed, tested, and have a safety/rollback story.",
                },
                {
                    "lo": 3,
                    "q": "Why wrap multi-step money transfers in a transaction?",
                    "choices": [
                        "So partial updates cannot leave balances inconsistent if a step fails",
                        "Because SQL forbids single statements",
                        "To disable foreign keys",
                        "To skip indexes",
                    ],
                    "answer": "A",
                    "explain": "Transactions commit all-or-nothing for a unit of work.",
                },
                {
                    "lo": 4,
                    "q": "A query filters frequently on `orders.user_id` and is slow. First database lever?",
                    "choices": [
                        "Add an appropriate index on `user_id` (and verify with the query plan)",
                        "Buy a new laptop for the developer",
                        "Remove the WHERE clause",
                        "Store all orders in a single JSON file",
                    ],
                    "answer": "A",
                    "explain": "Indexes + EXPLAIN/query plans are the core performance tools in this module.",
                },
                {
                    "lo": 4,
                    "q": "What does reading a query plan help you see?",
                    "choices": [
                        "Only the author's favorite color",
                        "Whether the database uses indexes, scans, joins, and costly steps",
                        "Python's GIL status",
                        "Git blame for the migration file",
                    ],
                    "answer": "B",
                    "explain": "Plans show how the engine executes SQL so you can fix real bottlenecks.",
                },
                {
                    "lo": 5,
                    "q": "What is the N+1 query problem?",
                    "choices": [
                        "Using one query total for the whole app",
                        "Running one query, then one extra query per returned row (often via lazy ORM loads)",
                        "Having exactly eleven tables",
                        "A migration with eleven steps",
                    ],
                    "answer": "B",
                    "explain": "N+1 is a classic ORM pitfall — fix with joins/eager loading/batch queries.",
                },
                {
                    "lo": 5,
                    "q": "An ORM call loads an entire table into memory without a limit. Risk?",
                    "choices": [
                        "None — memory is infinite",
                        "Unbounded queries can exhaust memory and crush latency",
                        "It improves indexes automatically",
                        "It deletes constraints",
                    ],
                    "answer": "B",
                    "explain": "Always bound list queries (pagination/limits) in real systems.",
                },
                {
                    "lo": 2,
                    "q": "Why prefer expandable migrations over rewrite-in-place of historical migration files already applied?",
                    "choices": [
                        "History already applied in other environments will diverge and break deploys",
                        "Git cannot store SQL",
                        "Databases ignore schemas",
                        "Rollback is illegal in SQL",
                    ],
                    "answer": "A",
                    "explain": "Applied migrations are history; change forward with new migrations.",
                },
                {
                    "lo": 3,
                    "q": "Isolation levels mainly trade off between…",
                    "choices": [
                        "Font size and line height",
                        "Consistency vs concurrency anomalies/performance",
                        "IPv4 and IPv6",
                        "JWT and sessions only",
                    ],
                    "answer": "B",
                    "explain": "Stronger isolation reduces anomalies but can reduce throughput; pick what the use case needs.",
                },
            ],
        },
        "06-security-basics": {
            "title": "Security Basics",
            "outcomes": [
                "Map real application risks to the OWASP Top 10 categories.",
                "Store and load secrets via config/secret managers — never commit them.",
                "Prevent injection using validation, encoding, and parameterized queries.",
                "Enforce authorization checks with least privilege on every sensitive action.",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "Broken access control in OWASP terms is closest to…",
                    "choices": [
                        "Users performing actions outside their permissions",
                        "Using a slow CSS animation",
                        "Having too many unit tests",
                        "Formatting code with ruff",
                    ],
                    "answer": "A",
                    "explain": "Access control failures let users act beyond their authorization.",
                },
                {
                    "lo": 2,
                    "q": "Where should a production database password live?",
                    "choices": [
                        "Committed in the repo as `password.txt`",
                        "In environment/config or a secret manager, not in source control",
                        "Hard-coded in a public frontend bundle",
                        "In a screenshot in the PR",
                    ],
                    "answer": "B",
                    "explain": "Secrets belong in env/secret stores — never in git.",
                },
                {
                    "lo": 3,
                    "q": "Which query style best prevents SQL injection?",
                    "choices": [
                        "String-concatenating raw user input into SQL",
                        "Parameterized queries / bound parameters",
                        "Disabling the database firewall only",
                        "Lowercasing the input and hoping",
                    ],
                    "answer": "B",
                    "explain": "Parameter binding keeps data from being interpreted as SQL code.",
                },
                {
                    "lo": 3,
                    "q": "Showing user-provided HTML in a page without encoding risks…",
                    "choices": [
                        "XSS (cross-site scripting)",
                        "Faster CSS",
                        "Automatic indexing",
                        "Stronger passwords",
                    ],
                    "answer": "A",
                    "explain": "Unencoded output enables XSS — validate/encode appropriately.",
                },
                {
                    "lo": 4,
                    "q": "Least privilege means…",
                    "choices": [
                        "Every user is admin for convenience",
                        "Grant only the permissions required for a role/task — nothing more",
                        "Disable AuthZ after login",
                        "Share one service account everywhere including CI screenshots",
                    ],
                    "answer": "B",
                    "explain": "Least privilege limits blast radius when accounts or tokens leak.",
                },
                {
                    "lo": 4,
                    "q": "After AuthN succeeds, what must still happen before deleting a billing record?",
                    "choices": [
                        "Nothing — login is enough for all actions",
                        "An AuthZ check that this identity may delete that record",
                        "A CSS theme switch",
                        "Disabling HTTPS",
                    ],
                    "answer": "B",
                    "explain": "Authentication ≠ authorization. Sensitive actions need explicit AuthZ.",
                },
                {
                    "lo": 2,
                    "q": "A secret was accidentally committed. Best immediate response?",
                    "choices": [
                        "Leave it; git history is private forever on the internet",
                        "Rotate/revoke the secret, remove it from the tree, and treat history as compromised",
                        "Rename the variable only",
                        "Add more comments",
                    ],
                    "answer": "B",
                    "explain": "Assume exposure: rotate, purge from future commits, and audit usage.",
                },
                {
                    "lo": 1,
                    "q": "Why map bugs to OWASP categories during review?",
                    "choices": [
                        "To sound fancy without changing code",
                        "To prioritize fixes using a shared language for common web risks",
                        "Because OWASP replaces tests",
                        "To avoid writing error messages",
                    ],
                    "answer": "B",
                    "explain": "OWASP gives a practical taxonomy for common vulnerabilities.",
                },
                {
                    "lo": 3,
                    "q": "Server-side validation is still required when the UI already validates because…",
                    "choices": [
                        "Clients can be bypassed; the server is the trust boundary",
                        "Browsers cannot send HTTP",
                        "Databases reject all input automatically",
                        "OpenAPI makes validation unnecessary",
                    ],
                    "answer": "A",
                    "explain": "Never trust the client. Validate again on the server.",
                },
                {
                    "lo": 4,
                    "q": "A background worker token can drop production tables. What principle is violated?",
                    "choices": [
                        "Least privilege",
                        "Pagination",
                        "Big-O notation",
                        "Semantic versioning only",
                    ],
                    "answer": "A",
                    "explain": "Over-privileged tokens violate least privilege and are dangerous if leaked.",
                },
            ],
        },
        "07-debugging-and-performance": {
            "title": "Debugging and Performance",
            "outcomes": [
                "Follow a reproduce → isolate → fix debugging workflow with evidence.",
                "Use logging and basic tracing to locate failures in running systems.",
                "Profile CPU and memory to find real hotspots before optimizing.",
                "Improve database performance using slow-query analysis and indexes.",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "What is the best first step when a bug is reported?",
                    "choices": [
                        "Rewrite the whole app",
                        "Reproduce it reliably with clear steps/inputs",
                        "Delete logs so they stay clean",
                        "Optimize unrelated code",
                    ],
                    "answer": "B",
                    "explain": "If you cannot reproduce, you cannot verify a fix.",
                },
                {
                    "lo": 1,
                    "q": "After reproducing, what comes next in a solid workflow?",
                    "choices": [
                        "Ship a random change",
                        "Isolate the failing component/layer, then fix with a regression test",
                        "Turn off monitoring",
                        "Blame the reporter",
                    ],
                    "answer": "B",
                    "explain": "Reproduce → isolate → fix (and lock with a test).",
                },
                {
                    "lo": 2,
                    "q": "Which log practice helps production debugging most?",
                    "choices": [
                        "Logging secrets and full card numbers",
                        "Structured logs with request IDs and actionable context (no secrets)",
                        "Printing nothing ever",
                        "Only logging on the developer laptop",
                    ],
                    "answer": "B",
                    "explain": "Structured, correlatable logs (minus secrets) make tracing failures possible.",
                },
                {
                    "lo": 3,
                    "q": "Why profile before micro-optimizing random functions?",
                    "choices": [
                        "Profiling is slower than guessing wrong forever",
                        "Evidence shows where time/memory actually go — intuition is often wrong",
                        "Profilers delete bugs automatically",
                        "Python forbids benchmarks",
                    ],
                    "answer": "B",
                    "explain": "Measure first; optimize the real hotspot.",
                },
                {
                    "lo": 3,
                    "q": "A memory profile shows unbounded growth on each request. Likely class of issue?",
                    "choices": [
                        "A leak / unbounded cache / retaining references",
                        "Perfect GC behavior",
                        "Too many useful indexes",
                        "Commit messages that are too clear",
                    ],
                    "answer": "A",
                    "explain": "Rising memory usually means retained objects, caches without bounds, or leaks.",
                },
                {
                    "lo": 4,
                    "q": "An endpoint is slow and DB time dominates. What should you inspect?",
                    "choices": [
                        "Only the favicon",
                        "Slow queries and whether indexes/plans match the filters",
                        "The office thermostat",
                        "Whether ruff can format SQL comments",
                    ],
                    "answer": "B",
                    "explain": "DB-bound latency is attacked with query analysis and indexing.",
                },
                {
                    "lo": 2,
                    "q": "Tracing across services primarily helps you…",
                    "choices": [
                        "See a request's path/latency across components",
                        "Replace unit tests",
                        "Avoid writing logs forever",
                        "Encrypt disks by itself",
                    ],
                    "answer": "A",
                    "explain": "Traces show where a request spends time across boundaries.",
                },
                {
                    "lo": 1,
                    "q": "Why add a regression test after fixing a bug?",
                    "choices": [
                        "To guarantee the same bug can return unnoticed",
                        "To lock the fixed behavior so it cannot silently break again",
                        "Because CI requires failing tests",
                        "To increase flakiness",
                    ],
                    "answer": "B",
                    "explain": "Regression tests are the durable part of isolate → fix.",
                },
                {
                    "lo": 4,
                    "q": "Adding an index on every column “just in case” is often bad because…",
                    "choices": [
                        "Indexes are free",
                        "Extra indexes slow writes and may never help reads",
                        "SQL forbids more than one index",
                        "Query plans ignore indexes always",
                    ],
                    "answer": "B",
                    "explain": "Index with intent from measured slow queries/plans.",
                },
                {
                    "lo": 3,
                    "q": "A micro-benchmark says a function is 2% faster, but users still wait 5s. What next?",
                    "choices": [
                        "Stop measuring",
                        "Profile the end-to-end path — the hotspot may be elsewhere (often I/O/DB)",
                        "Optimize the function another 50 times blindly",
                        "Disable logging of latency",
                    ],
                    "answer": "B",
                    "explain": "Local wins can miss the real end-to-end bottleneck.",
                },
            ],
        },
        "08-deployment-and-ci": {
            "title": "Deployment and CI",
            "outcomes": [
                "Separate environments and configuration (dev/stage/prod) without baking secrets into images.",
                "Use containers to make local and CI environments reproducible.",
                "Design CI pipelines with caching, matrices, and artifacts where they help.",
                "Deploy with health checks, safe migrations, and a rollback plan.",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "Why keep production config/secrets out of the container image?",
                    "choices": [
                        "Images are never stored anywhere",
                        "Images get copied widely — secrets belong in env/secret injection at runtime",
                        "Kubernetes forbids environment variables",
                        "Config never changes between environments",
                    ],
                    "answer": "B",
                    "explain": "Build once; inject config/secrets per environment at run time.",
                },
                {
                    "lo": 1,
                    "q": "Dev and prod should differ mainly by…",
                    "choices": [
                        "Completely different undocumented codepaths with no parity",
                        "Configuration/data — not “works on my machine” snowflake setups",
                        "Disabling HTTPS only in prod",
                        "Skipping tests only in prod",
                    ],
                    "answer": "B",
                    "explain": "Environment parity + config separation reduces deploy surprises.",
                },
                {
                    "lo": 2,
                    "q": "Containers help CI/local work by…",
                    "choices": [
                        "Guaranteeing marketing copy is correct",
                        "Packaging dependencies so runs are more reproducible across machines",
                        "Removing the need for tests",
                        "Making rollbacks impossible",
                    ],
                    "answer": "B",
                    "explain": "Containers shrink “works on my machine” gaps.",
                },
                {
                    "lo": 3,
                    "q": "Why cache dependencies in CI?",
                    "choices": [
                        "To hide failing tests",
                        "To speed pipelines by reusing downloaded packages between runs",
                        "To avoid ever updating libraries",
                        "To store production secrets in the cache",
                    ],
                    "answer": "B",
                    "explain": "Caching cuts install time; still invalidate when locks change.",
                },
                {
                    "lo": 3,
                    "q": "A CI matrix is useful when you need to…",
                    "choices": [
                        "Run the same checks across versions/platforms (e.g., Python 3.11 and 3.12)",
                        "Deploy on every keystroke to production",
                        "Skip linting forever",
                        "Store passwords in artifacts",
                    ],
                    "answer": "A",
                    "explain": "Matrices fan out jobs across dimensions you care about.",
                },
                {
                    "lo": 3,
                    "q": "CI artifacts are typically used to…",
                    "choices": [
                        "Publish build outputs (wheels, images metadata, coverage reports) for later jobs/humans",
                        "Replace git remotes",
                        "Bypass code review",
                        "Disable health checks",
                    ],
                    "answer": "A",
                    "explain": "Artifacts pass outputs between jobs or retain reports.",
                },
                {
                    "lo": 4,
                    "q": "What is a health check for in deployment?",
                    "choices": [
                        "A cosmetic README badge only",
                        "Letting the platform know whether the new instance is ready to receive traffic",
                        "Deleting the database nightly",
                        "Formatting Python files",
                    ],
                    "answer": "B",
                    "explain": "Health checks gate traffic until the service is actually ready.",
                },
                {
                    "lo": 4,
                    "q": "Before a migration that might fail in production, you should have…",
                    "choices": [
                        "No plan",
                        "A tested forward path and a rollback/mitigation plan",
                        "Only a screenshot of local success",
                        "Force-push to main during peak traffic",
                    ],
                    "answer": "B",
                    "explain": "Safe deploys pair migrations with rollback thinking.",
                },
                {
                    "lo": 4,
                    "q": "A bad deploy is live. What does a rollback plan enable?",
                    "choices": [
                        "Faster return to a known-good version while you diagnose",
                        "Permanent data corruption as a feature",
                        "Skipping blameless review forever",
                        "Turning off monitoring",
                    ],
                    "answer": "A",
                    "explain": "Rollback limits user impact when a release is bad.",
                },
                {
                    "lo": 2,
                    "q": "Why run the same container image in CI tests and staging when possible?",
                    "choices": [
                        "To maximize environment drift",
                        "To test what you actually ship",
                        "Because registries reject tags",
                        "To avoid writing Dockerfiles with any base image",
                    ],
                    "answer": "B",
                    "explain": "Testing the shippable artifact catches packaging mistakes early.",
                },
            ],
        },
        "core-concepts": {
            "title": "Core Concepts",
            "heading": "Core Concepts (Intermediate)",
            "outcomes": [
                "Model data idiomatically with clear types and boundaries.",
                "Handle errors in a way that is debuggable and safe for callers.",
                "Design modules that are testable without hidden global state.",
            ],
            "questions": [
                {
                    "lo": 1,
                    "q": "Why prefer clear data models/types at module boundaries?",
                    "choices": [
                        "To make invalid states harder and intent obvious to callers",
                        "Because Python forbids dicts",
                        "To slow imports on purpose",
                        "To avoid writing tests",
                    ],
                    "answer": "A",
                    "explain": "Idiomatic modeling documents contracts and catches mistakes earlier.",
                },
                {
                    "lo": 2,
                    "q": "Which error-handling approach is usually better for libraries?",
                    "choices": [
                        "Swallow all exceptions and return `None` silently",
                        "Raise specific errors (or return structured results) that callers can handle",
                        "Call `sys.exit` on every validation failure",
                        "Print secrets into logs when failing",
                    ],
                    "answer": "B",
                    "explain": "Callers need actionable, specific failure modes — not silent `None` or process death.",
                },
                {
                    "lo": 3,
                    "q": "Hidden global mutable state makes tests hard because…",
                    "choices": [
                        "Tests become order-dependent and hard to isolate",
                        "Pytest cannot import modules",
                        "Functions become pure automatically",
                        "Types disappear",
                    ],
                    "answer": "A",
                    "explain": "Inject dependencies and keep modules pure/testable where possible.",
                },
                {
                    "lo": 3,
                    "q": "Which design is easier to unit test?",
                    "choices": [
                        "A function that reads a hard-coded production database URL from a global",
                        "A function that accepts a repository/connection as a parameter",
                        "A module that writes files to random paths with no seams",
                        "Code that only runs inside a hidden import side effect",
                    ],
                    "answer": "B",
                    "explain": "Dependency injection creates a seam for fakes/fakes doubles in tests.",
                },
                {
                    "lo": 1,
                    "q": "Using a TypedDict/dataclass/Pydantic model for an API payload mainly helps by…",
                    "choices": [
                        "Documenting fields and validating shape early",
                        "Removing the need for HTTP status codes",
                        "Replacing authentication",
                        "Making Big-O irrelevant",
                    ],
                    "answer": "A",
                    "explain": "Structured models clarify and enforce the data contract.",
                },
                {
                    "lo": 2,
                    "q": "When logging an error, you should avoid…",
                    "choices": [
                        "Including a request ID",
                        "Including secrets or raw passwords",
                        "Including the error type",
                        "Including a short human message",
                    ],
                    "answer": "B",
                    "explain": "Debuggability must not leak secrets.",
                },
                {
                    "lo": 3,
                    "q": "A module imports and mutates a process-wide cache at import time. Risk?",
                    "choices": [
                        "Easier parallel testing",
                        "Surprising side effects and brittle tests",
                        "Guaranteed purity",
                        "Automatic rollbacks",
                    ],
                    "answer": "B",
                    "explain": "Import-time side effects hurt testability and predictability.",
                },
                {
                    "lo": 1,
                    "q": "“Make invalid states unrepresentable” is closest to which practice?",
                    "choices": [
                        "Using types/models so illegal combinations cannot be constructed easily",
                        "Storing everything as untyped `Any` blobs",
                        "Parsing JSON with `eval`",
                        "Skipping validation because the UI is trusted",
                    ],
                    "answer": "A",
                    "explain": "Good models encode legal states in the type/shape itself.",
                },
                {
                    "lo": 2,
                    "q": "A caller must distinguish “not found” from “permission denied.” What should your API/module do?",
                    "choices": [
                        "Use one generic `Exception` with no details",
                        "Signal distinct error types/codes for each case",
                        "Return `False` for both",
                        "Exit the process",
                    ],
                    "answer": "B",
                    "explain": "Distinct errors let callers branch correctly.",
                },
                {
                    "lo": 3,
                    "q": "Why keep “pure” logic separate from I/O in a module?",
                    "choices": [
                        "So business rules can be unit-tested without a database or network",
                        "Because I/O is illegal in Python",
                        "To prevent using functions",
                        "To force all code into one file",
                    ],
                    "answer": "A",
                    "explain": "Separating pure logic from I/O is core testable design.",
                },
            ],
        },
    }
)

fix_module_01()


def replace_outcomes(text: str, outcomes: list[str]) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        out.append(lines[i])
        if lines[i].strip() == "## Learning Outcomes":
            i += 1
            while i < len(lines) and (
                lines[i].startswith("- ") or lines[i].strip() == ""
            ):
                # stop at next ## heading
                if lines[i].startswith("## "):
                    break
                i += 1
            # if we stopped because blank lines before prerequisites, skip blanks then check
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            for outcome in outcomes:
                out.append(f"- {outcome}\n")
            out.append("\n")
            # do not consume the next heading
            continue
        i += 1
    return "".join(out)


def replace_outcomes_core(text: str, outcomes: list[str]) -> str:
    """core-concepts has Topics instead of Learning Outcomes — insert/replace Topics as outcomes."""
    if "## Learning Outcomes" in text:
        return replace_outcomes(text, outcomes)
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    replaced = False
    while i < len(lines):
        if lines[i].strip() == "## Topics" and not replaced:
            out.append("## Learning Outcomes\n")
            for outcome in outcomes:
                out.append(f"- {outcome}\n")
            out.append("\n")
            i += 1
            while i < len(lines) and (
                lines[i].startswith("- ") or lines[i].strip() == ""
            ):
                if lines[i].startswith("## "):
                    break
                i += 1
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            replaced = True
            continue
        out.append(lines[i])
        i += 1
    return "".join(out)


def letter(i: int) -> str:
    return "ABCD"[i]


def render_quiz(slug: str, meta: dict) -> str:
    title = meta.get("heading") or f"Python Intermediate — Module {slug.split('-')[0]}: {meta['title']}"
    if slug == "core-concepts":
        title = "Core Concepts (Intermediate)"
    lines = [
        f"# {title} Quiz: Test Your Understanding",
        "",
        "## Instructions",
        "",
        "Answer these questions about the skills in this module's learning outcomes.",
        "Try from memory first — then check the answers file for explanations.",
        "",
        "## Questions",
        "",
    ]
    for idx, item in enumerate(meta["questions"], start=1):
        lo = item["lo"]
        lines.append(f"### Question {idx}: {item['q']}")
        lines.append(f"**Checks outcome {lo}:** {meta['outcomes'][lo - 1]}")
        lines.append("")
        for c_i, choice in enumerate(item["choices"]):
            # choices may already include letter prefix or not
            text = choice
            if len(choice) >= 3 and choice[0] in "ABCD" and choice[1] == ")":
                text = choice[3:].lstrip()
            lines.append(f"{letter(c_i)}) {text}  ")
        lines.append("")
        lines.append("**Your answer:** _______________")
        lines.append("")
        lines.append("---")
        lines.append("")
    n = len(meta["questions"])
    almost = max(1, n - 2)
    lines.extend(
        [
            "## Check Your Answers",
            "",
            "Once you finish, check the answers file for explanations.",
            "",
            "## How Did You Do?",
            "",
            f"- **{n}/{n} correct:** Excellent — you can apply this module's outcomes.",
            f"- **{almost}-{n - 1} correct:** Strong — review the missed outcome(s).",
            f"- **0-{almost - 1} correct:** Revisit the lessons for those outcomes, then retry.",
            "",
            "---",
            "",
            "**Good luck!** Check your answers when you are ready.",
            "",
        ]
    )
    return "\n".join(lines)


def render_answers(slug: str, meta: dict) -> str:
    title = meta.get("heading") or f"Python Intermediate — Module {slug.split('-')[0]}: {meta['title']}"
    if slug == "core-concepts":
        title = "Core Concepts (Intermediate)"
    lines = [
        f"# {title} Quiz Answers",
        "",
    ]
    for idx, item in enumerate(meta["questions"], start=1):
        lo = item["lo"]
        ans = item["answer"]
        # find choice text
        ans_i = "ABCD".index(ans)
        choice_text = item["choices"][ans_i]
        if len(choice_text) >= 3 and choice_text[0] in "ABCD" and choice_text[1] == ")":
            choice_text = choice_text[3:].lstrip()
        lines.append(f"## Question {idx}: {item['q']}")
        lines.append(f"**Answer: {ans}** — {choice_text}")
        lines.append("")
        lines.append(f"**Outcome {lo}:** {meta['outcomes'][lo - 1]}")
        lines.append("")
        lines.append(f"**Explanation:** {item['explain']}")
        lines.append("")
        lines.append("---")
        lines.append("")
    n = len(meta["questions"])
    almost = max(1, n - 2)
    lines.extend(
        [
            "## How Did You Do?",
            "",
            f"- **{n}/{n} correct:** Excellent! You are ready to move on.",
            f"- **{almost}-{n - 1} correct:** Great work — review the missed outcomes.",
            f"- **0-{almost - 1} correct:** Revisit the module lessons, then try again.",
            "",
        ]
    )
    return "\n".join(lines)


def render_alignment_sheet() -> str:
    lines = [
        "# Python Intermediate — Quiz Alignment Sheet",
        "",
        "Codecademy-style mapping: each learning outcome is tested by at least one quiz item.",
        "",
        "Generated for `languages/python/intermediate/modules/`.",
        "",
    ]
    for slug, meta in MODULES.items():
        lines.append(f"## {slug}")
        lines.append("")
        lines.append("| Outcome | Quiz questions |")
        lines.append("|---|---|")
        buckets: dict[int, list[int]] = {i + 1: [] for i in range(len(meta["outcomes"]))}
        for qi, item in enumerate(meta["questions"], start=1):
            buckets[item["lo"]].append(qi)
        for i, outcome in enumerate(meta["outcomes"], start=1):
            qs = ", ".join(f"Q{n}" for n in buckets[i]) or "—"
            lines.append(f"| LO{i}: {outcome} | {qs} |")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    for slug, meta in MODULES.items():
        lesson = MOD_DIR / f"{slug}.md"
        quiz = MOD_DIR / f"{slug}.quiz.md"
        answers = MOD_DIR / f"{slug}.quiz-answers.md"
        if not lesson.exists():
            raise SystemExit(f"Missing lesson: {lesson}")
        text = lesson.read_text(encoding="utf-8")
        if slug == "core-concepts":
            new_text = replace_outcomes_core(text, meta["outcomes"])
        else:
            new_text = replace_outcomes(text, meta["outcomes"])
        if new_text == text and "## Learning Outcomes" in text:
            # still force rewrite if outcomes block unchanged detection failed
            pass
        lesson.write_text(new_text, encoding="utf-8", newline="\n")
        quiz.write_text(render_quiz(slug, meta), encoding="utf-8", newline="\n")
        answers.write_text(render_answers(slug, meta), encoding="utf-8", newline="\n")
        print(f"updated {slug}")

    sheet = (
        ROOT
        / "languages"
        / "python"
        / "intermediate"
        / "QUIZ-ALIGNMENT.md"
    )
    sheet.write_text(render_alignment_sheet(), encoding="utf-8", newline="\n")
    print(f"wrote {sheet.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
