/**
 * Shared helpers for Programming Foundations site UX.
 * Progress keys, nav state, and reset live here so pages stay in sync.
 */
(function (global) {
  const PASS_THRESHOLD = 0.7;
  const KEYS = {
    completions: "course-completions",
    quizCompletions: "quiz-completions",
    startSteps: "pf-start-steps",
  };

  const START_STEP_ORDER = ["open-online", "choose-course", "keep-learning", "download-local"];

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
  };

  const safeParse = (raw, fallback) => {
    try {
      return raw ? JSON.parse(raw) : fallback;
    } catch {
      return fallback;
    }
  };

  const getCompletions = () =>
    safeParse(localStorage.getItem(KEYS.completions), []);

  const saveCompletion = (path) => {
    if (!path) return getCompletions();
    const next = new Set(getCompletions());
    next.add(path);
    const list = [...next];
    localStorage.setItem(KEYS.completions, JSON.stringify(list));
    return list;
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
    return all;
  };

  const getStartSteps = () =>
    safeParse(localStorage.getItem(KEYS.startSteps), {});

  const saveStartSteps = (state) => {
    localStorage.setItem(KEYS.startSteps, JSON.stringify(state || {}));
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

  const courseProgress = (courseName) => {
    const modules = COURSE_MODULE_MAP[courseName] || [];
    const done = modules.filter((path) => isCompleted(path)).length;
    return {
      total: modules.length,
      done,
      percent: modules.length ? Math.round((done / modules.length) * 100) : 0,
    };
  };

  const resetAllProgress = () => {
    localStorage.removeItem(KEYS.completions);
    localStorage.removeItem(KEYS.quizCompletions);
    localStorage.removeItem(KEYS.startSteps);
    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => localStorage.removeItem(key));
  };

  const markNavCurrent = () => {
    const file = (location.pathname.split("/").pop() || "index.html").toLowerCase();
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

  const PF = {
    PASS_THRESHOLD,
    KEYS,
    START_STEP_ORDER,
    COURSE_MODULE_MAP,
    getCompletions,
    saveCompletion,
    isCompleted,
    getQuizCompletions,
    saveQuizResult,
    getStartSteps,
    saveStartSteps,
    inferLessonFromQuiz,
    courseProgress,
    resetAllProgress,
    markNavCurrent,
  };

  global.PF = PF;

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", markNavCurrent);
  } else {
    markNavCurrent();
  }
})(window);
