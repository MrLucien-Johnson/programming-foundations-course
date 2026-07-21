/**
 * Shared helpers for Programming Foundations site UX.
 * Progress keys, shared header, auth, and cloud sync live here.
 */
(function (global) {
  const PASS_THRESHOLD = 0.7;
  const KEYS = {
    completions: "course-completions",
    quizCompletions: "quiz-completions",
    startSteps: "pf-start-steps",
    authToken: "pf-auth-token",
    authUser: "pf-auth-user",
  };

  const START_STEP_ORDER = ["open-online", "choose-course", "keep-learning", "download-local"];

  const NAV_LINKS = [
    { href: "index.html", label: "Home" },
    { href: "start-here.html", label: "Start Here" },
    { href: "courses.html", label: "Courses" },
    { href: "guides.html", label: "Guides" },
    { href: "help.html", label: "Help" },
    { href: "support.html", label: "Support" },
    { href: "account.html", label: "Account" },
  ];

  const getDonateConfig = () => {
    const cfg = global.PF_CONFIG || {};
    const url = String(cfg.donateUrl || "").trim();
    const label = String(cfg.donateLabel || "Donate").trim() || "Donate";
    return { url, label, enabled: Boolean(url) };
  };

  /** Fill [data-pf-donate-slot] with a donate button when config.donateUrl is set. */
  const mountDonateSlots = () => {
    const { url, label, enabled } = getDonateConfig();
    document.querySelectorAll("[data-pf-donate-slot]").forEach((slot) => {
      if (!enabled) return;
      const existing = slot.querySelector("[data-pf-donate-btn]");
      if (existing) {
        existing.href = url;
        existing.textContent = label;
        return;
      }
      const anchor = document.createElement("a");
      anchor.className = "btn btn-primary";
      anchor.href = url;
      anchor.target = "_blank";
      anchor.rel = "noopener noreferrer";
      anchor.dataset.pfDonateBtn = "1";
      anchor.textContent = label;
      slot.prepend(anchor);
    });
    const status = document.getElementById("donate-status");
    if (status && enabled) {
      status.textContent =
        "Thank you — donations help keep this course free and fund more reliable hosting when we can.";
    }
  };

  const COURSE_MODULE_MAP = {
    "Python Course": [
      "python-beginner-workbook/module-01-setup/README.md",
      "python-beginner-workbook/module-02-basics/README.md",
      "python-beginner-workbook/module-03-control-flow/README.md",
      "python-beginner-workbook/module-04-functions/README.md",
      "python-beginner-workbook/module-05-collections/README.md",
      "python-beginner-workbook/module-06-oop/README.md",
      "python-beginner-workbook/module-07-task-tracker/README.md",
    ],
    "C# Course": [
      "csharp-beginner-workbook/module-01-setup/README.md",
      "csharp-beginner-workbook/module-02-basics/README.md",
      "csharp-beginner-workbook/module-03-control-flow/README.md",
      "csharp-beginner-workbook/module-04-methods/README.md",
      "csharp-beginner-workbook/module-05-collections/README.md",
      "csharp-beginner-workbook/module-06-oop-intro/README.md",
      "csharp-beginner-workbook/module-07-task-tracker/README.md",
    ],
    "AI Prompt Creation Course": [
      "languages/ai/beginner/modules/01-ai-foundations.md",
      "languages/ai/beginner/modules/02-prompting-basics.md",
      "languages/ai/beginner/modules/03-prompt-patterns.md",
      "languages/ai/beginner/modules/04-evaluation-and-iteration.md",
      "languages/ai/beginner/modules/05-safety-and-policy-basics.md",
      "languages/ai/beginner/modules/06-workflows-and-automation.md",
      "languages/ai/intermediate/modules/01-advanced-prompting-tool-use.md",
      "languages/ai/intermediate/modules/02-structured-outputs-and-schemas.md",
      "languages/ai/intermediate/modules/03-rag-foundations.md",
      "languages/ai/intermediate/modules/04-model-evaluation-and-testing.md",
      "languages/ai/intermediate/modules/05-guardrails-and-safety.md",
      "languages/ai/intermediate/modules/06-agentic-workflows.md",
      "languages/ai/intermediate/modules/07-cost-latency-and-ops.md",
      "languages/ai/intermediate/modules/08-deployment-basics.md",
      "languages/ai/advanced/modules/01-system-design-for-llm-apps.md",
      "languages/ai/advanced/modules/02-rag-advanced-retrieval.md",
      "languages/ai/advanced/modules/03-evals-at-scale.md",
      "languages/ai/advanced/modules/04-security-threat-modeling-llm.md",
      "languages/ai/advanced/modules/05-observability-and-monitoring-llm.md",
      "languages/ai/advanced/modules/06-reliability-and-fallbacks.md",
      "languages/ai/advanced/modules/07-data-governance-and-privacy.md",
      "languages/ai/advanced/modules/08-production-incident-playbooks.md",
    ],
    "C# Advanced Course": [
      "languages/csharp/intermediate/modules/01-dsa-practical.md",
      "languages/csharp/intermediate/modules/02-testing-and-quality.md",
      "languages/csharp/intermediate/modules/03-git-and-collaboration.md",
      "languages/csharp/intermediate/modules/04-apis-and-auth.md",
      "languages/csharp/intermediate/modules/05-databases.md",
      "languages/csharp/intermediate/modules/06-security-basics.md",
      "languages/csharp/intermediate/modules/07-debugging-and-performance.md",
      "languages/csharp/intermediate/modules/08-deployment-and-ci.md",
      "languages/csharp/intermediate/modules/core-concepts.md",
      "languages/csharp/advanced/modules/01-system-design-foundations.md",
      "languages/csharp/advanced/modules/02-architecture-patterns.md",
      "languages/csharp/advanced/modules/03-concurrency-and-async.md",
      "languages/csharp/advanced/modules/04-performance-and-profiling.md",
      "languages/csharp/advanced/modules/05-reliability-and-resilience.md",
      "languages/csharp/advanced/modules/06-security-advanced.md",
      "languages/csharp/advanced/modules/07-observability-and-slos.md",
      "languages/csharp/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/csharp/advanced/modules/system-design.md",
    ],
    "Go Advanced Course": [
      "languages/go/intermediate/modules/01-dsa-practical.md",
      "languages/go/intermediate/modules/02-testing-and-quality.md",
      "languages/go/intermediate/modules/03-git-and-collaboration.md",
      "languages/go/intermediate/modules/04-apis-and-auth.md",
      "languages/go/intermediate/modules/05-databases.md",
      "languages/go/intermediate/modules/06-security-basics.md",
      "languages/go/intermediate/modules/07-debugging-and-performance.md",
      "languages/go/intermediate/modules/08-deployment-and-ci.md",
      "languages/go/intermediate/modules/core-concepts.md",
      "languages/go/advanced/modules/01-system-design-foundations.md",
      "languages/go/advanced/modules/02-architecture-patterns.md",
      "languages/go/advanced/modules/03-concurrency-and-async.md",
      "languages/go/advanced/modules/04-performance-and-profiling.md",
      "languages/go/advanced/modules/05-reliability-and-resilience.md",
      "languages/go/advanced/modules/06-security-advanced.md",
      "languages/go/advanced/modules/07-observability-and-slos.md",
      "languages/go/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/go/advanced/modules/system-design.md",
    ],
    "Java Advanced Course": [
      "languages/java/intermediate/modules/01-dsa-practical.md",
      "languages/java/intermediate/modules/02-testing-and-quality.md",
      "languages/java/intermediate/modules/03-git-and-collaboration.md",
      "languages/java/intermediate/modules/04-apis-and-auth.md",
      "languages/java/intermediate/modules/05-databases.md",
      "languages/java/intermediate/modules/06-security-basics.md",
      "languages/java/intermediate/modules/07-debugging-and-performance.md",
      "languages/java/intermediate/modules/08-deployment-and-ci.md",
      "languages/java/intermediate/modules/core-concepts.md",
      "languages/java/advanced/modules/01-system-design-foundations.md",
      "languages/java/advanced/modules/02-architecture-patterns.md",
      "languages/java/advanced/modules/03-concurrency-and-async.md",
      "languages/java/advanced/modules/04-performance-and-profiling.md",
      "languages/java/advanced/modules/05-reliability-and-resilience.md",
      "languages/java/advanced/modules/06-security-advanced.md",
      "languages/java/advanced/modules/07-observability-and-slos.md",
      "languages/java/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/java/advanced/modules/system-design.md",
    ],
    "Kotlin Advanced Course": [
      "languages/kotlin/intermediate/modules/01-dsa-practical.md",
      "languages/kotlin/intermediate/modules/02-testing-and-quality.md",
      "languages/kotlin/intermediate/modules/03-git-and-collaboration.md",
      "languages/kotlin/intermediate/modules/04-apis-and-auth.md",
      "languages/kotlin/intermediate/modules/05-databases.md",
      "languages/kotlin/intermediate/modules/06-security-basics.md",
      "languages/kotlin/intermediate/modules/07-debugging-and-performance.md",
      "languages/kotlin/intermediate/modules/08-deployment-and-ci.md",
      "languages/kotlin/intermediate/modules/core-concepts.md",
      "languages/kotlin/advanced/modules/01-system-design-foundations.md",
      "languages/kotlin/advanced/modules/02-architecture-patterns.md",
      "languages/kotlin/advanced/modules/03-concurrency-and-async.md",
      "languages/kotlin/advanced/modules/04-performance-and-profiling.md",
      "languages/kotlin/advanced/modules/05-reliability-and-resilience.md",
      "languages/kotlin/advanced/modules/06-security-advanced.md",
      "languages/kotlin/advanced/modules/07-observability-and-slos.md",
      "languages/kotlin/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/kotlin/advanced/modules/system-design.md",
    ],
    "Python Advanced Course": [
      "languages/python/intermediate/modules/01-dsa-practical.md",
      "languages/python/intermediate/modules/02-testing-and-quality.md",
      "languages/python/intermediate/modules/03-git-and-collaboration.md",
      "languages/python/intermediate/modules/04-apis-and-auth.md",
      "languages/python/intermediate/modules/05-databases.md",
      "languages/python/intermediate/modules/06-security-basics.md",
      "languages/python/intermediate/modules/07-debugging-and-performance.md",
      "languages/python/intermediate/modules/08-deployment-and-ci.md",
      "languages/python/intermediate/modules/core-concepts.md",
      "languages/python/advanced/modules/01-system-design-foundations.md",
      "languages/python/advanced/modules/02-architecture-patterns.md",
      "languages/python/advanced/modules/03-concurrency-and-async.md",
      "languages/python/advanced/modules/04-performance-and-profiling.md",
      "languages/python/advanced/modules/05-reliability-and-resilience.md",
      "languages/python/advanced/modules/06-security-advanced.md",
      "languages/python/advanced/modules/07-observability-and-slos.md",
      "languages/python/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/python/advanced/modules/system-design.md",
    ],
    "Rust Advanced Course": [
      "languages/rust/intermediate/modules/01-dsa-practical.md",
      "languages/rust/intermediate/modules/02-testing-and-quality.md",
      "languages/rust/intermediate/modules/03-git-and-collaboration.md",
      "languages/rust/intermediate/modules/04-apis-and-auth.md",
      "languages/rust/intermediate/modules/05-databases.md",
      "languages/rust/intermediate/modules/06-security-basics.md",
      "languages/rust/intermediate/modules/07-debugging-and-performance.md",
      "languages/rust/intermediate/modules/08-deployment-and-ci.md",
      "languages/rust/intermediate/modules/core-concepts.md",
      "languages/rust/advanced/modules/01-system-design-foundations.md",
      "languages/rust/advanced/modules/02-architecture-patterns.md",
      "languages/rust/advanced/modules/03-concurrency-and-async.md",
      "languages/rust/advanced/modules/04-performance-and-profiling.md",
      "languages/rust/advanced/modules/05-reliability-and-resilience.md",
      "languages/rust/advanced/modules/06-security-advanced.md",
      "languages/rust/advanced/modules/07-observability-and-slos.md",
      "languages/rust/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/rust/advanced/modules/system-design.md",
    ],
    "SQL Advanced Course": [
      "languages/sql/intermediate/modules/01-dsa-practical.md",
      "languages/sql/intermediate/modules/02-testing-and-quality.md",
      "languages/sql/intermediate/modules/03-git-and-collaboration.md",
      "languages/sql/intermediate/modules/04-apis-and-auth.md",
      "languages/sql/intermediate/modules/05-databases.md",
      "languages/sql/intermediate/modules/06-security-basics.md",
      "languages/sql/intermediate/modules/07-debugging-and-performance.md",
      "languages/sql/intermediate/modules/08-deployment-and-ci.md",
      "languages/sql/intermediate/modules/core-concepts.md",
      "languages/sql/advanced/modules/01-system-design-foundations.md",
      "languages/sql/advanced/modules/02-architecture-patterns.md",
      "languages/sql/advanced/modules/03-concurrency-and-async.md",
      "languages/sql/advanced/modules/04-performance-and-profiling.md",
      "languages/sql/advanced/modules/05-reliability-and-resilience.md",
      "languages/sql/advanced/modules/06-security-advanced.md",
      "languages/sql/advanced/modules/07-observability-and-slos.md",
      "languages/sql/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/sql/advanced/modules/system-design.md",
    ],
    "Swift Advanced Course": [
      "languages/swift/intermediate/modules/01-dsa-practical.md",
      "languages/swift/intermediate/modules/02-testing-and-quality.md",
      "languages/swift/intermediate/modules/03-git-and-collaboration.md",
      "languages/swift/intermediate/modules/04-apis-and-auth.md",
      "languages/swift/intermediate/modules/05-databases.md",
      "languages/swift/intermediate/modules/06-security-basics.md",
      "languages/swift/intermediate/modules/07-debugging-and-performance.md",
      "languages/swift/intermediate/modules/08-deployment-and-ci.md",
      "languages/swift/intermediate/modules/core-concepts.md",
      "languages/swift/advanced/modules/01-system-design-foundations.md",
      "languages/swift/advanced/modules/02-architecture-patterns.md",
      "languages/swift/advanced/modules/03-concurrency-and-async.md",
      "languages/swift/advanced/modules/04-performance-and-profiling.md",
      "languages/swift/advanced/modules/05-reliability-and-resilience.md",
      "languages/swift/advanced/modules/06-security-advanced.md",
      "languages/swift/advanced/modules/07-observability-and-slos.md",
      "languages/swift/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/swift/advanced/modules/system-design.md",
    ],
    "TypeScript Advanced Course": [
      "languages/typescript/intermediate/modules/01-dsa-practical.md",
      "languages/typescript/intermediate/modules/02-testing-and-quality.md",
      "languages/typescript/intermediate/modules/03-git-and-collaboration.md",
      "languages/typescript/intermediate/modules/04-apis-and-auth.md",
      "languages/typescript/intermediate/modules/05-databases.md",
      "languages/typescript/intermediate/modules/06-security-basics.md",
      "languages/typescript/intermediate/modules/07-debugging-and-performance.md",
      "languages/typescript/intermediate/modules/08-deployment-and-ci.md",
      "languages/typescript/intermediate/modules/core-concepts.md",
      "languages/typescript/advanced/modules/01-system-design-foundations.md",
      "languages/typescript/advanced/modules/02-architecture-patterns.md",
      "languages/typescript/advanced/modules/03-concurrency-and-async.md",
      "languages/typescript/advanced/modules/04-performance-and-profiling.md",
      "languages/typescript/advanced/modules/05-reliability-and-resilience.md",
      "languages/typescript/advanced/modules/06-security-advanced.md",
      "languages/typescript/advanced/modules/07-observability-and-slos.md",
      "languages/typescript/advanced/modules/08-ci-cd-and-release-strategies.md",
      "languages/typescript/advanced/modules/system-design.md",
    ],
  };

  const ADVANCED_COURSES = [
    { id: "python-advanced", name: "Python", page: "python-advanced-course.html", icon: "Py" },
    { id: "typescript-advanced", name: "TypeScript", page: "typescript-advanced-course.html", icon: "TS" },
    { id: "java-advanced", name: "Java", page: "java-advanced-course.html", icon: "Java" },
    { id: "csharp-advanced", name: "C#", page: "csharp-advanced-course.html", icon: "C#" },
    { id: "go-advanced", name: "Go", page: "go-advanced-course.html", icon: "Go" },
    { id: "rust-advanced", name: "Rust", page: "rust-advanced-course.html", icon: "Rust" },
    { id: "kotlin-advanced", name: "Kotlin", page: "kotlin-advanced-course.html", icon: "Kt" },
    { id: "swift-advanced", name: "Swift", page: "swift-advanced-course.html", icon: "Swift" },
    { id: "sql-advanced", name: "SQL", page: "sql-advanced-course.html", icon: "SQL" },
  ];

  let syncTimer = null;
  let syncing = false;

  const safeParse = (raw, fallback) => {
    try {
      return raw ? JSON.parse(raw) : fallback;
    } catch {
      return fallback;
    }
  };

  const currentFile = () =>
    (location.pathname.split("/").pop() || "index.html").toLowerCase() || "index.html";

  const apiBaseUrl = () => {
    const configured = global.PF_CONFIG && global.PF_CONFIG.apiBaseUrl;
    return String(configured || "").replace(/\/$/, "");
  };

  const getToken = () => localStorage.getItem(KEYS.authToken) || "";
  const getUser = () => {
    const user = safeParse(localStorage.getItem(KEYS.authUser), null);
    // Stale user without a token should not look signed in.
    if (user && !getToken()) {
      localStorage.removeItem(KEYS.authUser);
      return null;
    }
    return user;
  };

  const setSession = (token, user) => {
    if (token) localStorage.setItem(KEYS.authToken, token);
    else localStorage.removeItem(KEYS.authToken);
    if (user) localStorage.setItem(KEYS.authUser, JSON.stringify(user));
    else localStorage.removeItem(KEYS.authUser);
  };

  const apiFetch = async (path, options = {}) => {
    const base = apiBaseUrl();
    if (!base) {
      throw new Error("API is not configured. Add docs/config.js with apiBaseUrl.");
    }
    const headers = Object.assign(
      { "Content-Type": "application/json" },
      options.headers || {}
    );
    const token = getToken();
    if (token) headers.Authorization = `Bearer ${token}`;

    let response;
    try {
      response = await fetch(`${base}${path}`, Object.assign({}, options, { headers }));
    } catch {
      throw new Error("Could not reach the API. Is the backend running?");
    }

    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      throw new Error(data.error || `Request failed (${response.status})`);
    }
    return data;
  };

  const collectModuleProgress = () => {
    const moduleProgress = {};
    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => {
        moduleProgress[key] = safeParse(localStorage.getItem(key), {});
      });
    return moduleProgress;
  };

  const readLocalProgress = () => ({
    completions: getCompletions(),
    quizCompletions: getQuizCompletions(),
    startSteps: getStartSteps(),
    moduleProgress: collectModuleProgress(),
    updatedAt: new Date().toISOString(),
  });

  const writeLocalProgress = (progress) => {
    localStorage.setItem(KEYS.completions, JSON.stringify(progress.completions || []));
    localStorage.setItem(
      KEYS.quizCompletions,
      JSON.stringify(progress.quizCompletions || {})
    );
    localStorage.setItem(KEYS.startSteps, JSON.stringify(progress.startSteps || {}));

    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => localStorage.removeItem(key));

    Object.entries(progress.moduleProgress || {}).forEach(([key, value]) => {
      localStorage.setItem(key, JSON.stringify(value));
    });
  };

  const mergeProgress = (localProgress, remoteProgress) => {
    const local = localProgress || {};
    const remote = remoteProgress || {};
    const completions = [
      ...new Set([...(local.completions || []), ...(remote.completions || [])]),
    ];

    const quizCompletions = Object.assign({}, remote.quizCompletions || {});
    Object.entries(local.quizCompletions || {}).forEach(([key, value]) => {
      const remoteValue = quizCompletions[key];
      if (!remoteValue) {
        quizCompletions[key] = value;
        return;
      }
      const localAt = Date.parse(value.at || 0) || 0;
      const remoteAt = Date.parse(remoteValue.at || 0) || 0;
      quizCompletions[key] = localAt >= remoteAt ? value : remoteValue;
    });

    const startSteps = {};
    const stepKeys = new Set([
      ...Object.keys(local.startSteps || {}),
      ...Object.keys(remote.startSteps || {}),
    ]);
    stepKeys.forEach((key) => {
      startSteps[key] = !!(local.startSteps?.[key] || remote.startSteps?.[key]);
    });

    const moduleProgress = Object.assign(
      {},
      remote.moduleProgress || {},
      local.moduleProgress || {}
    );

    return {
      completions,
      quizCompletions,
      startSteps,
      moduleProgress,
      updatedAt: new Date().toISOString(),
    };
  };

  const scheduleSync = () => {
    if (!getToken()) return;
    clearTimeout(syncTimer);
    syncTimer = setTimeout(() => {
      syncProgress().catch(() => {
        /* offline / API down — local progress still saved */
      });
    }, 700);
  };

  const syncProgress = async ({ force } = {}) => {
    if (!getToken()) {
      if (force) {
        throw new Error("Sign in again to sync — your session is missing or expired.");
      }
      return null;
    }
    if (syncing) return null;
    syncing = true;
    try {
      const remote = await apiFetch("/api/progress");
      const merged = mergeProgress(readLocalProgress(), remote.progress || {});
      writeLocalProgress(merged);
      const saved = await apiFetch("/api/progress", {
        method: "PUT",
        body: JSON.stringify(merged),
      });
      return saved.progress;
    } finally {
      syncing = false;
    }
  };

  const signIn = async ({ email, password }) => {
    const data = await apiFetch("/api/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
    setSession(data.token, data.user);
    await syncProgress({ force: true });
    mountHeader();
    return data.user;
  };

  const signUp = async ({ email, password, displayName }) => {
    const data = await apiFetch("/api/auth/register", {
      method: "POST",
      body: JSON.stringify({ email, password, displayName }),
    });
    setSession(data.token, data.user);
    await syncProgress({ force: true });
    mountHeader();
    return data.user;
  };

  const signOut = async () => {
    setSession("", null);
    mountHeader();
  };

  const getCompletions = () =>
    safeParse(localStorage.getItem(KEYS.completions), []);

  const saveCompletion = (path) => {
    if (!path) return getCompletions();
    const next = new Set(getCompletions());
    next.add(path);
    const list = [...next];
    localStorage.setItem(KEYS.completions, JSON.stringify(list));
    scheduleSync();
    return list;
  };

  const clearCompletion = (path) => {
    if (!path) return getCompletions();
    const list = getCompletions().filter((item) => item !== path);
    localStorage.setItem(KEYS.completions, JSON.stringify(list));
    scheduleSync();
    return list;
  };

  const toggleCompletion = (path) => {
    if (!path) return false;
    if (isCompleted(path)) {
      clearCompletion(path);
      return false;
    }
    saveCompletion(path);
    return true;
  };

  const isCompleted = (path) => getCompletions().includes(path);

  const getQuizCompletions = () =>
    safeParse(localStorage.getItem(KEYS.quizCompletions), {});

  const saveQuizResult = (quizPath, result) => {
    if (!quizPath) return getQuizCompletions();
    const all = getQuizCompletions();
    all[quizPath] = {
      score: result.score,
      total: result.total,
      passed: !!result.passed,
      at: new Date().toISOString(),
    };
    localStorage.setItem(KEYS.quizCompletions, JSON.stringify(all));
    scheduleSync();
    return all;
  };

  const getStartSteps = () =>
    safeParse(localStorage.getItem(KEYS.startSteps), {});

  const saveStartSteps = (state) => {
    localStorage.setItem(KEYS.startSteps, JSON.stringify(state || {}));
    scheduleSync();
    return state;
  };

  const inferLessonFromQuiz = (quizPath) => {
    if (!quizPath) return null;
    if (quizPath.endsWith("/exercises/quiz.md")) {
      return quizPath.replace(/\/exercises\/quiz\.md$/, "/README.md");
    }
    if (quizPath.endsWith(".quiz.md")) {
      return quizPath.replace(/\.quiz\.md$/, ".md");
    }
    return null;
  };

  const progressForModules = (modules) => {
    const list = Array.isArray(modules) ? modules : [];
    const done = list.filter((path) => isCompleted(path)).length;
    return {
      total: list.length,
      done,
      percent: list.length ? Math.round((done / list.length) * 100) : 0,
    };
  };

  const courseProgress = (courseName) =>
    progressForModules(COURSE_MODULE_MAP[courseName] || []);

  const bindProgressUI = ({ modules, textEl, fillEl, label = "Progress" }) => {
    const progress = progressForModules(modules);
    const textNode =
      typeof textEl === "string" ? document.getElementById(textEl) : textEl;
    const fillNode =
      typeof fillEl === "string" ? document.getElementById(fillEl) : fillEl;
    if (textNode) {
      textNode.textContent = `${label}: ${progress.done} of ${progress.total} complete`;
    }
    if (fillNode) fillNode.style.width = `${progress.percent}%`;
    return progress;
  };

  const resetAllProgress = () => {
    localStorage.removeItem(KEYS.completions);
    localStorage.removeItem(KEYS.quizCompletions);
    localStorage.removeItem(KEYS.startSteps);
    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => localStorage.removeItem(key));
    scheduleSync();
  };

  const markNavCurrent = () => {
    const file = currentFile();
    document.querySelectorAll(".nav a[href]").forEach((anchor) => {
      const href = (anchor.getAttribute("href") || "").split("?")[0].toLowerCase();
      const current =
        href === file ||
        (file === "" && href === "index.html") ||
        (file === "/" && href === "index.html");
      if (current) {
        anchor.setAttribute("aria-current", "page");
      } else {
        anchor.removeAttribute("aria-current");
      }
    });
  };

  const headerHTML = () => {
    const user = getUser();
    const nav = NAV_LINKS.map((link) => {
      const label = link.label;
      const signedInClass =
        link.href === "account.html" && user ? ' class="nav-account is-signed-in"' : "";
      const accountTitle =
        link.href === "account.html" && user
          ? ` title="Signed in as ${String(user.displayName || user.email || "").replace(/"/g, "")}"`
          : "";
      return `<a href="${link.href}"${signedInClass}${accountTitle}>${label}</a>`;
    }).join("\n        ");
    return `<header class="site-header">
      <div class="site-header-bar">
        <h1><a class="site-brand" href="index.html">Programming Foundations</a></h1>
        <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="site-nav">
          Menu
        </button>
      </div>
      <nav class="nav" id="site-nav" aria-label="Primary">
        ${nav}
      </nav>
    </header>`;
  };

  const wireNavToggle = () => {
    const toggle = document.querySelector(".nav-toggle");
    const nav = document.getElementById("site-nav");
    if (!toggle || !nav) return;
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", open ? "false" : "true");
      nav.classList.toggle("is-open", !open);
    });
  };

  const mountHeader = () => {
    const existing = document.querySelector("header.site-header");
    if (existing) {
      existing.outerHTML = headerHTML();
    } else {
      document.querySelectorAll("[data-pf-header]").forEach((slot) => {
        slot.outerHTML = headerHTML();
      });
    }
    // If placeholder still present (first paint), replace it
    document.querySelectorAll("[data-pf-header]").forEach((slot) => {
      slot.outerHTML = headerHTML();
    });
    wireNavToggle();
    markNavCurrent();
  };

  const boot = () => {
    mountHeader();
    mountDonateSlots();
    if (getToken()) {
      syncProgress().catch(() => {
        /* guest-capable offline */
      });
    }
  };

  const PF = {
    PASS_THRESHOLD,
    KEYS,
    START_STEP_ORDER,
    COURSE_MODULE_MAP,
    ADVANCED_COURSES,
    getCompletions,
    saveCompletion,
    clearCompletion,
    toggleCompletion,
    isCompleted,
    getQuizCompletions,
    saveQuizResult,
    getStartSteps,
    saveStartSteps,
    inferLessonFromQuiz,
    progressForModules,
    courseProgress,
    bindProgressUI,
    resetAllProgress,
    markNavCurrent,
    mountHeader,
    mountDonateSlots,
    getDonateConfig,
    getUser,
    getToken,
    signIn,
    signUp,
    signOut,
    syncProgress,
    scheduleSync,
    apiBaseUrl,
  };

  global.PF = PF;

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})(window);
