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
    lastLesson: "pf-last-lesson",
    lastQuiz: "pf-last-quiz",
    persona: "pf-org-persona",
  };

  /** Home learners pick which org framing fits them best. */
  const PERSONAS = {
    schools: {
      id: "schools",
      label: "Schools & colleges",
      short: "School",
      blurb:
        "Structured modules, quizzes, and UK exam-board skill alignment for classroom or independent study.",
      focus: "Follow modules in order, use Standards for GCSE-style skill mapping, earn a certificate.",
      recommendCourse: "python",
      standardsNote:
        "Framed for school and college learners — skills map to OCR / AQA / Edexcel programming topics.",
      heroHint: "Learn with classroom-ready structure and exam-board aligned skills.",
    },
    corporate: {
      id: "corporate",
      label: "Corporate L&D",
      short: "Workplace",
      blurb:
        "Practical skills for career change or upskilling at work — portfolio projects and clear checkpoints.",
      focus: "Prioritise portfolio projects, mark modules complete, sync progress across devices when signed in.",
      recommendCourse: "python",
      standardsNote:
        "Framed for workplace learning — outcomes you can show managers and add to a CV.",
      heroHint: "Build job-ready skills with projects you can show at work.",
    },
    saas: {
      id: "saas",
      label: "Self-serve / SaaS builders",
      short: "Builder",
      blurb:
        "Self-paced path for indie builders and product-minded learners shipping real tools.",
      focus: "Ship the Task Tracker, then branch into AI or advanced language tracks as you grow.",
      recommendCourse: "ai",
      standardsNote:
        "Framed for builders — fundamentals first, then product/AI tracks at your own pace.",
      heroHint: "Self-serve learning for people building products and side projects.",
    },
  };

  const START_STEP_ORDER = ["open-online", "choose-course", "keep-learning", "download-local"];

  /** Recommended path catalog per persona — used to seed org assignments. */
  const PERSONA_PATHS = {
    schools: {
      label: "Schools & colleges",
      courses: ["Python Course", "C# Course", "Python Advanced Course"],
      note: "Structured, exam-board aligned progression from beginner to intermediate.",
    },
    corporate: {
      label: "Corporate L&D",
      courses: ["Python Course", "Python Advanced Course", "SQL Advanced Course"],
      note: "Job-ready fundamentals plus data skills for workplace upskilling.",
    },
    saas: {
      label: "Self-serve / SaaS builders",
      courses: ["Python Course", "AI Prompt Creation Course", "TypeScript Advanced Course"],
      note: "Ship fast: fundamentals, AI/prompting, then a modern web language track.",
    },
  };

  const NAV_LINKS = [
    { href: "index.html", label: "Home" },
    { href: "start-here.html", label: "Start Here" },
    { href: "courses.html", label: "Courses" },
    { href: "tutorials.html", label: "Tutorials" },
    { href: "standards.html", label: "Standards" },
    { href: "help.html", label: "Help" },
    { href: "support.html", label: "Support" },
    { href: "teams.html", label: "Teams" },
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

  // --- Org-grade API helpers (organisations, gradebook, certificates, account) ---

  const orgApi = {
    list: () => apiFetch("/api/orgs").then((d) => d.orgs || []),
    create: (name) =>
      apiFetch("/api/orgs", { method: "POST", body: JSON.stringify({ name }) }).then((d) => d.org),
    get: (id) => apiFetch(`/api/orgs/${encodeURIComponent(id)}`).then((d) => d.org),
    setPlan: (id, plan) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}`, {
        method: "PATCH",
        body: JSON.stringify({ plan }),
      }),
    members: (id) => apiFetch(`/api/orgs/${encodeURIComponent(id)}/members`).then((d) => d.members || []),
    addMember: (id, email, role) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}/members`, {
        method: "POST",
        body: JSON.stringify({ email, role }),
      }).then((d) => d.member),
    setMemberRole: (id, userId, role) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}/members/${encodeURIComponent(userId)}`, {
        method: "PATCH",
        body: JSON.stringify({ role }),
      }),
    removeMember: (id, userId) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}/members/${encodeURIComponent(userId)}`, {
        method: "DELETE",
      }),
    assignments: (id) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}/assignments`).then((d) => d.assignments || []),
    assignPath: (id, courseName, userId) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}/assignments`, {
        method: "POST",
        body: JSON.stringify({ courseName, userId: userId || null }),
      }).then((d) => d.assignment),
    analytics: (id) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}/analytics`).then((d) => d.analytics),
    audit: (id, limit) =>
      apiFetch(`/api/orgs/${encodeURIComponent(id)}/audit?limit=${Number(limit) || 100}`).then(
        (d) => d.events || []
      ),
  };

  /** Download a CSV export that requires an auth header, via blob. */
  const downloadOrgCsv = async (orgId, kind, filename) => {
    const base = apiBaseUrl();
    if (!base) throw new Error("API is not configured.");
    const token = getToken();
    const response = await fetch(
      `${base}/api/orgs/${encodeURIComponent(orgId)}/${kind}.csv`,
      { headers: token ? { Authorization: `Bearer ${token}` } : {} }
    );
    if (!response.ok) {
      throw new Error(`Could not download ${kind} (${response.status}).`);
    }
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = filename || `${kind}.csv`;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };

  const logQuizAttempt = (quizPath, result) => {
    if (!getToken() || !quizPath) return Promise.resolve(null);
    return apiFetch("/api/quiz-attempts", {
      method: "POST",
      body: JSON.stringify({
        quizPath,
        courseName: (result && result.courseName) || "",
        score: Number(result && result.score) || 0,
        total: Number(result && result.total) || 0,
        passed: !!(result && result.passed),
      }),
    }).catch(() => null);
  };

  const listQuizAttempts = () =>
    apiFetch("/api/quiz-attempts").then((d) => d.attempts || []);

  const certApi = {
    issue: (learnerName, courseName) =>
      apiFetch("/api/certificates", {
        method: "POST",
        body: JSON.stringify({ learnerName, courseName }),
      }).then((d) => d.certificate),
    verify: (verifyId) =>
      apiFetch(`/api/certificates/verify/${encodeURIComponent(verifyId)}`),
    mine: () => apiFetch("/api/certificates").then((d) => d.certificates || []),
  };

  const accountApi = {
    export: () => apiFetch("/api/account/export"),
    remove: () => apiFetch("/api/account", { method: "DELETE" }),
    changePassword: (currentPassword, newPassword) =>
      apiFetch("/api/auth/change-password", {
        method: "POST",
        body: JSON.stringify({ currentPassword, newPassword }),
      }),
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
    // Durable server-side attempt log powers org gradebooks (best-effort).
    logQuizAttempt(quizPath, result);
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
    enhanceModuleLists();
    return progress;
  };

  /** Turn plain module <ol class="card"> lists into structured module rows. */
  const enhanceModuleLists = () => {
    document.querySelectorAll("ol.card, ul.card, ol.module-list, ul.module-list").forEach((list) => {
      if (list.dataset.moduleListReady === "1") return;
      const items = Array.from(list.children).filter((el) => el.tagName === "LI");
      if (!items.length) return;
      const hasLessonLink = items.some((li) =>
        Array.from(li.querySelectorAll("a")).some((a) =>
          /course-viewer\.html/i.test(a.getAttribute("href") || "")
        )
      );
      if (!hasLessonLink) return;

      list.classList.remove("card");
      list.classList.add("module-list");
      list.setAttribute("role", "list");

      items.forEach((li, index) => {
        if (li.querySelector(".module-list__title")) return;
        const anchors = Array.from(li.querySelectorAll("a"));
        if (!anchors.length) return;

        const actions = anchors.map((a) => {
          const href = a.getAttribute("href") || "#";
          const label = (a.textContent || "").trim() || "Open";
          let kind = "more";
          if (/course-viewer\.html/i.test(href) || /^lesson$/i.test(label)) kind = "lesson";
          else if (/quiz-viewer\.html/i.test(href) || /^quiz$/i.test(label)) kind = "quiz";
          else if (/tutorial/i.test(href) || /tutorial|setup|voiceover|guide|transcript/i.test(label))
            kind = "tutorial";
          return { href, label, kind };
        });

        const lessonHref = actions.find((a) => a.kind === "lesson")?.href || "";
        const pathMatch = lessonHref.match(/[?&]path=([^&]+)/i);
        const path = pathMatch ? decodeURIComponent(pathMatch[1]) : "";
        const done = Boolean(path && isCompleted(path));

        const clone = li.cloneNode(true);
        clone.querySelectorAll("a").forEach((a) => a.remove());
        let title = (clone.textContent || "")
          .replace(/[·•|]+/g, " ")
          .replace(/[—–-]+/g, "—")
          .replace(/\s+/g, " ")
          .replace(/^[\s—]+|[\s—]+$/g, "")
          .trim();
        if (!title) title = `Module ${index + 1}`;

          const num = String(index + 1).padStart(2, "0");
        li.className = `module-list__item${done ? " is-done" : ""}`;
        li.setAttribute("role", "listitem");
        if (path) li.setAttribute("data-module-path", path);
        li.innerHTML = `
          <span class="module-list__index" aria-hidden="true">${done ? "✓" : num}</span>
          <p class="module-list__title">${escapeHtml(title)}</p>
          <div class="module-list__actions">
              ${actions
                .map(
                  (a) =>
                    `<a class="module-list__action module-list__action--${a.kind}" href="${escapeHtml(a.href)}">${escapeHtml(a.label)}</a>`
                )
                .join("")}
          </div>
        `;
      });

      list.dataset.moduleListReady = "1";
    });
  };

  const resetAllProgress = () => {
    localStorage.removeItem(KEYS.completions);
    localStorage.removeItem(KEYS.quizCompletions);
    localStorage.removeItem(KEYS.startSteps);
    localStorage.removeItem(KEYS.lastLesson);
    localStorage.removeItem(KEYS.lastQuiz);
    localStorage.removeItem(KEYS.persona);
    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => localStorage.removeItem(key));
    mountResumeBanner();
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

  const getLastLesson = () => {
    try {
      return JSON.parse(localStorage.getItem(KEYS.lastLesson) || "null");
    } catch (error) {
      return null;
    }
  };

  const setLastLesson = (payload) => {
    if (!payload || !payload.path) return;
    try {
      localStorage.setItem(
        KEYS.lastLesson,
        JSON.stringify({
          path: payload.path,
          title: payload.title || "Lesson",
          course: payload.course || "",
          page: payload.page || "",
          ts: Date.now(),
        })
      );
    } catch (error) {
      /* quota / private mode */
    }
  };

  const setLastQuiz = (payload) => {
    if (!payload || !payload.quiz) return;
    try {
      localStorage.setItem(
        KEYS.lastQuiz,
        JSON.stringify({
          quiz: payload.quiz,
          title: payload.title || "Quiz",
          ts: Date.now(),
        })
      );
    } catch (error) {
      /* ignore */
    }
  };

  const escapeHtml = (str) =>
    String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");

  const getLastQuiz = () => {
    try {
      return JSON.parse(localStorage.getItem(KEYS.lastQuiz) || "null");
    } catch (error) {
      return null;
    }
  };

  const mountResumeBanner = () => {
    const host = document.getElementById("pf-resume-host");
    if (!host) return;
    const last = getLastLesson();
    const lastQuiz = getLastQuiz();
    if ((!last || !last.path) && (!lastQuiz || !lastQuiz.quiz)) {
      host.hidden = true;
      host.innerHTML = "";
      return;
    }
    const preferQuiz =
      lastQuiz &&
      lastQuiz.quiz &&
      (!last || !last.path || (Number(lastQuiz.ts) || 0) > (Number(last?.ts) || 0));
    if (preferQuiz) {
      host.hidden = false;
      host.innerHTML = `
      <div class="resume-banner" role="region" aria-label="Resume learning">
        <div class="resume-banner-copy">
          <strong>Continue your last quiz</strong>
          <span>${escapeHtml(lastQuiz.title || "Quiz")}</span>
        </div>
        <div class="resume-banner-actions">
          <a class="btn btn-primary" href="quiz-viewer.html?quiz=${encodeURIComponent(lastQuiz.quiz)}">Open quiz</a>
          ${
            last && last.path
              ? `<a class="btn btn-ghost" href="course-viewer.html?path=${encodeURIComponent(last.path)}">Last lesson</a>`
              : ""
          }
        </div>
      </div>`;
      return;
    }
    const done = isCompleted(last.path);
    const label = done ? "Review last lesson" : "Continue where you left off";
    const courseBit = last.course ? ` · ${last.course}` : "";
    host.hidden = false;
    host.innerHTML = `
      <div class="resume-banner" role="region" aria-label="Resume learning">
        <div class="resume-banner-copy">
          <strong>${label}</strong>
          <span>${escapeHtml(last.title)}${escapeHtml(courseBit)}</span>
        </div>
        <div class="resume-banner-actions">
          <a class="btn btn-primary" href="course-viewer.html?path=${encodeURIComponent(last.path)}">Open lesson</a>
          ${last.page ? `<a class="btn btn-ghost" href="${escapeHtml(last.page)}">Course home</a>` : ""}
          ${
            lastQuiz && lastQuiz.quiz
              ? `<a class="btn btn-ghost" href="quiz-viewer.html?quiz=${encodeURIComponent(lastQuiz.quiz)}">Last quiz</a>`
              : ""
          }
        </div>
      </div>`;
  };

  const enhancePlaygroundChallenges = () => {
    const toolbar = document.querySelector("#playground .playground-toolbar");
    const editor = document.getElementById("playground-code");
    if (!toolbar || !editor || toolbar.querySelector(".playground-challenges")) return;
    const challenges = [
      {
        name: "Hello",
        code: 'name = "Alex"\nprint("Hello, " + name + "!")\nprint("Ready to learn?")',
      },
      {
        name: "Variables",
        code: 'city = "London"\nyear = 2026\nprint("Learning in " + city)\nprint(year)',
      },
      {
        name: "Join strings",
        code: 'first = "Programming"\nsecond = "Foundations"\nprint(first + " " + second)',
      },
    ];
    const wrap = document.createElement("div");
    wrap.className = "playground-challenges";
    wrap.setAttribute("role", "group");
    wrap.setAttribute("aria-label", "Try a challenge");
    challenges.forEach((ch) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chip-btn";
      btn.textContent = ch.name;
      btn.addEventListener("click", () => {
        editor.value = ch.code;
        editor.focus();
        document.getElementById("playground-run")?.click();
      });
      wrap.appendChild(btn);
    });
    toolbar.appendChild(wrap);
  };

  const getPersonaId = () => {
    try {
      const id = localStorage.getItem(KEYS.persona) || "";
      return PERSONAS[id] ? id : "";
    } catch (error) {
      return "";
    }
  };

  const getPersona = () => PERSONAS[getPersonaId()] || null;

  const setPersona = (id) => {
    if (!PERSONAS[id]) return null;
    try {
      localStorage.setItem(KEYS.persona, id);
    } catch (error) {
      /* ignore */
    }
    applyPersonaCopy();
    mountPersonaPicker();
    document.dispatchEvent(
      new CustomEvent("pf:persona-changed", { detail: { persona: PERSONAS[id] } })
    );
    return PERSONAS[id];
  };

  const clearPersona = () => {
    try {
      localStorage.removeItem(KEYS.persona);
    } catch (error) {
      /* ignore */
    }
    applyPersonaCopy();
    mountPersonaPicker();
    document.dispatchEvent(new CustomEvent("pf:persona-changed", { detail: { persona: null } }));
  };

  const applyPersonaCopy = () => {
    const persona = getPersona();
    document.querySelectorAll("[data-pf-persona-copy]").forEach((el) => {
      const key = el.getAttribute("data-pf-persona-copy");
      if (!persona) {
        if (el.dataset.pfPersonaFallback !== undefined) {
          el.textContent = el.dataset.pfPersonaFallback;
        }
        el.hidden = !String(el.textContent || "").trim();
        return;
      }
      if (key && persona[key]) el.textContent = persona[key];
      el.hidden = !String(el.textContent || "").trim();
    });
    document.querySelectorAll("[data-pf-persona-show]").forEach((el) => {
      const want = el.getAttribute("data-pf-persona-show");
      el.hidden = !persona || persona.id !== want;
    });
    document.documentElement.dataset.pfPersona = persona ? persona.id : "";
  };

  const mountPersonaPicker = () => {
    const host = document.getElementById("pf-persona-host");
    if (!host) return;
    const selected = getPersonaId();
    const heading = host.dataset.heading || "Who are you learning for?";
    const lead =
      host.dataset.lead ||
      "Most people learn from home — pick the framing that fits you. You can change this anytime.";

    host.innerHTML = `
      <section class="persona-picker" aria-labelledby="persona-picker-heading">
        <h3 id="persona-picker-heading">${escapeHtml(heading)}</h3>
        <p class="persona-picker-lead">${escapeHtml(lead)}</p>
        <div class="persona-options" role="radiogroup" aria-label="Organisation persona">
          ${Object.values(PERSONAS)
            .map((p) => {
              const active = selected === p.id;
              return `
            <button type="button" class="persona-card${active ? " is-selected" : ""}"
              role="radio" aria-checked="${active ? "true" : "false"}" data-persona="${p.id}">
              <strong>${escapeHtml(p.label)}</strong>
              <span>${escapeHtml(p.blurb)}</span>
            </button>`;
            })
            .join("")}
        </div>
        <p class="note persona-picker-status" role="status">
          ${
            selected
              ? `Saved: <strong>${escapeHtml(PERSONAS[selected].label)}</strong>. <button type="button" class="linkish" data-persona-clear>Clear choice</button>`
              : "No persona saved yet — choose one to personalise tips and emphasis."
          }
        </p>
      </section>`;

    host.querySelectorAll("[data-persona]").forEach((btn) => {
      btn.addEventListener("click", () => setPersona(btn.getAttribute("data-persona")));
    });
    host.querySelector("[data-persona-clear]")?.addEventListener("click", () => clearPersona());
  };

  const mountAtmosphere = () => {
    if (document.querySelector(".pf-atmosphere")) return;
    const root = document.createElement("div");
    root.className = "pf-atmosphere";
    root.setAttribute("aria-hidden", "true");
    root.innerHTML = [
      '<div class="pf-atmosphere__shaft"></div>',
      '<div class="pf-atmosphere__motif"></div>',
      '<div class="pf-atmosphere__motif pf-atmosphere__motif--left"></div>',
    ].join("");
    document.body.prepend(root);
  };

  const boot = () => {
    mountAtmosphere();
    mountHeader();
    mountDonateSlots();
    mountResumeBanner();
    mountPersonaPicker();
    applyPersonaCopy();
    enhancePlaygroundChallenges();
    enhanceModuleLists();
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
    PERSONAS,
    PERSONA_PATHS,
    getCompletions,
    saveCompletion,
    clearCompletion,
    toggleCompletion,
    isCompleted,
    getQuizCompletions,
    saveQuizResult,
    getStartSteps,
    saveStartSteps,
    getLastLesson,
    setLastLesson,
    setLastQuiz,
    getLastQuiz,
    getPersonaId,
    getPersona,
    setPersona,
    clearPersona,
    mountResumeBanner,
    mountPersonaPicker,
    applyPersonaCopy,
    inferLessonFromQuiz,
    progressForModules,
    courseProgress,
    bindProgressUI,
    enhanceModuleLists,
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
    org: orgApi,
    downloadOrgCsv,
    logQuizAttempt,
    listQuizAttempts,
    cert: certApi,
    account: accountApi,
  };

  global.PF = PF;

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})(window);
