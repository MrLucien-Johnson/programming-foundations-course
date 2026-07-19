"""Skill-aligned quiz banks shared across languages/levels.

Each module maps slug -> {title, outcomes, questions}.
Questions use 1-based outcome indexes (`lo`) and A/B/C/D answers.
"""

from __future__ import annotations

INTERMEDIATE = {'01-dsa-practical': {'title': 'DSA (Practical)',
                      'outcomes': ['Choose list vs dict vs set for a given access pattern and '
                                   'justify the Big-O tradeoff.',
                                   'Apply stack/queue and BFS/DFS mental models to a small graph '
                                   'or tree-style problem.',
                                   "Decide when the language's built-in sort/search is enough "
                                   'versus writing a custom approach.',
                                   'Apply memoization or an LRU cache when recomputation is the '
                                   'bottleneck.',
                                   'Measure a change with a micro-benchmark and explain when '
                                   'profiling is the better tool.'],
                      'questions': [{'lo': 1,
                                     'q': 'You need average O(1) lookup of a user record by '
                                          '`user_id`. Which structure fits best?',
                                     'choices': ['A list you scan from the start each time',
                                                 'A hash map/dict keyed by `user_id`',
                                                 'A set/hash set of unsorted display names',
                                                 'A nested list of all fields without keys'],
                                     'answer': 'B',
                                     'explain': 'Hash maps/dicts give average O(1) keyed lookup. '
                                                'Scanning a list is O(n). Sets are for membership '
                                                'of values, not fielded records.'},
                                    {'lo': 1,
                                     'q': 'You must enforce unique email addresses and only care '
                                          'whether an email already exists. Best choice?',
                                     'choices': ['A list of emails',
                                                 'A hash map/dict mapping email → full user object '
                                                 '(required even if unused)',
                                                 'A set/hash set of emails',
                                                 'A queue of emails'],
                                     'answer': 'C',
                                     'explain': 'A set/hash set is ideal for unique membership '
                                                'checks. A dict works but stores unused values; a '
                                                'list makes uniqueness checks O(n).'},
                                    {'lo': 2,
                                     'q': 'You need to explore a graph level-by-level (nearest '
                                          'neighbors first). Which approach matches?',
                                     'choices': ['Depth-first search with a stack (or recursion)',
                                                 'Breadth-first search with a queue',
                                                 'Binary search on a sorted array',
                                                 'LRU eviction of the oldest key'],
                                     'answer': 'B',
                                     'explain': 'BFS uses a queue and visits nodes by '
                                                'distance/level. DFS goes deep first. Binary '
                                                'search and LRU solve different problems.'},
                                    {'lo': 2,
                                     'q': 'Undo/redo history in an editor is best modeled with '
                                          'which structure?',
                                     'choices': ['A queue (FIFO)',
                                                 'A stack (LIFO)',
                                                 'A hash set',
                                                 'A priority queue ordered by timestamp only once '
                                                 'at insert'],
                                     'answer': 'B',
                                     'explain': 'Undo reverses the most recent action first — '
                                                'classic LIFO/stack behavior.'},
                                    {'lo': 3,
                                     'q': 'You have a list of 50,000 comparable IDs and need them '
                                          'sorted once before a report. What should you do first?',
                                     'choices': ['Write a custom quicksort from scratch',
                                                 "Use the language's built-in sort unless you have "
                                                 'a measured reason not to',
                                                 'Always switch to a hand-rolled linked-list sort '
                                                 'for clarity',
                                                 'Sort with bubble sort so Big-O stays obvious'],
                                     'answer': 'B',
                                     'explain': 'Built-in sorts are highly optimized; custom sorts '
                                                'need measured justification.'},
                                    {'lo': 4,
                                     'q': 'A pure function is called repeatedly with the same '
                                          'arguments inside a hot loop. Which pattern helps first?',
                                     'choices': ['Delete the function and inline random values',
                                                 'Memoization or an LRU cache so repeated inputs '
                                                 'reuse results',
                                                 'Replace the dict with a list scan',
                                                 'Disable tests to save time'],
                                     'answer': 'B',
                                     'explain': 'Memoization/LRU caching avoids recomputing '
                                                "identical inputs — exactly this module's caching "
                                                'lesson.'},
                                    {'lo': 4,
                                     'q': 'An LRU cache is full and a new key arrives. What '
                                          'happens to the least recently used entry?',
                                     'choices': ['It stays forever',
                                                 'It is evicted to make room',
                                                 'It becomes the most recently used without '
                                                 'eviction',
                                                 'All keys are wiped'],
                                     'answer': 'B',
                                     'explain': 'LRU evicts the least recently used entry when '
                                                'capacity is exceeded.'},
                                    {'lo': 5,
                                     'q': 'You want a quick before/after timing of one helper '
                                          'function. Best first tool?',
                                     'choices': ['A micro-benchmark / timing of that function',
                                                 'Only a full-cluster production profiler with no '
                                                 'local measurement',
                                                 'Guessing from code review alone',
                                                 'Turning off tests so numbers look better'],
                                     'answer': 'A',
                                     'explain': 'Micro-benchmarks answer “is this function '
                                                'faster?” Profiling answers “where does the whole '
                                                'program spend time?” Start local and measured.'},
                                    {'lo': 5,
                                     'q': 'When is profiling usually better than a '
                                          'micro-benchmark?',
                                     'choices': ['When you already know the one-line hotspot with '
                                                 'certainty',
                                                 'When you need to find where a whole program '
                                                 'spends CPU or memory',
                                                 'When you want to skip measurements entirely',
                                                 'When sorting a 10-element list'],
                                     'answer': 'B',
                                     'explain': 'Profilers locate hotspots across a running '
                                                'program. Micro-benchmarks compare a narrow slice '
                                                'you already suspect.'},
                                    {'lo': 1,
                                     'q': 'Looking up whether an id is in a large unsorted list of '
                                          'IDs is typically:',
                                     'choices': ['O(1) average',
                                                 'O(n)',
                                                 'O(log n) without sorting',
                                                 'O(n²) always'],
                                     'answer': 'B',
                                     'explain': 'Membership in an unsorted list scans elements — '
                                                'O(n). A set/dict membership check is average '
                                                'O(1).'}]},
 '02-testing-and-quality': {'title': 'Testing and Quality',
                            'outcomes': ['Place tests on the test pyramid and choose what to mock '
                                         'versus what to hit for real.',
                                         'Write deterministic unit tests using fixtures/factories '
                                         'and meaningful assertions.',
                                         'Add an integration test that crosses a real boundary '
                                         '(HTTP, DB, filesystem, or process).',
                                         'Interpret coverage as a signal — not a substitute for '
                                         'strong assertions.',
                                         'Use lint, format, and typecheck as automated quality '
                                         'gates.'],
                            'questions': [{'lo': 1,
                                           'q': 'On the test pyramid, which layer should usually '
                                                'be the largest (most numerous)?',
                                           'choices': ['Manual-only exploratory tests',
                                                       'Unit tests',
                                                       'Full production canaries only',
                                                       'UI screenshot tests for every line of '
                                                       'code'],
                                           'answer': 'B',
                                           'explain': 'Unit tests are fast and numerous; '
                                                      'integration/E2E are fewer and slower.'},
                                          {'lo': 1,
                                           'q': 'You are unit-testing a pure pricing function. '
                                                'What should you usually avoid mocking?',
                                           'choices': ["The function's own arithmetic",
                                                       'An external payment HTTP API used by a '
                                                       'different module',
                                                       'A clock if the function under test does '
                                                       'not use time',
                                                       'Nothing — mock every name in scope'],
                                           'answer': 'A',
                                           'explain': "Don't mock the behavior you are trying to "
                                                      'prove. Mock slow/external boundaries, not '
                                                      'the subject itself.'},
                                          {'lo': 2,
                                           'q': 'A test fails only when run after another test. '
                                                'What is the likely problem?',
                                           'choices': ['The assertion is too meaningful',
                                                       'Shared mutable state — the suite is not '
                                                       'deterministic/isolated',
                                                       'Coverage is above 90%',
                                                       'The linter is too strict'],
                                           'answer': 'B',
                                           'explain': 'Order-dependent failures usually mean '
                                                      'leaked global/DB/file state. Tests must '
                                                      'isolate and reset fixtures.'},
                                          {'lo': 2,
                                           'q': 'Which assertion is stronger for '
                                                '`create_user(email)`?',
                                           'choices': ['`assert result is not None`',
                                                       '`assert result.email == email and '
                                                       'result.id is not None`',
                                                       '`assert True`',
                                                       '`assert result` with no further checks'],
                                           'answer': 'B',
                                           'explain': 'Meaningful assertions check observable '
                                                      'outcomes, not merely “something happened.”'},
                                          {'lo': 3,
                                           'q': 'Which example is an integration test?',
                                           'choices': ['Calling a pure function with mocked '
                                                       'everything including its own logic',
                                                       'Hitting a real test database or HTTP '
                                                       'endpoint and asserting the response',
                                                       'Reading the source code without running it',
                                                       'Running the formatter alone'],
                                           'answer': 'B',
                                           'explain': 'Integration tests cross a real boundary '
                                                      '(HTTP/DB/etc.), not just in-memory mocks of '
                                                      'the unit.'},
                                          {'lo': 4,
                                           'q': 'Coverage reports 100%, but a bug still ships. '
                                                'What lesson fits?',
                                           'choices': ['Coverage guarantees correctness',
                                                       'Coverage without meaningful assertions can '
                                                       'still miss behavior',
                                                       'You should delete all unit tests',
                                                       'Only E2E tests ever matter'],
                                           'answer': 'B',
                                           'explain': 'Coverage shows what ran, not whether you '
                                                      'asserted the right outcomes.'},
                                          {'lo': 5,
                                           'q': 'Why run lint/format/typecheck in CI as quality '
                                                'gates?',
                                           'choices': ['To replace unit tests entirely',
                                                       'To catch style, bug-prone patterns, and '
                                                       'type issues before merge',
                                                       'To slow developers with no signal',
                                                       'Only to generate prettier README '
                                                       'screenshots'],
                                           'answer': 'B',
                                           'explain': 'Automated gates keep a consistent baseline '
                                                      'so humans review design and behavior.'},
                                          {'lo': 3,
                                           'q': 'Your feature writes to Postgres. Which test '
                                                'strategy best proves the boundary works?',
                                           'choices': ['Mock the DB away and never talk to SQL',
                                                       'An integration test against an isolated '
                                                       'test schema/database',
                                                       'Print SQL in a comment and skip running it',
                                                       'Only type-check the ORM models'],
                                           'answer': 'B',
                                           'explain': 'DB behavior needs an isolated real (or '
                                                      'close-to-real) boundary — not only mocks.'},
                                          {'lo': 1,
                                           'q': 'When is mocking an HTTP client appropriate in a '
                                                'unit test?',
                                           'choices': ['Never',
                                                       'When the code under test calls an external '
                                                       'service and you want a fast, deterministic '
                                                       'unit test',
                                                       'When you want to avoid asserting anything',
                                                       'When replacing the test runner itself'],
                                           'answer': 'B',
                                           'explain': 'Mock external I/O for unit '
                                                      'speed/determinism; still keep some '
                                                      'integration tests that hit real '
                                                      'boundaries.'},
                                          {'lo': 5,
                                           'q': 'What is the main value of lint/format/typecheck '
                                                'gates in CI?',
                                           'choices': ['They replace all unit and integration '
                                                       'tests',
                                                       'They catch style, bug-prone patterns, and '
                                                       'type issues before merge',
                                                       'They exist only to slow developers with no '
                                                       'signal',
                                                       'They only generate prettier README '
                                                       'screenshots'],
                                           'answer': 'B',
                                           'explain': 'Automated quality gates keep a consistent '
                                                      'baseline so humans review design and '
                                                      'behavior.'}]},
 '03-git-and-collaboration': {'title': 'Git and Collaboration',
                              'outcomes': ['Use a clear branching strategy and write commits that '
                                           'explain why a change happened.',
                                           'Open and review pull requests using a practical '
                                           'checklist and actionable feedback.',
                                           'Resolve merge conflicts and rebase safely without '
                                           'rewriting shared history carelessly.',
                                           'Diagnose CI failures from logs and fix the underlying '
                                           'issue before merging.'],
                              'questions': [{'lo': 1,
                                             'q': 'Which commit message is more useful in review '
                                                  'history?',
                                             'choices': ['`fix`',
                                                         '`asdf`',
                                                         '`Validate email before creating user to '
                                                         'prevent duplicate accounts`',
                                                         '`Update file`'],
                                             'answer': 'C',
                                             'explain': 'Good commits state intent/why, not just '
                                                        'that something changed.'},
                                            {'lo': 1,
                                             'q': 'You are starting a feature on a shared repo '
                                                  'using short-lived feature branches. Where '
                                                  'should the work begin?',
                                             'choices': ['Commit directly to `main` with no review',
                                                         'A feature branch off an up-to-date '
                                                         '`main`',
                                                         'A random orphan branch with no base',
                                                         'Rewriting `main` history on every save'],
                                             'answer': 'B',
                                             'explain': 'Feature branches keep `main` stable and '
                                                        'make PRs reviewable.'},
                                            {'lo': 2,
                                             'q': 'What belongs on a PR review checklist?',
                                             'choices': ['Only whether the author used dark mode',
                                                         'Correctness, tests, risk, and clarity of '
                                                         'the change',
                                                         'Rejecting any change that touches more '
                                                         'than one file',
                                                         'Approving without reading if CI is '
                                                         'green'],
                                             'answer': 'B',
                                             'explain': 'Reviews focus on behavior, tests, risk, '
                                                        'and readability — not trivia.'},
                                            {'lo': 2,
                                             'q': 'Which review comment is more actionable?',
                                             'choices': ['`This is bad.`',
                                                         '`Please fix.`',
                                                         '`Can we extract the retry loop into a '
                                                         'helper and add a test for the timeout '
                                                         'path?`',
                                                         '`👀`'],
                                             'answer': 'C',
                                             'explain': 'Actionable feedback names the problem and '
                                                        'a concrete next step.'},
                                            {'lo': 3,
                                             'q': 'You and a teammate both edited the same lines. '
                                                  'Git stops with a conflict. What do you do?',
                                             'choices': ['Delete the repository',
                                                         'Resolve the conflicting hunks, test, '
                                                         'then continue the merge/rebase',
                                                         'Force-push without looking',
                                                         'Ignore the conflict markers and commit '
                                                         'them as-is'],
                                             'answer': 'B',
                                             'explain': 'Conflicts need intentional resolution and '
                                                        'verification — never commit conflict '
                                                        'markers.'},
                                            {'lo': 3,
                                             'q': 'When is rewriting history with rebase riskiest?',
                                             'choices': ['On a local branch only you use',
                                                         'On a shared branch others already pulled',
                                                         'Before the first commit exists',
                                                         'On a scratch file outside git'],
                                             'answer': 'B',
                                             'explain': 'Rebasing shared history forces teammates '
                                                        'to recover; prefer merge or coordinate '
                                                        'carefully.'},
                                            {'lo': 4,
                                             'q': 'CI fails on your PR. Best next step?',
                                             'choices': ['Merge anyway and hope',
                                                         'Open the failing job logs, reproduce '
                                                         'locally if possible, fix, and push',
                                                         'Disable the workflow permanently',
                                                         'Blame the linter and skip review'],
                                             'answer': 'B',
                                             'explain': 'CI failures are signals — read logs, fix '
                                                        'root cause, re-run.'},
                                            {'lo': 4,
                                             'q': 'A CI job fails with a flaky timeout only '
                                                  'sometimes. What is a professional response?',
                                             'choices': ['Ignore flakes forever',
                                                         'Stabilize the test '
                                                         '(determinism/timeouts/isolation) or '
                                                         'quarantine with a tracked fix',
                                                         'Delete all tests',
                                                         'Only run CI on Fridays'],
                                             'answer': 'B',
                                             'explain': 'Flakes erode trust. Fix isolation/timing '
                                                        'or track quarantine with an owner.'},
                                            {'lo': 1,
                                             'q': 'Why keep commits focused (one logical change) '
                                                  'when collaborating?',
                                             'choices': ['Git requires exactly one file per commit',
                                                         'Reviewers can understand, revert, and '
                                                         'bisect more easily',
                                                         'It makes CI slower on purpose',
                                                         'It hides the real diff'],
                                             'answer': 'B',
                                             'explain': 'Small, purposeful commits improve review '
                                                        'and recovery.'},
                                            {'lo': 2,
                                             'q': 'A PR description should mainly help reviewers '
                                                  'by…',
                                             'choices': ['Listing every keystroke',
                                                         'Explaining intent, risk, test plan, and '
                                                         'how to verify',
                                                         'Pasting unrelated stack traces only',
                                                         'Omitting context so review is a puzzle'],
                                             'answer': 'B',
                                             'explain': 'Good PR descriptions speed correct review '
                                                        'and reduce back-and-forth.'}]},
 '04-apis-and-auth': {'title': 'APIs and Auth',
                      'outcomes': ['Design REST endpoints with clear resources, status codes, and '
                                   'pagination.',
                                   'Validate input and return consistent error envelopes for '
                                   'clients.',
                                   'Distinguish authentication from authorization and apply '
                                   'sessions/JWT/roles appropriately.',
                                   'Add basic rate limiting / abuse protections to sensitive '
                                   'endpoints.',
                                   'Document the API with OpenAPI (or equivalent) including '
                                   'examples.'],
                      'questions': [{'lo': 1,
                                     'q': 'A client successfully creates a new resource. Which '
                                          'status code is most appropriate?',
                                     'choices': ['500',
                                                 '201 Created',
                                                 '404 Not Found',
                                                 '401 Unauthorized'],
                                     'answer': 'B',
                                     'explain': '201 indicates a resource was created. 500 is '
                                                'server error; 404 missing; 401 auth failure.'},
                                    {'lo': 1,
                                     'q': 'Why paginate list endpoints?',
                                     'choices': ['To hide errors from clients',
                                                 'To bound response size and keep latency '
                                                 'predictable as data grows',
                                                 'Because REST forbids returning more than one '
                                                 'item ever',
                                                 'To avoid using status codes'],
                                     'answer': 'B',
                                     'explain': 'Pagination protects performance and usability for '
                                                'large collections.'},
                                    {'lo': 2,
                                     'q': 'A client sends an invalid email format. What should the '
                                          'API do?',
                                     'choices': ['Store it anyway',
                                                 'Reject with 4xx and a clear, consistent error '
                                                 'body',
                                                 'Return 200 with empty data and no message',
                                                 'Crash the worker process'],
                                     'answer': 'B',
                                     'explain': 'Validate input and return a predictable error '
                                                'envelope clients can handle.'},
                                    {'lo': 3,
                                     'q': 'Authentication answers which question?',
                                     'choices': ['What is this user allowed to do?',
                                                 'Who is this user / is the identity proven?',
                                                 'How fast is the database?',
                                                 'Which CSS theme to use?'],
                                     'answer': 'B',
                                     'explain': 'AuthN = identity. AuthZ = permissions/roles after '
                                                'identity is known.'},
                                    {'lo': 3,
                                     'q': "A logged-in user tries to delete another user's private "
                                          'document. Which check failed if they are blocked?',
                                     'choices': ['Only DNS',
                                                 'Authorization (AuthZ) / permissions',
                                                 'Pagination',
                                                 'OpenAPI formatting'],
                                     'answer': 'B',
                                     'explain': 'They may be authenticated but not authorized for '
                                                'that resource action.'},
                                    {'lo': 3,
                                     'q': 'JWTs are commonly used to…',
                                     'choices': ['Replace HTTPS',
                                                 'Carry a signed identity/claims token the API can '
                                                 'verify without a server session store (depending '
                                                 'on design)',
                                                 'Encrypt the entire database at rest by '
                                                 'themselves',
                                                 'Format source code'],
                                     'answer': 'B',
                                     'explain': 'JWTs are a common AuthN token format; they do not '
                                                'replace transport security or AuthZ design.'},
                                    {'lo': 4,
                                     'q': 'Why rate-limit a login endpoint?',
                                     'choices': ['To make UX worse for no reason',
                                                 'To slow brute-force and abuse attempts',
                                                 'Because HTTP forbids retries',
                                                 'To increase 500 errors intentionally'],
                                     'answer': 'B',
                                     'explain': 'Rate limits are a basic abuse protection on '
                                                'sensitive endpoints.'},
                                    {'lo': 5,
                                     'q': 'What does OpenAPI documentation help API consumers do?',
                                     'choices': ['Guess endpoints from production outages only',
                                                 'See routes, schemas, status codes, and examples '
                                                 'in one contract',
                                                 'Bypass authentication permanently',
                                                 'Avoid writing any server code'],
                                     'answer': 'B',
                                     'explain': 'OpenAPI is the machine/human-readable contract '
                                                'for the API surface.'},
                                    {'lo': 2,
                                     'q': 'Which error response style is more client-friendly?',
                                     'choices': ['Random HTML stack traces with no structure',
                                                 'A consistent JSON envelope like `{ "error": { '
                                                 '"code": "validation_error", "message": "..." } '
                                                 '}`',
                                                 'Empty 200 OK for failures',
                                                 'Closing the TCP connection silently'],
                                     'answer': 'B',
                                     'explain': 'Consistent envelopes let clients branch on `code` '
                                                'and show `message` safely.'},
                                    {'lo': 1,
                                     'q': '`GET /users/{id}` when the user does not exist should '
                                          'typically return:',
                                     'choices': ['201 Created',
                                                 '404 Not Found',
                                                 '100 Continue forever',
                                                 '302 to a random site'],
                                     'answer': 'B',
                                     'explain': 'Missing resources map to 404 in common REST '
                                                'practice.'}]},
 '05-databases': {'title': 'Databases',
                  'outcomes': ['Design schemas with constraints that protect data integrity.',
                               'Write forward/backwards-safe migrations and apply them carefully.',
                               'Use transactions and reason about basic isolation needs.',
                               'Choose indexes and read query plans to fix slow queries.',
                               'Avoid common ORM/query-builder pitfalls (N+1, lazy loads, '
                               'unbounded queries).'],
                  'questions': [{'lo': 1,
                                 'q': 'You need emails to be unique per user. Where should that '
                                      'rule live primarily?',
                                 'choices': ['Only in a comment in the README',
                                             'As a database unique constraint (and validated in '
                                             'the app)',
                                             "Only in the UI's placeholder text",
                                             'In a spreadsheet outside the repo'],
                                 'answer': 'B',
                                 'explain': 'Integrity constraints in the DB enforce rules even if '
                                            'app code misses a check.'},
                                {'lo': 1,
                                 'q': 'A foreign key constraint helps by…',
                                 'choices': ['Speeding up CSS',
                                             'Preventing orphan rows that reference missing '
                                             'parents',
                                             'Removing the need for indexes forever',
                                             'Encrypting backups automatically'],
                                 'answer': 'B',
                                 'explain': 'FKs preserve referential integrity between tables.'},
                                {'lo': 2,
                                 'q': 'What makes a migration safer to ship?',
                                 'choices': ['Editing production data by hand with no script',
                                             'A reviewed migration that is '
                                             'expandable/rollback-aware and tested on a copy first',
                                             'Dropping columns in peak traffic without a plan',
                                             'Storing the SQL only in chat history'],
                                 'answer': 'B',
                                 'explain': 'Migrations should be reviewed, tested, and have a '
                                            'safety/rollback story.'},
                                {'lo': 3,
                                 'q': 'Why wrap multi-step money transfers in a transaction?',
                                 'choices': ['So partial updates cannot leave balances '
                                             'inconsistent if a step fails',
                                             'Because SQL forbids single statements',
                                             'To disable foreign keys',
                                             'To skip indexes'],
                                 'answer': 'A',
                                 'explain': 'Transactions commit all-or-nothing for a unit of '
                                            'work.'},
                                {'lo': 4,
                                 'q': 'A query filters frequently on `orders.user_id` and is slow. '
                                      'First database lever?',
                                 'choices': ['Add an appropriate index on `user_id` (and verify '
                                             'with the query plan)',
                                             'Buy a new laptop for the developer',
                                             'Remove the WHERE clause',
                                             'Store all orders in a single JSON file'],
                                 'answer': 'A',
                                 'explain': 'Indexes + EXPLAIN/query plans are the core '
                                            'performance tools in this module.'},
                                {'lo': 4,
                                 'q': 'What does reading a query plan help you see?',
                                 'choices': ["Only the author's favorite color",
                                             'Whether the database uses indexes, scans, joins, and '
                                             'costly steps',
                                             'The editor color theme',
                                             'Git blame for the migration file'],
                                 'answer': 'B',
                                 'explain': 'Plans show how the engine executes SQL so you can fix '
                                            'real bottlenecks.'},
                                {'lo': 5,
                                 'q': 'What is the N+1 query problem?',
                                 'choices': ['Using one query total for the whole app',
                                             'Running one query, then one extra query per returned '
                                             'row (often via lazy ORM loads)',
                                             'Having exactly eleven tables',
                                             'A migration with eleven steps'],
                                 'answer': 'B',
                                 'explain': 'N+1 is a classic ORM pitfall — fix with joins/eager '
                                            'loading/batch queries.'},
                                {'lo': 5,
                                 'q': 'An ORM call loads an entire table into memory without a '
                                      'limit. Risk?',
                                 'choices': ['None — memory is infinite',
                                             'Unbounded queries can exhaust memory and crush '
                                             'latency',
                                             'It improves indexes automatically',
                                             'It deletes constraints'],
                                 'answer': 'B',
                                 'explain': 'Always bound list queries (pagination/limits) in real '
                                            'systems.'},
                                {'lo': 2,
                                 'q': 'Why prefer expandable migrations over rewrite-in-place of '
                                      'historical migration files already applied?',
                                 'choices': ['History already applied in other environments will '
                                             'diverge and break deploys',
                                             'Git cannot store SQL',
                                             'Databases ignore schemas',
                                             'Rollback is illegal in SQL'],
                                 'answer': 'A',
                                 'explain': 'Applied migrations are history; change forward with '
                                            'new migrations.'},
                                {'lo': 3,
                                 'q': 'Isolation levels mainly trade off between…',
                                 'choices': ['Font size and line height',
                                             'Consistency vs concurrency anomalies/performance',
                                             'IPv4 and IPv6',
                                             'JWT and sessions only'],
                                 'answer': 'B',
                                 'explain': 'Stronger isolation reduces anomalies but can reduce '
                                            'throughput; pick what the use case needs.'}]},
 '06-security-basics': {'title': 'Security Basics',
                        'outcomes': ['Map real application risks to the OWASP Top 10 categories.',
                                     'Store and load secrets via config/secret managers — never '
                                     'commit them.',
                                     'Prevent injection using validation, encoding, and '
                                     'parameterized queries.',
                                     'Enforce authorization checks with least privilege on every '
                                     'sensitive action.'],
                        'questions': [{'lo': 1,
                                       'q': 'Broken access control in OWASP terms is closest to…',
                                       'choices': ['Users performing actions outside their '
                                                   'permissions',
                                                   'Using a slow CSS animation',
                                                   'Having too many unit tests',
                                                   'Formatting code with the linter'],
                                       'answer': 'A',
                                       'explain': 'Access control failures let users act beyond '
                                                  'their authorization.'},
                                      {'lo': 2,
                                       'q': 'Where should a production database password live?',
                                       'choices': ['Committed in the repo as `password.txt`',
                                                   'In environment/config or a secret manager, not '
                                                   'in source control',
                                                   'Hard-coded in a public frontend bundle',
                                                   'In a screenshot in the PR'],
                                       'answer': 'B',
                                       'explain': 'Secrets belong in env/secret stores — never in '
                                                  'git.'},
                                      {'lo': 3,
                                       'q': 'Which query style best prevents SQL injection?',
                                       'choices': ['String-concatenating raw user input into SQL',
                                                   'Parameterized queries / bound parameters',
                                                   'Disabling the database firewall only',
                                                   'Lowercasing the input and hoping'],
                                       'answer': 'B',
                                       'explain': 'Parameter binding keeps data from being '
                                                  'interpreted as SQL code.'},
                                      {'lo': 3,
                                       'q': 'Showing user-provided HTML in a page without encoding '
                                            'risks…',
                                       'choices': ['XSS (cross-site scripting)',
                                                   'Faster CSS',
                                                   'Automatic indexing',
                                                   'Stronger passwords'],
                                       'answer': 'A',
                                       'explain': 'Unencoded output enables XSS — validate/encode '
                                                  'appropriately.'},
                                      {'lo': 4,
                                       'q': 'Least privilege means…',
                                       'choices': ['Every user is admin for convenience',
                                                   'Grant only the permissions required for a '
                                                   'role/task — nothing more',
                                                   'Disable AuthZ after login',
                                                   'Share one service account everywhere including '
                                                   'CI screenshots'],
                                       'answer': 'B',
                                       'explain': 'Least privilege limits blast radius when '
                                                  'accounts or tokens leak.'},
                                      {'lo': 4,
                                       'q': 'After AuthN succeeds, what must still happen before '
                                            'deleting a billing record?',
                                       'choices': ['Nothing — login is enough for all actions',
                                                   'An AuthZ check that this identity may delete '
                                                   'that record',
                                                   'A CSS theme switch',
                                                   'Disabling HTTPS'],
                                       'answer': 'B',
                                       'explain': 'Authentication ≠ authorization. Sensitive '
                                                  'actions need explicit AuthZ.'},
                                      {'lo': 2,
                                       'q': 'A secret was accidentally committed. Best immediate '
                                            'response?',
                                       'choices': ['Leave it; git history is private forever on '
                                                   'the internet',
                                                   'Rotate/revoke the secret, remove it from the '
                                                   'tree, and treat history as compromised',
                                                   'Rename the variable only',
                                                   'Add more comments'],
                                       'answer': 'B',
                                       'explain': 'Assume exposure: rotate, purge from future '
                                                  'commits, and audit usage.'},
                                      {'lo': 1,
                                       'q': 'Why map bugs to OWASP categories during review?',
                                       'choices': ['To sound fancy without changing code',
                                                   'To prioritize fixes using a shared language '
                                                   'for common web risks',
                                                   'Because OWASP replaces tests',
                                                   'To avoid writing error messages'],
                                       'answer': 'B',
                                       'explain': 'OWASP gives a practical taxonomy for common '
                                                  'vulnerabilities.'},
                                      {'lo': 3,
                                       'q': 'Server-side validation is still required when the UI '
                                            'already validates because…',
                                       'choices': ['Clients can be bypassed; the server is the '
                                                   'trust boundary',
                                                   'Browsers cannot send HTTP',
                                                   'Databases reject all input automatically',
                                                   'OpenAPI makes validation unnecessary'],
                                       'answer': 'A',
                                       'explain': 'Never trust the client. Validate again on the '
                                                  'server.'},
                                      {'lo': 4,
                                       'q': 'A background worker token can drop production tables. '
                                            'What principle is violated?',
                                       'choices': ['Least privilege',
                                                   'Pagination',
                                                   'Big-O notation',
                                                   'Semantic versioning only'],
                                       'answer': 'A',
                                       'explain': 'Over-privileged tokens violate least privilege '
                                                  'and are dangerous if leaked.'}]},
 '07-debugging-and-performance': {'title': 'Debugging and Performance',
                                  'outcomes': ['Follow a reproduce → isolate → fix debugging '
                                               'workflow with evidence.',
                                               'Use logging and basic tracing to locate failures '
                                               'in running systems.',
                                               'Profile CPU and memory to find real hotspots '
                                               'before optimizing.',
                                               'Improve database performance using slow-query '
                                               'analysis and indexes.'],
                                  'questions': [{'lo': 1,
                                                 'q': 'What is the best first step when a bug is '
                                                      'reported?',
                                                 'choices': ['Rewrite the whole app',
                                                             'Reproduce it reliably with clear '
                                                             'steps/inputs',
                                                             'Delete logs so they stay clean',
                                                             'Optimize unrelated code'],
                                                 'answer': 'B',
                                                 'explain': 'If you cannot reproduce, you cannot '
                                                            'verify a fix.'},
                                                {'lo': 1,
                                                 'q': 'After reproducing, what comes next in a '
                                                      'solid workflow?',
                                                 'choices': ['Ship a random change',
                                                             'Isolate the failing component/layer, '
                                                             'then fix with a regression test',
                                                             'Turn off monitoring',
                                                             'Blame the reporter'],
                                                 'answer': 'B',
                                                 'explain': 'Reproduce → isolate → fix (and lock '
                                                            'with a test).'},
                                                {'lo': 2,
                                                 'q': 'Which log practice helps production '
                                                      'debugging most?',
                                                 'choices': ['Logging secrets and full card '
                                                             'numbers',
                                                             'Structured logs with request IDs and '
                                                             'actionable context (no secrets)',
                                                             'Printing nothing ever',
                                                             'Only logging on the developer '
                                                             'laptop'],
                                                 'answer': 'B',
                                                 'explain': 'Structured, correlatable logs (minus '
                                                            'secrets) make tracing failures '
                                                            'possible.'},
                                                {'lo': 3,
                                                 'q': 'Why profile before micro-optimizing random '
                                                      'functions?',
                                                 'choices': ['Profiling is slower than guessing '
                                                             'wrong forever',
                                                             'Evidence shows where time/memory '
                                                             'actually go — intuition is often '
                                                             'wrong',
                                                             'Profilers delete bugs automatically',
                                                             'Benchmarks are forbidden by the language'],
                                                 'answer': 'B',
                                                 'explain': 'Measure first; optimize the real '
                                                            'hotspot.'},
                                                {'lo': 3,
                                                 'q': 'A memory profile shows unbounded growth on '
                                                      'each request. Likely class of issue?',
                                                 'choices': ['A leak / unbounded cache / retaining '
                                                             'references',
                                                             'Perfect GC behavior',
                                                             'Too many useful indexes',
                                                             'Commit messages that are too clear'],
                                                 'answer': 'A',
                                                 'explain': 'Rising memory usually means retained '
                                                            'objects, caches without bounds, or '
                                                            'leaks.'},
                                                {'lo': 4,
                                                 'q': 'An endpoint is slow and DB time dominates. '
                                                      'What should you inspect?',
                                                 'choices': ['Only the favicon',
                                                             'Slow queries and whether '
                                                             'indexes/plans match the filters',
                                                             'The office thermostat',
                                                             'Whether the README mentions SQL '
                                                             'comments'],
                                                 'answer': 'B',
                                                 'explain': 'DB-bound latency is attacked with '
                                                            'query analysis and indexing.'},
                                                {'lo': 2,
                                                 'q': 'Tracing across services primarily helps '
                                                      'you…',
                                                 'choices': ["See a request's path/latency across "
                                                             'components',
                                                             'Replace unit tests',
                                                             'Avoid writing logs forever',
                                                             'Encrypt disks by itself'],
                                                 'answer': 'A',
                                                 'explain': 'Traces show where a request spends '
                                                            'time across boundaries.'},
                                                {'lo': 1,
                                                 'q': 'Why add a regression test after fixing a '
                                                      'bug?',
                                                 'choices': ['To guarantee the same bug can return '
                                                             'unnoticed',
                                                             'To lock the fixed behavior so it '
                                                             'cannot silently break again',
                                                             'Because CI requires failing tests',
                                                             'To increase flakiness'],
                                                 'answer': 'B',
                                                 'explain': 'Regression tests are the durable part '
                                                            'of isolate → fix.'},
                                                {'lo': 4,
                                                 'q': 'Adding an index on every column “just in '
                                                      'case” is often bad because…',
                                                 'choices': ['Indexes are free',
                                                             'Extra indexes slow writes and may '
                                                             'never help reads',
                                                             'SQL forbids more than one index',
                                                             'Query plans ignore indexes always'],
                                                 'answer': 'B',
                                                 'explain': 'Index with intent from measured slow '
                                                            'queries/plans.'},
                                                {'lo': 3,
                                                 'q': 'A micro-benchmark says a function is 2% '
                                                      'faster, but users still wait 5s. What next?',
                                                 'choices': ['Stop measuring',
                                                             'Profile the end-to-end path — the '
                                                             'hotspot may be elsewhere (often '
                                                             'I/O/DB)',
                                                             'Optimize the function another 50 '
                                                             'times blindly',
                                                             'Disable logging of latency'],
                                                 'answer': 'B',
                                                 'explain': 'Local wins can miss the real '
                                                            'end-to-end bottleneck.'}]},
 '08-deployment-and-ci': {'title': 'Deployment and CI',
                          'outcomes': ['Separate environments and configuration (dev/stage/prod) '
                                       'without baking secrets into images.',
                                       'Use containers to make local and CI environments '
                                       'reproducible.',
                                       'Design CI pipelines with caching, matrices, and artifacts '
                                       'where they help.',
                                       'Deploy with health checks, safe migrations, and a rollback '
                                       'plan.'],
                          'questions': [{'lo': 1,
                                         'q': 'Why keep production config/secrets out of the '
                                              'container image?',
                                         'choices': ['Images are never stored anywhere',
                                                     'Images get copied widely — secrets belong in '
                                                     'env/secret injection at runtime',
                                                     'Kubernetes forbids environment variables',
                                                     'Config never changes between environments'],
                                         'answer': 'B',
                                         'explain': 'Build once; inject config/secrets per '
                                                    'environment at run time.'},
                                        {'lo': 1,
                                         'q': 'Dev and prod should differ mainly by…',
                                         'choices': ['Completely different undocumented codepaths '
                                                     'with no parity',
                                                     'Configuration/data — not “works on my '
                                                     'machine” snowflake setups',
                                                     'Disabling HTTPS only in prod',
                                                     'Skipping tests only in prod'],
                                         'answer': 'B',
                                         'explain': 'Environment parity + config separation '
                                                    'reduces deploy surprises.'},
                                        {'lo': 2,
                                         'q': 'Containers help CI/local work by…',
                                         'choices': ['Guaranteeing marketing copy is correct',
                                                     'Packaging dependencies so runs are more '
                                                     'reproducible across machines',
                                                     'Removing the need for tests',
                                                     'Making rollbacks impossible'],
                                         'answer': 'B',
                                         'explain': 'Containers shrink “works on my machine” '
                                                    'gaps.'},
                                        {'lo': 3,
                                         'q': 'Why cache dependencies in CI?',
                                         'choices': ['To hide failing tests',
                                                     'To speed pipelines by reusing downloaded '
                                                     'packages between runs',
                                                     'To avoid ever updating libraries',
                                                     'To store production secrets in the cache'],
                                         'answer': 'B',
                                         'explain': 'Caching cuts install time; still invalidate '
                                                    'when locks change.'},
                                        {'lo': 3,
                                         'q': 'A CI matrix is useful when you need to…',
                                         'choices': ['Run the same checks across '
                                                     'versions/platforms (e.g., 3.11 and '
                                                     '3.12)',
                                                     'Deploy on every keystroke to production',
                                                     'Skip linting forever',
                                                     'Store passwords in artifacts'],
                                         'answer': 'A',
                                         'explain': 'Matrices fan out jobs across dimensions you '
                                                    'care about.'},
                                        {'lo': 3,
                                         'q': 'CI artifacts are typically used to…',
                                         'choices': ['Publish build outputs (wheels, images '
                                                     'metadata, coverage reports) for later '
                                                     'jobs/humans',
                                                     'Replace git remotes',
                                                     'Bypass code review',
                                                     'Disable health checks'],
                                         'answer': 'A',
                                         'explain': 'Artifacts pass outputs between jobs or retain '
                                                    'reports.'},
                                        {'lo': 4,
                                         'q': 'What is a health check for in deployment?',
                                         'choices': ['A cosmetic README badge only',
                                                     'Letting the platform know whether the new '
                                                     'instance is ready to receive traffic',
                                                     'Deleting the database nightly',
                                                     'Formatting source files'],
                                         'answer': 'B',
                                         'explain': 'Health checks gate traffic until the service '
                                                    'is actually ready.'},
                                        {'lo': 4,
                                         'q': 'Before a migration that might fail in production, '
                                              'you should have…',
                                         'choices': ['No plan',
                                                     'A tested forward path and a '
                                                     'rollback/mitigation plan',
                                                     'Only a screenshot of local success',
                                                     'Force-push to main during peak traffic'],
                                         'answer': 'B',
                                         'explain': 'Safe deploys pair migrations with rollback '
                                                    'thinking.'},
                                        {'lo': 4,
                                         'q': 'A bad deploy is live. What does a rollback plan '
                                              'enable?',
                                         'choices': ['Faster return to a known-good version while '
                                                     'you diagnose',
                                                     'Permanent data corruption as a feature',
                                                     'Skipping blameless review forever',
                                                     'Turning off monitoring'],
                                         'answer': 'A',
                                         'explain': 'Rollback limits user impact when a release is '
                                                    'bad.'},
                                        {'lo': 2,
                                         'q': 'Why run the same container image in CI tests and '
                                              'staging when possible?',
                                         'choices': ['To maximize environment drift',
                                                     'To test what you actually ship',
                                                     'Because registries reject tags',
                                                     'To avoid writing Dockerfiles with any base '
                                                     'image'],
                                         'answer': 'B',
                                         'explain': 'Testing the shippable artifact catches '
                                                    'packaging mistakes early.'}]},
 'core-concepts': {'title': 'Core Concepts',
                   'outcomes': ['Model data idiomatically with clear types and boundaries.',
                                'Handle errors in a way that is debuggable and safe for callers.',
                                'Design modules that are testable without hidden global state.'],
                   'questions': [{'lo': 1,
                                  'q': 'Why prefer clear data models/types at module boundaries?',
                                  'choices': ['To make invalid states harder and intent obvious to '
                                              'callers',
                                              'Because maps/dicts are illegal',
                                              'To slow imports on purpose',
                                              'To avoid writing tests'],
                                  'answer': 'A',
                                  'explain': 'Idiomatic modeling documents contracts and catches '
                                             'mistakes earlier.'},
                                 {'lo': 2,
                                  'q': 'Which error-handling approach is usually better for '
                                       'libraries?',
                                  'choices': ['Swallow all exceptions and return `None` silently',
                                              'Raise specific errors (or return structured '
                                              'results) that callers can handle',
                                              'Call `sys.exit` on every validation failure',
                                              'Print secrets into logs when failing'],
                                  'answer': 'B',
                                  'explain': 'Callers need actionable, specific failure modes — '
                                             'not silent `None` or process death.'},
                                 {'lo': 3,
                                  'q': 'Hidden global mutable state makes tests hard because…',
                                  'choices': ['Tests become order-dependent and hard to isolate',
                                              'The test runner cannot import modules',
                                              'Functions become pure automatically',
                                              'Types disappear'],
                                  'answer': 'A',
                                  'explain': 'Inject dependencies and keep modules pure/testable '
                                             'where possible.'},
                                 {'lo': 3,
                                  'q': 'Which design is easier to unit test?',
                                  'choices': ['A function that reads a hard-coded production '
                                              'database URL from a global',
                                              'A function that accepts a repository/connection as '
                                              'a parameter',
                                              'A module that writes files to random paths with no '
                                              'seams',
                                              'Code that only runs inside a hidden import side '
                                              'effect'],
                                  'answer': 'B',
                                  'explain': 'Dependency injection creates a seam for fakes/fakes '
                                             'doubles in tests.'},
                                 {'lo': 1,
                                  'q': 'Using a typed model / schema object for an API payload '
                                       'mainly helps by…',
                                  'choices': ['Documenting fields and validating shape early',
                                              'Removing the need for HTTP status codes',
                                              'Replacing authentication',
                                              'Making Big-O irrelevant'],
                                  'answer': 'A',
                                  'explain': 'Structured models clarify and enforce the data '
                                             'contract.'},
                                 {'lo': 2,
                                  'q': 'When logging an error, you should avoid…',
                                  'choices': ['Including a request ID',
                                              'Including secrets or raw passwords',
                                              'Including the error type',
                                              'Including a short human message'],
                                  'answer': 'B',
                                  'explain': 'Debuggability must not leak secrets.'},
                                 {'lo': 3,
                                  'q': 'A module imports and mutates a process-wide cache at '
                                       'import time. Risk?',
                                  'choices': ['Easier parallel testing',
                                              'Surprising side effects and brittle tests',
                                              'Guaranteed purity',
                                              'Automatic rollbacks'],
                                  'answer': 'B',
                                  'explain': 'Import-time side effects hurt testability and '
                                             'predictability.'},
                                 {'lo': 1,
                                  'q': '“Make invalid states unrepresentable” is closest to which '
                                       'practice?',
                                  'choices': ['Using types/models so illegal combinations cannot '
                                              'be constructed easily',
                                              'Storing everything as untyped `Any` blobs',
                                              'Parsing JSON with `eval`',
                                              'Skipping validation because the UI is trusted'],
                                  'answer': 'A',
                                  'explain': 'Good models encode legal states in the type/shape '
                                             'itself.'},
                                 {'lo': 2,
                                  'q': 'A caller must distinguish “not found” from “permission '
                                       'denied.” What should your API/module do?',
                                  'choices': ['Use one generic `Exception` with no details',
                                              'Signal distinct error types/codes for each case',
                                              'Return `False` for both',
                                              'Exit the process'],
                                  'answer': 'B',
                                  'explain': 'Distinct errors let callers branch correctly.'},
                                 {'lo': 3,
                                  'q': 'Why keep “pure” logic separate from I/O in a module?',
                                  'choices': ['So business rules can be unit-tested without a '
                                              'database or network',
                                              'Because I/O is illegal in all languages',
                                              'To prevent using functions',
                                              'To force all code into one file'],
                                  'answer': 'A',
                                  'explain': 'Separating pure logic from I/O is core testable '
                                             'design.'}]}}

ADVANCED = {'01-system-design-foundations': {'title': 'System Design Foundations',
                                  'outcomes': ['Turn vague product goals into requirements, '
                                               'constraints, and rough capacity estimates.',
                                               'Choose caching, load balancing, and data '
                                               'partitioning approaches for a given load pattern.',
                                               'Apply CAP/consistency tradeoffs to pick a '
                                               'consistency model for a use case.',
                                               'Design async workflows with queues or streams when '
                                               'synchronous request paths are insufficient.'],
                                  'questions': [{'lo': 1,
                                                 'q': 'A stakeholder says “make it scale.” What '
                                                      'should you produce first?',
                                                 'choices': ['A production deploy with no written '
                                                             'constraints',
                                                             'Measurable requirements, hard '
                                                             'constraints, and rough capacity '
                                                             'estimates',
                                                             'A choice of logo colors',
                                                             'Only a list of frameworks you like'],
                                                 'answer': 'B',
                                                 'explain': 'Requirements and estimates bound the '
                                                            'design; “scale” alone is not a design '
                                                            'input.'},
                                                {'lo': 1,
                                                 'q': 'Which estimate is most useful early in a '
                                                      'design?',
                                                 'choices': ['Exact microsecond latency of every '
                                                             'function',
                                                             'Order-of-magnitude QPS, storage, and '
                                                             'payload size',
                                                             'The CEO’s favorite database brand',
                                                             'How many linters the repo has'],
                                                 'answer': 'B',
                                                 'explain': 'Rough capacity estimates drive '
                                                            'caching, sharding, and hardware '
                                                            'choices.'},
                                                {'lo': 2,
                                                 'q': 'Read-heavy traffic with mostly identical '
                                                      'responses. First lever?',
                                                 'choices': ['Replicate writes to every client '
                                                             'browser',
                                                             'A cache in front of the origin with '
                                                             'a clear TTL/invalidation story',
                                                             'Disable the load balancer',
                                                             'Store everything in one giant '
                                                             'unsorted file'],
                                                 'answer': 'B',
                                                 'explain': 'Caching cuts origin load for hot '
                                                            'reads when invalidation is planned.'},
                                                {'lo': 2,
                                                 'q': 'Why partition (shard) a growing dataset?',
                                                 'choices': ['To make CAP irrelevant',
                                                             'To keep each node’s data and query '
                                                             'load within capacity',
                                                             'Because load balancers cannot '
                                                             'distribute connections',
                                                             'To avoid writing indexes forever'],
                                                 'answer': 'B',
                                                 'explain': 'Partitions spread data and load; they '
                                                            'also add operational complexity.'},
                                                {'lo': 3,
                                                 'q': 'CAP “partition tolerance” in practice '
                                                      'means…',
                                                 'choices': ['You never need retries',
                                                             'The system keeps operating despite '
                                                             'network splits between nodes',
                                                             'All writes are free',
                                                             'Caches never expire'],
                                                 'answer': 'B',
                                                 'explain': 'Real distributed systems must '
                                                            'tolerate partitions; you then trade C '
                                                            'vs A.'},
                                                {'lo': 3,
                                                 'q': 'A bank ledger needs strong correctness '
                                                      'across accounts. Prefer…',
                                                 'choices': ['Eventual consistency with no '
                                                             'conflict handling',
                                                             'Strong consistency (or ACID '
                                                             'transactions) for money movement',
                                                             'Best-effort UDP without acks',
                                                             'Client-side-only validation'],
                                                 'answer': 'B',
                                                 'explain': 'Financial correctness usually needs '
                                                            'strong consistency, not pure '
                                                            'eventual.'},
                                                {'lo': 4,
                                                 'q': 'When are queues/streams a better fit than '
                                                      'sync request/response?',
                                                 'choices': ['For every static CSS file',
                                                             'When work is bursty, long-running, '
                                                             'or must fan out asynchronously',
                                                             'When you want to avoid all '
                                                             'observability',
                                                             'When CAP says consistency is free'],
                                                 'answer': 'B',
                                                 'explain': 'Async pipelines absorb spikes and '
                                                            'decouple producers from slow '
                                                            'consumers.'},
                                                {'lo': 4,
                                                 'q': 'A stream consumer crashes mid-batch. What '
                                                      'design concern appears?',
                                                 'choices': ['Only CSS theming',
                                                             'At-least-once delivery and '
                                                             'idempotent processing',
                                                             'Whether OpenAPI fonts are pretty',
                                                             'Deleting the partition key forever'],
                                                 'answer': 'B',
                                                 'explain': 'Async systems retry; handlers must '
                                                            'tolerate duplicates.'},
                                                {'lo': 2,
                                                 'q': 'A load balancer’s primary job is to…',
                                                 'choices': ['Encrypt backups by itself',
                                                             'Distribute traffic across healthy '
                                                             'instances',
                                                             'Replace the database schema',
                                                             'Write ADRs automatically'],
                                                 'answer': 'B',
                                                 'explain': 'LBs spread load and route away from '
                                                            'unhealthy nodes.'},
                                                {'lo': 1,
                                                 'q': 'Which constraint most changes a chatty '
                                                      'mobile API design?',
                                                 'choices': ['The office snack budget',
                                                             'Bandwidth, battery, and high latency '
                                                             'on poor networks',
                                                             'Whether CI uses matrices',
                                                             'The number of README badges'],
                                                 'answer': 'B',
                                                 'explain': 'Mobile constraints push toward fewer '
                                                            'round-trips and smaller payloads.'}]},
 '02-architecture-patterns': {'title': 'Architecture Patterns',
                              'outcomes': ['Compare layered, hexagonal, and clean architecture and '
                                           'place dependencies correctly.',
                                           'Model domain concepts with entities, value objects, '
                                           'and aggregates.',
                                           'Design event-driven flows and sagas for multi-step '
                                           'business processes.',
                                           'Decide when CQRS helps — and when it adds unjustified '
                                           'complexity.'],
                              'questions': [{'lo': 1,
                                             'q': 'In hexagonal architecture, domain logic should '
                                                  'depend on…',
                                             'choices': ['Concrete HTTP frameworks and SQL drivers '
                                                         'directly',
                                                         'Ports (interfaces); adapters implement '
                                                         'infrastructure outside',
                                                         'Global mutable singletons only',
                                                         'The presentation layer’s CSS'],
                                             'answer': 'B',
                                             'explain': 'Ports/adapters keep the domain '
                                                        'independent of frameworks.'},
                                            {'lo': 1,
                                             'q': 'Layered architecture usually forbids…',
                                             'choices': ['Having a UI at all',
                                                         'Lower layers depending upward on '
                                                         'UI/controllers',
                                                         'Using a database',
                                                         'Writing tests'],
                                             'answer': 'B',
                                             'explain': 'Dependencies should point '
                                                        'inward/downward, not from domain to UI.'},
                                            {'lo': 2,
                                             'q': 'A money amount with currency is best modeled '
                                                  'as…',
                                             'choices': ['Two unrelated ints with no rules',
                                                         'A value object enforcing valid '
                                                         'combinations',
                                                         'A UI color picker',
                                                         'A thread ID'],
                                             'answer': 'B',
                                             'explain': 'Value objects capture immutable domain '
                                                        'rules without identity.'},
                                            {'lo': 2,
                                             'q': 'An aggregate boundary mainly protects…',
                                             'choices': ['CSS specificity',
                                                         'Consistency of a cluster of entities '
                                                         'updated together',
                                                         'DNS TTLs',
                                                         'Lint rule names'],
                                             'answer': 'B',
                                             'explain': 'Aggregates define transactional '
                                                        'consistency boundaries in DDD.'},
                                            {'lo': 3,
                                             'q': 'A saga is useful when…',
                                             'choices': ['A single local ACID transaction covers '
                                                         'the whole business process',
                                                         'A long process spans services and needs '
                                                         'compensating steps on failure',
                                                         'You only render static HTML',
                                                         'You want to avoid all failure handling'],
                                             'answer': 'B',
                                             'explain': 'Sagas coordinate distributed steps with '
                                                        'compensations, not one giant DB TX.'},
                                            {'lo': 3,
                                             'q': 'Event-driven design primarily helps by…',
                                             'choices': ['Deleting all APIs',
                                                         'Decoupling producers from consumers via '
                                                         'facts that happened',
                                                         'Guaranteeing exactly-once everywhere for '
                                                         'free',
                                                         'Removing the need for schemas'],
                                             'answer': 'B',
                                             'explain': 'Events decouple; delivery semantics still '
                                                        'need careful design.'},
                                            {'lo': 4,
                                             'q': 'CQRS is often overkill when…',
                                             'choices': ['Read and write models are simple and '
                                                         'change together',
                                                         'You already have extreme read/write '
                                                         'asymmetry and scaling pain',
                                                         'You need separate optimized projections '
                                                         'proven by load',
                                                         'Audit projections are a hard '
                                                         'requirement'],
                                             'answer': 'A',
                                             'explain': 'CQRS adds dual models/complexity; use it '
                                                        'when asymmetry justifies it.'},
                                            {'lo': 4,
                                             'q': 'A team adopts CQRS “for purity” on a CRUD admin '
                                                  'tool. Risk?',
                                             'choices': ['Too little ceremony',
                                                         'Extra moving parts without a '
                                                         'scaling/consistency payoff',
                                                         'Automatic CAP compliance',
                                                         'Free idempotency'],
                                             'answer': 'B',
                                             'explain': 'Patterns must earn their complexity '
                                                        'against real constraints.'},
                                            {'lo': 1,
                                             'q': 'Clean architecture’s dependency rule says '
                                                  'source code dependencies point…',
                                             'choices': ['Outward toward frameworks',
                                                         'Inward toward enterprise/domain policy',
                                                         'Only sideways between random packages',
                                                         'Nowhere — cycles are encouraged'],
                                             'answer': 'B',
                                             'explain': 'Inner policy must not depend on outer '
                                                        'details.'},
                                            {'lo': 2,
                                             'q': 'Two entities that must stay consistent in one '
                                                  'transaction likely belong…',
                                             'choices': ['In separate aggregates with no '
                                                         'coordination',
                                                         'In the same aggregate (or a carefully '
                                                         'designed process)',
                                                         'Only in the CDN',
                                                         'In client localStorage exclusively'],
                                             'answer': 'B',
                                             'explain': 'Aggregate design follows consistency '
                                                        'needs.'}]},
 '03-concurrency-and-async': {'title': 'Concurrency and Async',
                              'outcomes': ['Identify race conditions and choose safe '
                                           'synchronization or ownership patterns.',
                                           'Apply backpressure with bounded queues so producers '
                                           'cannot overwhelm consumers.',
                                           'Use timeouts, cancellation, and structured concurrency '
                                           'to bound work lifetimes.',
                                           'Design for at-least-once delivery and idempotent '
                                           'handlers — not mythical exactly-once.'],
                              'questions': [{'lo': 1,
                                             'q': 'Two threads increment the same counter without '
                                                  'synchronization. Result?',
                                             'choices': ['Always perfectly accurate counts',
                                                         'A race: lost updates are possible',
                                                         'Automatic database indexing',
                                                         'CAP becoming irrelevant'],
                                             'answer': 'B',
                                             'explain': 'Unsycned shared mutable state races; use '
                                                        'atomics/locks/ownership.'},
                                            {'lo': 1,
                                             'q': 'Which approach often prevents races better than '
                                                  'sprinkling locks everywhere?',
                                             'choices': ['Sharing more mutable globals',
                                                         'Owning data per task/actor and '
                                                         'communicating by messages',
                                                         'Disabling tests',
                                                         'Sleeping randomly longer'],
                                             'answer': 'B',
                                             'explain': 'Isolation/ownership removes '
                                                        'shared-mutation races at the design '
                                                        'level.'},
                                            {'lo': 2,
                                             'q': 'An unbounded in-memory queue under load '
                                                  'typically causes…',
                                             'choices': ['Perfect backpressure',
                                                         'Memory growth and eventual collapse',
                                                         'Faster GC forever',
                                                         'Stronger consistency'],
                                             'answer': 'B',
                                             'explain': 'Bound queues; apply backpressure or '
                                                        'drop/shed load deliberately.'},
                                            {'lo': 2,
                                             'q': 'Backpressure means…',
                                             'choices': ['Producers keep sending at full speed no '
                                                         'matter what',
                                                         'Consumers/signals slow or block '
                                                         'producers when buffers fill',
                                                         'Deleting metrics',
                                                         'Turning off timeouts'],
                                             'answer': 'B',
                                             'explain': 'Backpressure protects the system by '
                                                        'limiting in-flight work.'},
                                            {'lo': 3,
                                             'q': 'Why set timeouts on outbound calls?',
                                             'choices': ['To guarantee success',
                                                         'To bound wait time when dependencies '
                                                         'hang',
                                                         'Because retries are illegal',
                                                         'To increase cardinality of every metric'],
                                             'answer': 'B',
                                             'explain': 'Timeouts stop hung dependencies from '
                                                        'holding resources forever.'},
                                            {'lo': 3,
                                             'q': 'Structured concurrency encourages…',
                                             'choices': ['Fire-and-forget tasks with no parent '
                                                         'ownership',
                                                         'Parent scopes that cancel/wait for child '
                                                         'tasks cleanly',
                                                         'Ignoring cancellation forever',
                                                         'Sharing one global mutable list for all '
                                                         'jobs'],
                                             'answer': 'B',
                                             'explain': 'Parents own lifetimes so cancellation and '
                                                        'errors propagate predictably.'},
                                            {'lo': 4,
                                             'q': '“Exactly-once delivery” across unreliable '
                                                  'networks is…',
                                             'choices': ['Trivial if you enable a checkbox',
                                                         'Effectively achieved via idempotent '
                                                         'processing of at-least-once deliveries',
                                                         'Guaranteed by UDP',
                                                         'Unnecessary if you use JSON'],
                                             'answer': 'B',
                                             'explain': 'Networks duplicate; make handlers '
                                                        'idempotent and dedupe.'},
                                            {'lo': 4,
                                             'q': 'An idempotency key on a payment create endpoint '
                                                  'helps when…',
                                             'choices': ['The client retries after a timeout and '
                                                         'might double-charge',
                                                         'You want to skip AuthZ',
                                                         'Caches should never expire',
                                                         'You delete audit logs'],
                                             'answer': 'A',
                                             'explain': 'Retries + side effects need dedupe via '
                                                        'idempotency keys.'},
                                            {'lo': 2,
                                             'q': 'A worker pool of size N with a bounded queue of '
                                                  'size M is full. A good policy is…',
                                             'choices': ['Allocate infinite threads silently',
                                                         'Reject, block, or shed load with a clear '
                                                         'signal',
                                                         'Drop ACLs',
                                                         'Disable health checks'],
                                             'answer': 'B',
                                             'explain': 'Saturation needs an explicit policy — not '
                                                        'unbounded growth.'},
                                            {'lo': 3,
                                             'q': 'A cancelled request should ideally…',
                                             'choices': ['Keep running forever consuming CPU/DB',
                                                         'Propagate cancellation so downstream '
                                                         'work stops promptly',
                                                         'Delete the database schema',
                                                         'Raise cardinality of user-id labels'],
                                             'answer': 'B',
                                             'explain': 'Cancellation frees resources and protects '
                                                        'dependencies.'}]},
 '04-performance-and-profiling': {'title': 'Performance and Profiling',
                                  'outcomes': ['Establish performance baselines before changing '
                                               'code.',
                                               'Run load tests and locate bottlenecks with '
                                               'evidence.',
                                               'Tune databases using indexes, query plans, and '
                                               'lock analysis.',
                                               'Choose cache invalidation strategies that match '
                                               'correctness needs.'],
                                  'questions': [{'lo': 1,
                                                 'q': 'Why capture a baseline before optimizing?',
                                                 'choices': ['So you can claim victory without '
                                                             'numbers',
                                                             'To know whether a change actually '
                                                             'improved latency/throughput',
                                                             'Baselines are illegal in production',
                                                             'To avoid writing tests'],
                                                 'answer': 'B',
                                                 'explain': 'Without a baseline you cannot prove '
                                                            'improvement.'},
                                                {'lo': 1,
                                                 'q': 'A good baseline includes…',
                                                 'choices': ['Only vibes from code review',
                                                             'Workload definition plus measured '
                                                             'latency/error/resource metrics',
                                                             'A single untimed run on a laptop '
                                                             'during a meeting',
                                                             'Disabling monitoring'],
                                                 'answer': 'B',
                                                 'explain': 'Baselines need a defined load and '
                                                            'recorded metrics.'},
                                                {'lo': 2,
                                                 'q': 'Load testing primarily answers…',
                                                 'choices': ['Whether the logo is centered',
                                                             'How the system behaves under '
                                                             'target/peak concurrency and data '
                                                             'size',
                                                             'Whether CAP is solved',
                                                             'Whether commits explain why'],
                                                 'answer': 'B',
                                                 'explain': 'Load tests reveal bottlenecks under '
                                                            'realistic pressure.'},
                                                {'lo': 2,
                                                 'q': 'CPU is idle but latency is high. Likely '
                                                      'bottleneck class?',
                                                 'choices': ['Always the sorting algorithm',
                                                             'I/O waits, locks, or external '
                                                             'dependencies',
                                                             'Too many unit tests',
                                                             'Missing README badges'],
                                                 'answer': 'B',
                                                 'explain': 'Idle CPU with high latency often '
                                                            'means waiting on I/O or locks.'},
                                                {'lo': 3,
                                                 'q': 'A slow filter on `user_id` with sequential '
                                                      'scans suggests…',
                                                 'choices': ['Deleting the WHERE clause',
                                                             'Adding/using an appropriate index '
                                                             'and verifying the plan',
                                                             'Buying a new laptop only',
                                                             'Caching the entire internet'],
                                                 'answer': 'B',
                                                 'explain': 'Indexes + plans are the primary DB '
                                                            'performance tools.'},
                                                {'lo': 3,
                                                 'q': 'Lock contention shows up as…',
                                                 'choices': ['Faster writes always',
                                                             'Sessions waiting on locks held by '
                                                             'other transactions',
                                                             'Free consistency',
                                                             'Lower cardinality metrics'],
                                                 'answer': 'B',
                                                 'explain': 'Contended locks serialize work and '
                                                            'inflate latency.'},
                                                {'lo': 4,
                                                 'q': 'Cache-aside with TTL mainly risks…',
                                                 'choices': ['Serving stale data until '
                                                             'TTL/invalidation',
                                                             'Never needing a database',
                                                             'Guaranteed linearizability',
                                                             'Automatic threat models'],
                                                 'answer': 'A',
                                                 'explain': 'TTLs trade freshness for simplicity; '
                                                            'invalidate when correctness demands.'},
                                                {'lo': 4,
                                                 'q': 'Write-through caching means…',
                                                 'choices': ['Writes update cache and store '
                                                             'together (sync path)',
                                                             'Never writing to the store',
                                                             'Only invalidating on Fridays',
                                                             'Deleting keys randomly for fun'],
                                                 'answer': 'A',
                                                 'explain': 'Write-through keeps cache warmer at '
                                                            'the cost of write latency.'},
                                                {'lo': 2,
                                                 'q': 'You found a hotspot function via profiler. '
                                                      'Next step?',
                                                 'choices': ['Rewrite the whole monorepo',
                                                             'Optimize that hotspot and re-measure '
                                                             'against the baseline',
                                                             'Disable the profiler forever',
                                                             'Add random sleeps'],
                                                 'answer': 'B',
                                                 'explain': 'Measure → change → re-measure the '
                                                            'same scenario.'},
                                                {'lo': 1,
                                                 'q': 'Micro-optimizing before profiling is risky '
                                                      'because…',
                                                 'choices': ['Profilers always lie',
                                                             'You may optimize the wrong place '
                                                             'while the real hotspot remains',
                                                             'Baselines forbid improvements',
                                                             'Load tests are illegal'],
                                                 'answer': 'B',
                                                 'explain': 'Evidence first; intuition about '
                                                            'hotspots is often wrong.'}]},
 '05-reliability-and-resilience': {'title': 'Reliability and Resilience',
                                   'outcomes': ['Configure retries with timeouts, budgets, and '
                                                'jitter for transient faults.',
                                                'Apply circuit breakers, bulkheads, and rate '
                                                'limits to contain failures.',
                                                'Use idempotency keys and dedupe to make retried '
                                                'writes safe.',
                                                'Write and follow runbooks for common incident '
                                                'classes.'],
                                   'questions': [{'lo': 1,
                                                  'q': 'Retrying immediately forever without '
                                                       'jitter tends to…',
                                                  'choices': ['Heal dependencies gently',
                                                              'Create synchronized retry storms '
                                                              'that worsen outages',
                                                              'Guarantee exactly-once',
                                                              'Reduce error budgets automatically'],
                                                  'answer': 'B',
                                                  'explain': 'Backoff + jitter spreads retries; '
                                                             'budgets cap total attempts.'},
                                                 {'lo': 1,
                                                  'q': 'A timeout without a retry budget means…',
                                                  'choices': ['You may still hammer a sick '
                                                              'dependency indefinitely via client '
                                                              'loops',
                                                              'Reliability is solved',
                                                              'CAP is fixed',
                                                              'Caches never expire'],
                                                  'answer': 'A',
                                                  'explain': 'Pair timeouts with limited retries '
                                                             'and overall deadlines.'},
                                                 {'lo': 2,
                                                  'q': 'A circuit breaker opens when…',
                                                  'choices': ['Error rates/latency cross a '
                                                              'threshold, failing fast instead of '
                                                              'calling the dependency',
                                                              'The logo changes',
                                                              'CI is green',
                                                              'A single log line appears'],
                                                  'answer': 'A',
                                                  'explain': 'Open circuits shed load from '
                                                             'unhealthy dependencies.'},
                                                 {'lo': 2,
                                                  'q': 'Bulkheads help by…',
                                                  'choices': ['Sharing one thread pool for all '
                                                              'workloads',
                                                              'Isolating resources so one failure '
                                                              'domain cannot exhaust another',
                                                              'Removing rate limits',
                                                              'Disabling AuthZ'],
                                                  'answer': 'B',
                                                  'explain': 'Bulkheads compartmentalize blast '
                                                             'radius.'},
                                                 {'lo': 3,
                                                  'q': 'Idempotency keys are most critical for…',
                                                  'choices': ['Read-only GETs with no side effects',
                                                              'Create/payment operations that '
                                                              'clients may retry',
                                                              'Static asset caching only',
                                                              'Choosing font families'],
                                                  'answer': 'B',
                                                  'explain': 'Retried side-effecting writes need '
                                                             'dedupe.'},
                                                 {'lo': 3,
                                                  'q': 'Deduping consumer messages by event ID '
                                                       'prevents…',
                                                  'choices': ['All network partitions',
                                                              'Double-applying the same business '
                                                              'effect after redelivery',
                                                              'The need for schemas',
                                                              'On-call rotations'],
                                                  'answer': 'B',
                                                  'explain': 'At-least-once delivery + dedupe ≈ '
                                                             'safe processing.'},
                                                 {'lo': 4,
                                                  'q': 'A runbook should primarily contain…',
                                                  'choices': ['Only motivational quotes',
                                                              'Detection signals, mitigation '
                                                              'steps, owners, and escalation paths',
                                                              'Unrelated architecture trivia',
                                                              'Passwords in plaintext'],
                                                  'answer': 'B',
                                                  'explain': 'Runbooks make incidents executable '
                                                             'under pressure.'},
                                                 {'lo': 4,
                                                  'q': 'During an incident, the first reliability '
                                                       'move is often…',
                                                  'choices': ['Rewrite the platform',
                                                              'Mitigate user impact (rollback, '
                                                              'feature flag, degrade) then '
                                                              'diagnose',
                                                              'Delete metrics',
                                                              'Disable communication'],
                                                  'answer': 'B',
                                                  'explain': 'Stop the bleeding, then find root '
                                                             'cause.'},
                                                 {'lo': 2,
                                                  'q': 'Rate limiting a dependency client '
                                                       'protects…',
                                                  'choices': ['Only the marketing site fonts',
                                                              'Both your service and the '
                                                              'dependency from overload',
                                                              'Nothing if retries exist',
                                                              'Only disk encryption'],
                                                  'answer': 'B',
                                                  'explain': 'Client-side limits are part of being '
                                                             'a good citizen under stress.'},
                                                 {'lo': 1,
                                                  'q': 'Which retry policy is safest for '
                                                       'non-idempotent POSTs without keys?',
                                                  'choices': ['Blind unlimited retries',
                                                              'Fail clearly / get an idempotency '
                                                              'key before retrying side effects',
                                                              'Retry every microsecond',
                                                              'Retry only on 200 OK'],
                                                  'answer': 'B',
                                                  'explain': 'Do not blindly retry unsafe side '
                                                             'effects.'}]},
 '06-security-advanced': {'title': 'Security (Advanced)',
                          'outcomes': ['Threat-model a feature including abuse cases and '
                                       'prioritised mitigations.',
                                       'Apply encryption at rest/in transit with sound key '
                                       'management.',
                                       'Enforce supply-chain controls for dependencies and build '
                                       'artifacts.',
                                       'Execute a hardening checklist covering auth, config, and '
                                       'security tests.'],
                          'questions': [{'lo': 1,
                                         'q': 'Threat modeling starts by…',
                                         'choices': ['Buying a bigger WAF only',
                                                     'Listing assets, entry points, threats, and '
                                                     'mitigations for the feature',
                                                     'Disabling logs',
                                                     'Skipping AuthN'],
                                         'answer': 'B',
                                         'explain': 'Structured threat models drive prioritized '
                                                    'defenses.'},
                                        {'lo': 1,
                                         'q': 'An “abuse case” focuses on…',
                                         'choices': ['Happy-path UX copy',
                                                     'How a motivated attacker or abusive user '
                                                     'misuses the system',
                                                     'Only unit test names',
                                                     'CDN cache hit ratios'],
                                         'answer': 'B',
                                         'explain': 'Abuse cases complement functional '
                                                    'requirements.'},
                                        {'lo': 2,
                                         'q': 'TLS primarily protects…',
                                         'choices': ['Data in transit from eavesdropping/tampering',
                                                     'Disk sectors at rest by itself',
                                                     'Supply-chain commits',
                                                     'Error budgets'],
                                         'answer': 'A',
                                         'explain': 'In-transit encryption ≠ at-rest encryption.'},
                                        {'lo': 2,
                                         'q': 'Where should encryption keys live?',
                                         'choices': ['Committed next to source',
                                                     'In a managed KMS/HSM with rotation and '
                                                     'access control',
                                                     'In client-side JavaScript comments',
                                                     'In screenshots of the dashboard'],
                                         'answer': 'B',
                                         'explain': 'Key management is the hard part of '
                                                    'encryption.'},
                                        {'lo': 3,
                                         'q': 'Pinning dependency versions and verifying checksums '
                                              'helps against…',
                                         'choices': ['UI alignment bugs',
                                                     'Malicious or swapped packages in the supply '
                                                     'chain',
                                                     'Slow CSS',
                                                     'CAP tradeoffs'],
                                         'answer': 'B',
                                         'explain': 'Supply-chain controls reduce dependency '
                                                    'compromise risk.'},
                                        {'lo': 3,
                                         'q': 'A compromised build pipeline can…',
                                         'choices': ['Only affect documentation typos',
                                                     'Inject malicious artifacts into what you '
                                                     'ship',
                                                     'Improve SLO burn rates automatically',
                                                     'Replace threat models'],
                                         'answer': 'B',
                                         'explain': 'Protect CI/CD like production — it produces '
                                                    'production.'},
                                        {'lo': 4,
                                         'q': 'A hardening checklist should include…',
                                         'choices': ['Only choosing fonts',
                                                     'AuthZ reviews, secret hygiene, dependency '
                                                     'updates, and security test gates',
                                                     'Disabling HTTPS in prod',
                                                     'Sharing root credentials in chat'],
                                         'answer': 'B',
                                         'explain': 'Hardening is a repeatable checklist, not a '
                                                    'one-off slogan.'},
                                        {'lo': 4,
                                         'q': 'Security tests in CI are valuable because they…',
                                         'choices': ['Replace threat modeling forever',
                                                     'Catch regressions in injection, authz, and '
                                                     'dependency policy before release',
                                                     'Make retries unnecessary',
                                                     'Guarantee zero incidents'],
                                         'answer': 'B',
                                         'explain': 'Automate what you can; still model new '
                                                    'threats.'},
                                        {'lo': 1,
                                         'q': 'Prioritising mitigations should weigh…',
                                         'choices': ['Only how trendy the control is',
                                                     'Likelihood × impact and exploitability of '
                                                     'each threat',
                                                     'Whether the control uses purple gradients',
                                                     'Commit message length'],
                                         'answer': 'B',
                                         'explain': 'Risk-based prioritization beats checkbox '
                                                    'theater.'},
                                        {'lo': 2,
                                         'q': 'Encrypting a database volume but logging raw PAN '
                                              'data means…',
                                         'choices': ['You are fully safe',
                                                     'Sensitive data still leaks via another '
                                                     'channel',
                                                     'TLS is unnecessary',
                                                     'Keys can be public'],
                                         'answer': 'B',
                                         'explain': 'Encryption must cover actual sensitive data '
                                                    'paths end-to-end.'}]},
 '07-observability-and-slos': {'title': 'Observability and SLOs',
                               'outcomes': ['Define SLIs/SLOs and manage error budgets for a '
                                            'service.',
                                            'Apply RED/USE metrics while avoiding high-cardinality '
                                            'label explosions.',
                                            'Propagate trace context across services to diagnose '
                                            'latency.',
                                            'Design alerts that are actionable and kind to '
                                            'on-call.'],
                               'questions': [{'lo': 1,
                                              'q': 'An SLI is…',
                                              'choices': ['A motivational poster',
                                                          'A quantitative measure of user-visible '
                                                          'reliability (e.g., success rate)',
                                                          'A CSS variable',
                                                          'A git branch name'],
                                              'answer': 'B',
                                              'explain': 'SLIs measure experience; SLOs set '
                                                         'targets on those measures.'},
                                             {'lo': 1,
                                              'q': 'An error budget is…',
                                              'choices': ['Unlimited downtime as a treat',
                                                          'Allowed unreliability derived from the '
                                                          'SLO before you must slow feature work',
                                                          'A caching TTL',
                                                          'A threat model section'],
                                              'answer': 'B',
                                              'explain': 'Budgets balance velocity vs '
                                                         'reliability.'},
                                             {'lo': 2,
                                              'q': 'RED metrics stand for…',
                                              'choices': ['Redact, Encrypt, Delete',
                                                          'Rate, Errors, Duration',
                                                          'Retry, Evict, Drop',
                                                          'Read, Edit, Deploy'],
                                              'answer': 'B',
                                              'explain': 'RED is a common request-centric metric '
                                                         'set.'},
                                             {'lo': 2,
                                              'q': 'High-cardinality labels (user_id on every '
                                                   'metric) typically cause…',
                                              'choices': ['Cheaper metrics forever',
                                                          'Metric store explosion and useless '
                                                          'dashboards',
                                                          'Stronger consistency',
                                                          'Free tracing'],
                                              'answer': 'B',
                                              'explain': 'Keep label cardinality bounded.'},
                                             {'lo': 3,
                                              'q': 'Trace context propagation lets you…',
                                              'choices': ['See one request across service spans',
                                                          'Delete logs forever',
                                                          'Skip SLOs',
                                                          'Avoid timeouts'],
                                              'answer': 'A',
                                              'explain': 'Propagation stitches spans into one '
                                                         'distributed trace.'},
                                             {'lo': 3,
                                              'q': 'A span without parent linkage in a deep call '
                                                   'chain usually means…',
                                              'choices': ['Perfect observability',
                                                          'Broken context propagation at a '
                                                          'boundary',
                                                          'CAP solved',
                                                          'Idempotency keys are wrong'],
                                              'answer': 'B',
                                              'explain': 'Missing parents break end-to-end latency '
                                                         'diagnosis.'},
                                             {'lo': 4,
                                              'q': 'A good alert is…',
                                              'choices': ['Triggered by every DEBUG log line',
                                                          'Tied to user impact / SLO burn and '
                                                          'actionable for humans',
                                                          'Emailed hourly with no owner',
                                                          'Only a Slack emoji'],
                                              'answer': 'B',
                                              'explain': 'Alert on symptoms that need human '
                                                         'action.'},
                                             {'lo': 4,
                                              'q': 'Pager fatigue usually comes from…',
                                              'choices': ['Too few actionable alerts',
                                                          'Noisy, non-actionable alerts that train '
                                                          'people to ignore pages',
                                                          'Perfect SLOs',
                                                          'Too much tracing context'],
                                              'answer': 'B',
                                              'explain': 'Hygiene: fewer, better alerts.'},
                                             {'lo': 1,
                                              'q': 'Burning the error budget quickly should '
                                                   'trigger…',
                                              'choices': ['Ignoring reliability work',
                                                          'Prioritizing reliability fixes over '
                                                          'risky feature launches',
                                                          'Deleting SLIs',
                                                          'Disabling canaries forever'],
                                              'answer': 'B',
                                              'explain': 'Budgets are decision tools, not vanity '
                                                         'charts.'},
                                             {'lo': 2,
                                              'q': 'USE metrics focus on…',
                                              'choices': ['Utilization, Saturation, Errors for '
                                                          'resources',
                                                          'Only user-facing request rates',
                                                          'Unrelated marketing KPIs',
                                                          'Git blame'],
                                              'answer': 'A',
                                              'explain': 'USE complements RED for resource-centric '
                                                         'views.'}]},
 '08-ci-cd-and-release-strategies': {'title': 'CI/CD and Release Strategies',
                                     'outcomes': ['Choose canary, blue-green, or rolling releases '
                                                  'for a risk profile.',
                                                  'Use feature flags and safe config changes to '
                                                  'control exposure.',
                                                  'Plan production database migrations that avoid '
                                                  'downtime and lockouts.',
                                                  'Execute rollbacks with clear versioning and '
                                                  'changelogs.'],
                                     'questions': [{'lo': 1,
                                                    'q': 'A canary release primarily…',
                                                    'choices': ['Ships to 100% instantly',
                                                                'Exposes a new version to a small '
                                                                'slice of traffic first',
                                                                'Deletes the old version '
                                                                'immediately',
                                                                'Skips health checks'],
                                                    'answer': 'B',
                                                    'explain': 'Canaries limit blast radius while '
                                                               'you watch metrics.'},
                                                   {'lo': 1,
                                                    'q': 'Blue-green deployment keeps…',
                                                    'choices': ['Two environments so you can '
                                                                'switch traffic atomically and '
                                                                'roll back fast',
                                                                'No way to roll back',
                                                                'Only canary pods forever',
                                                                'Secrets in the image'],
                                                    'answer': 'A',
                                                    'explain': 'Blue-green trades cost for fast '
                                                               'switch/rollback.'},
                                                   {'lo': 2,
                                                    'q': 'Feature flags help you…',
                                                    'choices': ['Avoid all testing',
                                                                'Decouple deploy from release and '
                                                                'kill-switch bad behavior',
                                                                'Skip AuthZ',
                                                                'Ignore migrations'],
                                                    'answer': 'B',
                                                    'explain': 'Flags control exposure without '
                                                               'redeploying binaries every time.'},
                                                   {'lo': 2,
                                                    'q': 'A risky config change should be…',
                                                    'choices': ['Pushed globally with no kill '
                                                                'switch',
                                                                'Rolled out gradually with '
                                                                'monitoring and a fast revert path',
                                                                'Stored only in chat history',
                                                                'Applied by editing production DB '
                                                                'by hand mid-flight'],
                                                    'answer': 'B',
                                                    'explain': 'Treat config like code: staged, '
                                                               'observable, reversible.'},
                                                   {'lo': 3,
                                                    'q': 'Expand/contract migrations reduce risk '
                                                         'by…',
                                                    'choices': ['Dropping columns in the same '
                                                                'deploy that removes all readers',
                                                                'Adding new schema first, '
                                                                'dual-writing/reading, then '
                                                                'removing old later',
                                                                'Rewriting applied migration files '
                                                                'in place',
                                                                'Skipping backups'],
                                                    'answer': 'B',
                                                    'explain': 'Online migrations are multi-phase '
                                                               'and backwards compatible.'},
                                                   {'lo': 3,
                                                    'q': 'Taking a long ACCESS EXCLUSIVE lock on a '
                                                         'hot table during peak…',
                                                    'choices': ['Is ideal for UX',
                                                                'Can stall writes/reads and cause '
                                                                'an outage',
                                                                'Improves canaries',
                                                                'Replaces feature flags'],
                                                    'answer': 'B',
                                                    'explain': 'Plan locks and backfills carefully '
                                                               'in production.'},
                                                   {'lo': 4,
                                                    'q': 'A rollback plan needs…',
                                                    'choices': ['Hope',
                                                                'A known-good version, data '
                                                                'compatibility rules, and a '
                                                                'practiced switch',
                                                                'Deleting metrics first',
                                                                'Force-pushing secrets'],
                                                    'answer': 'B',
                                                    'explain': 'Rollbacks fail when versions/data '
                                                               'are incompatible or unpracticed.'},
                                                   {'lo': 4,
                                                    'q': 'Changelogs/versioning help incidents by…',
                                                    'choices': ['Hiding what shipped',
                                                                'Making it obvious what changed '
                                                                'when symptoms started',
                                                                'Replacing monitoring',
                                                                'Guaranteeing zero bugs'],
                                                    'answer': 'B',
                                                    'explain': 'Version clarity speeds bisect and '
                                                               'rollback decisions.'},
                                                   {'lo': 1,
                                                    'q': 'Rolling deploys gradually replace '
                                                         'instances. Main risk to watch?',
                                                    'choices': ['Mixed versions briefly serving '
                                                                'traffic',
                                                                'Instant dual environments for '
                                                                'free',
                                                                'Automatic schema expand/contract',
                                                                'Feature flags becoming '
                                                                'unnecessary'],
                                                    'answer': 'A',
                                                    'explain': 'Ensure mixed-version compatibility '
                                                               'during the roll.'},
                                                   {'lo': 2,
                                                    'q': 'Turning a flag on for 5% of users is '
                                                         'similar in spirit to…',
                                                    'choices': ['A full blue-green cutover with no '
                                                                'metrics',
                                                                'A canary / progressive delivery '
                                                                'of a behavior',
                                                                'Deleting the old code path '
                                                                'immediately in DB',
                                                                'Skipping CI'],
                                                    'answer': 'B',
                                                    'explain': 'Flags enable progressive delivery '
                                                               'of features.'}]},
 'system-design': {'title': 'System Design',
                   'outcomes': ['Design a service for expected scale with explicit bottlenecks and '
                                'mitigations.',
                                'Document architecture tradeoffs and rejected alternatives '
                                'clearly.',
                                'Define verification (tests, load checks, or probes) that match '
                                'the design risks.'],
                   'questions': [{'lo': 1,
                                  'q': 'A scalable design doc should state…',
                                  'choices': ['Only the framework fashion of the week',
                                              'Expected load, bottlenecks, and how the design '
                                              'handles them',
                                              'No numbers at all',
                                              'Secrets in plaintext'],
                                  'answer': 'B',
                                  'explain': 'Scale claims need load assumptions and bottleneck '
                                             'thinking.'},
                                 {'lo': 1,
                                  'q': 'Vertical scaling alone becomes a problem when…',
                                  'choices': ['A single machine’s limits or cost ceiling are hit',
                                              'You add read replicas thoughtfully',
                                              'You cache hot keys',
                                              'You use a load balancer'],
                                  'answer': 'A',
                                  'explain': 'Eventually you need horizontal strategies.'},
                                 {'lo': 2,
                                  'q': 'Recording rejected alternatives in an ADR helps reviewers…',
                                  'choices': ['Re-litigate the same debates forever',
                                              'Understand why this option won given constraints',
                                              'Skip reading the design',
                                              'Avoid tests'],
                                  'answer': 'B',
                                  'explain': 'Tradeoff docs preserve decision rationale.'},
                                 {'lo': 2,
                                  'q': '“We picked eventual consistency” without saying why is '
                                       'weak because…',
                                  'choices': ['Eventual consistency is illegal',
                                              'Reviewers cannot judge fitness without constraints '
                                              'and failure modes',
                                              'CAP forbids documentation',
                                              'Queues cannot be mentioned'],
                                  'answer': 'B',
                                  'explain': 'Name the constraint that forced the tradeoff.'},
                                 {'lo': 3,
                                  'q': 'If the design hinges on a cache hit rate, verification '
                                       'should include…',
                                  'choices': ['Only a unit test of string concat',
                                              'A load or rehearsal that measures hit rate under '
                                              'realistic keys',
                                              'Deleting metrics',
                                              'A logo review'],
                                  'answer': 'B',
                                  'explain': 'Validate the risky assumptions, not only happy-path '
                                             'code.'},
                                 {'lo': 3,
                                  'q': 'A design that adds many new failure domains should plan…',
                                  'choices': ['No probes or alerts',
                                              'Health checks, SLOs, and failure drills for those '
                                              'domains',
                                              'Only manual SSH forever',
                                              'Skipping runbooks'],
                                  'answer': 'B',
                                  'explain': 'New complexity needs operable verification.'},
                                 {'lo': 1,
                                  'q': 'Sharding by user_id helps when…',
                                  'choices': ['Traffic and data grow beyond one node fairly evenly '
                                              'by user',
                                              'You never read data',
                                              'CAP is optional',
                                              'You want cross-shard transactions for free'],
                                  'answer': 'A',
                                  'explain': 'Key choice must match access patterns — cross-shard '
                                             'ops stay hard.'},
                                 {'lo': 2,
                                  'q': 'A good tradeoff write-up compares options on…',
                                  'choices': ['Only aesthetics',
                                              'Cost, complexity, consistency, and operability '
                                              'against requirements',
                                              'Twitter likes',
                                              'Variable names alone'],
                                  'answer': 'B',
                                  'explain': 'Tradeoffs are multi-dimensional against real '
                                             'constraints.'}]}}

AI_BEGINNER = {'01-ai-foundations': {'title': 'AI Foundations',
                       'outcomes': ['Translate a vague request into goal, constraints, and success '
                                    'criteria.',
                                    'Write a one-page task spec with inputs, outputs, and failure '
                                    'modes.',
                                    'Build a small eval set covering good, bad, and ambiguous '
                                    'cases.',
                                    'Add grounding/fallback rules and measure their effect on '
                                    'failures.',
                                    'Version prompt/spec changes with an iteration log.'],
                       'questions': [{'lo': 1,
                                      'q': 'A stakeholder says “summarize tickets better.” First '
                                           'deliverable?',
                                      'choices': ['Ship to all users with no criteria',
                                                  'A clear goal, constraints, and success criteria',
                                                  'A new model fine-tune immediately',
                                                  'Deleting the eval set'],
                                      'answer': 'B',
                                      'explain': 'Vague asks become buildable only after goals and '
                                                 'success criteria.'},
                                     {'lo': 1,
                                      'q': 'Success criteria should be…',
                                      'choices': ['Unmeasurable vibes',
                                                  'Observable checks you can score on examples',
                                                  'Hidden from the team',
                                                  'Only the model’s temperature'],
                                      'answer': 'B',
                                      'explain': 'If you cannot score it, you cannot iterate.'},
                                     {'lo': 2,
                                      'q': 'A solid task spec includes…',
                                      'choices': ['Only “be helpful”',
                                                  'Inputs, outputs, constraints, and do-not-do / '
                                                  'failure modes',
                                                  'Passwords for production',
                                                  'A random poem'],
                                      'answer': 'B',
                                      'explain': 'Specs make prompts repeatable across people and '
                                                 'runs.'},
                                     {'lo': 2,
                                      'q': 'Why list failure modes in the spec?',
                                      'choices': ['To scare stakeholders',
                                                  'So the system has planned behavior for '
                                                  'empty/ambiguous/sensitive input',
                                                  'Because models ignore constraints',
                                                  'To avoid evaluation'],
                                      'answer': 'B',
                                      'explain': 'Failure modes drive fallbacks and tests.'},
                                     {'lo': 3,
                                      'q': 'An eval set should include…',
                                      'choices': ['Only perfect happy paths',
                                                  'Good, bad, and ambiguous cases',
                                                  'One example total',
                                                  'Only adversarial jailbreaks with no normals'],
                                      'answer': 'B',
                                      'explain': 'Coverage of messiness finds regressions early.'},
                                     {'lo': 3,
                                      'q': 'Why keep a fixed eval set across iterations?',
                                      'choices': ['So scores are comparable over time',
                                                  'So you never improve',
                                                  'Because models forbid new cases',
                                                  'To skip documentation'],
                                      'answer': 'A',
                                      'explain': 'Comparable runs prove whether a change helped.'},
                                     {'lo': 4,
                                      'q': 'A grounding rule (“only use provided text”) mainly '
                                           'reduces…',
                                      'choices': ['Latency to zero',
                                                  'Invented facts not in the source',
                                                  'The need for any constraints',
                                                  'JSON validity issues only'],
                                      'answer': 'B',
                                      'explain': 'Grounding targets hallucination against the '
                                                 'given context.'},
                                     {'lo': 4,
                                      'q': 'Low-quality input with missing fields — good fallback?',
                                      'choices': ['Invent owners and deadlines confidently',
                                                  'Ask a clarifying question or return '
                                                  'insufficient-info',
                                                  'Crash the workflow',
                                                  'Ignore the policy'],
                                      'answer': 'B',
                                      'explain': 'Fallbacks beat confident fabrication.'},
                                     {'lo': 5,
                                      'q': 'An iteration log should record…',
                                      'choices': ['Nothing — memory is enough',
                                                  'What changed, scores, and what '
                                                  'improved/worsened',
                                                  'Only the final prompt forever',
                                                  'API keys'],
                                      'answer': 'B',
                                      'explain': 'Versioned notes make improvements explainable.'},
                                     {'lo': 5,
                                      'q': 'Changing prompt, temperature, and examples all at once '
                                           'is bad because…',
                                      'choices': ['It is faster to learn',
                                                  'You cannot tell which change caused the score '
                                                  'delta',
                                                  'Eval sets forbid it legally',
                                                  'Models reject single changes'],
                                      'answer': 'B',
                                      'explain': 'Isolate variables when iterating.'}]},
 '02-prompting-basics': {'title': 'Prompting Basics',
                         'outcomes': ['Write prompts with explicit constraints and output format.',
                                      'Separate instructions from user content with clear '
                                      'delimiters.',
                                      'Add few-shot examples that demonstrate the desired '
                                      'behavior.',
                                      'Handle missing info with clarify-or-refuse rules.',
                                      'Score outputs on format, factuality, and helpfulness.'],
                         'questions': [{'lo': 1,
                                        'q': '“Be helpful” alone is a weak prompt because…',
                                        'choices': ['Models hate help',
                                                    'It lacks constraints and a checkable output '
                                                    'shape',
                                                    'It is always too long',
                                                    'It forces JSON'],
                                        'answer': 'B',
                                        'explain': 'Constraints and format make behavior '
                                                   'repeatable.'},
                                       {'lo': 1,
                                        'q': 'Asking for bullet summaries with “no invented '
                                             'policies” is an example of…',
                                        'choices': ['Removing all constraints',
                                                    'An explicit behavioral constraint',
                                                    'A temperature setting',
                                                    'A vector index'],
                                        'answer': 'B',
                                        'explain': 'Constraints bound what the model may say.'},
                                       {'lo': 2,
                                        'q': 'Why delimit user content from instructions?',
                                        'choices': ['To confuse the model',
                                                    'To reduce instruction/data mix-ups and '
                                                    'injection success',
                                                    'Because Markdown is illegal',
                                                    'To hide the system prompt from logs forever'],
                                        'answer': 'B',
                                        'explain': 'Delimiters clarify what is data vs policy.'},
                                       {'lo': 2,
                                        'q': 'Putting untrusted ticket text in the same blob as '
                                             'rules without markers risks…',
                                        'choices': ['Perfect compliance',
                                                    'The model treating user text as new '
                                                    'instructions',
                                                    'Faster evals',
                                                    'Automatic citations'],
                                        'answer': 'B',
                                        'explain': 'Injection thrives when data and instructions '
                                                   'blur.'},
                                       {'lo': 3,
                                        'q': 'Few-shot examples help most when they…',
                                        'choices': ['Contradict the constraints',
                                                    'Show the exact format and edge-case handling '
                                                    'you want',
                                                    'Are unrelated poems',
                                                    'Include secrets'],
                                        'answer': 'B',
                                        'explain': 'Examples teach shape and judgment better than '
                                                   'adjectives.'},
                                       {'lo': 3,
                                        'q': 'Three short diverse examples usually beat…',
                                        'choices': ['One huge contradictory dump',
                                                    'No examples when format is tricky — wait, '
                                                    'actually examples still help',
                                                    'Clear constraints',
                                                    'An eval set'],
                                        'answer': 'A',
                                        'explain': 'Contradictory or bloated examples hide the '
                                                   'rule.'},
                                       {'lo': 4,
                                        'q': 'Notes missing an owner — preferred behavior?',
                                        'choices': ['Invent a plausible owner',
                                                    'Clarify or refuse per the rule',
                                                    'Skip the field silently in JSON as success',
                                                    'Delete the notes'],
                                        'answer': 'B',
                                        'explain': 'Clarify/refuse beats fabrication for missing '
                                                   'keys.'},
                                       {'lo': 4,
                                        'q': 'A negative test for prompting checks that…',
                                        'choices': ['Happy paths always pass',
                                                    'The model asks/refuses when required info is '
                                                    'absent',
                                                    'Temperature is 0',
                                                    'The CDN is warm'],
                                        'answer': 'B',
                                        'explain': 'Negative tests lock safe behavior.'},
                                       {'lo': 5,
                                        'q': 'A scorecard with format/factuality/helpfulness lets '
                                             'you…',
                                        'choices': ['Avoid measuring anything',
                                                    'Track regressions across prompt versions',
                                                    'Skip constraints',
                                                    'Guarantee zero hallucinations'],
                                        'answer': 'B',
                                        'explain': 'Multi-axis scores catch format wins that hurt '
                                                   'factuality.'},
                                       {'lo': 1,
                                        'q': 'Structured output requests (headings/JSON fields) '
                                             'mainly improve…',
                                        'choices': ['Random creativity',
                                                    'Downstream parsing and consistent evaluation',
                                                    'Model parameter count',
                                                    'Threat modeling'],
                                        'answer': 'B',
                                        'explain': 'Structure makes outputs usable and '
                                                   'testable.'}]},
 '03-prompt-patterns': {'title': 'Prompt Patterns',
                        'outcomes': ['Design extraction prompts that emit valid structured fields.',
                                     'Specify required-field checklists and missing-data behavior.',
                                     'Add a review/repair pass that fixes structure without '
                                     'inventing facts.',
                                     'Build an error taxonomy and track reductions across '
                                     'iterations.',
                                     'Cover tricky cases with targeted few-shot examples.'],
                        'questions': [{'lo': 1,
                                       'q': 'Extraction prompts should define…',
                                       'choices': ['Only tone of voice',
                                                   'Field names, types, and allowed empties',
                                                   'The cloud vendor',
                                                   'A canary percentage'],
                                       'answer': 'B',
                                       'explain': 'Schemas make extraction evaluable.'},
                                      {'lo': 1,
                                       'q': 'Free text → JSON is brittle unless you…',
                                       'choices': ['Never validate',
                                                   'Specify schema and validate outputs',
                                                   'Raise temperature to max',
                                                   'Skip examples'],
                                       'answer': 'B',
                                       'explain': 'Validation closes the loop.'},
                                      {'lo': 2,
                                       'q': 'A required-field checklist tells the model…',
                                       'choices': ['To invent values for every field always',
                                                   'Which fields must be present and what to do if '
                                                   'absent',
                                                   'To ignore urgency',
                                                   'To output HTML only'],
                                       'answer': 'B',
                                       'explain': 'Missing-data policy is part of the contract.'},
                                      {'lo': 2,
                                       'q': 'If account ID is missing, a good pattern is…',
                                       'choices': ['Hallucinate an ID',
                                                   'Leave null/omit per schema and flag '
                                                   'incompleteness',
                                                   'Crash the API key',
                                                   'Retry infinitely'],
                                       'answer': 'B',
                                       'explain': 'Explicit incomplete beats fake completeness.'},
                                      {'lo': 3,
                                       'q': 'A repair prompt should…',
                                       'choices': ['Add new facts to “help”',
                                                   'Fix invalid JSON/structure without changing '
                                                   'meaning',
                                                   'Remove all fields',
                                                   'Translate to another language silently'],
                                       'answer': 'B',
                                       'explain': 'Repair ≠ rewrite content.'},
                                      {'lo': 3,
                                       'q': 'A second review pass is useful to…',
                                       'choices': ['Increase cost only',
                                                   'Flag missing fields or contradictions before '
                                                   'finalizing',
                                                   'Bypass safety',
                                                   'Delete the taxonomy'],
                                       'answer': 'B',
                                       'explain': 'Review catches structural and consistency '
                                                  'issues.'},
                                      {'lo': 4,
                                       'q': 'An error taxonomy helps iteration by…',
                                       'choices': ['Hiding failures',
                                                   'Focusing fixes on the largest failure '
                                                   'categories first',
                                                   'Replacing the eval set',
                                                   'Guaranteeing 100% validity'],
                                       'answer': 'B',
                                       'explain': 'Categorize → prioritize → fix.'},
                                      {'lo': 4,
                                       'q': 'Tracking “invalid JSON” vs “wrong urgency” separately '
                                            'matters because…',
                                       'choices': ['They need different mitigations',
                                                   'They are the same bug',
                                                   'Taxonomies are decorative',
                                                   'Repair prompts fix urgency labels only'],
                                       'answer': 'A',
                                       'explain': 'Different failures need different prompt/tool '
                                                  'fixes.'},
                                      {'lo': 5,
                                       'q': 'Few-shots for sarcasm/multiple issues help because…',
                                       'choices': ['They waste tokens only',
                                                   'They demonstrate judgment on hard cases the '
                                                   'base rules under-specify',
                                                   'They replace schemas',
                                                   'They disable validation'],
                                       'answer': 'B',
                                       'explain': 'Hard cases need demonstrated patterns.'},
                                      {'lo': 1,
                                       'q': 'Measuring % valid JSON on a fixed set proves…',
                                       'choices': ['Marketing copy quality',
                                                   'Structural compliance of the extraction '
                                                   'pattern',
                                                   'Retrieval hit-rate',
                                                   'TLS configuration'],
                                       'answer': 'B',
                                       'explain': 'Validity rate is a core extraction metric.'}]},
 '04-evaluation-and-iteration': {'title': 'Evaluation and Iteration',
                                 'outcomes': ['Create a rubric scorers can apply consistently.',
                                              'Build a regression set and compare baseline vs '
                                              'improved prompts.',
                                              'Use golden answers for qualitative spot checks.',
                                              'Prioritize fixes by failure-category frequency.',
                                              'Add abstain/fallback rules tied to confidence '
                                              'thresholds.'],
                                 'questions': [{'lo': 1,
                                                'q': 'A good rubric is…',
                                                'choices': ['“Looks fine”',
                                                            'Clear enough that two reviewers score '
                                                            'similarly',
                                                            'Secret and unwritten',
                                                            'Only latency'],
                                                'answer': 'B',
                                                'explain': 'Inter-rater clarity makes scores '
                                                           'meaningful.'},
                                               {'lo': 1,
                                                'q': 'Rubric dimensions for summaries often '
                                                     'include…',
                                                'choices': ['Only token count',
                                                            'Factuality, completeness, '
                                                            'actionability, tone',
                                                            'GPU brand',
                                                            'Git blame'],
                                                'answer': 'B',
                                                'explain': 'Multi-axis rubrics match product '
                                                           'quality.'},
                                               {'lo': 2,
                                                'q': 'A baseline score exists so you can…',
                                                'choices': ['Skip later evals',
                                                            'Prove whether a change improved or '
                                                            'regressed',
                                                            'Avoid golden answers',
                                                            'Raise temperature freely'],
                                                'answer': 'B',
                                                'explain': 'No baseline → no proof.'},
                                               {'lo': 2,
                                                'q': 'Changing many prompt knobs at once on a '
                                                     'regression set…',
                                                'choices': ['Maximizes learning clarity',
                                                            'Confounds which change caused the '
                                                            'delta',
                                                            'Is required by eval harnesses',
                                                            'Removes the need for rubrics'],
                                                'answer': 'B',
                                                'explain': 'Isolate changes.'},
                                               {'lo': 3,
                                                'q': 'Golden answers are best used to…',
                                                'choices': ['Replace the whole regression set '
                                                            'forever',
                                                            'Spot-check quality on a small labeled '
                                                            'subset',
                                                            'Store API keys',
                                                            'Skip factuality'],
                                                'answer': 'B',
                                                'explain': 'Goldens anchor qualitative '
                                                           'comparison.'},
                                               {'lo': 4,
                                                'q': 'You see 40% failures as “missing actions.” '
                                                     'Next?',
                                                'choices': ['Ignore the taxonomy',
                                                            'Target that category in the next '
                                                            'prompt iteration',
                                                            'Only tweak unrelated tone examples',
                                                            'Delete the regression set'],
                                                'answer': 'B',
                                                'explain': 'Fix the biggest bucket first.'},
                                               {'lo': 4,
                                                'q': 'Failure categories turn raw fails into…',
                                                'choices': ['Noise',
                                                            'An actionable backlog for iteration',
                                                            'A reason to stop measuring',
                                                            'Deployment blockers only in '
                                                            'marketing'],
                                                'answer': 'B',
                                                'explain': 'Taxonomies drive the backlog.'},
                                               {'lo': 5,
                                                'q': 'Abstain/ask-when-uncertain rules help when…',
                                                'choices': ['Confident wrong answers are costly',
                                                            'You want maximum hallucination',
                                                            'Evals are perfect',
                                                            'Latency must be infinite'],
                                                'answer': 'A',
                                                'explain': 'Thresholded fallbacks reduce harmful '
                                                           'guesses.'},
                                               {'lo': 5,
                                                'q': 'A simple harness outline is…',
                                                'choices': ['Inputs → model → scores logged',
                                                            'Only production traffic with no '
                                                            'labels',
                                                            'Manual memory of one example',
                                                            'Deploy without measurement'],
                                                'answer': 'A',
                                                'explain': 'Harnesses make iteration mechanical.'},
                                               {'lo': 2,
                                                'q': 'Edge cases and adversarial inputs in the '
                                                     'regression set…',
                                                'choices': ['Are optional fluff',
                                                            'Catch brittle prompts before users do',
                                                            'Invalidate rubrics',
                                                            'Replace golden answers'],
                                                'answer': 'B',
                                                'explain': 'Hard cases protect quality under '
                                                           'stress.'}]},
 '05-safety-and-policy-basics': {'title': 'Safety and Policy Basics',
                                 'outcomes': ['Apply a safety checklist covering privacy, harm, '
                                              'and injection.',
                                              'Design refuse/redirect behaviors for unsafe '
                                              'requests.',
                                              'Use source-only answering to reduce hallucinations '
                                              'in doc Q&A.',
                                              'Red-team prompts for injection and exfiltration '
                                              'attempts.',
                                              'Define severity levels and escalation paths for '
                                              'high-risk cases.'],
                                 'questions': [{'lo': 1,
                                                'q': 'A safety checklist for a summarizer should '
                                                     'cover…',
                                                'choices': ['Only font size',
                                                            'Privacy, harmful content, and prompt '
                                                            'injection',
                                                            'CDN TTLs',
                                                            'Blue-green math'],
                                                'answer': 'B',
                                                'explain': 'Checklists make safety reviewable.'},
                                               {'lo': 1,
                                                'q': 'Treating user input as trusted instructions '
                                                     'is dangerous because…',
                                                'choices': ['Users are always right',
                                                            'It enables prompt injection and '
                                                            'policy bypass',
                                                            'It speeds evals',
                                                            'It improves grounding'],
                                                'answer': 'B',
                                                'explain': 'Untrusted input must not override '
                                                           'policy.'},
                                               {'lo': 2,
                                                'q': 'Refuse/redirect is better than “refuse '
                                                     'everything” when…',
                                                'choices': ['You can safely help within policy '
                                                            '(e.g., point to allowed resources)',
                                                            'You want maximum user frustration',
                                                            'Safety does not matter',
                                                            'The model is offline'],
                                                'answer': 'A',
                                                'explain': 'Proportionate safe completion beats '
                                                           'blanket refusal.'},
                                               {'lo': 2,
                                                'q': 'Unsafe request handling should be…',
                                                'choices': ['Improvised each time',
                                                            'Specified as explicit behaviors in '
                                                            'the prompt/policy',
                                                            'Logged with full secrets',
                                                            'Hidden from tests'],
                                                'answer': 'B',
                                                'explain': 'Specified behavior is testable.'},
                                               {'lo': 3,
                                                'q': 'Source-only Q&A means…',
                                                'choices': ['Answer from general knowledge always',
                                                            'Answer only with evidence from '
                                                            'provided sources or abstain',
                                                            'Ignore retrieved docs',
                                                            'Cite random URLs'],
                                                'answer': 'B',
                                                'explain': 'Grounding cuts hallucinations in '
                                                           'RAG-like flows.'},
                                               {'lo': 3,
                                                'q': 'If sources lack the answer, prefer…',
                                                'choices': ['Confident invention',
                                                            'Abstain / say insufficient evidence',
                                                            'Fetch passwords from logs',
                                                            'Raise temperature'],
                                                'answer': 'B',
                                                'explain': 'Abstention is a safety feature.'},
                                               {'lo': 4,
                                                'q': 'Red-team sets should include…',
                                                'choices': ['Only friendly greetings',
                                                            'Injection and data-exfiltration style '
                                                            'attacks',
                                                            'Only schema-valid JSON',
                                                            'Production secret values'],
                                                'answer': 'B',
                                                'explain': 'Adversarial coverage finds policy '
                                                           'holes.'},
                                               {'lo': 4,
                                                'q': 'A prompt that says “ignore previous '
                                                     'instructions” in user data tests…',
                                                'choices': ['Latency SLOs',
                                                            'Injection resistance',
                                                            'Cache hit rate',
                                                            'Blue-green cutover'],
                                                'answer': 'B',
                                                'explain': 'Classic injection probe.'},
                                               {'lo': 5,
                                                'q': 'Severity models (low/med/high) drive…',
                                                'choices': ['Random fonts',
                                                            'Different required actions and '
                                                            'escalations',
                                                            'Token discounts',
                                                            'Vector dimensions'],
                                                'answer': 'B',
                                                'explain': 'Severity maps to response playbooks.'},
                                               {'lo': 5,
                                                'q': 'High-risk cases often need…',
                                                'choices': ['Silent auto-approve',
                                                            'Human handoff, logging, and/or blocks',
                                                            'Higher temperature',
                                                            'Fewer tests'],
                                                'answer': 'B',
                                                'explain': 'Escalation paths contain blast '
                                                           'radius.'}]},
 '06-workflows-and-automation': {'title': 'Workflows and Automation',
                                 'outcomes': ['Design multi-step workflows with explicit step I/O '
                                              'contracts.',
                                              'Add verification steps before accepting '
                                              'intermediate outputs.',
                                              'Set retry budgets and stop conditions for uncertain '
                                              'results.',
                                              'Log privacy-safe audit fields for each run.',
                                              'Define fallbacks when a step fails or confidence is '
                                              'low.'],
                                 'questions': [{'lo': 1,
                                                'q': 'A 3-step notes workflow should define…',
                                                'choices': ['Only the final sentence tone',
                                                            'Input/output contracts per step '
                                                            '(extract → verify → finalize)',
                                                            'Unlimited hidden tools',
                                                            'No stop conditions'],
                                                'answer': 'B',
                                                'explain': 'Contracts make steps testable and '
                                                           'composable.'},
                                               {'lo': 1,
                                                'q': 'Why split extract vs verify?',
                                                'choices': ['To spend more tokens always',
                                                            'To catch missing/invalid actions '
                                                            'before delivery',
                                                            'To skip evaluation',
                                                            'To store raw PII longer'],
                                                'answer': 'B',
                                                'explain': 'Verification reduces bad outputs '
                                                           'shipping.'},
                                               {'lo': 2,
                                                'q': 'Verification against sources prevents…',
                                                'choices': ['All latency',
                                                            'Unfounded claims in later steps',
                                                            'The need for schemas',
                                                            'Audit logs'],
                                                'answer': 'B',
                                                'explain': 'Check facts before acting.'},
                                               {'lo': 3,
                                                'q': 'A retry budget exists to…',
                                                'choices': ['Loop forever on failure',
                                                            'Bound cost/latency when steps fail or '
                                                            'are uncertain',
                                                            'Disable stop conditions',
                                                            'Ignore fallbacks'],
                                                'answer': 'B',
                                                'explain': 'Budgets prevent runaway automation.'},
                                               {'lo': 3,
                                                'q': 'Stop-if-uncertain rules protect…',
                                                'choices': ['Only marketing copy',
                                                            'Users from automated wrong actions',
                                                            'The CDN',
                                                            'Git history'],
                                                'answer': 'B',
                                                'explain': 'Uncertainty should halt side effects.'},
                                               {'lo': 4,
                                                'q': 'Audit logs should include…',
                                                'choices': ['Raw passwords and full card numbers',
                                                            'Run id, prompt version, result '
                                                            'category, and redacted context',
                                                            'Nothing — logs are optional',
                                                            'Only emoji'],
                                                'answer': 'B',
                                                'explain': 'Privacy-safe provenance beats dumping '
                                                           'secrets.'},
                                               {'lo': 4,
                                                'q': 'Redaction before logging is important '
                                                     'because…',
                                                'choices': ['Logs are never accessed',
                                                            'Logs are a common leak channel for '
                                                            'sensitive data',
                                                            'It slows attackers’ CPUs',
                                                            'It replaces AuthZ'],
                                                'answer': 'B',
                                                'explain': 'Minimize sensitive retention in '
                                                           'telemetry.'},
                                               {'lo': 5,
                                                'q': 'When a step fails, a fallback might…',
                                                'choices': ['Invent success',
                                                            'Ask a human, abstain, or return a '
                                                            'safe degraded result',
                                                            'Disable all policies',
                                                            'Retry without budget'],
                                                'answer': 'B',
                                                'explain': 'Explicit fallbacks beat silent '
                                                           'failure.'},
                                               {'lo': 5,
                                                'q': 'Agentic multi-step flows need stop '
                                                     'conditions because…',
                                                'choices': ['Models never loop',
                                                            'Unbounded tool loops can runaway in '
                                                            'cost and harm',
                                                            'Contracts forbid stops',
                                                            'Evals cannot run'],
                                                'answer': 'B',
                                                'explain': 'Bounds are a core automation control.'},
                                               {'lo': 2,
                                                'q': 'End-to-end testing a workflow on 10 cases '
                                                     'mainly checks…',
                                                'choices': ['Only one unit function',
                                                            'Contracts, verification, and '
                                                            'fallbacks under realistic inputs',
                                                            'Font rendering',
                                                            'Kubernetes YAML comments'],
                                                'answer': 'B',
                                                'explain': 'E2E proves the pipeline, not just '
                                                           'prompts in isolation.'}]},
 'foundations': {'title': 'Foundations',
                 'outcomes': ['Structure prompts with roles, constraints, and iteration notes.',
                              'Demonstrate safe refuse/redirect behavior on risky inputs.',
                              'Keep a prompt journal showing what improved and what did not.'],
                 'questions': [{'lo': 1,
                                'q': 'System vs user roles in a prompt mainly separate…',
                                'choices': ['Fonts',
                                            'Stable policy/instructions from untrusted user '
                                            'content',
                                            'Vector indexes from BM25',
                                            'Canary from blue-green'],
                                'answer': 'B',
                                'explain': 'Roles clarify authority of instructions.'},
                               {'lo': 1,
                                'q': 'Iteration notes should capture…',
                                'choices': ['Only the final string',
                                            'Changes tried and measured outcomes',
                                            'API secrets',
                                            'Nothing if temperature changed'],
                                'answer': 'B',
                                'explain': 'Journals make learning transferable.'},
                               {'lo': 2,
                                'q': 'A safe response to a disallowed request is…',
                                'choices': ['Comply quietly',
                                            'Refuse or redirect per policy without leaking '
                                            'sensitive data',
                                            'Print internal system prompts',
                                            'Raise temperature'],
                                'answer': 'B',
                                'explain': 'Safety basics: refuse/redirect cleanly.'},
                               {'lo': 2,
                                'q': 'Including a sensitive ID in the model answer when not '
                                     'required…',
                                'choices': ['Is always fine',
                                            'Is a privacy miss — minimize sensitive echo',
                                            'Improves grounding',
                                            'Replaces evaluation'],
                                'answer': 'B',
                                'explain': 'Minimize sensitive data in outputs.'},
                               {'lo': 3,
                                'q': 'A prompt journal entry that says “tried X, score fell on '
                                     'factuality” helps by…',
                                'choices': ['Hiding regressions',
                                            'Preventing repeated failed experiments',
                                            'Deleting the eval set',
                                            'Skipping safety'],
                                'answer': 'B',
                                'explain': 'Documented failures save future time.'},
                               {'lo': 3,
                                'q': 'You improved format adherence but hurt factuality. Journal '
                                     'should…',
                                'choices': ['Only celebrate format',
                                            'Record both effects so the next change can rebalance',
                                            'Delete the old prompt',
                                            'Ignore metrics'],
                                'answer': 'B',
                                'explain': 'Tradeoffs belong in the journal.'},
                               {'lo': 1,
                                'q': 'Constraints in a beginner prompt should be…',
                                'choices': ['Buried in a novel-length preamble',
                                            'Short, explicit, and testable',
                                            'Omitted to maximize creativity',
                                            'Stored only in Slack'],
                                'answer': 'B',
                                'explain': 'Clarity beats prompt bloat.'},
                               {'lo': 2,
                                'q': 'Why test at least one refusal case in foundations?',
                                'choices': ['Refusal never matters',
                                            'To prove policy behavior is intentional, not '
                                            'accidental',
                                            'To slow the course',
                                            'To replace happy-path tests'],
                                'answer': 'B',
                                'explain': 'Safety needs positive evidence.'}]}}

AI_INTERMEDIATE = {'01-advanced-prompting-tool-use': {'title': 'Advanced Prompting: Tool Use',
                                    'outcomes': ['Write tool contracts with typed arguments and '
                                                 'error cases.',
                                                 'Choose among answer, clarify, or call-tool based '
                                                 'on the request.',
                                                 'Verify tool results against the user request '
                                                 'before finalizing.',
                                                 'Apply retry budgets and clear errors for tool '
                                                 'failures.',
                                                 'Log tool calls in an audit schema without '
                                                 'leaking secrets.'],
                                    'questions': [{'lo': 1,
                                                   'q': 'A tool contract should specify…',
                                                   'choices': ['Only a friendly name',
                                                               'Args, types, side effects, and '
                                                               'error modes',
                                                               'The model’s favorite color',
                                                               'Unlimited privileges'],
                                                   'answer': 'B',
                                                   'explain': 'Contracts make tool use testable '
                                                              'and safe.'},
                                                  {'lo': 1,
                                                   'q': 'create_task(title, owner, due_date) '
                                                        'without types risks…',
                                                   'choices': ['Perfect validation',
                                                               'Ambiguous/invalid calls the model '
                                                               'invents',
                                                               'Faster audits',
                                                               'No side effects'],
                                                   'answer': 'B',
                                                   'explain': 'Typed args reduce malformed calls.'},
                                                  {'lo': 2,
                                                   'q': 'When required fields are missing, prefer…',
                                                   'choices': ['Calling the tool with guesses',
                                                               'Asking a clarifying question',
                                                               'Ignoring the user',
                                                               'Disabling the tool forever'],
                                                   'answer': 'B',
                                                   'explain': 'Clarify before side-effecting '
                                                              'tools.'},
                                                  {'lo': 2,
                                                   'q': 'If the question is answerable without '
                                                        'tools…',
                                                   'choices': ['Always call every tool',
                                                               'Answer directly per policy',
                                                               'Refuse always',
                                                               'Invent a tool result'],
                                                   'answer': 'B',
                                                   'explain': 'Tool use is optional — not a '
                                                              'reflex.'},
                                                  {'lo': 3,
                                                   'q': 'Verification after a tool call checks…',
                                                   'choices': ['That any JSON returned is '
                                                               'celebrated',
                                                               'That the result matches the '
                                                               'requested action/constraints',
                                                               'Only latency',
                                                               'The CDN'],
                                                   'answer': 'B',
                                                   'explain': 'Never trust tool output blindly.'},
                                                  {'lo': 3,
                                                   'q': 'Tool returns a due date in the past vs '
                                                        'request. You should…',
                                                   'choices': ['Ship it anyway',
                                                               'Flag/repair or ask before '
                                                               'confirming to the user',
                                                               'Hide the field',
                                                               'Raise temperature'],
                                                   'answer': 'B',
                                                   'explain': 'Verify semantic fit, not only parse '
                                                              'success.'},
                                                  {'lo': 4,
                                                   'q': 'Tool timeouts should be handled with…',
                                                   'choices': ['Infinite silent waits',
                                                               'Budgeted retries and explicit '
                                                               'user-visible errors',
                                                               'Pretend success',
                                                               'Deleting the audit log'],
                                                   'answer': 'B',
                                                   'explain': 'Failures need budgets and clear '
                                                              'messaging.'},
                                                  {'lo': 4,
                                                   'q': 'Adversarial “call admin tools” prompts '
                                                        'should…',
                                                   'choices': ['Bypass contracts',
                                                               'Be refused when outside allowed '
                                                               'tool policy',
                                                               'Auto-approve',
                                                               'Disable verification'],
                                                   'answer': 'B',
                                                   'explain': 'Tool policy is a safety boundary.'},
                                                  {'lo': 5,
                                                   'q': 'Audit logs for tools should capture…',
                                                   'choices': ['Raw secrets in arguments',
                                                               'Who/what/when/why with redaction',
                                                               'Nothing',
                                                               'Only emoji reactions'],
                                                   'answer': 'B',
                                                   'explain': 'Provenance without sensitive '
                                                              'dumps.'},
                                                  {'lo': 5,
                                                   'q': 'Why log tool failures as well as '
                                                        'successes?',
                                                   'choices': ['To inflate metrics',
                                                               'To diagnose retries, abuse, and '
                                                               'reliability issues',
                                                               'Because successes do not matter',
                                                               'To store PII longer'],
                                                   'answer': 'B',
                                                   'explain': 'Failure telemetry improves ops and '
                                                              'safety.'}]},
 '02-structured-outputs-and-schemas': {'title': 'Structured Outputs and Schemas',
                                       'outcomes': ['Design schemas for task outputs with required '
                                                    'and optional fields.',
                                                    'Validate outputs and measure '
                                                    'validity/completeness on a dataset.',
                                                    'Add capped repair passes that fix structure '
                                                    'without new facts.',
                                                    'Version schemas and plan migrations for '
                                                    'breaking changes.',
                                                    'Fail closed with a fallback when strict '
                                                    'validation fails.'],
                                       'questions': [{'lo': 1,
                                                      'q': 'A ticket schema should define…',
                                                      'choices': ['Only free prose',
                                                                  'Fields like category, summary, '
                                                                  'urgency, actions — with types',
                                                                  'GPU SKUs',
                                                                  'Git remotes'],
                                                      'answer': 'B',
                                                      'explain': 'Schemas encode the product '
                                                                 'contract.'},
                                                     {'lo': 1,
                                                      'q': 'Optional vs required fields matter '
                                                           'because…',
                                                      'choices': ['Validators ignore them',
                                                                  'They change pass/fail and '
                                                                  'missing-data behavior',
                                                                  'They only affect fonts',
                                                                  'They replace evals'],
                                                      'answer': 'B',
                                                      'explain': 'Requirements drive validation.'},
                                                     {'lo': 2,
                                                      'q': 'Measuring JSON validity + '
                                                           'required-field completeness tells you…',
                                                      'choices': ['Brand sentiment only',
                                                                  'Structural quality of '
                                                                  'structured outputs',
                                                                  'Retrieval recall',
                                                                  'TLS grade'],
                                                      'answer': 'B',
                                                      'explain': 'These are core structured-output '
                                                                 'metrics.'},
                                                     {'lo': 2,
                                                      'q': 'A 30-case dataset is useful to…',
                                                      'choices': ['Avoid automation',
                                                                  'Estimate validity rates beyond '
                                                                  'anecdotes',
                                                                  'Replace schemas',
                                                                  'Skip repair'],
                                                      'answer': 'B',
                                                      'explain': 'Sample size beats one lucky '
                                                                 'example.'},
                                                     {'lo': 3,
                                                      'q': 'Repair must not…',
                                                      'choices': ['Fix commas/braces',
                                                                  'Invent missing business facts '
                                                                  'to satisfy the schema',
                                                                  'Normalize field order',
                                                                  'Re-emit valid JSON of the same '
                                                                  'meaning'],
                                                      'answer': 'B',
                                                      'explain': 'Repair is structural, not '
                                                                 'creative.'},
                                                     {'lo': 3,
                                                      'q': 'Capping repair attempts prevents…',
                                                      'choices': ['All invalid JSON',
                                                                  'Unbounded cost loops on '
                                                                  'hopeless outputs',
                                                                  'Schema versioning',
                                                                  'Fallbacks'],
                                                      'answer': 'B',
                                                      'explain': 'Budgets apply to repair too.'},
                                                     {'lo': 4,
                                                      'q': 'Schema versioning helps when…',
                                                      'choices': ['Fields never change',
                                                                  'Producers/consumers evolve '
                                                                  'without silent breakages',
                                                                  'You delete validators',
                                                                  'You store secrets in schemas'],
                                                      'answer': 'B',
                                                      'explain': 'Versions + migrations keep '
                                                                 'contracts coherent.'},
                                                     {'lo': 4,
                                                      'q': 'A breaking field rename should '
                                                           'include…',
                                                      'choices': ['Silent cutover with no notes',
                                                                  'A migration plan and dual-read '
                                                                  'period if needed',
                                                                  'Removing all examples',
                                                                  'Disabling strict mode forever'],
                                                      'answer': 'B',
                                                      'explain': 'Treat schema breaks like API '
                                                                 'breaks.'},
                                                     {'lo': 5,
                                                      'q': 'Strict mode fails validation — best '
                                                           'response?',
                                                      'choices': ['Return invalid JSON anyway',
                                                                  'Fallback: error, abstain, or '
                                                                  'safe partial per policy',
                                                                  'Invent fields',
                                                                  'Disable logging'],
                                                      'answer': 'B',
                                                      'explain': 'Fail closed with an explicit '
                                                                 'fallback.'},
                                                     {'lo': 5,
                                                      'q': 'Red-team “extra fields / injected '
                                                           'instructions” tests…',
                                                      'choices': ['Latency only',
                                                                  'Whether validators and prompts '
                                                                  'reject schema abuse',
                                                                  'Canary math',
                                                                  'Cache keys'],
                                                      'answer': 'B',
                                                      'explain': 'Structured outputs need '
                                                                 'adversarial coverage too.'}]},
 '03-rag-foundations': {'title': 'RAG Foundations',
                        'outcomes': ['Chunk documents and attach metadata for retrieval.',
                                     'Answer only from retrieved context with citations.',
                                     'Abstain when evidence is missing and measure hallucination '
                                     'drop.',
                                     'Separate retrieval failures from generation failures in '
                                     'evals.',
                                     'Improve hit-rate with query rewriting and simple offline '
                                     'metrics.'],
                        'questions': [{'lo': 1,
                                       'q': 'Chunking strategy matters because…',
                                       'choices': ['Models ignore context size',
                                                   'It affects what can be retrieved and cited',
                                                   'It replaces embeddings',
                                                   'It deletes metadata'],
                                       'answer': 'B',
                                       'explain': 'Chunks are the retrieval unit.'},
                                      {'lo': 1,
                                       'q': 'Useful metadata often includes…',
                                       'choices': ['Random UUIDs only',
                                                   'Doc type, version, and access tags',
                                                   'User passwords',
                                                   'GPU temperature'],
                                       'answer': 'B',
                                       'explain': 'Metadata enables filters and governance.'},
                                      {'lo': 2,
                                       'q': 'Grounded answering requires…',
                                       'choices': ['Ignoring retrieved excerpts',
                                                   'Using retrieved context and citing supporting '
                                                   'excerpts',
                                                   'Always using parametric memory first',
                                                   'No abstentions ever'],
                                       'answer': 'B',
                                       'explain': 'Citations make grounding checkable.'},
                                      {'lo': 2,
                                       'q': '“No evidence → abstain” mainly reduces…',
                                       'choices': ['Index size',
                                                   'Unsupported claims',
                                                   'Chunk count',
                                                   'Embedding dim'],
                                       'answer': 'B',
                                       'explain': 'Abstention is an anti-hallucination control.'},
                                      {'lo': 3,
                                       'q': 'If retrieval returns empty, generation should…',
                                       'choices': ['Improvise from the web silently',
                                                   'Abstain or ask — not fabricate',
                                                   'Raise temperature',
                                                   'Disable citations'],
                                       'answer': 'B',
                                       'explain': 'Empty retrieval is a retrieval failure, not a '
                                                  'writing prompt.'},
                                      {'lo': 4,
                                       'q': 'Tracking retrieval vs generation failures separately '
                                            'helps because…',
                                       'choices': ['They share one fix always',
                                                   'Wrong mitigations waste effort (index vs '
                                                   'prompt)',
                                                   'Evals forbid it',
                                                   'Citations become optional'],
                                       'answer': 'B',
                                       'explain': 'Split metrics target the right layer.'},
                                      {'lo': 4,
                                       'q': 'A wrong answer with perfect citations to irrelevant '
                                            'chunks is usually…',
                                       'choices': ['A pure generation grammar bug',
                                                   'A retrieval relevance problem (and/or ranking)',
                                                   'A TLS issue',
                                                   'A canary bug'],
                                       'answer': 'B',
                                       'explain': 'Bad evidence in → grounded-but-wrong out.'},
                                      {'lo': 5,
                                       'q': 'Query rewriting can improve…',
                                       'choices': ['Disk encryption',
                                                   'Retrieval hit-rate on a fixed question set',
                                                   'Blue-green cutovers',
                                                   'OWASP mapping'],
                                       'answer': 'B',
                                       'explain': 'Better queries → better candidates.'},
                                      {'lo': 5,
                                       'q': 'Precision@k as a proxy evaluates…',
                                       'choices': ['Only final prose tone',
                                                   'Whether top-k retrieved chunks are relevant',
                                                   'Token price only',
                                                   'Feature flags'],
                                       'answer': 'B',
                                       'explain': 'Offline retrieval metrics guide '
                                                  'indexing/chunking.'},
                                      {'lo': 2,
                                       'q': 'Why cite excerpts rather than say “according to '
                                            'docs”?',
                                       'choices': ['Citations are decorative',
                                                   'They let humans verify the claim against '
                                                   'evidence',
                                                   'They increase hallucination',
                                                   'They replace chunking'],
                                       'answer': 'B',
                                       'explain': 'Verifiability is the point of grounding.'}]},
 '04-model-evaluation-and-testing': {'title': 'Model Evaluation and Testing',
                                     'outcomes': ['Run a repeatable eval harness on a fixed case '
                                                  'set.',
                                                  'Set pass/fail thresholds for schema and rubric '
                                                  'scores.',
                                                  'Score adversarial cases separately from the '
                                                  'main set.',
                                                  'Produce regression reports with change impact '
                                                  'and rollback criteria.',
                                                  'Record cost and latency alongside quality '
                                                  'metrics.'],
                                     'questions': [{'lo': 1,
                                                    'q': 'A harness is “repeatable” when…',
                                                    'choices': ['Inputs, prompt version, and '
                                                                'scoring rules are fixed/logged',
                                                                'You change everything each run',
                                                                'Only production traffic is used',
                                                                'Scores are remembered mentally'],
                                                    'answer': 'A',
                                                    'explain': 'Reproducibility needs versioned '
                                                               'inputs and scorers.'},
                                                   {'lo': 1,
                                                    'q': 'Fifty labeled cases beat five anecdotes '
                                                         'because…',
                                                    'choices': ['Anecdotes are illegal',
                                                                'Variance and coverage become '
                                                                'visible',
                                                                'Harnesses forbid small sets',
                                                                'Latency disappears'],
                                                    'answer': 'B',
                                                    'explain': 'More cases → stabler decisions.'},
                                                   {'lo': 2,
                                                    'q': 'Thresholds like “90% schema validity” '
                                                         'act as…',
                                                    'choices': ['Decorations',
                                                                'Release gates for quality',
                                                                'Replacements for rubrics',
                                                                'Cache keys'],
                                                    'answer': 'B',
                                                    'explain': 'Gates turn metrics into go/no-go.'},
                                                   {'lo': 2,
                                                    'q': 'Failing a threshold should…',
                                                    'choices': ['Be ignored if demos look cool',
                                                                'Block or roll back per policy',
                                                                'Delete the harness',
                                                                'Raise temperature'],
                                                    'answer': 'B',
                                                    'explain': 'Gates without enforcement are '
                                                               'theater.'},
                                                   {'lo': 3,
                                                    'q': 'Separate adversarial scores prevent…',
                                                    'choices': ['Safety visibility',
                                                                'Happy-path averages from hiding '
                                                                'injection failures',
                                                                'Cost tracking',
                                                                'Golden sets'],
                                                    'answer': 'B',
                                                    'explain': 'Safety regressions must not be '
                                                               'averaged away.'},
                                                   {'lo': 3,
                                                    'q': 'Injection cases in evals are…',
                                                    'choices': ['Optional fluff',
                                                                'First-class tests for policy '
                                                                'robustness',
                                                                'Only for advanced RAG',
                                                                'Replaced by latency SLOs'],
                                                    'answer': 'B',
                                                    'explain': 'Adversarial coverage is required.'},
                                                   {'lo': 4,
                                                    'q': 'A regression report should state…',
                                                    'choices': ['Only “LGTM”',
                                                                'What changed, what broke, metrics '
                                                                'deltas, and rollback decision',
                                                                'API keys',
                                                                'Nothing if CI is green'],
                                                    'answer': 'B',
                                                    'explain': 'Reports make A/B prompt decisions '
                                                               'auditable.'},
                                                   {'lo': 4,
                                                    'q': 'A/B prompt versions need rollback '
                                                         'criteria so…',
                                                    'choices': ['You never revert',
                                                                'You know when to switch back on '
                                                                'quality/safety drops',
                                                                'Canaries are illegal',
                                                                'Cost is ignored'],
                                                    'answer': 'B',
                                                    'explain': 'Predeclare failure → action.'},
                                                   {'lo': 5,
                                                    'q': 'Logging cost/latency per eval run helps…',
                                                    'choices': ['Only finance memes',
                                                                'Catch quality wins that are '
                                                                'operationally unaffordable',
                                                                'Replace rubrics',
                                                                'Delete thresholds'],
                                                    'answer': 'B',
                                                    'explain': 'Ops metrics belong next to '
                                                               'quality.'},
                                                   {'lo': 1,
                                                    'q': 'Deterministic eval settings (fixed '
                                                         'seed/temp where possible) reduce…',
                                                    'choices': ['All model stochasticity forever',
                                                                'Noise that confuses regression '
                                                                'interpretation',
                                                                'The need for datasets',
                                                                'Safety tests'],
                                                    'answer': 'B',
                                                    'explain': 'Control what you can when '
                                                               'comparing versions.'}]},
 '05-guardrails-and-safety': {'title': 'Guardrails and Safety',
                              'outcomes': ['Enforce input/output controls including source-only '
                                           'and refusal rules.',
                                           'Constrain tools with least privilege and verify via '
                                           'tests.',
                                           'Build red-team suites that target top abuse paths.',
                                           'Add safety gates in CI that fail on safety '
                                           'regressions.',
                                           'Design escalation paths for high-risk model outputs.'],
                              'questions': [{'lo': 1,
                                             'q': 'Output controls in RAG should…',
                                             'choices': ['Allow answers without evidence',
                                                         'Require evidence or refuse/abstain',
                                                         'Strip all citations',
                                                         'Log raw secrets'],
                                             'answer': 'B',
                                             'explain': 'Source-only is an output guardrail.'},
                                            {'lo': 1,
                                             'q': 'Input controls typically…',
                                             'choices': ['Trust all user text as system policy',
                                                         'Detect/block injection and disallowed '
                                                         'content before tools run',
                                                         'Disable AuthZ',
                                                         'Skip evals'],
                                             'answer': 'B',
                                             'explain': 'Filter early to reduce blast radius.'},
                                            {'lo': 2,
                                             'q': 'Least-privilege tools mean…',
                                             'choices': ['Every agent can drop production tables',
                                                         'Only tools needed for the task are '
                                                         'exposed, with arg limits',
                                                         'No tools ever',
                                                         'Tools without contracts'],
                                             'answer': 'B',
                                             'explain': 'Privilege minimization is a guardrail.'},
                                            {'lo': 2,
                                             'q': 'Tests should try to make the agent…',
                                             'choices': ['Only summarize kindly',
                                                         'Call disallowed tools or exfiltrate '
                                                         'secrets — and verify denial',
                                                         'Skip audit logs',
                                                         'Disable refusals'],
                                             'answer': 'B',
                                             'explain': 'Negative tests prove constraints hold.'},
                                            {'lo': 3,
                                             'q': 'Red-team suites focus on…',
                                             'choices': ['Happy-path UX copy',
                                                         'Highest-impact abuse and bypass attempts',
                                                         'Font kerning',
                                                         'CDN purge times'],
                                             'answer': 'B',
                                             'explain': 'Prioritize real threats.'},
                                            {'lo': 3,
                                             'q': 'Prompt injection into tool args is dangerous '
                                                  'because…',
                                             'choices': ['Args are never executed',
                                                         'It can trigger unintended side effects',
                                                         'It only affects CSS',
                                                         'It improves grounding'],
                                             'answer': 'B',
                                             'explain': 'Tools turn text into actions.'},
                                            {'lo': 4,
                                             'q': 'A CI safety gate should…',
                                             'choices': ['Be optional forever',
                                                         'Fail the build when safety evals regress '
                                                         'beyond threshold',
                                                         'Only run on Fridays',
                                                         'Store production keys in artifacts'],
                                             'answer': 'B',
                                             'explain': 'Automate the regression tripwire.'},
                                            {'lo': 4,
                                             'q': 'Safety tests belong in the harness so…',
                                             'choices': ['They are forgotten',
                                                         'Every prompt change re-checks policy '
                                                         'behavior',
                                                         'Latency is ignored',
                                                         'Schemas are deleted'],
                                             'answer': 'B',
                                             'explain': 'Safety is a continuous eval, not a '
                                                        'one-off.'},
                                            {'lo': 5,
                                             'q': 'Escalation for high-risk outputs may include…',
                                             'choices': ['Auto-publish always',
                                                         'Human review, block, or safe-complete '
                                                         'paths',
                                                         'Higher temperature',
                                                         'Disabling logs'],
                                             'answer': 'B',
                                             'explain': 'Severity drives response path.'},
                                            {'lo': 5,
                                             'q': 'Audit-friendly logging for safety events '
                                                  'should…',
                                             'choices': ['Include full sensitive payloads always',
                                                         'Record category and action taken without '
                                                         'unnecessary secrets',
                                                         'Be off in production',
                                                         'Replace threat models'],
                                             'answer': 'B',
                                             'explain': 'Investigate without creating new '
                                                        'leaks.'}]},
 '06-agentic-workflows': {'title': 'Agentic Workflows',
                          'outcomes': ['Specify agent plans with tool boundaries and stop '
                                       'conditions.',
                                       'Insert verification steps that check claims against '
                                       'sources.',
                                       'Enforce tool budgets to prevent runaway loops.',
                                       'Require human approval for high-risk actions.',
                                       'Emit post-run reports covering actions, evidence, and '
                                       'uncertainties.'],
                          'questions': [{'lo': 1,
                                         'q': 'An agent workflow spec should state…',
                                         'choices': ['“Figure it out” only',
                                                     'Steps, allowed tools, stop conditions, and '
                                                     'outputs',
                                                     'Unlimited recursive self-calls',
                                                     'No verification'],
                                         'answer': 'B',
                                         'explain': 'Specs bound autonomy.'},
                                        {'lo': 1,
                                         'q': 'Tool boundaries exist to…',
                                         'choices': ['Maximize surprise side effects',
                                                     'Prevent actions outside the task’s privilege '
                                                     'set',
                                                     'Remove stop conditions',
                                                     'Skip evals'],
                                         'answer': 'B',
                                         'explain': 'Boundaries are safety and product '
                                                    'constraints.'},
                                        {'lo': 2,
                                         'q': 'Verification before deliver means…',
                                         'choices': ['Trusting the first draft always',
                                                     'Checking facts against provided sources',
                                                     'Deleting uncertainties',
                                                     'Calling more tools randomly'],
                                         'answer': 'B',
                                         'explain': 'Verify reduces hallucinated actions.'},
                                        {'lo': 3,
                                         'q': 'A tool budget of N calls stops…',
                                         'choices': ['All useful work',
                                                     'Runaway loops that burn cost and time',
                                                     'Human approvals',
                                                     'Audit reports'],
                                         'answer': 'B',
                                         'explain': 'Budgets are circuit breakers for agents.'},
                                        {'lo': 3,
                                         'q': 'Missing stop conditions typically cause…',
                                         'choices': ['Cleaner traces',
                                                     'Endless plan/execute cycles',
                                                     'Stronger grounding',
                                                     'Cheaper runs'],
                                         'answer': 'B',
                                         'explain': 'Agents need explicit halting rules.'},
                                        {'lo': 4,
                                         'q': 'Human approval checkpoints belong on…',
                                         'choices': ['Every adjective choice',
                                                     'High-risk side effects (refunds, emails, '
                                                     'deletes)',
                                                     'Read-only lookups only',
                                                     'Cache hits'],
                                         'answer': 'B',
                                         'explain': 'Match human gates to blast radius.'},
                                        {'lo': 4,
                                         'q': 'Adversarial cases that push secret leakage should…',
                                         'choices': ['Be omitted',
                                                     'Be in the eval set with expected denials',
                                                     'Auto-succeed',
                                                     'Disable reports'],
                                         'answer': 'B',
                                         'explain': 'Agents need red-team coverage.'},
                                        {'lo': 5,
                                         'q': 'A post-run report should include…',
                                         'choices': ['Only “done”',
                                                     'Actions taken, evidence, and remaining '
                                                     'uncertainties',
                                                     'Raw API keys',
                                                     'Unrelated metrics'],
                                         'answer': 'B',
                                         'explain': 'Reports make autonomy reviewable.'},
                                        {'lo': 5,
                                         'q': 'Listing uncertainties helps operators…',
                                         'choices': ['Ignore risk',
                                                     'Decide what needs human follow-up',
                                                     'Delete sources',
                                                     'Raise budgets silently'],
                                         'answer': 'B',
                                         'explain': 'Uncertainty is an operational signal.'},
                                        {'lo': 2,
                                         'q': 'Simulating tool-down failures in tests checks…',
                                         'choices': ['Happy-path only',
                                                     'Whether the agent degrades safely '
                                                     '(retry/stop/escalate)',
                                                     'Font loading',
                                                     'Schema cosmetics'],
                                         'answer': 'B',
                                         'explain': 'Failure injection validates agent '
                                                    'resilience.'}]},
 '07-cost-latency-and-ops': {'title': 'Cost, Latency, and Ops',
                             'outcomes': ['Set cost/latency budgets and enforce them in workflows.',
                                          'Design cache keys and reuse strategies that preserve '
                                          'correctness.',
                                          'Add early-exit/abstain rules when confidence is low.',
                                          'Monitor quality, cost, and latency with actionable '
                                          'alerts.',
                                          'Plan canary/rollback for prompt and model version '
                                          'changes.'],
                             'questions': [{'lo': 1,
                                            'q': 'A budget without an enforcement action is…',
                                            'choices': ['A complete control',
                                                        'Just a hope — define fallback when '
                                                        'exceeded',
                                                        'A cache key',
                                                        'An SLO replacement'],
                                            'answer': 'B',
                                            'explain': 'Budgets need tripwires and fallbacks.'},
                                           {'lo': 1,
                                            'q': 'When a latency budget is exceeded, a workflow '
                                                 'might…',
                                            'choices': ['Hang forever',
                                                        'Fallback to a cheaper/faster path or '
                                                        'abstain',
                                                        'Disable monitoring',
                                                        'Delete caches'],
                                            'answer': 'B',
                                            'explain': 'Degrade deliberately.'},
                                           {'lo': 2,
                                            'q': 'Cache keys for LLM calls should usually include…',
                                            'choices': ['Only the user id',
                                                        'Prompt version + normalized inputs that '
                                                        'determine the output',
                                                        'Wall-clock seconds always',
                                                        'Random UUID each time'],
                                            'answer': 'B',
                                            'explain': 'Keys must match semantic inputs.'},
                                           {'lo': 2,
                                            'q': 'Caching answers without prompt version in the '
                                                 'key risks…',
                                            'choices': ['Perfect invalidation',
                                                        'Serving stale answers after a prompt '
                                                        'change',
                                                        'Lower latency forever safely',
                                                        'Free evals'],
                                            'answer': 'B',
                                            'explain': 'Version the cache namespace.'},
                                           {'lo': 3,
                                            'q': 'Early exit on low confidence trades…',
                                            'choices': ['Nothing',
                                                        'Some coverage for lower cost/risk of bad '
                                                        'answers',
                                                        'Away all safety',
                                                        'Monitoring for silence'],
                                            'answer': 'B',
                                            'explain': 'Abstain/ask can be the cheapest correct '
                                                       'action.'},
                                           {'lo': 3,
                                            'q': 'Context trimming in RAG helps latency/cost by…',
                                            'choices': ['Sending more tokens always',
                                                        'Keeping only necessary retrieved evidence',
                                                        'Removing citations forever',
                                                        'Disabling abstention'],
                                            'answer': 'B',
                                            'explain': 'Less context → less spend if relevance '
                                                       'holds.'},
                                           {'lo': 4,
                                            'q': 'Ops dashboards for LLM features should show…',
                                            'choices': ['Only marketing NPS',
                                                        'Quality proxies, cost, latency, and '
                                                        'error/fallback rates',
                                                        'Nothing after launch',
                                                        'Raw prompts with secrets'],
                                            'answer': 'B',
                                            'explain': 'Triangulate quality and spend.'},
                                           {'lo': 4,
                                            'q': 'An alert on cost spike should be…',
                                            'choices': ['Ignored',
                                                        'Actionable: check canaries, caches, '
                                                        'runaway agents',
                                                        'Paged every DEBUG log',
                                                        'Secret-only'],
                                            'answer': 'B',
                                            'explain': 'Tie alerts to operator playbooks.'},
                                           {'lo': 5,
                                            'q': 'Prompt canaries reduce risk by…',
                                            'choices': ['Shipping to 100% first',
                                                        'Exposing a new prompt version to a small '
                                                        'cohort while watching metrics',
                                                        'Skipping eval gates',
                                                        'Disabling rollback'],
                                            'answer': 'B',
                                            'explain': 'Progressive delivery for prompts.'},
                                           {'lo': 5,
                                            'q': 'Rollback criteria for prompt releases should be '
                                                 'predefined so…',
                                            'choices': ['Debates happen during an outage',
                                                        'You revert quickly on quality/cost/safety '
                                                        'regressions',
                                                        'Canaries never end',
                                                        'Caches ignore versions'],
                                            'answer': 'B',
                                            'explain': 'Decide thresholds before the fire.'}]},
 '08-deployment-basics': {'title': 'Deployment Basics',
                          'outcomes': ['Create a deployment checklist including eval and safety '
                                       'gates.',
                                       'Version prompts/schemas and keep a change log.',
                                       'Define rollback triggers from eval and user-impact '
                                       'signals.',
                                       'Run smoke tests on critical flows post-deploy.',
                                       'Use staged rollout with shadow evaluation where '
                                       'appropriate.'],
                          'questions': [{'lo': 1,
                                         'q': 'Pre-deploy for an AI feature should include…',
                                         'choices': ['Only a gut check',
                                                     'Eval harness + safety tests passing gates',
                                                     'Disabling monitoring',
                                                     'Hard-coding secrets in the image'],
                                         'answer': 'B',
                                         'explain': 'Gates before traffic.'},
                                        {'lo': 1,
                                         'q': 'A deployment checklist exists to…',
                                         'choices': ['Slow teams randomly',
                                                     'Make release steps consistent and auditable',
                                                     'Replace runbooks forever',
                                                     'Skip smoke tests'],
                                         'answer': 'B',
                                         'explain': 'Checklists catch skipped critical steps.'},
                                        {'lo': 2,
                                         'q': 'Prompt versioning enables…',
                                         'choices': ['Mystery regressions',
                                                     'Pinning, comparing, and rolling back '
                                                     'specific behaviors',
                                                     'Deleting change logs',
                                                     'Skipping schemas'],
                                         'answer': 'B',
                                         'explain': 'Versions make releases reversible.'},
                                        {'lo': 2,
                                         'q': 'Schema version in a rollout matters when…',
                                         'choices': ['Clients parse structured outputs',
                                                     'You only return free text forever',
                                                     'Evals are off',
                                                     'Flags do not exist'],
                                         'answer': 'A',
                                         'explain': 'Breaking schemas break consumers.'},
                                        {'lo': 3,
                                         'q': 'Rollback triggers might include…',
                                         'choices': ['A slightly nicer font',
                                                     'Eval score drops, safety failures, or '
                                                     'user-impact spikes',
                                                     'Successful smoke tests',
                                                     'Lower cost with stable quality'],
                                         'answer': 'B',
                                         'explain': 'Predefine what “bad” means.'},
                                        {'lo': 3,
                                         'q': 'User-impact signals complement offline evals '
                                              'because…',
                                         'choices': ['Offline sets cover all live diversity '
                                                     'forever',
                                                     'Production can reveal gaps offline missed',
                                                     'Evals are useless',
                                                     'Canaries are illegal'],
                                         'answer': 'B',
                                         'explain': 'Online + offline together.'},
                                        {'lo': 4,
                                         'q': 'Smoke tests after deploy should hit…',
                                         'choices': ['Obscure dead code only',
                                                     'The most important user flows quickly',
                                                     'Nothing if CI passed once last month',
                                                     'Only the marketing site'],
                                         'answer': 'B',
                                         'explain': 'Fast confidence on critical paths.'},
                                        {'lo': 4,
                                         'q': 'A failed smoke test should…',
                                         'choices': ['Be ignored during launch parties',
                                                     'Stop rollout / trigger rollback per playbook',
                                                     'Disable alerts',
                                                     'Raise temperature'],
                                         'answer': 'B',
                                         'explain': 'Smoke fails are stop-the-line signals.'},
                                        {'lo': 5,
                                         'q': 'Shadow evaluation means…',
                                         'choices': ['Deleting prod traffic logs',
                                                     'Scoring a new version on live inputs without '
                                                     'affecting users',
                                                     'Shipping without metrics',
                                                     'Skipping privacy review'],
                                         'answer': 'B',
                                         'explain': 'Shadow = observe before expose.'},
                                        {'lo': 5,
                                         'q': 'Staged rollout without a rollback plan is risky '
                                              'because…',
                                         'choices': ['Stages are illegal',
                                                     'You may lack a fast path back to known-good',
                                                     'Smoke tests replace rollback',
                                                     'Versioning forbids rollback'],
                                         'answer': 'B',
                                         'explain': 'Progressive delivery still needs an escape '
                                                    'hatch.'}]},
 'evaluation-harness': {'title': 'Evaluation Harness',
                        'outcomes': ['Assemble golden/test sets for automated or rubric scoring.',
                                     'Run the harness repeatedly and track regressions over time.',
                                     'Produce evaluation reports that drive go/no-go decisions.'],
                        'questions': [{'lo': 1,
                                       'q': 'Golden sets are valuable because…',
                                       'choices': ['They replace all metrics',
                                                   'They provide expected outputs/labels for '
                                                   'scoring',
                                                   'They store secrets safely',
                                                   'They remove the need for rubrics'],
                                       'answer': 'B',
                                       'explain': 'Labels anchor automated and human scoring.'},
                                      {'lo': 1,
                                       'q': 'Rubric checks in a harness…',
                                       'choices': ['Cannot be partially automated',
                                                   'Turn quality dimensions into scored fields',
                                                   'Only measure latency',
                                                   'Forbid golden sets'],
                                       'answer': 'B',
                                       'explain': 'Rubrics operationalize quality.'},
                                      {'lo': 2,
                                       'q': 'Regression tracking requires…',
                                       'choices': ['Deleting old scores',
                                                   'Comparable runs on a stable case set with '
                                                   'logged versions',
                                                   'Random new cases each time only',
                                                   'No thresholds'],
                                       'answer': 'B',
                                       'explain': 'Stability enables trend detection.'},
                                      {'lo': 2,
                                       'q': 'A score drop after a prompt edit should…',
                                       'choices': ['Be celebrated blindly',
                                                   'Trigger investigation and possibly revert',
                                                   'Delete the harness',
                                                   'Disable CI'],
                                       'answer': 'B',
                                       'explain': 'Harnesses exist to catch regressions.'},
                                      {'lo': 3,
                                       'q': 'An evaluation report for release should include…',
                                       'choices': ['Only screenshots of chat',
                                                   'Metrics, failing cases, and a clear pass/fail '
                                                   'recommendation',
                                                   'API keys',
                                                   'Unrelated sprint velocity'],
                                       'answer': 'B',
                                       'explain': 'Reports support go/no-go.'},
                                      {'lo': 3,
                                       'q': 'Findings without next actions are weak because…',
                                       'choices': ['Actions are optional forever',
                                                   'Teams need mitigations or accept-risk '
                                                   'decisions',
                                                   'Harnesses forbid actions',
                                                   'Goldens replace decisions'],
                                       'answer': 'B',
                                       'explain': 'Close the loop: measure → decide → act.'},
                                      {'lo': 1,
                                       'q': 'Mixing unlabeled production samples into scoring '
                                            'without a scheme…',
                                       'choices': ['Always improves precision',
                                                   'Can bias results unless sampling/labeling is '
                                                   'controlled',
                                                   'Is required for harnesses',
                                                   'Removes variance'],
                                       'answer': 'B',
                                       'explain': 'Sampling design matters.'},
                                      {'lo': 2,
                                       'q': 'Pinning dataset and scorer versions prevents…',
                                       'choices': ['All model drift',
                                                   'Fake “improvements” from changing the test '
                                                   'itself',
                                                   'Cost tracking',
                                                   'Safety tests'],
                                       'answer': 'B',
                                       'explain': 'Don’t move the goalposts silently.'}]}}

AI_ADVANCED = {'01-system-design-for-llm-apps': {'title': 'System Design for LLM Apps',
                                   'outcomes': ['Draw architecture and data flow for an LLM '
                                                'feature including failure modes.',
                                                'Plan scaling with caches, queues, and '
                                                'backpressure for model/tool workloads.',
                                                'Define latency/quality SLOs and error budgets for '
                                                'the feature.',
                                                'Design prompt/schema migrations with backward '
                                                'compatibility.',
                                                'Apply privacy-by-design (minimization, retention, '
                                                'access control).'],
                                   'questions': [{'lo': 1,
                                                  'q': 'An LLM feature architecture diagram should '
                                                       'show…',
                                                  'choices': ['Only the marketing funnel',
                                                              'Request path, '
                                                              'model/tools/retrieval, stores, and '
                                                              'failure/fallback paths',
                                                              'Office seating',
                                                              'Font tokens'],
                                                  'answer': 'B',
                                                  'explain': 'Design for the real runtime and its '
                                                             'failures.'},
                                                 {'lo': 1,
                                                  'q': 'Listing failure modes early helps you…',
                                                  'choices': ['Skip fallbacks',
                                                              'Attach mitigations before launch',
                                                              'Avoid SLOs',
                                                              'Delete evals'],
                                                  'answer': 'B',
                                                  'explain': 'Failure modes drive resilience '
                                                             'design.'},
                                                 {'lo': 2,
                                                  'q': 'Queues in front of expensive model calls '
                                                       'provide…',
                                                  'choices': ['Unlimited concurrency forever',
                                                              'Smoothing and backpressure under '
                                                              'bursty load',
                                                              'Free quality',
                                                              'Automatic citations'],
                                                  'answer': 'B',
                                                  'explain': 'Absorb spikes; protect downstream.'},
                                                 {'lo': 2,
                                                  'q': 'Without backpressure, a viral traffic '
                                                       'spike tends to…',
                                                  'choices': ['Improve p99',
                                                              'Overwhelm workers and blow '
                                                              'cost/latency budgets',
                                                              'Fix CAP',
                                                              'Version prompts'],
                                                  'answer': 'B',
                                                  'explain': 'Unbounded admission is a reliability '
                                                             'bug.'},
                                                 {'lo': 3,
                                                  'q': 'An error budget for quality SLO means…',
                                                  'choices': ['Unlimited bad answers',
                                                              'Allowed degradation before you must '
                                                              'prioritize reliability work',
                                                              'A cache TTL',
                                                              'A threat ID'],
                                                  'answer': 'B',
                                                  'explain': 'Budgets govern ship vs fix '
                                                             'decisions.'},
                                                 {'lo': 3,
                                                  'q': 'Latency SLO without a quality SLO risks…',
                                                  'choices': ['Balanced tradeoffs',
                                                              'Optimizing speed while shipping '
                                                              'junk answers',
                                                              'Perfect RAG',
                                                              'Free privacy'],
                                                  'answer': 'B',
                                                  'explain': 'Measure both dimensions users care '
                                                             'about.'},
                                                 {'lo': 4,
                                                  'q': 'Backward-compatible prompt/schema '
                                                       'migration means…',
                                                  'choices': ['Breaking all clients at once',
                                                              'Old and new versions coexist safely '
                                                              'during rollout',
                                                              'Deleting version numbers',
                                                              'Skipping dual-read'],
                                                  'answer': 'B',
                                                  'explain': 'Compatibility windows prevent '
                                                             'cutover outages.'},
                                                 {'lo': 4,
                                                  'q': 'Changing a required JSON field name '
                                                       'without a plan…',
                                                  'choices': ['Is invisible',
                                                              'Breaks consumers mid-flight',
                                                              'Improves SLOs automatically',
                                                              'Is required for canaries'],
                                                  'answer': 'B',
                                                  'explain': 'Treat schema like an API.'},
                                                 {'lo': 5,
                                                  'q': 'Privacy-by-design for prompts/outputs '
                                                       'includes…',
                                                  'choices': ['Logging everything forever',
                                                              'Minimization, retention limits, and '
                                                              'access controls',
                                                              'Public training on private tickets '
                                                              'by default',
                                                              'Disabling redaction'],
                                                  'answer': 'B',
                                                  'explain': 'Collect less, keep less, restrict '
                                                             'access.'},
                                                 {'lo': 5,
                                                  'q': 'Access controls on retrieved docs matter '
                                                       'because…',
                                                  'choices': ['RAG ignores permissions',
                                                              'Otherwise users can read neighbors’ '
                                                              'private content via the model',
                                                              'Embeddings encrypt data',
                                                              'SLOs replace ACLs'],
                                                  'answer': 'B',
                                                  'explain': 'Retrieval must enforce '
                                                             'authorization.'}]},
 '02-rag-advanced-retrieval': {'title': 'RAG: Advanced Retrieval',
                               'outcomes': ['Evaluate retrieval with hit-rate, groundedness, and '
                                            'abstention metrics.',
                                            'Compare chunking strategies with measured tradeoffs.',
                                            'Add reranking and quantify lift on a fixed question '
                                            'set.',
                                            'Enforce access-control-aware retrieval to prevent '
                                            'leakage.',
                                            'Test freshness so new docs become retrievable within '
                                            'a target window.'],
                               'questions': [{'lo': 1,
                                              'q': 'Separating hit-rate from groundedness tells '
                                                   'you…',
                                              'choices': ['Nothing useful',
                                                          'Whether misses are retrieval or '
                                                          'generation problems',
                                                          'Only cost',
                                                          'Only latency'],
                                              'answer': 'B',
                                              'explain': 'Split metrics guide fixes.'},
                                             {'lo': 1,
                                              'q': 'High abstention with high hit-rate may mean…',
                                              'choices': ['Perfect system',
                                                          'Over-strict grounding or poor evidence '
                                                          'use in generation',
                                                          'Index corruption only',
                                                          'TLS failure'],
                                              'answer': 'B',
                                              'explain': 'Interpret metric pairs, not single '
                                                         'numbers.'},
                                             {'lo': 2,
                                              'q': 'Comparing two chunking strategies requires…',
                                              'choices': ['Vibes',
                                                          'The same question set and recorded '
                                                          'metrics',
                                                          'Deleting metadata',
                                                          'Disabling rerank'],
                                              'answer': 'B',
                                              'explain': 'Controlled A/B on retrieval units.'},
                                             {'lo': 2,
                                              'q': 'Huge chunks often hurt because…',
                                              'choices': ['They always fit context',
                                                          'Irrelevant text dilutes retrieval and '
                                                          'context windows',
                                                          'Metadata becomes richer automatically',
                                                          'ACLs improve'],
                                              'answer': 'B',
                                              'explain': 'Chunk size is a relevance/context '
                                                         'tradeoff.'},
                                             {'lo': 3,
                                              'q': 'Reranking helps when…',
                                              'choices': ['First-stage retrieval is perfect '
                                                          'forever',
                                                          'Top-n candidates need relevance '
                                                          'reordering before generation',
                                                          'You want to skip citations',
                                                          'Freshness is irrelevant'],
                                              'answer': 'B',
                                              'explain': 'Rerank refines candidate lists.'},
                                             {'lo': 3,
                                              'q': 'Measure rerank lift by…',
                                              'choices': ['Shipping without numbers',
                                                          'Diffing metrics on a fixed question set '
                                                          'with/without rerank',
                                                          'Only watching GPU fans',
                                                          'Changing the question set each trial'],
                                              'answer': 'B',
                                              'explain': 'Hold the set constant.'},
                                             {'lo': 4,
                                              'q': 'ACL-aware retrieval means…',
                                              'choices': ['Search all docs then hope the model '
                                                          'filters',
                                                          'Only retrieve documents the caller is '
                                                          'allowed to see',
                                                          'Encrypt embeddings with ROT13',
                                                          'Disable metadata'],
                                              'answer': 'B',
                                              'explain': 'Filter at retrieval time, not after '
                                                         'generation.'},
                                             {'lo': 4,
                                              'q': 'Leakage across permissions is a…',
                                              'choices': ['Cosmetic bug',
                                                          'Security/privacy incident class for RAG',
                                                          'Latency optimization',
                                                          'Canary feature'],
                                              'answer': 'B',
                                              'explain': 'Treat cross-tenant retrieval as a breach '
                                                         'path.'},
                                             {'lo': 5,
                                              'q': 'Freshness tests verify…',
                                              'choices': ['Old docs remain forever unfindable',
                                                          'Newly added docs become retrievable '
                                                          'within an agreed window',
                                                          'Embeddings never update',
                                                          'Rerank is off'],
                                              'answer': 'B',
                                              'explain': 'Index lag is a product bug for many '
                                                         'domains.'},
                                             {'lo': 1,
                                              'q': 'Groundedness scoring checks…',
                                              'choices': ['Whether claims are supported by '
                                                          'retrieved evidence',
                                                          'Only JSON braces',
                                                          'Only token price',
                                                          'Only p99 latency'],
                                              'answer': 'A',
                                              'explain': 'Groundedness is evidence alignment.'}]},
 '03-evals-at-scale': {'title': 'Evals at Scale',
                       'outcomes': ['Design batch eval runners with retries, budgets, and '
                                    'reproducibility.',
                                    'Detect quality drift with stratified sampling and cadence.',
                                    'Define stop-the-line criteria for regressions.',
                                    'Run privacy-safe shadow evaluation on live traffic.',
                                    'Operate human labeling with calibration across raters.'],
                       'questions': [{'lo': 1,
                                      'q': 'A scalable eval runner should log…',
                                      'choices': ['Nothing',
                                                  'Dataset, prompt, scorer versions plus '
                                                  'budgets/retries',
                                                  'Only wall time',
                                                  'Production passwords'],
                                      'answer': 'B',
                                      'explain': 'Reproducibility at scale needs provenance.'},
                                     {'lo': 1,
                                      'q': 'Batching evals primarily helps…',
                                      'choices': ['Hide failures',
                                                  'Throughput and cost control for large sets',
                                                  'Delete stratification',
                                                  'Skip gates'],
                                      'answer': 'B',
                                      'explain': 'Scale the mechanics, not just the set size.'},
                                     {'lo': 2,
                                      'q': 'Stratified sampling matters because…',
                                      'choices': ['All users are identical',
                                                  'Overall averages can hide regressions in a '
                                                  'segment',
                                                  'Drift cannot exist',
                                                  'Labels are free'],
                                      'answer': 'B',
                                      'explain': 'Segments reveal localized failures.'},
                                     {'lo': 2,
                                      'q': 'A drift metric without a cadence is weak because…',
                                      'choices': ['Cadence is optional decoration',
                                                  'You will not notice slow quality decay in time',
                                                  'Shadow evals forbid cadence',
                                                  'Budgets replace monitoring'],
                                      'answer': 'B',
                                      'explain': 'Schedule the checks.'},
                                     {'lo': 3,
                                      'q': 'Stop-the-line criteria should be…',
                                      'choices': ['Invented during the outage',
                                                  'Predeclared thresholds that halt releases',
                                                  'Secret from eng',
                                                  'Only aesthetic'],
                                      'answer': 'B',
                                      'explain': 'Gates need prior agreement.'},
                                     {'lo': 3,
                                      'q': 'A sudden schema-validity collapse should…',
                                      'choices': ['Ship anyway',
                                                  'Trip stop-the-line and rollback/investigate',
                                                  'Raise temperature',
                                                  'Delete the dataset'],
                                      'answer': 'B',
                                      'explain': 'Hard quality cliffs are release blockers.'},
                                     {'lo': 4,
                                      'q': 'Shadow eval on live traffic must be…',
                                      'choices': ['Logged with full sensitive payloads publicly',
                                                  'Privacy-safe (minimize/redact) and '
                                                  'non-user-impacting',
                                                  'Allowed to change user answers',
                                                  'Unversioned'],
                                      'answer': 'B',
                                      'explain': 'Observe without exposing users or PII.'},
                                     {'lo': 4,
                                      'q': 'Shadow scoring a new prompt helps you…',
                                      'choices': ['Skip offline sets forever',
                                                  'Estimate live impact before progressive '
                                                  'delivery',
                                                  'Avoid canaries',
                                                  'Disable labeling'],
                                      'answer': 'B',
                                      'explain': 'Bridge offline and online confidence.'},
                                     {'lo': 5,
                                      'q': 'Rater calibration reduces…',
                                      'choices': ['Dataset size needs',
                                                  'Inconsistent human scores that muddy drift '
                                                  'signals',
                                                  'The need for automation',
                                                  'Budgets'],
                                      'answer': 'B',
                                      'explain': 'Humans need shared standards.'},
                                     {'lo': 5,
                                      'q': 'A labeling workflow should include…',
                                      'choices': ['One rater forever with no guide',
                                                  'Guidelines, examples, and periodic agreement '
                                                  'checks',
                                                  'Public posting of raw customer text',
                                                  'No audit trail'],
                                      'answer': 'B',
                                      'explain': 'Process quality → label quality.'}]},
 '04-security-threat-modeling-llm': {'title': 'Security Threat Modeling for LLM Apps',
                                     'outcomes': ['Produce a threat model with mitigations for an '
                                                  'LLM app.',
                                                  'Build red-team suites targeting top threats '
                                                  '(injection, tool abuse).',
                                                  'Enforce least-privilege tool policies verified '
                                                  'by tests.',
                                                  'Apply data minimization and retention to '
                                                  'prompts/outputs.',
                                                  'Plan incident response and supply-chain '
                                                  'controls for AI artifacts.'],
                                     'questions': [{'lo': 1,
                                                    'q': 'Threat modeling an agent should list…',
                                                    'choices': ['Only UX colors',
                                                                'Assets, attackers, abuse paths, '
                                                                'and mitigations',
                                                                'Font pairings',
                                                                'Canary percentages only'],
                                                    'answer': 'B',
                                                    'explain': 'Structured threats → prioritized '
                                                               'controls.'},
                                                   {'lo': 1,
                                                    'q': 'Tool abuse as a threat means…',
                                                    'choices': ['Tools never fail',
                                                                'Attackers coerce the agent into '
                                                                'harmful side effects',
                                                                'Retrieval is perfect',
                                                                'Evals are offline only'],
                                                    'answer': 'B',
                                                    'explain': 'Agents + tools = actionable attack '
                                                               'surface.'},
                                                   {'lo': 2,
                                                    'q': 'Red-team suites should map to…',
                                                    'choices': ['Random jokes',
                                                                'Top threats from the model',
                                                                'Only latency cases',
                                                                'CDN purge tests'],
                                                    'answer': 'B',
                                                    'explain': 'Tests follow the threat model.'},
                                                   {'lo': 2,
                                                    'q': 'Injection that tries to exfiltrate '
                                                         'secrets should expect…',
                                                    'choices': ['Compliance',
                                                                'Containment/refusal and no secret '
                                                                'leakage',
                                                                'Higher privileges',
                                                                'Disabled audits'],
                                                    'answer': 'B',
                                                    'explain': 'Security tests assert negative '
                                                               'outcomes.'},
                                                   {'lo': 3,
                                                    'q': 'Least-privilege tool policy is verified '
                                                         'by…',
                                                    'choices': ['Documentation alone',
                                                                'Tests that attempt disallowed '
                                                                'tools/args and expect denial',
                                                                'Turning off AuthZ',
                                                                'Logging secrets'],
                                                    'answer': 'B',
                                                    'explain': 'Prove the policy holds.'},
                                                   {'lo': 3,
                                                    'q': 'Over-broad tools increase…',
                                                    'choices': ['Safety',
                                                                'Blast radius when injection '
                                                                'succeeds',
                                                                'Groundedness',
                                                                'Cache hit rate'],
                                                    'answer': 'B',
                                                    'explain': 'Privilege amplifies compromise.'},
                                                   {'lo': 4,
                                                    'q': 'Retention rules for prompts/outputs '
                                                         'reduce…',
                                                    'choices': ['All model errors',
                                                                'Long-term exposure of sensitive '
                                                                'content',
                                                                'The need for ACLs',
                                                                'Eval versioning'],
                                                    'answer': 'B',
                                                    'explain': 'Minimize how long risk lives.'},
                                                   {'lo': 4,
                                                    'q': 'Data minimization says…',
                                                    'choices': ['Send entire customer histories by '
                                                                'default',
                                                                'Collect/process only what the '
                                                                'task needs',
                                                                'Log raw PANs for convenience',
                                                                'Train publicly on private tickets '
                                                                'without review'],
                                                    'answer': 'B',
                                                    'explain': 'Less data → less breach impact.'},
                                                   {'lo': 5,
                                                    'q': 'Supply-chain policy for prompts/evals '
                                                         'covers…',
                                                    'choices': ['Only npm logos',
                                                                'Integrity/ownership of prompt '
                                                                'packs, datasets, and scorers',
                                                                'Office Wi-Fi SSIDs',
                                                                'Font licenses only'],
                                                    'answer': 'B',
                                                    'explain': 'AI artifacts are part of the '
                                                               'trusted compute base.'},
                                                   {'lo': 5,
                                                    'q': 'Incident response for a prompt-injection '
                                                         'breach should include…',
                                                    'choices': ['Silence',
                                                                'Triage, containment (flags/tool '
                                                                'lockdown), and follow-up '
                                                                'hardening',
                                                                'Raising temperature',
                                                                'Deleting threat models'],
                                                    'answer': 'B',
                                                    'explain': 'Security IR applies to LLM apps '
                                                               'too.'}]},
 '05-observability-and-monitoring-llm': {'title': 'Observability and Monitoring for LLM Apps',
                                         'outcomes': ['Define SLIs/SLOs for quality, safety, cost, '
                                                      'and latency.',
                                                      'Design dashboards and alert thresholds '
                                                      'operators can act on.',
                                                      'Trace multi-step LLM flows (retrieval, '
                                                      'generation, tools).',
                                                      'Sample quality safely (privacy-preserving) '
                                                      'with escalation paths.',
                                                      'Run continuous canary evaluation in '
                                                      'production.'],
                                         'questions': [{'lo': 1,
                                                        'q': 'LLM SLIs often include…',
                                                        'choices': ['Only CPU temperature',
                                                                    'Success/groundedness proxies, '
                                                                    'safety hits, latency, cost',
                                                                    'Git blame counts',
                                                                    'Office occupancy'],
                                                        'answer': 'B',
                                                        'explain': 'User-visible and operational '
                                                                   'signals together.'},
                                                       {'lo': 1,
                                                        'q': 'Mapping SLOs to metrics ensures…',
                                                        'choices': ['Pretty charts without '
                                                                    'decisions',
                                                                    'Error budgets and alerts '
                                                                    'attach to real targets',
                                                                    'Traces are optional forever',
                                                                    'Canaries are banned'],
                                                        'answer': 'B',
                                                        'explain': 'SLOs without metrics are '
                                                                   'slogans.'},
                                                       {'lo': 2,
                                                        'q': 'Alert thresholds should be…',
                                                        'choices': ['So sensitive every blip pages',
                                                                    'Tied to user impact / budget '
                                                                    'burn and actionable',
                                                                    'Hidden from on-call',
                                                                    'Based only on vanity KPIs'],
                                                        'answer': 'B',
                                                        'explain': 'Hygiene beats noise.'},
                                                       {'lo': 2,
                                                        'q': 'A dashboard without owners…',
                                                        'choices': ['Still pages usefully',
                                                                    'Tends to rot; assign '
                                                                    'responders per signal',
                                                                    'Replaces runbooks',
                                                                    'Fixes drift'],
                                                        'answer': 'B',
                                                        'explain': 'Observability needs '
                                                                   'operational ownership.'},
                                                       {'lo': 3,
                                                        'q': 'Tracing retrieval → generation → '
                                                             'tools shows…',
                                                        'choices': ['Only DNS',
                                                                    'Where latency and failures '
                                                                    'occur in the LLM pipeline',
                                                                    'Font metrics',
                                                                    'Threat models'],
                                                        'answer': 'B',
                                                        'explain': 'Spans localize bottlenecks.'},
                                                       {'lo': 3,
                                                        'q': 'Missing trace context between '
                                                             'retrieval and generation…',
                                                        'choices': ['Is fine',
                                                                    'Breaks end-to-end latency '
                                                                    'diagnosis',
                                                                    'Improves groundedness',
                                                                    'Reduces cardinality issues'],
                                                        'answer': 'B',
                                                        'explain': 'Propagate context across '
                                                                   'steps.'},
                                                       {'lo': 4,
                                                        'q': 'Privacy-safe quality sampling means…',
                                                        'choices': ['Dumping raw tickets to public '
                                                                    'Slack',
                                                                    'Redacting/minimizing content '
                                                                    'while still scoring subsets',
                                                                    'Never sampling',
                                                                    'Storing secrets longer'],
                                                        'answer': 'B',
                                                        'explain': 'Learn quality without '
                                                                   'leaking.'},
                                                       {'lo': 4,
                                                        'q': 'Escalation for quality drop should '
                                                             'be documented so…',
                                                        'choices': ['On-call improvises each time',
                                                                    'Responders know when to '
                                                                    'flag/rollback/page '
                                                                    'specialists',
                                                                    'Metrics are deleted',
                                                                    'Canaries continue blindly'],
                                                        'answer': 'B',
                                                        'explain': 'Playbooks attach to signals.'},
                                                       {'lo': 5,
                                                        'q': 'Continuous canary eval…',
                                                        'choices': ['Replaces all offline sets',
                                                                    'Detects live regressions '
                                                                    'early on a small cohort',
                                                                    'Guarantees zero cost',
                                                                    'Disables SLOs'],
                                                        'answer': 'B',
                                                        'explain': 'Always-on progressive '
                                                                   'checking.'},
                                                       {'lo': 5,
                                                        'q': 'Monitoring must verify fallbacks '
                                                             'because…',
                                                        'choices': ['Fallbacks never fail',
                                                                    'Broken fallbacks can silently '
                                                                    'degrade UX or safety',
                                                                    'Alerts forbid fallbacks',
                                                                    'Traces replace fallbacks'],
                                                        'answer': 'B',
                                                        'explain': 'Watch the safety nets too.'}]},
 '06-reliability-and-fallbacks': {'title': 'Reliability and Fallbacks',
                                  'outcomes': ['Define fallbacks per top failure mode (model, '
                                               'retrieval, tools).',
                                               'Set retry budgets and stop conditions for degraded '
                                               'paths.',
                                               'Failure-inject outages/timeouts in the harness.',
                                               'Specify degraded modes: abstain, ask, cached '
                                               'answer, human queue.',
                                               'Run post-incident reviews that harden evals and '
                                               'guardrails.'],
                                  'questions': [{'lo': 1,
                                                 'q': 'Model-down fallback might be…',
                                                 'choices': ['Hang the UI forever',
                                                             'Cached answer, smaller model, or '
                                                             'human handoff',
                                                             'Disable all monitoring',
                                                             'Invent success'],
                                                 'answer': 'B',
                                                 'explain': 'Degrade explicitly per mode.'},
                                                {'lo': 1,
                                                 'q': 'Empty retrieval fallback should…',
                                                 'choices': ['Hallucinate confidently',
                                                             'Abstain/ask rather than fabricate',
                                                             'Call admin tools',
                                                             'Raise budgets infinitely'],
                                                 'answer': 'B',
                                                 'explain': 'No evidence → no invented answer.'},
                                                {'lo': 2,
                                                 'q': 'Retry budgets on tool errors prevent…',
                                                 'choices': ['All outages',
                                                             'Unbounded cost and delayed failure '
                                                             'signals',
                                                             'Human queues',
                                                             'Cached answers'],
                                                 'answer': 'B',
                                                 'explain': 'Bound recovery attempts.'},
                                                {'lo': 2,
                                                 'q': 'Stop conditions in degraded mode…',
                                                 'choices': ['Are optional flair',
                                                             'Ensure the system does not thrash '
                                                             'forever',
                                                             'Forbid abstention',
                                                             'Delete runbooks'],
                                                 'answer': 'B',
                                                 'explain': 'Know when to quit.'},
                                                {'lo': 3,
                                                 'q': 'Failure injection in harnesses proves…',
                                                 'choices': ['Only happy paths',
                                                             'Fallbacks actually trigger and '
                                                             'behave safely',
                                                             'SLOs are unnecessary',
                                                             'Caches never expire'],
                                                 'answer': 'B',
                                                 'explain': 'Test the dark paths.'},
                                                {'lo': 3,
                                                 'q': 'Simulating timeouts without assertions…',
                                                 'choices': ['Fully validates resilience',
                                                             'Misses whether fallbacks ran '
                                                             'correctly',
                                                             'Replaces IR',
                                                             'Fixes drift'],
                                                 'answer': 'B',
                                                 'explain': 'Inject and assert.'},
                                                {'lo': 4,
                                                 'q': 'Human-in-the-loop queues need…',
                                                 'choices': ['No SLA',
                                                             'Clear routing, SLA, and escalation',
                                                             'Automatic approval of all risks',
                                                             'Secret-only tickets'],
                                                 'answer': 'B',
                                                 'explain': 'Humans are a capacity-limited '
                                                            'dependency.'},
                                                {'lo': 4,
                                                 'q': 'Cached answers as degraded mode require…',
                                                 'choices': ['Ignoring staleness forever',
                                                             'Freshness/validity rules so wrong '
                                                             'cache is not “reliability”',
                                                             'No version keys',
                                                             'Disabling abstain'],
                                                 'answer': 'B',
                                                 'explain': 'Stale cache can be worse than '
                                                            'abstain.'},
                                                {'lo': 5,
                                                 'q': 'Post-incident reviews should update…',
                                                 'choices': ['Nothing if users calmed down',
                                                             'Evals, guardrails, and runbooks to '
                                                             'prevent repeats',
                                                             'Only the logo',
                                                             'Temperature defaults randomly'],
                                                 'answer': 'B',
                                                 'explain': 'Convert pain into controls.'},
                                                {'lo': 5,
                                                 'q': 'A fallback strategy tied to SLOs means…',
                                                 'choices': ['Fallbacks are aesthetic',
                                                             'You know when degraded mode is '
                                                             'acceptable vs stop-the-line',
                                                             'Retries are unlimited',
                                                             'Shadow evals are banned'],
                                                 'answer': 'B',
                                                 'explain': 'Budgets frame degradation choices.'}]},
 '07-data-governance-and-privacy': {'title': 'Data Governance and Privacy',
                                    'outcomes': ['Write data-handling policies for what is stored, '
                                                 'why, and how long.',
                                                 'Implement and test PII redaction on '
                                                 'inputs/outputs.',
                                                 'Enforce permission-aware retrieval and '
                                                 'no-leakage tests.',
                                                 'Design safe logging schemas that avoid raw '
                                                 'sensitive text.',
                                                 'Add privacy review checklists to release '
                                                 'process.'],
                                    'questions': [{'lo': 1,
                                                   'q': 'A data handling policy should answer…',
                                                   'choices': ['Only “we care about privacy”',
                                                               'What is stored, purpose, '
                                                               'retention, and who can access',
                                                               'Preferred IDE themes',
                                                               'Canary math'],
                                                   'answer': 'B',
                                                   'explain': 'Concrete policy beats slogans.'},
                                                  {'lo': 1,
                                                   'q': 'Purpose limitation means…',
                                                   'choices': ['Reuse data for any future idea '
                                                               'silently',
                                                               'Use collected data only for stated '
                                                               'purposes',
                                                               'Log everything publicly',
                                                               'Skip retention'],
                                                   'answer': 'B',
                                                   'explain': 'Purpose binds processing.'},
                                                  {'lo': 2,
                                                   'q': 'Redaction tests should include…',
                                                   'choices': ['Only empty strings',
                                                               'Samples where PII must not appear '
                                                               'in outputs/logs',
                                                               'Only latency cases',
                                                               'Only schema braces'],
                                                   'answer': 'B',
                                                   'explain': 'Negative cases prove redaction.'},
                                                  {'lo': 2,
                                                   'q': 'Redacting in the UI but logging raw text…',
                                                   'choices': ['Fully solves privacy',
                                                               'Leaves a major leak channel',
                                                               'Improves groundedness',
                                                               'Is required for traces'],
                                                   'answer': 'B',
                                                   'explain': 'Protect all channels.'},
                                                  {'lo': 3,
                                                   'q': 'No-leakage tests for RAG verify…',
                                                   'choices': ['Users can read any tenant’s docs',
                                                               'Unauthorized docs never appear in '
                                                               'context/answers',
                                                               'Embeddings are public',
                                                               'ACLs are optional'],
                                                   'answer': 'B',
                                                   'explain': 'AuthZ belongs in retrieval tests.'},
                                                  {'lo': 3,
                                                   'q': 'Permission metadata on chunks enables…',
                                                   'choices': ['Slower disks only',
                                                               'Filtering retrieval by caller '
                                                               'rights',
                                                               'Automatic encryption keys in '
                                                               'prompts',
                                                               'Higher temperature'],
                                                   'answer': 'B',
                                                   'explain': 'Metadata drives ACL filters.'},
                                                  {'lo': 4,
                                                   'q': 'Safe logging schemas typically store…',
                                                   'choices': ['Full prompts with secrets',
                                                               'IDs, categories, hashes/redacted '
                                                               'snippets — not raw secrets',
                                                               'PANs for convenience',
                                                               'Session cookies'],
                                                   'answer': 'B',
                                                   'explain': 'Minimize sensitive telemetry.'},
                                                  {'lo': 4,
                                                   'q': 'Audit queries (“who accessed what”) '
                                                        'support…',
                                                   'choices': ['Only marketing',
                                                               'Accountability and incident '
                                                               'investigation',
                                                               'Faster GPUs',
                                                               'Reranking'],
                                                   'answer': 'B',
                                                   'explain': 'Governance needs auditability.'},
                                                  {'lo': 5,
                                                   'q': 'Privacy review in releases catches…',
                                                   'choices': ['Font issues',
                                                               'New data flows that expand '
                                                               'retention or exposure',
                                                               'Only unit test names',
                                                               'CDN TTLs'],
                                                   'answer': 'B',
                                                   'explain': 'Ship checks for data risk.'},
                                                  {'lo': 5,
                                                   'q': '“Data should not appear” negative tests '
                                                        'are critical because…',
                                                   'choices': ['Absence is hard to notice without '
                                                               'assertions',
                                                               'Presence tests suffice always',
                                                               'Policies forbid tests',
                                                               'Redaction is optional'],
                                                   'answer': 'A',
                                                   'explain': 'Assert non-presence explicitly.'}]},
 '08-production-incident-playbooks': {'title': 'Production Incident Playbooks',
                                      'outcomes': ['Write playbooks for cost spikes, safety '
                                                   'regressions, and quality drops.',
                                                   'Define immediate mitigations: flags, degrade '
                                                   'modes, stricter filters.',
                                                   'Run incident drills that exercise detection '
                                                   'and response.',
                                                   'Prepare internal and user-facing communication '
                                                   'templates.',
                                                   'Close the loop by updating evals and '
                                                   'guardrails after incidents.'],
                                      'questions': [{'lo': 1,
                                                     'q': 'A cost-spike playbook’s first '
                                                          'mitigations often include…',
                                                     'choices': ['Ignoring dashboards',
                                                                 'Rate limits, disabling expensive '
                                                                 'paths, or rolling back a canary',
                                                                 'Raising temperature',
                                                                 'Deleting budgets'],
                                                     'answer': 'B',
                                                     'explain': 'Stop the bleeding on spend.'},
                                                    {'lo': 1,
                                                     'q': 'A safety-regression playbook should '
                                                          'prioritize…',
                                                     'choices': ['New features',
                                                                 'Containment (stricter '
                                                                 'filters/flags off) before deep '
                                                                 'debugging',
                                                                 'Silence',
                                                                 'Higher tool privileges'],
                                                     'answer': 'B',
                                                     'explain': 'Safety first, then root cause.'},
                                                    {'lo': 2,
                                                     'q': 'Feature flags in incidents enable…',
                                                     'choices': ['Slower mitigations',
                                                                 'Fast disable of risky behavior '
                                                                 'without full redeploy',
                                                                 'Secret leakage',
                                                                 'Skipping drills'],
                                                     'answer': 'B',
                                                     'explain': 'Flags are kill switches.'},
                                                    {'lo': 2,
                                                     'q': 'Degraded mode during an incident should '
                                                          'be…',
                                                     'choices': ['Undefined',
                                                                 'Predeclared so operators know '
                                                                 'the safe subset of behavior',
                                                                 'Identical to normal mode',
                                                                 'Hidden from users always without '
                                                                 'notice when needed'],
                                                     'answer': 'B',
                                                     'explain': 'Know the safe subset in advance.'},
                                                    {'lo': 3,
                                                     'q': 'Incident drills matter because…',
                                                     'choices': ['Playbooks are self-executing',
                                                                 'Practice reveals gaps in '
                                                                 'detection and steps under time '
                                                                 'pressure',
                                                                 'They replace monitoring',
                                                                 'They delete templates'],
                                                     'answer': 'B',
                                                     'explain': 'Drill → improve playbooks.'},
                                                    {'lo': 3,
                                                     'q': 'A drill that never triggers alerts '
                                                          'shows…',
                                                     'choices': ['Perfect detection',
                                                                 'A detection gap to fix',
                                                                 'That playbooks are unnecessary',
                                                                 'That cost spikes are impossible'],
                                                     'answer': 'B',
                                                     'explain': 'Detection is part of the '
                                                                'playbook.'},
                                                    {'lo': 4,
                                                     'q': 'Communication templates reduce…',
                                                     'choices': ['Clarity',
                                                                 'Ad-hoc conflicting messages '
                                                                 'during stress',
                                                                 'The need for mitigations',
                                                                 'Eval updates'],
                                                     'answer': 'B',
                                                     'explain': 'Say the right thing quickly.'},
                                                    {'lo': 4,
                                                     'q': 'User-facing incident notes should…',
                                                     'choices': ['Include internal secrets',
                                                                 'Be accurate, calm, and '
                                                                 'actionable without oversharing',
                                                                 'Blame individuals',
                                                                 'Promise impossible ETAs '
                                                                 'casually'],
                                                     'answer': 'B',
                                                     'explain': 'Honest, careful communication.'},
                                                    {'lo': 5,
                                                     'q': 'After action items should include…',
                                                     'choices': ['Nothing if mitigated',
                                                                 'New eval cases and tighter '
                                                                 'guardrails for the failure mode',
                                                                 'Only a pizza party',
                                                                 'Deleting metrics'],
                                                     'answer': 'B',
                                                     'explain': 'Turn incidents into permanent '
                                                                'controls.'},
                                                    {'lo': 5,
                                                     'q': 'Updating evals post-incident prevents…',
                                                     'choices': ['All future bugs',
                                                                 'The same failure class from '
                                                                 'shipping unnoticed again',
                                                                 'Canaries',
                                                                 'Shadow evaluation'],
                                                     'answer': 'B',
                                                     'explain': 'Regression tests for production '
                                                                'pain.'}]},
 'optimization-safety': {'title': 'Optimization and Safety',
                         'outcomes': ['Budget cost and latency without sacrificing required safety '
                                      'checks.',
                                      'Apply caching/reuse only when correctness and privacy '
                                      'allow.',
                                      'Plan safety evaluations and red-teaming alongside '
                                      'performance work.'],
                         'questions': [{'lo': 1,
                                        'q': 'Cutting tokens by removing safety instructions is…',
                                        'choices': ['A valid optimization',
                                                    'Unsafe — keep required policy checks even '
                                                    'under budget pressure',
                                                    'Required for SLOs',
                                                    'Fine if latency improves'],
                                        'answer': 'B',
                                        'explain': 'Do not optimize away safety.'},
                                       {'lo': 1,
                                        'q': 'A cost plan should state…',
                                        'choices': ['Only vibes',
                                                    'Budgets, enforcement, and what quality/safety '
                                                    'must not regress',
                                                    'Unlimited spend',
                                                    'No metrics'],
                                        'answer': 'B',
                                        'explain': 'Budgets need hard constraints and '
                                                   'non-negotiables.'},
                                       {'lo': 2,
                                        'q': 'Caching model outputs is inappropriate when…',
                                        'choices': ['Answers are identical and non-sensitive',
                                                    'Outputs are user-specific/sensitive or must '
                                                    'reflect fresh private data',
                                                    'Prompt versions are keyed',
                                                    'TTLs are short and validated'],
                                        'answer': 'B',
                                        'explain': 'Privacy and freshness gate caching.'},
                                       {'lo': 2,
                                        'q': 'Reuse strategies should document…',
                                        'choices': ['Nothing',
                                                    'Cache keys, invalidation, and sensitivity '
                                                    'rules',
                                                    'Only hit-rate dreams',
                                                    'How to skip red-teams'],
                                        'answer': 'B',
                                        'explain': 'Operationalize safe reuse.'},
                                       {'lo': 3,
                                        'q': 'Performance work without safety evals risks…',
                                        'choices': ['Balanced launches',
                                                    'Faster, cheaper, more dangerous systems',
                                                    'Automatic threat models',
                                                    'Perfect groundedness'],
                                        'answer': 'B',
                                        'explain': 'Optimize with red-team gates.'},
                                       {'lo': 3,
                                        'q': 'A safety assessment summary for optimization should '
                                             'include…',
                                        'choices': ['Only speedups',
                                                    'What was changed, residual risks, and eval '
                                                    'evidence',
                                                    'API keys',
                                                    'Unrelated OKRs'],
                                        'answer': 'B',
                                        'explain': 'Evidence that safety still holds.'},
                                       {'lo': 1,
                                        'q': 'Latency wins that increase jailbreak success should…',
                                        'choices': ['Ship immediately',
                                                    'Be rejected or redesigned until safety gates '
                                                    'pass',
                                                    'Ignore red-teams',
                                                    'Disable abstention'],
                                        'answer': 'B',
                                        'explain': 'Safety is a release constraint.'},
                                       {'lo': 2,
                                        'q': 'Shared caches across tenants without isolation…',
                                        'choices': ['Are always fine',
                                                    'Risk cross-tenant data leakage',
                                                    'Improve ACLs',
                                                    'Replace encryption'],
                                        'answer': 'B',
                                        'explain': 'Isolation is a caching safety rule.'}]}}

BANKS = {
    ("*", "intermediate"): INTERMEDIATE,
    ("*", "advanced"): ADVANCED,
    ("ai", "beginner"): AI_BEGINNER,
    ("ai", "intermediate"): AI_INTERMEDIATE,
    ("ai", "advanced"): AI_ADVANCED,
}
