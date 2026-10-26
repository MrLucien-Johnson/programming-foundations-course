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
    /** YYYY-MM-DD activity days for study streak (local device) */
    activityDays: "pf-activity-days",
    /** 'granted' | 'denied' — PECR/UK GDPR transparency for on-device guest progress */
    deviceProgressConsent: "pf-device-progress-consent",
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

  /** Site maintenance stamp — keep year and month current on each audit. */
  const SITE_YEAR = 2026;
  const SITE_MAINTAINED_LABEL = "26 October 2026";

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

  const getBrandConfig = () => {
    const cfg = global.PF_CONFIG || {};
    const url = String(
      cfg.abelSolutionsUrl || "https://mrlucien-johnson.github.io/AbelSolutions/"
    ).trim();
    const label = String(cfg.abelSolutionsLabel || "Abel Solutions").trim() || "Abel Solutions";
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

  /** Quiet “A project by Abel Solutions” credit in page footers. */
  const FOOTER_LINKS = [
    { href: "privacy.html", label: "Privacy" },
    { href: "help.html", label: "Help" },
    { href: "support.html", label: "Support" },
    { href: "certificate.html", label: "Certificate" },
  ];

  const ensureFooterLinks = (footer) => {
    let nav = footer.querySelector("[data-pf-footer-links]");
    if (!nav) {
      nav = document.createElement("p");
      nav.className = "footer-links";
      nav.dataset.pfFooterLinks = "1";
      footer.appendChild(nav);
    }
    const existingHrefs = new Set(
      Array.from(footer.querySelectorAll("a[href]")).map((a) =>
        (a.getAttribute("href") || "").split("#")[0].toLowerCase()
      )
    );
    FOOTER_LINKS.forEach(({ href, label }) => {
      if (existingHrefs.has(href.toLowerCase())) return;
      if (nav.textContent.trim() && !nav.textContent.trim().endsWith("·")) {
        nav.append(document.createTextNode(" · "));
      } else if (nav.childNodes.length) {
        nav.append(document.createTextNode(" · "));
      }
      const a = document.createElement("a");
      a.href = href;
      a.textContent = label;
      nav.appendChild(a);
      existingHrefs.add(href.toLowerCase());
    });
  };

  const mountBrandCredit = () => {
    const { url, label, enabled } = getBrandConfig();

    let footers = Array.from(document.querySelectorAll("footer.footer"));
    if (!footers.length) {
      const main = document.querySelector("main");
      if (!main) return;
      const footer = document.createElement("footer");
      footer.className = "footer";
      main.insertAdjacentElement("afterend", footer);
      footers = [footer];
    }

    footers.forEach((footer) => {
      ensureFooterLinks(footer);
      if (!enabled || footer.querySelector("[data-pf-brand-credit]")) return;
      const credit = document.createElement("p");
      credit.className = "footer-credit";
      credit.dataset.pfBrandCredit = "1";
      credit.append("A project by ");
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.rel = "noopener noreferrer";
      anchor.textContent = label;
      credit.appendChild(anchor);
      footer.prepend(credit);
    });
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
    "DevOps Foundations Course": [
      "languages/devops/modules/01-devops-mindset.md",
      "languages/devops/modules/02-git-branching-for-teams.md",
      "languages/devops/modules/03-ci-pipelines.md",
      "languages/devops/modules/04-cd-and-releases.md",
      "languages/devops/modules/05-containers-basics.md",
      "languages/devops/modules/06-compose-and-local-envs.md",
      "languages/devops/modules/07-observability-basics.md",
      "languages/devops/modules/08-incident-response.md",
      "languages/devops/modules/09-security-in-the-pipeline.md",
      "languages/devops/modules/10-capstone-delivery.md",
    ],
    "AWS Cloud Course": [
      "languages/aws/modules/01-aws-foundations.md",
      "languages/aws/modules/02-iam-and-security.md",
      "languages/aws/modules/03-vpc-networking.md",
      "languages/aws/modules/04-ec2-and-compute.md",
      "languages/aws/modules/05-s3-and-storage.md",
      "languages/aws/modules/06-rds-and-data.md",
      "languages/aws/modules/07-lambda-serverless.md",
      "languages/aws/modules/08-monitoring-cloudwatch.md",
      "languages/aws/modules/09-cost-and-well-architected.md",
      "languages/aws/modules/10-capstone-aws-app.md",
    ],
    "Azure Cloud Course": [
      "languages/azure/modules/01-azure-foundations.md",
      "languages/azure/modules/02-entra-id-and-rbac.md",
      "languages/azure/modules/03-vnet-networking.md",
      "languages/azure/modules/04-compute-options.md",
      "languages/azure/modules/05-storage-and-blobs.md",
      "languages/azure/modules/06-app-service.md",
      "languages/azure/modules/07-azure-sql-and-data.md",
      "languages/azure/modules/08-monitor-and-insights.md",
      "languages/azure/modules/09-governance-and-cost.md",
      "languages/azure/modules/10-capstone-azure-app.md",
    ],
    "GCP Cloud Course": [
      "languages/gcp/modules/01-gcp-foundations.md",
      "languages/gcp/modules/02-iam-and-org-policy.md",
      "languages/gcp/modules/03-vpc-networking.md",
      "languages/gcp/modules/04-compute-engine.md",
      "languages/gcp/modules/05-gcs-and-data.md",
      "languages/gcp/modules/06-cloud-run.md",
      "languages/gcp/modules/07-gke-intro.md",
      "languages/gcp/modules/08-ops-and-logging.md",
      "languages/gcp/modules/09-billing-and-cost.md",
      "languages/gcp/modules/10-capstone-gcp-service.md",
    ],
    "Kubernetes Course": [
      "languages/kubernetes/modules/01-k8s-mental-model.md",
      "languages/kubernetes/modules/02-pods-and-workloads.md",
      "languages/kubernetes/modules/03-services-and-ingress.md",
      "languages/kubernetes/modules/04-configmaps-secrets.md",
      "languages/kubernetes/modules/05-storage-and-pv.md",
      "languages/kubernetes/modules/06-deployments-rollouts.md",
      "languages/kubernetes/modules/07-autoscaling-basics.md",
      "languages/kubernetes/modules/08-observability-on-k8s.md",
      "languages/kubernetes/modules/09-security-basics.md",
      "languages/kubernetes/modules/10-capstone-k8s-app.md",
    ],
    "Terraform & IaC Course": [
      "languages/terraform/modules/01-iac-why-terraform.md",
      "languages/terraform/modules/02-providers-and-resources.md",
      "languages/terraform/modules/03-state-and-backends.md",
      "languages/terraform/modules/04-variables-outputs.md",
      "languages/terraform/modules/05-modules.md",
      "languages/terraform/modules/06-workspaces-environments.md",
      "languages/terraform/modules/07-plan-apply-destroy.md",
      "languages/terraform/modules/08-testing-and-policy.md",
      "languages/terraform/modules/09-ci-for-terraform.md",
      "languages/terraform/modules/10-capstone-module.md",
    ],
  };

  const PREMIUM_COURSES = [
    { id: "devops", name: "DevOps Foundations Course", page: "devops-course.html", pathPrefix: "languages/devops/" },
    { id: "aws", name: "AWS Cloud Course", page: "aws-course.html", pathPrefix: "languages/aws/" },
    { id: "azure", name: "Azure Cloud Course", page: "azure-course.html", pathPrefix: "languages/azure/" },
    { id: "gcp", name: "GCP Cloud Course", page: "gcp-course.html", pathPrefix: "languages/gcp/" },
    { id: "kubernetes", name: "Kubernetes Course", page: "kubernetes-course.html", pathPrefix: "languages/kubernetes/" },
    { id: "terraform", name: "Terraform & IaC Course", page: "terraform-course.html", pathPrefix: "languages/terraform/" },
  ];

  const PREMIUM_PATH_PREFIXES = PREMIUM_COURSES.map((c) => c.pathPrefix);

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
  let syncQueued = false;

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
    if (syncing) {
      syncQueued = true;
      return null;
    }
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
      if (syncQueued) {
        syncQueued = false;
        scheduleSync();
      }
    }
  };

  const signIn = async ({ email, password, totpToken, code } = {}) => {
    let data;
    if (totpToken && code) {
      data = await apiFetch("/api/auth/login/totp", {
        method: "POST",
        body: JSON.stringify({ totpToken, code }),
      });
    } else {
      data = await apiFetch("/api/auth/login", {
        method: "POST",
        body: JSON.stringify({ email, password }),
      });
      if (data.requiresTotp) {
        return data;
      }
    }
    if (!data.token || !data.user) {
      throw new Error("Sign in did not return a session. Try again.");
    }
    setSession(data.token, data.user);
    await syncProgress({ force: true });
    mountHeader();
    return data;
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
    me: () => apiFetch("/api/auth/me").then((d) => d.user),
    entitlements: () => apiFetch("/api/account/entitlements"),
    grantPremium: (email, note) =>
      apiFetch("/api/account/premium/grant", {
        method: "POST",
        body: JSON.stringify({ email, note }),
      }),
    revokePremium: (email) =>
      apiFetch("/api/account/premium/revoke", {
        method: "POST",
        body: JSON.stringify({ email }),
      }),
    totpSetup: () =>
      apiFetch("/api/auth/totp/setup", { method: "POST", body: JSON.stringify({}) }),
    totpConfirm: (code) =>
      apiFetch("/api/auth/totp/confirm", {
        method: "POST",
        body: JSON.stringify({ code }),
      }),
    totpDisable: (password, code) =>
      apiFetch("/api/auth/totp/disable", {
        method: "POST",
        body: JSON.stringify({ password, code }),
      }),
  };

  const isPremiumPath = (path) => {
    const clean = String(path || "");
    return PREMIUM_PATH_PREFIXES.some((prefix) => clean.startsWith(prefix));
  };

  const isPremiumCourseName = (name) =>
    PREMIUM_COURSES.some((c) => c.name === name || c.page === name);

  const refreshPremiumEntitlements = async () => {
    if (!getToken()) {
      return { premiumAccess: false, isDonor: false, allowlisted: false, reason: "signed-out" };
    }
    try {
      const data = await accountApi.entitlements();
      const user = Object.assign({}, getUser() || {}, {
        premiumAccess: !!data.premiumAccess,
        isDonor: !!data.isDonor,
        premiumReason: data.reason || "none",
      });
      setSession(getToken(), user);
      return data;
    } catch {
      const user = getUser() || {};
      return {
        premiumAccess: !!user.premiumAccess,
        isDonor: !!user.isDonor,
        allowlisted: false,
        reason: user.premiumReason || "cached",
      };
    }
  };

  const canAccessPremium = async () => {
    const user = getUser();
    if (user && user.premiumAccess) return true;
    if (!getToken()) return false;
    const entitlements = await refreshPremiumEntitlements();
    return !!entitlements.premiumAccess;
  };

  const ensurePremiumAccess = async ({ soft } = {}) => {
    const ok = await canAccessPremium();
    if (ok) return true;
    if (!soft) {
      throw new Error(
        "This donor course needs a signed-in allowlisted or donor account."
      );
    }
    return false;
  };

  const getCompletions = () => {
    const raw = safeParse(localStorage.getItem(KEYS.completions), []);
    if (Array.isArray(raw)) return raw.filter((item) => typeof item === "string" && item);
    // Tolerate legacy/object-shaped storage ({ path: true }) from older experiments.
    if (raw && typeof raw === "object") {
      return Object.keys(raw).filter((key) => Boolean(raw[key]));
    }
    return [];
  };

  const getDeviceProgressConsent = () => {
    try {
      return localStorage.getItem(KEYS.deviceProgressConsent) || "";
    } catch {
      return "";
    }
  };

  const setDeviceProgressConsent = (value) => {
    try {
      if (value === "granted" || value === "denied") {
        localStorage.setItem(KEYS.deviceProgressConsent, value);
      } else {
        localStorage.removeItem(KEYS.deviceProgressConsent);
      }
    } catch {
      /* private mode / blocked storage */
    }
  };

  const hasChosenDeviceProgressConsent = () => {
    const value = getDeviceProgressConsent();
    return value === "granted" || value === "denied";
  };

  /** If the learner already has on-device progress but never clicked Yes/No, treat that as granted so we stop re-asking. */
  const adoptExistingGuestProgressConsent = () => {
    if (getToken() || hasChosenDeviceProgressConsent()) return;
    try {
      const hasProgress =
        getCompletions().length > 0 ||
        Object.keys(getQuizCompletions()).length > 0 ||
        Object.keys(getStartSteps()).some((key) => getStartSteps()[key]) ||
        Boolean(getLastLesson()) ||
        Boolean(getLastQuiz()) ||
        Boolean(getPersonaId());
      if (hasProgress) setDeviceProgressConsent("granted");
    } catch {
      /* ignore */
    }
  };

  const canPersistGuestProgress = () => {
    // Signed-in users sync via account. Guests keep progress until they refuse.
    if (getToken()) return true;
    return getDeviceProgressConsent() !== "denied";
  };

  const writeProgressKey = (key, value) => {
    if (!canPersistGuestProgress()) return false;
    localStorage.setItem(key, value);
    return true;
  };

  const saveCompletion = (path) => {
    if (!path) return getCompletions();
    if (!canPersistGuestProgress()) return getCompletions();
    const next = new Set(getCompletions());
    next.add(path);
    const list = [...next];
    writeProgressKey(KEYS.completions, JSON.stringify(list));
    recordActivityDay();
    scheduleSync();
    return list;
  };

  const clearCompletion = (path) => {
    if (!path) return getCompletions();
    if (!canPersistGuestProgress()) return getCompletions();
    const list = getCompletions().filter((item) => item !== path);
    writeProgressKey(KEYS.completions, JSON.stringify(list));
    scheduleSync();
    return list;
  };

  const toggleCompletion = (path) => {
    if (!path) return { completed: false, persisted: false };
    if (!canPersistGuestProgress()) {
      return { completed: isCompleted(path), persisted: false };
    }
    if (isCompleted(path)) {
      clearCompletion(path);
      return { completed: false, persisted: true };
    }
    saveCompletion(path);
    return { completed: true, persisted: true };
  };

  const isCompleted = (path) => getCompletions().includes(path);

  const getQuizCompletions = () =>
    safeParse(localStorage.getItem(KEYS.quizCompletions), {});

  const saveQuizResult = (quizPath, result) => {
    if (!quizPath) return getQuizCompletions();
    if (!canPersistGuestProgress()) return getQuizCompletions();
    const all = getQuizCompletions();
    all[quizPath] = {
      score: result.score,
      total: result.total,
      passed: !!result.passed,
      at: new Date().toISOString(),
    };
    writeProgressKey(KEYS.quizCompletions, JSON.stringify(all));
    scheduleSync();
    // Durable server-side attempt log powers org gradebooks (best-effort).
    logQuizAttempt(quizPath, result);
    return all;
  };

  const getStartSteps = () =>
    safeParse(localStorage.getItem(KEYS.startSteps), {});

  const saveStartSteps = (state) => {
    if (!canPersistGuestProgress()) return state;
    writeProgressKey(KEYS.startSteps, JSON.stringify(state || {}));
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
        if (li.querySelector(".module-list__body")) return;
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
          <div class="module-list__index" aria-hidden="true">${done ? "✓" : num}</div>
          <div class="module-list__body">
            <p class="module-list__title">${escapeHtml(title)}</p>
            <div class="module-list__actions">
              ${actions
                .map(
                  (a) =>
                    `<a class="module-list__action module-list__action--${a.kind}" href="${escapeHtml(a.href)}">${escapeHtml(a.label)}</a>`
                )
                .join("")}
            </div>
          </div>
        `;
      });

      list.dataset.moduleListReady = "1";
    });
    highlightNextModules();
  };

  /** Flag the first incomplete module in each list as the clear “up next” step. */
  const highlightNextModules = () => {
    document.querySelectorAll(".module-list").forEach((list) => {
      list.querySelectorAll(".module-list__item").forEach((li) => {
        const path = li.getAttribute("data-module-path");
        if (path) {
          const done = isCompleted(path);
          li.classList.toggle("is-done", done);
          const index = li.querySelector(".module-list__index");
          if (index) {
            if (done) index.textContent = "✓";
            else if (index.textContent === "✓") {
              const siblings = Array.from(list.querySelectorAll(".module-list__item"));
              const n = siblings.indexOf(li) + 1;
              index.textContent = String(n).padStart(2, "0");
            }
          }
        }
        li.classList.remove("is-next");
        li.querySelector(".module-list__next-badge")?.remove();
      });
      const next = Array.from(list.querySelectorAll(".module-list__item")).find(
        (li) => !li.classList.contains("is-done")
      );
      if (!next) return;
      next.classList.add("is-next");
      const body = next.querySelector(".module-list__body");
      if (body && !body.querySelector(".module-list__next-badge")) {
        const badge = document.createElement("span");
        badge.className = "module-list__next-badge";
        badge.textContent = "Up next";
        body.insertBefore(badge, body.firstChild);
      }
    });
  };

  const emptyProgressPayload = () => ({
    completions: [],
    quizCompletions: {},
    startSteps: {},
    moduleProgress: {},
    updatedAt: new Date().toISOString(),
  });

  const resetAllProgress = () => {
    localStorage.removeItem(KEYS.completions);
    localStorage.removeItem(KEYS.quizCompletions);
    localStorage.removeItem(KEYS.startSteps);
    localStorage.removeItem(KEYS.lastLesson);
    localStorage.removeItem(KEYS.lastQuiz);
    localStorage.removeItem(KEYS.persona);
    localStorage.removeItem(KEYS.activityDays);
    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => localStorage.removeItem(key));
    writeLocalProgress(emptyProgressPayload());
    mountResumeBanner();
    // Push empty cloud state when signed in — merge-sync would restore remote progress.
    if (getToken()) {
      apiFetch("/api/progress", {
        method: "PUT",
        body: JSON.stringify(emptyProgressPayload()),
      }).catch(() => {
        /* offline / API down — local clear still applied */
      });
    }
  };

  const exportGuestProgress = () => {
    const moduleProgress = {};
    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => {
        moduleProgress[key] = safeParse(localStorage.getItem(key), {});
      });
    return {
      format: "programming-foundations-guest-progress",
      version: 1,
      exportedAt: new Date().toISOString(),
      deviceOnly: true,
      progress: {
        completions: getCompletions(),
        quizCompletions: getQuizCompletions(),
        startSteps: getStartSteps(),
        moduleProgress,
        lastLesson: getLastLesson(),
        lastQuiz: getLastQuiz(),
        persona: getPersonaId() || null,
      },
    };
  };

  const downloadGuestProgress = () => {
    const data = exportGuestProgress();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `programming-foundations-progress-${new Date().toISOString().slice(0, 10)}.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    return data;
  };

  const importGuestProgress = (payload) => {
    const data = typeof payload === "string" ? safeParse(payload, null) : payload;
    if (!data || typeof data !== "object") {
      throw new Error("That file does not look like a progress backup.");
    }
    const progress = data.progress && typeof data.progress === "object" ? data.progress : data;
    const completions = Array.isArray(progress.completions) ? progress.completions : [];
    const quizCompletions =
      progress.quizCompletions && typeof progress.quizCompletions === "object"
        ? progress.quizCompletions
        : {};
    const startSteps =
      progress.startSteps && typeof progress.startSteps === "object" ? progress.startSteps : {};
    const moduleProgress =
      progress.moduleProgress && typeof progress.moduleProgress === "object"
        ? progress.moduleProgress
        : {};

    localStorage.setItem(KEYS.completions, JSON.stringify(completions));
    localStorage.setItem(KEYS.quizCompletions, JSON.stringify(quizCompletions));
    localStorage.setItem(KEYS.startSteps, JSON.stringify(startSteps));

    Object.keys(localStorage)
      .filter((key) => key.startsWith("module-progress:"))
      .forEach((key) => localStorage.removeItem(key));
    Object.entries(moduleProgress).forEach(([key, value]) => {
      if (String(key).startsWith("module-progress:")) {
        localStorage.setItem(key, JSON.stringify(value || {}));
      }
    });

    if (progress.lastLesson) {
      localStorage.setItem(KEYS.lastLesson, JSON.stringify(progress.lastLesson));
    }
    if (progress.lastQuiz) {
      localStorage.setItem(KEYS.lastQuiz, JSON.stringify(progress.lastQuiz));
    }
    if (progress.persona) {
      localStorage.setItem(KEYS.persona, String(progress.persona));
    }

    // Importing a backup counts as choosing to keep progress on this device.
    setDeviceProgressConsent("granted");
    mountResumeBanner();
    applyPersonaCopy();
    scheduleSync();
    return true;
  };

  const DEVICE_PROGRESS_LOSS_WARNING =
    "If this browser’s data is cleared or lost, guest progress cannot be recovered unless you accept on-device storage again (and rebuild it or import a backup) or you use an account.";

  const dismissDeviceProgressAftermath = () => {
    document.getElementById("pf-device-progress-aftermath")?.remove();
  };

  const mountDeviceProgressAftermath = (choice) => {
    dismissDeviceProgressAftermath();
    const host = document.createElement("div");
    host.id = "pf-device-progress-aftermath";
    host.className = "device-progress-aftermath";
    host.setAttribute("role", "alert");
    const lead =
      choice === "denied"
        ? "On-device progress is off and any guest progress on this device was cleared. That clear cannot be undone."
        : "On-device progress is on for this browser.";
    host.innerHTML = `
      <div class="device-progress-aftermath__inner">
        <p>
          <strong>Important:</strong> ${lead}
          ${DEVICE_PROGRESS_LOSS_WARNING}
            Change this anytime in
            <a href="account.html#device-progress-settings">Account settings</a>.
            <a href="privacy.html#guest-progress">Privacy &amp; backups</a>
            ·
            <a href="account.html">Free account</a>
        </p>
        <button type="button" class="btn btn-secondary" data-aftermath-dismiss>Got it</button>
      </div>
    `;
    document.body.appendChild(host);
    host.querySelector("[data-aftermath-dismiss]")?.addEventListener("click", () => {
      dismissDeviceProgressAftermath();
    });
  };

  const dismissDeviceProgressNotice = () => {
    document.getElementById("pf-device-progress-notice")?.remove();
  };

  const mountDeviceProgressNotice = () => {
    if (getToken()) return;
    adoptExistingGuestProgressConsent();
    // Ask once only. After Yes or No, change the choice in Account settings.
    if (hasChosenDeviceProgressConsent()) return;
    if (document.getElementById("pf-device-progress-notice")) return;

    const host = document.createElement("div");
    host.id = "pf-device-progress-notice";
    host.className = "device-progress-notice";
    host.setAttribute("role", "region");
    host.setAttribute("aria-label", "Save learning progress on this device");
    host.innerHTML = `
      <div class="device-progress-notice__inner">
        <div class="device-progress-notice__copy">
          <strong>Save your learning progress in this browser?</strong>
          <p>
            This browser can keep course data on <em>your device only</em> so you can continue after
            a reboot. It is not sent to our servers unless you create an account and sync later.
            Choose once — we will not ask again on every page. You can opt out later in
            <a href="account.html#device-progress-settings">Account settings</a>.
          </p>
          <ul class="device-progress-notice__list">
            <li>Lessons you mark complete</li>
            <li>Quiz scores and pass/fail</li>
            <li>Start Here checklist ticks</li>
            <li>In-lesson checklist ticks</li>
            <li>Last lesson / quiz so “Continue” works</li>
            <li>Optional learning persona (Schools / Workplace / Self-serve)</li>
          </ul>
          <p>
            We do <strong>not</strong> store your name, email, payment details, or browsing history
            in guest mode — and we don’t use this for ads.
            <a href="privacy.html#guest-progress">Full privacy details</a>
            ·
            <a href="account.html">Free account for cloud sync</a>
          </p>
          <p class="device-progress-notice__warn">
            <strong>After you choose:</strong> if browser data is lost, progress is lost unless
            on-device storage was accepted (and you still have a backup) or you use an account.
          </p>
        </div>
        <div class="device-progress-notice__actions">
          <button type="button" class="btn btn-primary" data-consent="granted">
            Yes — save progress on this device
          </button>
          <button type="button" class="btn btn-secondary" data-consent="denied">
            No — don’t save progress
          </button>
        </div>
      </div>
    `;
    document.body.appendChild(host);

    host.addEventListener("click", (event) => {
      const btn = event.target.closest("[data-consent]");
      if (!btn) return;
      const value = btn.getAttribute("data-consent");
      if (value === "denied") {
        const ok = window.confirm(
          "Turn off on-device progress and clear guest progress on this device?\n\n" +
            "Clearing cannot be undone.\n\n" +
            DEVICE_PROGRESS_LOSS_WARNING
        );
        if (!ok) return;
      }
      setDeviceProgressConsent(value);
      // Re-read to confirm storage stuck; if it failed, keep the banner.
      if (getDeviceProgressConsent() !== value) {
        const status = document.getElementById("pf-device-progress-status");
        if (status) {
          status.textContent =
            "This browser blocked saving your choice. Allow site data for this site, or use a free account.";
        }
        return;
      }
      dismissDeviceProgressNotice();
      if (value === "denied") {
        resetAllProgress();
      }
      mountDeviceProgressAftermath(value);
      const status = document.getElementById("pf-device-progress-status");
      if (status) {
        status.textContent =
          value === "denied"
            ? `On-device progress is off and guest progress was cleared. That clear cannot be undone. Change this anytime in Account settings. ${DEVICE_PROGRESS_LOSS_WARNING}`
            : `On-device progress is on. We will not ask again on every page — change this anytime in Account settings. ${DEVICE_PROGRESS_LOSS_WARNING}`;
      }
    });
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

  const closeNavMenu = () => {
    const toggle = document.querySelector(".nav-toggle");
    const nav = document.getElementById("site-nav");
    if (!toggle || !nav) return;
    toggle.setAttribute("aria-expanded", "false");
    nav.classList.remove("is-open");
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
    nav.querySelectorAll("a[href]").forEach((anchor) => {
      anchor.addEventListener("click", () => closeNavMenu());
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeNavMenu();
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
    if (!canPersistGuestProgress()) return;
    try {
      writeProgressKey(
        KEYS.lastLesson,
        JSON.stringify({
          path: payload.path,
          title: payload.title || "Lesson",
          course: payload.course || "",
          page: payload.page || "",
          ts: Date.now(),
        })
      );
      recordActivityDay();
    } catch (error) {
      /* quota / private mode */
    }
  };

  const setLastQuiz = (payload) => {
    if (!payload || !payload.quiz) return;
    if (!canPersistGuestProgress()) return;
    try {
      writeProgressKey(
        KEYS.lastQuiz,
        JSON.stringify({
          quiz: payload.quiz,
          title: payload.title || "Quiz",
          ts: Date.now(),
        })
      );
      recordActivityDay();
    } catch (error) {
      /* ignore */
    }
  };

  /** Local calendar day key (YYYY-MM-DD) for streak tracking. */
  const activityDayKey = (date = new Date()) => {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, "0");
    const d = String(date.getDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
  };

  const getActivityDays = () => {
    const raw = safeParse(localStorage.getItem(KEYS.activityDays), []);
    return Array.isArray(raw) ? raw.filter((d) => typeof d === "string") : [];
  };

  /** Record today as an active study day (kept for ~90 days). */
  const recordActivityDay = () => {
    if (!canPersistGuestProgress()) return getActivityDays();
    try {
      const today = activityDayKey();
      const next = new Set(getActivityDays());
      next.add(today);
      const pruned = [...next]
        .filter((d) => /^\d{4}-\d{2}-\d{2}$/.test(d))
        .sort()
        .slice(-90);
      writeProgressKey(KEYS.activityDays, JSON.stringify(pruned));
      window.setTimeout(() => {
        try {
          celebrateStreakMilestones();
        } catch (error) {
          /* ignore */
        }
      }, 0);
      return pruned;
    } catch (error) {
      return getActivityDays();
    }
  };

  /** One-time toast when a study streak crosses a milestone. */
  const celebrateStreakMilestones = () => {
    const streak = getStudyStreak();
    const labels = {
      3: "3-day streak — solid start",
      7: "7-day streak — a full week",
      14: "2-week streak — strong habit",
      30: "30-day streak — outstanding",
    };
    if (!labels[streak]) return;
    const key = "pf-streak-milestones";
    let seen = [];
    try {
      const raw = localStorage.getItem(key) || sessionStorage.getItem(key) || "[]";
      seen = JSON.parse(raw);
    } catch (error) {
      seen = [];
    }
    if (!Array.isArray(seen)) seen = [];
    if (seen.includes(streak)) return;
    seen.push(streak);
    try {
      if (canPersistGuestProgress()) writeProgressKey(key, JSON.stringify(seen));
      else sessionStorage.setItem(key, JSON.stringify(seen));
    } catch (error) {
      /* private mode */
    }
    showToast(labels[streak], { tone: "success" });
  };

  /** Consecutive active days ending today or yesterday. */
  const getStudyStreak = () => {
    const days = new Set(getActivityDays());
    if (!days.size) return 0;
    const cursor = new Date();
    const today = activityDayKey(cursor);
    if (!days.has(today)) {
      cursor.setDate(cursor.getDate() - 1);
      if (!days.has(activityDayKey(cursor))) return 0;
    }
    let streak = 0;
    while (days.has(activityDayKey(cursor))) {
      streak += 1;
      cursor.setDate(cursor.getDate() - 1);
      if (streak > 365) break;
    }
    return streak;
  };

  const escapeHtml = (str) =>
    String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");

  /** Human-friendly relative time for resume / activity stamps. */
  const formatRelativeTime = (ts) => {
    const ms = Number(ts) || 0;
    if (!ms) return "";
    const diff = Date.now() - ms;
    if (diff < 0) return "just now";
    const sec = Math.floor(diff / 1000);
    if (sec < 45) return "just now";
    const min = Math.floor(sec / 60);
    if (min < 60) return min === 1 ? "1 minute ago" : `${min} minutes ago`;
    const hr = Math.floor(min / 60);
    if (hr < 24) return hr === 1 ? "1 hour ago" : `${hr} hours ago`;
    const day = Math.floor(hr / 24);
    if (day === 1) return "yesterday";
    if (day < 14) return `${day} days ago`;
    try {
      return new Date(ms).toLocaleDateString(undefined, {
        year: "numeric",
        month: "short",
        day: "numeric",
      });
    } catch (error) {
      return "";
    }
  };

  const prefersReducedMotion = () =>
    typeof window.matchMedia === "function" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

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
    const params = new URLSearchParams(window.location.search);
    const currentLessonPath = params.get("path") || "";
    const currentQuizPath = params.get("quiz") || "";
    const onCurrentLesson =
      currentLessonPath && last && last.path && currentLessonPath === last.path;
    const onCurrentQuiz =
      currentQuizPath && lastQuiz && lastQuiz.quiz && currentQuizPath === lastQuiz.quiz;

    if ((!last || !last.path) && (!lastQuiz || !lastQuiz.quiz)) {
      host.hidden = true;
      host.innerHTML = "";
      return;
    }
    const preferQuiz =
      lastQuiz &&
      lastQuiz.quiz &&
      (!last || !last.path || (Number(lastQuiz.ts) || 0) > (Number(last?.ts) || 0));

    // Don't advertise "continue" for the page the learner is already viewing.
    if (preferQuiz && onCurrentQuiz) {
      if (last && last.path && !onCurrentLesson) {
        // Fall through to lesson resume instead of hiding entirely.
      } else {
        host.hidden = true;
        host.innerHTML = "";
        return;
      }
    }
    if (!preferQuiz && onCurrentLesson) {
      if (lastQuiz && lastQuiz.quiz && !onCurrentQuiz) {
        // Prefer showing last quiz when already on the lesson.
      } else {
        host.hidden = true;
        host.innerHTML = "";
        return;
      }
    }

    const showQuiz =
      preferQuiz && lastQuiz && lastQuiz.quiz && !onCurrentQuiz
        ? true
        : !preferQuiz && onCurrentLesson && lastQuiz && lastQuiz.quiz && !onCurrentQuiz;

    const dayPartGreeting = () => {
      const now = new Date();
      const hour = now.getHours();
      const weekday = now.getDay(); // 0 Sun … 6 Sat
      const month = now.getMonth(); // 0 Jan … 11 Dec
      const dayOfMonth = now.getDate();
      const firstWeekdayOfMonth = weekday === 1 && dayOfMonth <= 7;
      const midMonth = dayOfMonth >= 10 && dayOfMonth <= 16;
      const lateMonth = dayOfMonth >= 17 && dayOfMonth <= 23;
      const monthEnd = dayOfMonth >= 24;
      const closingOctober = month === 9 && dayOfMonth >= 26; // late October
      if (firstWeekdayOfMonth && hour < 12) return "New month energy";
      if (midMonth && hour < 12) return "Mid-month momentum";
      if (lateMonth && hour < 12) return "Late-month push";
      if (closingOctober && hour < 12) return "Closing October strong";
      if (monthEnd && hour < 12) return "Month-end stretch";
      if (month === 9 && hour < 12) return "Crisp autumn focus"; // October
      if (weekday === 1 && hour < 12) return "Fresh week ahead";
      if ((weekday === 0 || weekday === 6) && hour < 12) return "Easy weekend morning";
      if ((weekday === 0 || weekday === 6) && hour < 17) return "Weekend pace";
      if (hour < 12) return "Good morning";
      if (hour < 17) return "Good afternoon";
      return "Good evening";
    };

    const welcomeBack = (ts) => {
      const delta = Date.now() - (Number(ts) || 0);
      if (!ts || delta < 18 * 60 * 60 * 1000) return `${dayPartGreeting()} — `;
      if (delta < 6 * 24 * 60 * 60 * 1000) return "Welcome back — ";
      return "Good to see you again — ";
    };

    if (showQuiz) {
      const when = formatRelativeTime(lastQuiz.ts);
      const greet = welcomeBack(lastQuiz.ts);
      host.hidden = false;
      host.innerHTML = `
      <div class="resume-banner" role="region" aria-label="Resume learning">
        <div class="resume-banner-copy">
          <strong>${greet}Continue your last quiz</strong>
          <span>${escapeHtml(lastQuiz.title || "Quiz")}${
            when ? ` <em class="resume-when">· ${escapeHtml(when)}</em>` : ""
          }</span>
        </div>
        <div class="resume-banner-actions">
          <a class="btn btn-primary resume-cta-pulse" href="quiz-viewer.html?quiz=${encodeURIComponent(lastQuiz.quiz)}">Open quiz</a>
          ${
            last && last.path && !onCurrentLesson
              ? `<a class="btn btn-secondary" href="course-viewer.html?path=${encodeURIComponent(last.path)}">Last lesson</a>`
              : ""
          }
        </div>
      </div>`;
      return;
    }
    if (!last || !last.path || onCurrentLesson) {
      host.hidden = true;
      host.innerHTML = "";
      return;
    }
    const done = isCompleted(last.path);
    const greet = welcomeBack(last.ts);
    const label = done
      ? `${greet}Review last lesson`
      : `${greet}Continue where you left off`;
    const courseBit = last.course ? ` · ${last.course}` : "";
    const when = formatRelativeTime(last.ts);
    host.hidden = false;
    host.innerHTML = `
      <div class="resume-banner" role="region" aria-label="Resume learning">
        <div class="resume-banner-copy">
          <strong>${label}</strong>
          <span>${escapeHtml(last.title)}${escapeHtml(courseBit)}${
            when ? ` <em class="resume-when">· ${escapeHtml(when)}</em>` : ""
          }</span>
        </div>
        <div class="resume-banner-actions">
          <a class="btn btn-primary resume-cta-pulse" href="course-viewer.html?path=${encodeURIComponent(last.path)}">Open lesson</a>
          ${last.page ? `<a class="btn btn-secondary" href="${escapeHtml(last.page)}">Course home</a>` : ""}
          ${
            lastQuiz && lastQuiz.quiz
              ? `<a class="btn btn-secondary" href="quiz-viewer.html?quiz=${encodeURIComponent(lastQuiz.quiz)}">Last quiz</a>`
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
    if (!canPersistGuestProgress()) {
      const host = document.getElementById("pf-persona-host");
      const status = host?.querySelector(".persona-picker-status");
      if (status) {
        status.innerHTML =
          "On-device progress is off. Turn it back on in <a href=\"privacy.html#guest-progress\">Privacy</a>, then choose again.";
      }
      return null;
    }
    try {
      writeProgressKey(KEYS.persona, id);
    } catch (error) {
      /* ignore */
    }
    applyPersonaCopy();
    mountPersonaPicker();
    document.dispatchEvent(
      new CustomEvent("pf:persona-changed", { detail: { persona: PERSONAS[id] } })
    );
    showToast(`Learning focus: ${PERSONAS[id].label}`, { tone: "success" });
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

  /** Stamp footers with current year + last maintenance date. */
  const enhanceFooters = () => {
    document.querySelectorAll("footer.footer").forEach((footer) => {
      if (footer.querySelector(".site-meta")) return;
      const meta = document.createElement("p");
      meta.className = "site-meta";
      meta.innerHTML = `© ${SITE_YEAR} Programming Foundations · Last maintained ${SITE_MAINTAINED_LABEL}`;
      footer.appendChild(meta);
    });
  };

  /** Compact sticky header after scroll for more reading space. */
  const wireHeaderScroll = () => {
    const header = document.querySelector(".site-header");
    if (!header) return;
    const onScroll = () => {
      header.classList.toggle("is-compact", window.scrollY > 28);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  };

  /** Floating back-to-top control once the learner scrolls past the fold. */
  const mountBackToTop = () => {
    if (document.getElementById("pf-back-top")) return;
    const btn = document.createElement("button");
    btn.type = "button";
    btn.id = "pf-back-top";
    btn.className = "back-to-top";
    btn.setAttribute("aria-label", "Back to top");
    btn.title = "Back to top (b)";
    btn.innerHTML = '<span aria-hidden="true">↑</span>';
    btn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: prefersReducedMotion() ? "auto" : "smooth" });
    });
    document.body.appendChild(btn);
    const onScroll = () => {
      btn.classList.toggle("is-visible", window.scrollY > 420);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  };

  /** Press “b” to jump back to the top when scrolled. */
  const wireBackToTopHotkey = () => {
    if (document.documentElement.dataset.pfBackTopKey === "1") return;
    document.documentElement.dataset.pfBackTopKey = "1";
    document.addEventListener("keydown", (event) => {
      if (event.key !== "b" && event.key !== "B") return;
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      if (window.scrollY < 120) return;
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: prefersReducedMotion() ? "auto" : "smooth" });
      const btn = document.getElementById("pf-back-top");
      if (btn) {
        btn.classList.add("is-hotkey");
        window.setTimeout(() => btn.classList.remove("is-hotkey"), 500);
      }
    });
  };

  /** Thin reading progress bar under the sticky header. */
  const mountReadingProgress = () => {
    if (document.getElementById("pf-read-progress")) return;
    const onLesson = Boolean(document.getElementById("lesson-content"));
    const bar = document.createElement("div");
    bar.id = "pf-read-progress";
    bar.className = "read-progress";
    bar.setAttribute("role", "progressbar");
    bar.setAttribute("aria-valuemin", "0");
    bar.setAttribute("aria-valuemax", "100");
    bar.setAttribute("aria-valuenow", "0");
    bar.setAttribute("aria-label", "Page reading progress");
    bar.innerHTML =
      '<div class="read-progress__fill"></div>' +
      (onLesson ? '<span class="read-progress__label" hidden>0%</span>' : "");
    document.body.appendChild(bar);
    const fill = bar.querySelector(".read-progress__fill");
    const label = bar.querySelector(".read-progress__label");
    if (onLesson && !document.documentElement.dataset.pfTitleBase) {
      document.documentElement.dataset.pfTitleBase = document.title;
    }
    const update = () => {
      const doc = document.documentElement;
      const max = Math.max(doc.scrollHeight - window.innerHeight, 1);
      const pct = Math.min(100, Math.max(0, (window.scrollY / max) * 100));
      const rounded = Math.round(pct);
      if (fill) fill.style.width = `${pct}%`;
      bar.setAttribute("aria-valuenow", String(rounded));
      if (label) {
        label.textContent = `${rounded}%`;
        label.hidden = rounded < 4;
        label.classList.toggle("is-near-end", rounded >= 92);
      }
      if (onLesson) {
        const base = document.documentElement.dataset.pfTitleBase || document.title;
        document.title = rounded >= 4 ? `(${rounded}%) ${base}` : base;
      }
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update, { passive: true });
  };

  /** Soft status toast for progress / interactive feedback. */
  let toastTimer = null;
  const showToast = (message, { tone = "info" } = {}) => {
    const text = String(message || "").trim();
    if (!text) return;
    let host = document.getElementById("pf-toast");
    if (!host) {
      host = document.createElement("div");
      host.id = "pf-toast";
      host.className = "pf-toast";
      host.setAttribute("role", "status");
      host.setAttribute("aria-live", "polite");
      document.body.appendChild(host);
      if (!document.documentElement.dataset.pfToastEsc) {
        document.documentElement.dataset.pfToastEsc = "1";
        document.addEventListener("keydown", (event) => {
          if (event.key !== "Escape") return;
          const toast = document.getElementById("pf-toast");
          if (!toast?.classList.contains("is-visible")) return;
          toast.classList.remove("is-visible");
          if (toastTimer) window.clearTimeout(toastTimer);
        });
      }
    }
    host.dataset.tone = tone;
    host.textContent = text;
    host.classList.add("is-visible");
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      host.classList.remove("is-visible");
    }, 2800);
  };

  /** Gentle scroll-reveal for section content across pages. */
  const enhanceScrollReveal = () => {
    const main = document.getElementById("main");
    if (main) main.classList.add("page-enter");
    if (prefersReducedMotion()) return;
    const targets = document.querySelectorAll(
      "main .section, main .widget-section, main .help-card, main .feature-card, main .course-tile, main .step, main .support-panel, main .persona-picker"
    );
    if (!targets.length || !("IntersectionObserver" in window)) return;
    targets.forEach((el, i) => {
      if (el.classList.contains("reveal") || el.closest(".hero-bleed")) return;
      el.classList.add("reveal");
      el.style.setProperty("--reveal-delay", `${Math.min(i % 6, 5) * 40}ms`);
    });
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-inview");
          io.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
  };

  /** Soft pulse on matcher / playground success for clearer feedback. */
  const enhanceInteractiveSurfaces = () => {
    const matcher = document.getElementById("matcher-result");
    if (matcher) {
      const pulse = () => {
        matcher.classList.remove("is-fresh");
        void matcher.offsetWidth;
        matcher.classList.add("is-fresh");
      };
      const mo = new MutationObserver(pulse);
      mo.observe(matcher, { childList: true, subtree: true });
    }
    const output = document.getElementById("playground-output");
    if (output) {
      const pulse = () => {
        output.classList.remove("is-fresh");
        void output.offsetWidth;
        output.classList.add("is-fresh");
      };
      const mo = new MutationObserver(pulse);
      mo.observe(output, { characterData: true, childList: true, subtree: true });
    }
  };

  /** Resolve COURSE_MODULE_MAP key from a tile heading. */
  const resolveCourseMapKey = (label) => {
    const name = String(label || "").trim();
    if (!name) return "";
    if (COURSE_MODULE_MAP[name]) return name;
    const withCourse = `${name} Course`;
    if (COURSE_MODULE_MAP[withCourse]) return withCourse;
    const foundations = `${name} Foundations Course`;
    if (COURSE_MODULE_MAP[foundations]) return foundations;
    // Donor hubs use short titles like "AWS Cloud" → "AWS Cloud Course"
    const found = Object.keys(COURSE_MODULE_MAP).find(
      (key) => key === name || key.startsWith(`${name} `) || key.replace(/ Course$/, "") === name
    );
    return found || "";
  };

  /** Show live progress chips on course tiles when progress exists. */
  const enhanceCourseTiles = () => {
    const last = getLastLesson();
    const lastCourse = String(last?.course || "").trim().toLowerCase();
    document.querySelectorAll(".course-tile").forEach((tile) => {
      if (tile.querySelector(".course-tile-progress")) return;
      const heading = tile.querySelector("h3, h4");
      const name = (heading?.textContent || "").trim();
      const mapKey = resolveCourseMapKey(name);
      if (!mapKey || !COURSE_MODULE_MAP[mapKey]) return;
      const progress = courseProgress(mapKey);
      if (!progress.total) return;
      tile.dataset.pfProgressPct = String(progress.percent || 0);
      tile.dataset.pfProgressDone = String(progress.done || 0);
      tile.dataset.pfProgressTotal = String(progress.total || 0);
      const chip = document.createElement("p");
      chip.className = "course-tile-progress";
      chip.setAttribute("aria-label", `${name} progress`);
      const ring = document.createElement("span");
      ring.className = "course-tile-ring";
      ring.setAttribute("aria-hidden", "true");
      ring.style.setProperty("--pct", String(progress.percent || 0));
      const label = document.createElement("span");
      label.className = "course-tile-progress__label";
      if (progress.done === 0) {
        label.textContent = `${progress.total} modules · not started`;
      } else if (progress.done >= progress.total) {
        label.innerHTML = `<strong>Complete</strong> · ${progress.total} modules`;
        tile.classList.add("is-complete");
      } else {
        label.innerHTML = `<strong>${progress.percent}%</strong> · ${progress.done} of ${progress.total} modules`;
        tile.classList.add("is-in-progress");
      }
      chip.appendChild(ring);
      chip.appendChild(label);
      const body = tile.querySelector(".course-tile-body") || tile;
      const buttons = body.querySelector(".button-row");
      if (buttons) body.insertBefore(chip, buttons);
      else body.appendChild(chip);

      // Soft “last opened” cue for the course matching the learner’s last lesson.
      if (
        lastCourse &&
        !tile.querySelector(".course-tile-last") &&
        (mapKey.toLowerCase() === lastCourse ||
          mapKey.toLowerCase().startsWith(lastCourse) ||
          lastCourse.startsWith(name.toLowerCase()) ||
          name.toLowerCase().includes(lastCourse.replace(/ course$/, "")))
      ) {
        tile.classList.add("is-last-opened");
        const badge = document.createElement("span");
        badge.className = "course-tile-last";
        badge.textContent = "Last opened";
        const titleRow = heading?.parentElement || body;
        if (heading) heading.insertAdjacentElement("afterend", badge);
        else titleRow.prepend(badge);
      }
    });
  };

  /** Highlight deep-linked steps (Start Here, Help anchors). */
  const enhanceHashTargets = () => {
    const apply = () => {
      document.querySelectorAll(".is-hash-target").forEach((el) => {
        el.classList.remove("is-hash-target");
      });
      const id = (location.hash || "").replace(/^#/, "");
      if (!id) return;
      const target = document.getElementById(id);
      if (!target) return;
      target.classList.add("is-hash-target");
      if (!prefersReducedMotion()) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    };
    apply();
    window.addEventListener("hashchange", apply);
  };

  /** Live-filter course tiles on the Courses page. */
  const wireCourseTileFilter = () => {
    const input = document.getElementById("course-tile-filter");
    const status = document.getElementById("course-tile-filter-status");
    const tiles = Array.from(document.querySelectorAll(".course-tile"));
    if (!input || !tiles.length) return;
    const apply = () => {
      const q = input.value.trim().toLowerCase();
      let shown = 0;
      tiles.forEach((tile) => {
        const hay = tile.textContent.toLowerCase();
        const match = !q || hay.includes(q);
        tile.hidden = !match;
        if (match) shown += 1;
      });
      if (status) {
        status.textContent = q
          ? shown
            ? `${shown} course${shown === 1 ? "" : "s"} match “${input.value.trim()}”.`
            : "No courses match — try another word."
          : "";
        status.classList.toggle("is-empty", Boolean(q) && shown === 0);
      }
      let empty = document.getElementById("course-tile-filter-empty");
      if (q && shown === 0) {
        if (!empty) {
          empty = document.createElement("p");
          empty.id = "course-tile-filter-empty";
          empty.className = "course-filter-empty note";
          empty.innerHTML =
            'Nothing matched. <button type="button" class="chip-btn" data-clear-filter>Clear filter</button>';
          input.parentElement?.appendChild(empty);
          empty.querySelector("[data-clear-filter]")?.addEventListener("click", () => {
            input.value = "";
            input.dispatchEvent(new Event("input", { bubbles: true }));
            input.focus();
          });
        }
        empty.hidden = false;
      } else if (empty) {
        empty.hidden = true;
      }
    };
    input.addEventListener("input", apply);
  };

  /** Press "/" to jump to the nearest page search/filter field. */
  const wireQuickFindShortcut = () => {
    const candidates = [
      document.getElementById("course-tile-filter"),
      document.getElementById("help-filter"),
      document.getElementById("tutorial-filter"),
      document.getElementById("course-search"),
    ].filter(Boolean);
    if (!candidates.length) return;
    document.addEventListener("keydown", (event) => {
      if (event.key !== "/" || event.metaKey || event.ctrlKey || event.altKey) return;
      const tag = (event.target && event.target.tagName) || "";
      if (/^(INPUT|TEXTAREA|SELECT)$/i.test(tag) || event.target?.isContentEditable) return;
      event.preventDefault();
      const field = candidates[0];
      field.focus();
      if (typeof field.select === "function") field.select();
    });
  };

  /** Mark current path nodes for clearer progress feedback. */
  const enhancePathNodes = () => {
    const apply = () => {
      document.querySelectorAll(".path-node").forEach((node) => {
        const alive = node.classList.contains("is-complete") || node.classList.contains("is-active");
        node.classList.toggle("path-node--alive", alive);
      });
    };
    apply();
    document.querySelectorAll(".path-viz").forEach((viz) => {
      if (viz.dataset.pfPathObserved) return;
      viz.dataset.pfPathObserved = "1";
      const mo = new MutationObserver(apply);
      mo.observe(viz, { attributes: true, subtree: true, attributeFilter: ["class"] });
    });
    // Page scripts sync path state after boot — catch the late update.
    window.setTimeout(apply, 0);
    window.setTimeout(apply, 120);
  };

  const isTypingTarget = (target) => {
    const tag = (target && target.tagName) || "";
    return /^(INPUT|TEXTAREA|SELECT)$/i.test(tag) || Boolean(target?.isContentEditable);
  };

  /** Press “?” for a lightweight keyboard shortcuts sheet. */
  const mountKeyboardShortcuts = () => {
    if (document.getElementById("pf-shortcut-sheet")) return;
    const sheet = document.createElement("div");
    sheet.id = "pf-shortcut-sheet";
    sheet.className = "shortcut-sheet";
    sheet.hidden = true;
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.setAttribute("aria-label", "Keyboard shortcuts");
    sheet.innerHTML = `
      <div class="shortcut-sheet__panel">
        <div class="shortcut-sheet__head">
          <strong>Keyboard shortcuts</strong>
          <button type="button" class="shortcut-sheet__close" aria-label="Close shortcuts">Close</button>
        </div>
        <ul class="shortcut-sheet__list">
          <li><kbd>?</kbd> <span>Show or hide this help</span></li>
          <li><kbd>/</kbd> <span>Jump to page search or filter</span></li>
          <li><kbd>g</kbd> then <kbd>h</kbd> / <kbd>c</kbd> / <kbd>s</kbd> / <kbd>a</kbd> / <kbd>t</kbd> / <kbd>e</kbd> / <kbd>r</kbd> <span>Go Home / Courses / Start Here / Account / Tutorials / Help / Resume</span></li>
          <li><kbd>g</kbd> then <kbd>g</kbd> <span>Jump to top of page</span></li>
          <li><kbd>[</kbd> / <kbd>]</kbd> <span>Previous / next lesson</span></li>
          <li><kbd>n</kbd> <span>Open the “Up next” module</span></li>
          <li><kbd>j</kbd> / <kbd>k</kbd> <span>Next / previous module in the list</span></li>
          <li><kbd>1</kbd>–<kbd>4</kbd> / <kbd>A</kbd>–<kbd>D</kbd> <span>Pick a quiz answer</span></li>
          <li><kbd>Enter</kbd> <span>Check quiz answers or open focused module</span></li>
          <li><kbd>f</kbd> <span>Focus mode (lessons)</span></li>
          <li><kbd>o</kbd> <span>Jump to lesson outline</span></li>
          <li><kbd>b</kbd> <span>Back to top</span></li>
          <li><kbd>Ctrl</kbd> + <kbd>Enter</kbd> <span>Run playground (home)</span></li>
          <li><kbd>Esc</kbd> <span>Close dialogs, toast, go-chord, and this sheet</span></li>
        </ul>
        <p class="note">Shortcuts skip when you are typing in a field.</p>
      </div>`;
    document.body.appendChild(sheet);
    const close = () => {
      sheet.hidden = true;
    };
    const open = () => {
      sheet.hidden = false;
      sheet.querySelector(".shortcut-sheet__close")?.focus();
    };
    sheet.querySelector(".shortcut-sheet__close")?.addEventListener("click", close);
    sheet.addEventListener("click", (event) => {
      if (event.target === sheet) close();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !sheet.hidden) {
        event.preventDefault();
        close();
        return;
      }
      if (event.key !== "?" || event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      event.preventDefault();
      if (sheet.hidden) open();
      else close();
    });
  };

  /** Compact floating resume chip when the main banner scrolls out of view. */
  const mountStickyResume = () => {
    if (document.getElementById("pf-sticky-resume")) return;
    const chip = document.createElement("a");
    chip.id = "pf-sticky-resume";
    chip.className = "sticky-resume";
    chip.hidden = true;
    document.body.appendChild(chip);

    const sync = () => {
      const host = document.getElementById("pf-resume-host");
      const banner = host?.querySelector(".resume-banner");
      const primary = banner?.querySelector(".resume-banner-actions .btn-primary");
      if (!host || host.hidden || !banner || !primary) {
        chip.hidden = true;
        return;
      }
      const href = primary.getAttribute("href") || "";
      const label =
        banner.querySelector(".resume-banner-copy strong")?.textContent?.trim() || "Continue learning";
      chip.href = href;
      chip.textContent = label;
      const rect = banner.getBoundingClientRect();
      const outOfView = rect.bottom < 8;
      chip.hidden = !outOfView || !href;
    };

    sync();
    window.addEventListener("scroll", sync, { passive: true });
    window.addEventListener("resize", sync, { passive: true });
    const host = document.getElementById("pf-resume-host");
    if (host) {
      const mo = new MutationObserver(sync);
      mo.observe(host, { childList: true, subtree: true, attributes: true });
    }
  };

  /** Estimate reading time for the open lesson. */
  const enhanceLessonReadingMeta = () => {
    const content = document.getElementById("lesson-content");
    const title = document.getElementById("lesson-title");
    if (!content || !title) return;
    let meta = document.getElementById("lesson-reading-meta");
    if (!meta) {
      meta = document.createElement("p");
      meta.id = "lesson-reading-meta";
      meta.className = "lesson-reading-meta note";
      title.insertAdjacentElement("afterend", meta);
    }
    const update = () => {
      const text = (content.innerText || "").replace(/\s+/g, " ").trim();
      if (!text || /loading|unavailable/i.test(title.textContent || "")) {
        meta.hidden = true;
        meta.textContent = "";
        return;
      }
      const words = text.split(" ").filter(Boolean).length;
      const minutes = Math.max(1, Math.round(words / 200));
      const bar = document.getElementById("pf-read-progress");
      const pct = Number(bar?.getAttribute("aria-valuenow") || 0);
      const left = Math.max(1, Math.ceil(minutes * (1 - pct / 100)));
      meta.hidden = false;
      meta.textContent =
        pct >= 8 && pct < 96
          ? `About ${minutes} min read · ~${left} min left · ${words.toLocaleString()} words`
          : `About ${minutes} min read · ${words.toLocaleString()} words`;
    };
    update();
    const mo = new MutationObserver(update);
    mo.observe(content, { childList: true, subtree: true, characterData: true });
    if (!meta.dataset.pfRemainWired) {
      meta.dataset.pfRemainWired = "1";
      window.addEventListener("scroll", update, { passive: true });
      window.addEventListener("resize", update, { passive: true });
    }
  };

  /** Compact in-lesson outline from h2/h3 with scroll-spy highlighting. */
  const mountLessonOutline = () => {
    const content = document.getElementById("lesson-content");
    const title = document.getElementById("lesson-title");
    if (!content || !title) return;
    if (content.dataset.pfOutlineWired === "1") return;
    content.dataset.pfOutlineWired = "1";

    const slugify = (text, used) => {
      let base = String(text || "")
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-|-$/g, "")
        .slice(0, 48) || "section";
      let id = base;
      let n = 2;
      while (used.has(id) || document.getElementById(id)) {
        id = `${base}-${n}`;
        n += 1;
      }
      used.add(id);
      return id;
    };

    const sync = () => {
      const headings = Array.from(content.querySelectorAll("h2, h3")).filter((h) =>
        (h.textContent || "").trim()
      );
      let nav = document.getElementById("pf-lesson-outline");
      if (headings.length < 3) {
        if (nav) nav.remove();
        return;
      }
      const used = new Set();
      const items = headings.map((heading) => {
        if (!heading.id) heading.id = slugify(heading.textContent, used);
        else used.add(heading.id);
        return {
          id: heading.id,
          label: (heading.textContent || "").trim(),
          level: heading.tagName === "H3" ? 3 : 2,
        };
      });
      if (!nav) {
        nav = document.createElement("nav");
        nav.id = "pf-lesson-outline";
        nav.className = "lesson-outline";
        nav.setAttribute("aria-label", "On this lesson");
        const meta = document.getElementById("lesson-reading-meta");
        if (meta) meta.insertAdjacentElement("afterend", nav);
        else title.insertAdjacentElement("afterend", nav);
      }
      const wasCollapsed = nav.classList.contains("is-collapsed");
      const canCollapse = items.length > 6;
      const passedCount = Number(nav.dataset.pfPassed || 0);
      const progressBit =
        passedCount > 0
          ? ` · ${Math.min(passedCount, items.length)} of ${items.length} reached`
          : ` · ${items.length} sections`;
      nav.innerHTML = `
        <div class="lesson-outline__head">
          <p class="lesson-outline__label">On this lesson${progressBit}</p>
          ${
            canCollapse
              ? `<button type="button" class="lesson-outline__toggle" aria-expanded="${
                  wasCollapsed ? "false" : "true"
                }">${wasCollapsed ? "Show all" : "Show less"}</button>`
              : ""
          }
        </div>
        <ol class="lesson-outline__list">
          ${items
            .map(
              (item) =>
                `<li class="lesson-outline__item lesson-outline__item--h${item.level}">
                  <a href="#${escapeHtml(item.id)}">${escapeHtml(item.label)}</a>
                </li>`
            )
            .join("")}
        </ol>`;
      if (canCollapse && wasCollapsed) nav.classList.add("is-collapsed");
      else nav.classList.remove("is-collapsed");
      const toggle = nav.querySelector(".lesson-outline__toggle");
      if (toggle) {
        toggle.addEventListener("click", () => {
          const collapsed = nav.classList.toggle("is-collapsed");
          toggle.setAttribute("aria-expanded", collapsed ? "false" : "true");
          toggle.textContent = collapsed ? "Show all" : "Show less";
        });
      }
      // On narrow viewports, collapse after jumping to a section so the lesson stays in view.
      nav.querySelectorAll(".lesson-outline__list a").forEach((link) => {
        link.addEventListener("click", () => {
          if (window.matchMedia("(max-width: 720px)").matches && canCollapse) {
            window.setTimeout(() => {
              nav.classList.add("is-collapsed");
              const t = nav.querySelector(".lesson-outline__toggle");
              if (t) {
                t.setAttribute("aria-expanded", "false");
                t.textContent = "Show all";
              }
            }, 320);
          }
        });
      });
    };

    const spy = () => {
      const nav = document.getElementById("pf-lesson-outline");
      if (!nav) return;
      const links = Array.from(nav.querySelectorAll("a[href^='#']"));
      if (!links.length) return;
      const offset = 96;
      let activeId = "";
      let activeIndex = -1;
      links.forEach((link, index) => {
        const id = decodeURIComponent((link.getAttribute("href") || "").slice(1));
        const el = document.getElementById(id);
        if (!el) return;
        if (el.getBoundingClientRect().top <= offset) {
          activeId = id;
          activeIndex = index;
        }
      });
      if (!activeId) {
        activeId = decodeURIComponent((links[0].getAttribute("href") || "").slice(1));
        activeIndex = 0;
      }
      links.forEach((link, index) => {
        const id = decodeURIComponent((link.getAttribute("href") || "").slice(1));
        link.classList.toggle("is-active", id === activeId);
        link.classList.toggle("is-passed", index < activeIndex);
      });
      const passed = Math.max(activeIndex + 1, 0);
      const prevPassed = Number(nav.dataset.pfPassed || 0);
      if (passed !== prevPassed) {
        nav.dataset.pfPassed = String(passed);
        const label = nav.querySelector(".lesson-outline__label");
        if (label) {
          label.textContent = `On this lesson · ${passed} of ${links.length} reached`;
        }
      }
    };

    sync();
    spy();
    const mo = new MutationObserver(() => {
      sync();
      spy();
    });
    mo.observe(content, { childList: true, subtree: true, characterData: true });
    window.addEventListener("scroll", spy, { passive: true });
    window.addEventListener("resize", spy, { passive: true });
  };

  /** Press “o” to jump to the lesson outline (when present). */
  const wireOutlineHotkey = () => {
    if (document.documentElement.dataset.pfOutlineKey === "1") return;
    document.documentElement.dataset.pfOutlineKey = "1";
    document.addEventListener("keydown", (event) => {
      if (event.key !== "o" && event.key !== "O") return;
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      const nav = document.getElementById("pf-lesson-outline");
      if (!nav) return;
      event.preventDefault();
      if (nav.classList.contains("is-collapsed")) {
        nav.classList.remove("is-collapsed");
        const toggle = nav.querySelector(".lesson-outline__toggle");
        if (toggle) {
          toggle.setAttribute("aria-expanded", "true");
          toggle.textContent = "Show less";
        }
      }
      nav.scrollIntoView({ block: "start", behavior: prefersReducedMotion() ? "auto" : "smooth" });
      nav.classList.add("is-flash");
      window.setTimeout(() => nav.classList.remove("is-flash"), 900);
      nav.querySelector(".lesson-outline__list a")?.focus({ preventScroll: true });
    });
  };

  /** Prefetch internal HTML pages on hover/focus for snappier navigation. */
  const enhanceInternalPrefetch = () => {
    if (document.documentElement.dataset.pfPrefetch === "1") return;
    document.documentElement.dataset.pfPrefetch = "1";
    const seen = new Set();
    const prefetch = (href) => {
      try {
        const url = new URL(href, window.location.href);
        if (url.origin !== window.location.origin) return;
        if (!/\.html?$/i.test(url.pathname)) return;
        const key = url.pathname + url.search;
        if (seen.has(key)) return;
        seen.add(key);
        const link = document.createElement("link");
        link.rel = "prefetch";
        link.href = url.pathname + url.search;
        link.as = "document";
        document.head.appendChild(link);
      } catch (error) {
        /* ignore bad hrefs */
      }
    };
    document.addEventListener(
      "pointerenter",
      (event) => {
        const a = event.target?.closest?.("a[href]");
        if (!a) return;
        prefetch(a.getAttribute("href") || "");
      },
      true
    );
    document.addEventListener(
      "focusin",
      (event) => {
        const a = event.target?.closest?.("a[href]");
        if (!a) return;
        prefetch(a.getAttribute("href") || "");
      },
      true
    );
  };

  /** One-click copy of the current lesson/quiz URL. */
  const mountCopyLinkButton = () => {
    const row =
      document.getElementById("lesson-actions-row") ||
      document.querySelector("#quiz-actions .button-row");
    if (!row || row.querySelector("[data-pf-copy-link]")) return;
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "btn btn-ghost";
    btn.setAttribute("data-pf-copy-link", "1");
    btn.textContent = "Copy link";
    btn.addEventListener("click", async () => {
      const url = window.location.href;
      try {
        if (navigator.clipboard?.writeText) {
          await navigator.clipboard.writeText(url);
        } else {
          const input = document.createElement("input");
          input.value = url;
          document.body.appendChild(input);
          input.select();
          document.execCommand("copy");
          input.remove();
        }
        showToast("Link copied", { tone: "success" });
        btn.textContent = "Copied";
        window.setTimeout(() => {
          btn.textContent = "Copy link";
        }, 1600);
      } catch (error) {
        showToast("Could not copy — copy from the address bar", { tone: "info" });
      }
    });
    row.appendChild(btn);
  };

  /** Live-filter tutorial clips once the catalog has rendered. */
  const wireTutorialFilter = () => {
    const input = document.getElementById("tutorial-filter");
    const status = document.getElementById("tutorial-filter-status");
    if (!input) return;
    const apply = () => {
      const clips = Array.from(document.querySelectorAll(".promo-clip"));
      if (!clips.length) {
        if (status) status.textContent = "";
        return;
      }
      const q = input.value.trim().toLowerCase();
      let shown = 0;
      clips.forEach((clip) => {
        const hay = clip.textContent.toLowerCase();
        const match = !q || hay.includes(q);
        clip.hidden = !match;
        if (match) shown += 1;
      });
      if (status) {
        status.textContent = q
          ? shown
            ? `${shown} tutorial${shown === 1 ? "" : "s"} match “${input.value.trim()}”.`
            : "No tutorials match — try setup, Python, or captions."
          : "";
      }
    };
    input.addEventListener("input", apply);
    const catalog = document.getElementById("tutorial-catalog");
    if (catalog) {
      const mo = new MutationObserver(apply);
      mo.observe(catalog, { childList: true, subtree: true });
    }
    apply();
  };

  /** Clarify links that open a new tab. */
  const enhanceExternalLinks = () => {
    document.querySelectorAll('a[target="_blank"]').forEach((anchor) => {
      if (!anchor.getAttribute("rel")) {
        anchor.setAttribute("rel", "noopener noreferrer");
      }
      if (!anchor.classList.contains("is-external")) {
        anchor.classList.add("is-external");
      }
      const label = (anchor.getAttribute("aria-label") || anchor.textContent || "").trim();
      if (label && !/new (tab|window)/i.test(label) && !anchor.getAttribute("aria-label")) {
        anchor.setAttribute("aria-label", `${label} (opens in a new tab)`);
      }
    });
  };

  /** Dim chrome and widen the lesson column for focused reading. */
  const mountLessonFocusMode = () => {
    const content = document.getElementById("lesson-content");
    if (!content || document.getElementById("pf-focus-toggle")) return;
    const row =
      document.getElementById("lesson-actions-row") ||
      document.querySelector(".lesson-actions .button-row");
    if (!row) return;
    const btn = document.createElement("button");
    btn.type = "button";
    btn.id = "pf-focus-toggle";
    btn.className = "btn btn-ghost";
    btn.setAttribute("aria-pressed", "false");
    btn.textContent = "Focus mode";
    const apply = (on) => {
      document.body.classList.toggle("is-focus-mode", on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      btn.textContent = on ? "Exit focus" : "Focus mode";
      try {
        sessionStorage.setItem("pf-focus-mode", on ? "1" : "0");
      } catch (error) {
        /* ignore */
      }
    };
    let on = false;
    try {
      on = sessionStorage.getItem("pf-focus-mode") === "1";
    } catch (error) {
      on = false;
    }
    apply(on);
    btn.addEventListener("click", () => apply(!document.body.classList.contains("is-focus-mode")));
    row.appendChild(btn);
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && document.body.classList.contains("is-focus-mode")) {
        const sheet = document.getElementById("pf-shortcut-sheet");
        if (sheet && !sheet.hidden) return;
        apply(false);
        return;
      }
      if (event.key !== "f" && event.key !== "F") return;
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      if (!document.getElementById("lesson-content")) return;
      event.preventDefault();
      apply(!document.body.classList.contains("is-focus-mode"));
    });
  };

  /** Bracket keys jump previous / next lesson when nav links exist. */
  const wireLessonNavKeys = () => {
    document.addEventListener("keydown", (event) => {
      if (event.key !== "[" && event.key !== "]") return;
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      const nav = document.getElementById("lesson-nav");
      if (!nav) return;
      const links = Array.from(nav.querySelectorAll("a[href]"));
      if (!links.length) return;
      const target = event.key === "[" ? links[0] : links[links.length - 1];
      if (!target?.href) return;
      event.preventDefault();
      window.location.href = target.href;
    });
  };

  /** Remember scroll depth per lesson so returning learners land near where they stopped. */
  const mountLessonScrollMemory = () => {
    const content = document.getElementById("lesson-content");
    if (!content) return;
    const params = new URLSearchParams(window.location.search);
    const path = params.get("path") || "";
    if (!path) return;
    const storageKey = `pf-lesson-scroll:${path}`;
    let restored = false;
    const save = () => {
      try {
        sessionStorage.setItem(
          storageKey,
          JSON.stringify({ y: Math.round(window.scrollY), ts: Date.now() })
        );
      } catch (error) {
        /* ignore */
      }
    };
    let timer = null;
    window.addEventListener(
      "scroll",
      () => {
        if (timer) clearTimeout(timer);
        timer = setTimeout(save, 180);
      },
      { passive: true }
    );
    window.addEventListener("pagehide", save);
    const tryRestore = () => {
      if (restored) return;
      let saved = null;
      try {
        saved = JSON.parse(sessionStorage.getItem(storageKey) || "null");
      } catch (error) {
        saved = null;
      }
      if (!saved || typeof saved.y !== "number" || saved.y < 120) return;
      if (content.innerText.trim().length < 80) return;
      restored = true;
      const y = saved.y;
      window.requestAnimationFrame(() => {
        window.scrollTo({ top: y, behavior: prefersReducedMotion() ? "auto" : "smooth" });
        showToast("Restored your place in this lesson", { tone: "info" });
      });
    };
    const mo = new MutationObserver(() => tryRestore());
    mo.observe(content, { childList: true, subtree: true, characterData: true });
    window.setTimeout(tryRestore, 400);
    window.setTimeout(tryRestore, 1200);
  };

  /** Number keys / letters select the focused quiz question; Enter checks answers. */
  const wireQuizKeyboard = () => {
    if (document.documentElement.dataset.pfQuizKeys === "1") return;
    document.documentElement.dataset.pfQuizKeys = "1";
    const hintHost = () => {
      const actions = document.getElementById("quiz-actions");
      if (!actions || actions.querySelector(".quiz-key-hint")) return;
      const hint = document.createElement("p");
      hint.className = "quiz-key-hint note";
      hint.innerHTML =
        'Tip: press <kbd>1</kbd>–<kbd>4</kbd> or <kbd>A</kbd>–<kbd>D</kbd> to answer · <kbd>Enter</kbd> to check · <kbd>?</kbd> for more shortcuts.';
      actions.prepend(hint);
      enhancePressFeedback();
    };
    hintHost();
    const moRoot = document.getElementById("quiz-container") || document.body;
    const mo = new MutationObserver(hintHost);
    mo.observe(moRoot, { childList: true, subtree: true });

    document.addEventListener("keydown", (event) => {
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      const questions = Array.from(document.querySelectorAll(".quiz-question"));
      if (!questions.length) return;

      if (event.key === "Enter") {
        const check = document.getElementById("check-answers");
        if (!check || check.disabled || check.hidden) return;
        event.preventDefault();
        check.click();
        return;
      }

      let index = -1;
      if (/^[1-9]$/.test(event.key)) index = Number(event.key) - 1;
      else if (/^[a-dA-D]$/.test(event.key)) index = event.key.toUpperCase().charCodeAt(0) - 65;
      if (index < 0) return;

      const active =
        questions.find((q) => q.contains(document.activeElement)) ||
        questions.find((q) => {
          const checked = q.querySelector("input[type='radio']:checked");
          return !checked;
        }) ||
        questions[0];
      const options = Array.from(active.querySelectorAll(".quiz-option input[type='radio']"));
      if (!options[index]) return;
      event.preventDefault();
      options[index].checked = true;
      options[index].dispatchEvent(new Event("change", { bubbles: true }));
      options[index].focus({ preventScroll: true });
      active.classList.add("is-keyed");
      window.setTimeout(() => active.classList.remove("is-keyed"), 420);
      const rect = active.getBoundingClientRect();
      const pad = 96;
      if (rect.top < pad || rect.bottom > window.innerHeight - 24) {
        active.scrollIntoView({
          block: "center",
          behavior: prefersReducedMotion() ? "auto" : "smooth",
        });
      }
    });
  };

  /** Compact progress rail above module lists on course hub pages. */
  const mountCourseHubRail = () => {
    const lists = Array.from(document.querySelectorAll(".module-list"));
    if (!lists.length) return;
    lists.forEach((list) => {
      if (list.previousElementSibling?.classList?.contains("course-hub-rail")) return;
      const items = Array.from(list.querySelectorAll(".module-list__item"));
      if (!items.length) return;
      const done = items.filter((li) => li.classList.contains("is-done")).length;
      const total = items.length;
      const next = items.find((li) => li.classList.contains("is-next"));
      const nextLesson =
        next?.querySelector(".module-list__action--lesson")?.getAttribute("href") || "";
      const nextTitle =
        next?.querySelector(".module-list__title")?.textContent?.trim() || "next module";
      const rail = document.createElement("div");
      rail.className = "course-hub-rail";
      rail.setAttribute("role", "status");
      const pct = total ? Math.round((done / total) * 100) : 0;
      const remaining = Math.max(total - done, 0);
      const etaMins = remaining * 12;
      const etaLabel =
        remaining === 0
          ? ""
          : etaMins < 60
            ? `About ${etaMins} min left`
            : etaMins % 60 === 0
              ? `About ${etaMins / 60} hr left`
              : `About ${Math.floor(etaMins / 60)} hr ${etaMins % 60} min left`;
      rail.innerHTML = `
        <div class="course-hub-rail__copy">
          <strong>${done} of ${total} modules</strong>
          <span>${
            remaining === 0
              ? "Course complete — nice work."
              : remaining === 1
                ? "1 module left."
                : `${remaining} modules left.`
          }${etaLabel ? ` · ${etaLabel}` : ""}</span>
        </div>
        <div class="course-hub-rail__meter" aria-hidden="true"><span style="width:${pct}%"></span></div>
        ${
          remaining === 0
            ? `<a class="btn btn-primary course-hub-rail__cta" href="certificate.html">Claim certificate</a>`
            : nextLesson
              ? `<a class="btn btn-secondary course-hub-rail__cta" href="${escapeHtml(nextLesson)}">Continue · ${escapeHtml(nextTitle)}</a>`
              : ""
        }`;
      list.parentElement?.insertBefore(rail, list);
    });
  };

  /** Refresh hub rails after module completion state syncs. */
  const refreshCourseHubRails = () => {
    document.querySelectorAll(".course-hub-rail").forEach((el) => el.remove());
    mountCourseHubRail();
  };

  /** Sitewide learning momentum chip (home + start-here). */
  const mountLearningMomentum = () => {
    const host =
      document.getElementById("pf-momentum-host") ||
      document.getElementById("path-viz-home") ||
      document.querySelector(".page-home #pf-resume-host");
    if (!host || document.getElementById("pf-momentum")) return;
    const completions = getCompletions();
    const quizzes = getQuizCompletions();
    const quizPass = Object.values(quizzes || {}).filter((q) => q && q.passed).length;
    const lessonCount = Array.isArray(completions) ? completions.length : 0;
    if (lessonCount === 0 && quizPass === 0) return;

    const chip = document.createElement("div");
    chip.id = "pf-momentum";
    chip.className = "learning-momentum";
    chip.setAttribute("role", "status");
    const bits = [];
    if (lessonCount) bits.push(`${lessonCount} lesson${lessonCount === 1 ? "" : "s"} done`);
    if (quizPass) bits.push(`${quizPass} quiz${quizPass === 1 ? "" : "zes"} passed`);
    const streak = getStudyStreak();
    if (streak >= 2) bits.push(`${streak}-day streak`);
    else if (streak === 1) bits.push("studied today");
    const last = getLastLesson();
    const when = last?.ts ? formatRelativeTime(last.ts) : "";
    chip.innerHTML = `
      <span class="learning-momentum__pulse" aria-hidden="true"></span>
      <div class="learning-momentum__copy">
        <strong>Your momentum</strong>
        <span>${escapeHtml(bits.join(" · "))}${when ? ` · last active ${escapeHtml(when)}` : ""}</span>
      </div>`;
    if (host.id === "pf-resume-host") {
      host.insertAdjacentElement("afterend", chip);
    } else if (host.id === "path-viz-home") {
      host.insertAdjacentElement("beforebegin", chip);
    } else {
      host.appendChild(chip);
    }
  };

  /** Celebrate mark-complete with a brief button flourish. */
  const wireCompletionCelebrate = () => {
    const btn = document.getElementById("mark-complete");
    if (!btn || btn.dataset.pfCelebrate === "1") return;
    btn.dataset.pfCelebrate = "1";
    btn.addEventListener("click", () => {
      window.requestAnimationFrame(() => {
        const pressed = /complete|done|✓/i.test(btn.textContent || "") || btn.getAttribute("aria-pressed") === "true";
        btn.classList.remove("is-celebrating");
        void btn.offsetWidth;
        if (pressed || btn.classList.contains("is-complete")) {
          btn.classList.add("is-celebrating");
          window.setTimeout(() => btn.classList.remove("is-celebrating"), 900);
        }
      });
    });
  };

  /** Press “n” to open the current Up next module lesson. */
  const wireNextModuleHotkey = () => {
    if (document.documentElement.dataset.pfNextKey === "1") return;
    document.documentElement.dataset.pfNextKey = "1";
    document.addEventListener("keydown", (event) => {
      if (event.key !== "n" && event.key !== "N") return;
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      const next =
        document.querySelector(".module-list__item.is-next .module-list__action--lesson") ||
        document.querySelector(".course-hub-rail__cta");
      if (!next?.href) return;
      event.preventDefault();
      window.location.href = next.href;
    });
  };

  /** j/k moves focus through module list items; Enter opens the lesson. */
  const wireModuleListKeys = () => {
    if (document.documentElement.dataset.pfModuleKeys === "1") return;
    if (!document.querySelector(".module-list__item")) return;
    document.documentElement.dataset.pfModuleKeys = "1";
    let index = -1;
    const items = () => Array.from(document.querySelectorAll(".module-list__item:not([hidden])"));
    const paint = (list, idx) => {
      list.forEach((el, i) => el.classList.toggle("is-kbd-focus", i === idx));
      const active = list[idx];
      if (active) {
        active.scrollIntoView({ block: "nearest", behavior: prefersReducedMotion() ? "auto" : "smooth" });
      }
    };
    document.addEventListener("keydown", (event) => {
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      const list = items();
      if (!list.length) return;
      const key = event.key;
      if (key === "j" || key === "J" || key === "k" || key === "K") {
        event.preventDefault();
        if (index < 0) {
          const nextIdx = list.findIndex((el) => el.classList.contains("is-next"));
          index = nextIdx >= 0 ? nextIdx : 0;
        } else if (key === "j" || key === "J") {
          index = Math.min(list.length - 1, index + 1);
        } else {
          index = Math.max(0, index - 1);
        }
        paint(list, index);
        return;
      }
      if (key === "Enter" && index >= 0) {
        const lesson = list[index]?.querySelector(".module-list__action--lesson");
        if (!lesson?.href) return;
        // Avoid stealing Enter from quiz check when both exist on page.
        if (document.getElementById("check-answers") && document.activeElement?.closest?.(".quiz-question")) {
          return;
        }
        event.preventDefault();
        window.location.href = lesson.href;
      }
    });
  };

  /** Soft pulse on playground output after Run. */
  const wirePlaygroundFeel = () => {
    const runBtn = document.getElementById("playground-run");
    const output = document.getElementById("playground-output");
    if (!runBtn || !output || runBtn.dataset.pfFeel === "1") return;
    runBtn.dataset.pfFeel = "1";
    runBtn.addEventListener("click", () => {
      output.classList.remove("is-fresh");
      void output.offsetWidth;
      output.classList.add("is-fresh");
      window.setTimeout(() => output.classList.remove("is-fresh"), 700);
    });
  };

  /** Celebrate when the learning path viz reaches full completion (once per session). */
  const wirePathCompleteCelebrate = () => {
    const viz = document.getElementById("path-viz-home");
    if (!viz || viz.dataset.pfPathCelebrate === "1") return;
    viz.dataset.pfPathCelebrate = "1";
    const check = () => {
      const nodes = Array.from(viz.querySelectorAll(".path-node"));
      if (nodes.length < 4) return;
      const allDone = nodes.every((n) => n.classList.contains("is-complete"));
      if (!allDone) return;
      try {
        if (sessionStorage.getItem("pf-path-celebrated") === "1") return;
        sessionStorage.setItem("pf-path-celebrated", "1");
      } catch {
        /* private mode */
      }
      viz.classList.add("is-path-complete");
      showToast("Learning path complete — brilliant work.", { tone: "success" });
    };
    check();
    const mo = new MutationObserver(check);
    mo.observe(viz, { attributes: true, subtree: true, attributeFilter: ["class"] });
    window.setTimeout(check, 250);
  };

  /** Soft page-ready class for first-paint entrance (respects reduced motion via CSS). */
  const markPageReady = () => {
    document.documentElement.classList.add("pf-ready");
  };

  /** Quiz answered-progress strip (dots + count) above the question list. */
  const mountQuizProgressStrip = () => {
    const container = document.getElementById("quiz-container");
    if (!container) return;
    const sync = () => {
      const questions = Array.from(container.querySelectorAll(".quiz-question"));
      if (!questions.length) {
        document.getElementById("pf-quiz-progress")?.remove();
        return;
      }
      let strip = document.getElementById("pf-quiz-progress");
      if (!strip) {
        strip = document.createElement("div");
        strip.id = "pf-quiz-progress";
        strip.className = "quiz-progress-strip";
        strip.setAttribute("role", "status");
        strip.setAttribute("aria-live", "polite");
        const actions = document.getElementById("quiz-actions");
        if (actions) actions.insertAdjacentElement("beforebegin", strip);
        else container.insertAdjacentElement("beforebegin", strip);
      }
      const answered = questions.filter((q) => q.querySelector("input[type='radio']:checked")).length;
      const total = questions.length;
      const dots = questions
        .map((q, i) => {
          const done = Boolean(q.querySelector("input[type='radio']:checked"));
          return `<button type="button" class="quiz-progress-strip__dot${done ? " is-answered" : ""}" data-q="${i}" aria-label="Question ${i + 1}${done ? ", answered" : ""}"></button>`;
        })
        .join("");
      strip.innerHTML = `
        <div class="quiz-progress-strip__copy">
          <strong>${answered} of ${total} answered</strong>
          <span>${answered === total ? "Ready to check" : "Pick an answer for each question"}</span>
        </div>
        <div class="quiz-progress-strip__dots" aria-hidden="true">${dots}</div>`;
      strip.querySelectorAll("[data-q]").forEach((btn) => {
        btn.addEventListener("click", () => {
          const idx = Number(btn.getAttribute("data-q"));
          const target = questions[idx];
          if (!target) return;
          target.scrollIntoView({ block: "center", behavior: prefersReducedMotion() ? "auto" : "smooth" });
          const first = target.querySelector("input[type='radio']");
          first?.focus({ preventScroll: true });
        });
      });
    };
    sync();
    if (container.dataset.pfQuizStrip === "1") return;
    container.dataset.pfQuizStrip = "1";
    container.addEventListener("change", sync);
    const mo = new MutationObserver(sync);
    mo.observe(container, { childList: true, subtree: true });
  };

  /** Chord navigation: press g, then h/c/s/a/t/e/r within ~1s. */
  const wireGoChords = () => {
    if (document.documentElement.dataset.pfGoChords === "1") return;
    document.documentElement.dataset.pfGoChords = "1";
    let armed = false;
    let timer = null;
    const routes = {
      h: "index.html",
      c: "courses.html",
      s: "start-here.html",
      a: "account.html",
      t: "tutorials.html",
      e: "help.html",
    };
    const resumeHref = () => {
      const last = getLastLesson();
      const lastQuiz = getLastQuiz();
      const lessonTs = Number(last?.ts) || 0;
      const quizTs = Number(lastQuiz?.ts) || 0;
      if (lastQuiz?.quiz && quizTs >= lessonTs) {
        return `quiz-viewer.html?quiz=${encodeURIComponent(lastQuiz.quiz)}`;
      }
      if (last?.path) {
        return `course-viewer.html?path=${encodeURIComponent(last.path)}`;
      }
      if (lastQuiz?.quiz) {
        return `quiz-viewer.html?quiz=${encodeURIComponent(lastQuiz.quiz)}`;
      }
      return "courses.html";
    };
    const disarm = () => {
      armed = false;
      if (timer) {
        clearTimeout(timer);
        timer = null;
      }
      document.documentElement.classList.remove("pf-go-armed");
    };
    document.addEventListener("keydown", (event) => {
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (isTypingTarget(event.target)) return;
      const key = event.key.toLowerCase();
      if (!armed) {
        if (key !== "g") return;
        event.preventDefault();
        armed = true;
        document.documentElement.classList.add("pf-go-armed");
        timer = window.setTimeout(disarm, 1100);
        return;
      }
      if (event.key === "Escape") {
        event.preventDefault();
        disarm();
        return;
      }
      if (key === "r") {
        disarm();
        event.preventDefault();
        window.location.href = resumeHref();
        return;
      }
      if (key === "g") {
        disarm();
        event.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: prefersReducedMotion() ? "auto" : "smooth",
        });
        const topBtn = document.getElementById("pf-back-top");
        if (topBtn) {
          topBtn.classList.add("is-hotkey");
          window.setTimeout(() => topBtn.classList.remove("is-hotkey"), 700);
        }
        return;
      }
      const href = routes[key];
      disarm();
      if (!href) return;
      event.preventDefault();
      window.location.href = href;
    });
  };

  /** Quiet offline banner; brief toast when connectivity returns. */
  const mountConnectivityBanner = () => {
    if (document.documentElement.dataset.pfConnectivity === "1") return;
    document.documentElement.dataset.pfConnectivity = "1";
    let wasOffline = !navigator.onLine;
    const sync = () => {
      let el = document.getElementById("pf-connectivity");
      if (!navigator.onLine) {
        if (!el) {
          el = document.createElement("div");
          el.id = "pf-connectivity";
          el.className = "connectivity-banner";
          el.setAttribute("role", "status");
          el.textContent =
            "You're offline — progress stays on this device until you're back online.";
          document.body.appendChild(el);
        }
        requestAnimationFrame(() => el.classList.add("is-visible"));
        wasOffline = true;
        return;
      }
      if (el) el.classList.remove("is-visible");
      if (wasOffline) {
        wasOffline = false;
        showToast("Back online", { tone: "success" });
      }
    };
    sync();
    window.addEventListener("offline", sync);
    window.addEventListener("online", sync);
  };

  /** Gentle once-per-session nudge after a long idle stretch on a lesson. */
  const wireLessonIdlePresence = () => {
    if (!document.getElementById("lesson-content")) return;
    if (document.documentElement.dataset.pfIdlePresence === "1") return;
    document.documentElement.dataset.pfIdlePresence = "1";
    const IDLE_MS = 15 * 60 * 1000;
    let timer = null;
    let nudged = false;
    const arm = () => {
      if (nudged) return;
      if (timer) window.clearTimeout(timer);
      timer = window.setTimeout(() => {
        if (nudged) return;
        try {
          if (sessionStorage.getItem("pf-idle-nudged") === "1") return;
          sessionStorage.setItem("pf-idle-nudged", "1");
        } catch (error) {
          /* private mode */
        }
        nudged = true;
        showToast("Still here? Your place in this lesson is saved.", { tone: "info" });
      }, IDLE_MS);
    };
    ["pointerdown", "keydown", "scroll", "touchstart"].forEach((evt) => {
      window.addEventListener(evt, arm, { passive: true });
    });
    arm();
  };

  /** Soft same-page anchor scrolling for in-page links. */
  const wireInPageAnchors = () => {
    if (document.documentElement.dataset.pfInPageAnchors === "1") return;
    document.documentElement.dataset.pfInPageAnchors = "1";
    document.addEventListener("click", (event) => {
      const link = event.target?.closest?.("a[href^='#']");
      if (!link) return;
      const href = link.getAttribute("href") || "";
      if (!href || href === "#") return;
      const id = decodeURIComponent(href.slice(1));
      const target = document.getElementById(id);
      if (!target) return;
      event.preventDefault();
      const reduce = prefersReducedMotion();
      target.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
      try {
        history.pushState(null, "", `#${id}`);
      } catch {
        location.hash = id;
      }
      target.classList.add("is-hash-target");
      window.setTimeout(() => target.classList.remove("is-hash-target"), 1600);
      if (typeof target.focus === "function") {
        const prevTab = target.getAttribute("tabindex");
        if (prevTab === null) target.setAttribute("tabindex", "-1");
        target.focus({ preventScroll: true });
        if (prevTab === null) {
          target.addEventListener(
            "blur",
            () => target.removeAttribute("tabindex"),
            { once: true }
          );
        }
      }
    });
  };

  /** Session study timer chip on lesson and quiz pages. */
  const mountStudySessionChip = () => {
    const onLesson = Boolean(document.getElementById("lesson-content"));
    const onQuiz = Boolean(document.getElementById("quiz-container"));
    if (!onLesson && !onQuiz) return;
    if (document.getElementById("pf-session-chip")) return;
    const started = Date.now();
    const chip = document.createElement("div");
    chip.id = "pf-session-chip";
    chip.className = "study-session-chip";
    chip.setAttribute("role", "status");
    chip.setAttribute("aria-live", "off");
    chip.hidden = true;
    document.body.appendChild(chip);
    const format = (ms) => {
      const mins = Math.floor(ms / 60000);
      if (mins < 1) return "Session · just started";
      if (mins === 1) return "Session · 1 min";
      if (mins < 60) return `Session · ${mins} min`;
      const hrs = Math.floor(mins / 60);
      const rem = mins % 60;
      return rem ? `Session · ${hrs}h ${rem}m` : `Session · ${hrs}h`;
    };
    const sync = () => {
      const elapsed = Date.now() - started;
      chip.textContent = format(elapsed);
      chip.hidden = elapsed < 45 * 1000;
    };
    sync();
    window.setInterval(sync, 15000);
  };

  /** Near the end of a lesson, gently nudge mark-complete when unfinished. */
  const mountLessonFinishNudge = () => {
    const btn = document.getElementById("mark-complete");
    const content = document.getElementById("lesson-content");
    if (!btn || !content) return;
    if (document.getElementById("pf-finish-nudge")) return;
    const nudge = document.createElement("p");
    nudge.id = "pf-finish-nudge";
    nudge.className = "lesson-finish-nudge note";
    nudge.hidden = true;
    nudge.innerHTML =
      'Nearly there — <button type="button" class="linkish" data-finish-nudge>mark this lesson complete</button> when you are ready.';
    btn.insertAdjacentElement("afterend", nudge);
    nudge.querySelector("[data-finish-nudge]")?.addEventListener("click", () => {
      btn.click();
    });
    const sync = () => {
      const bar = document.getElementById("pf-read-progress");
      const pct = Number(bar?.getAttribute("aria-valuenow") || 0);
      const done =
        btn.classList.contains("is-complete") ||
        /complete|done|✓/i.test(btn.textContent || "") ||
        btn.getAttribute("aria-pressed") === "true";
      const show = !done && pct >= 88;
      nudge.hidden = !show;
      nudge.classList.toggle("is-visible", show);
    };
    sync();
    window.addEventListener("scroll", sync, { passive: true });
    btn.addEventListener("click", () => window.setTimeout(sync, 80));
    const mo = new MutationObserver(sync);
    mo.observe(btn, { attributes: true, childList: true, characterData: true, subtree: true });
  };

  /** Brief “Saved” flash when progress is written from mark-complete. */
  const wireSavedFlash = () => {
    const btn = document.getElementById("mark-complete");
    if (!btn || btn.dataset.pfSavedFlash === "1") return;
    btn.dataset.pfSavedFlash = "1";
    btn.addEventListener("click", () => {
      window.setTimeout(() => {
        const done =
          btn.classList.contains("is-complete") ||
          /complete|done|✓/i.test(btn.textContent || "") ||
          btn.getAttribute("aria-pressed") === "true";
        if (!done) return;
        let flash = document.getElementById("pf-saved-flash");
        if (!flash) {
          flash = document.createElement("div");
          flash.id = "pf-saved-flash";
          flash.className = "saved-flash";
          flash.setAttribute("aria-hidden", "true");
          flash.textContent = "Saved";
          document.body.appendChild(flash);
        }
        flash.classList.remove("is-visible");
        void flash.offsetWidth;
        flash.classList.add("is-visible");
        window.setTimeout(() => flash.classList.remove("is-visible"), 1400);
      }, 60);
    });
  };

  /** Soft selected state on course matcher buttons. */
  const wireMatcherFeel = () => {
    const root = document.getElementById("matcher-widget");
    if (!root || root.dataset.pfFeel === "1") return;
    root.dataset.pfFeel = "1";
    root.querySelectorAll(".matcher-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        root.querySelectorAll(".matcher-btn").forEach((b) => b.classList.remove("is-selected"));
        btn.classList.add("is-selected");
        const result = document.getElementById("matcher-result");
        if (result) {
          result.classList.remove("is-revealed");
          void result.offsetWidth;
          result.classList.add("is-revealed");
        }
      });
    });
  };

  /** Soft press feedback on primary interactive controls. */
  const enhancePressFeedback = () => {
    document.querySelectorAll(".btn, .chip-btn, .matcher-btn, .quiz-option").forEach((el) => {
      if (el.dataset.pfPress === "1") return;
      el.dataset.pfPress = "1";
      el.classList.add("has-press");
    });
  };

  /** Sort course tiles by progress (in-progress first, then % complete). */
  const wireCourseProgressSort = () => {
    const host = document.getElementById("course-sort-host");
    if (!host || host.dataset.pfWired) return;
    host.dataset.pfWired = "1";
    const grids = Array.from(document.querySelectorAll("main .section.grid")).filter((grid) =>
      grid.querySelector(".course-tile")
    );
    if (!grids.length) return;
    const originals = new Map();
    grids.forEach((grid) => {
      originals.set(grid, Array.from(grid.children));
    });
    host.innerHTML = `
      <div class="course-sort" role="group" aria-label="Sort courses">
        <span class="course-sort__label">Sort</span>
        <button type="button" class="chip-btn is-active" data-sort="default">Default</button>
        <button type="button" class="chip-btn" data-sort="progress">In progress first</button>
      </div>`;
    const apply = (mode) => {
      host.querySelectorAll("[data-sort]").forEach((btn) => {
        btn.classList.toggle("is-active", btn.getAttribute("data-sort") === mode);
      });
      grids.forEach((grid) => {
        const base = originals.get(grid) || Array.from(grid.children);
        const tiles = base.filter((el) => el.classList?.contains("course-tile"));
        const other = base.filter((el) => !el.classList?.contains("course-tile"));
        if (mode === "default") {
          base.forEach((el) => grid.appendChild(el));
          return;
        }
        const ranked = tiles.slice().sort((a, b) => {
          const aDone = Number(a.dataset.pfProgressDone || 0);
          const bDone = Number(b.dataset.pfProgressDone || 0);
          const aTotal = Number(a.dataset.pfProgressTotal || 0);
          const bTotal = Number(b.dataset.pfProgressTotal || 0);
          const aPct = Number(a.dataset.pfProgressPct || 0);
          const bPct = Number(b.dataset.pfProgressPct || 0);
          const aActive = aDone > 0 && aDone < aTotal ? 1 : 0;
          const bActive = bDone > 0 && bDone < bTotal ? 1 : 0;
          if (aActive !== bActive) return bActive - aActive;
          if (aPct !== bPct) return bPct - aPct;
          return 0;
        });
        ranked.forEach((el) => grid.appendChild(el));
        other.forEach((el) => grid.appendChild(el));
      });
    };
    host.querySelectorAll("[data-sort]").forEach((btn) => {
      btn.addEventListener("click", () => apply(btn.getAttribute("data-sort") || "default"));
    });
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
    const run = (label, fn) => {
      try {
        fn();
      } catch (error) {
        console.warn(`[PF] ${label} failed`, error);
      }
    };
    run("atmosphere", mountAtmosphere);
    run("header", mountHeader);
    run("headerScroll", wireHeaderScroll);
    run("donate", mountDonateSlots);
    run("brand", mountBrandCredit);
    run("footers", enhanceFooters);
    run("deviceProgress", mountDeviceProgressNotice);
    run("resume", mountResumeBanner);
    run("stickyResume", mountStickyResume);
    run("persona", mountPersonaPicker);
    run("personaCopy", applyPersonaCopy);
    run("playground", enhancePlaygroundChallenges);
    run("modules", enhanceModuleLists);
    run("nextModules", highlightNextModules);
    run("hubRail", mountCourseHubRail);
    run("momentum", mountLearningMomentum);
    run("courseTiles", enhanceCourseTiles);
    run("reveal", enhanceScrollReveal);
    run("surfaces", enhanceInteractiveSurfaces);
    run("press", enhancePressFeedback);
    run("hash", enhanceHashTargets);
    run("pathNodes", enhancePathNodes);
    run("externalLinks", enhanceExternalLinks);
    run("readingMeta", enhanceLessonReadingMeta);
    run("lessonOutline", mountLessonOutline);
    run("outlineKey", wireOutlineHotkey);
    run("prefetch", enhanceInternalPrefetch);
    run("copyLink", mountCopyLinkButton);
    run("focusMode", mountLessonFocusMode);
    run("scrollMemory", mountLessonScrollMemory);
    run("lessonNavKeys", wireLessonNavKeys);
    run("nextModuleKey", wireNextModuleHotkey);
    run("moduleKeys", wireModuleListKeys);
    run("quizKeys", wireQuizKeyboard);
    run("celebrate", wireCompletionCelebrate);
    run("pathCelebrate", wirePathCompleteCelebrate);
    run("playgroundFeel", wirePlaygroundFeel);
    run("matcherFeel", wireMatcherFeel);
    run("quizStrip", mountQuizProgressStrip);
    run("goChords", wireGoChords);
    run("connectivity", mountConnectivityBanner);
    run("idlePresence", wireLessonIdlePresence);
    run("inPageAnchors", wireInPageAnchors);
    run("sessionChip", mountStudySessionChip);
    run("finishNudge", mountLessonFinishNudge);
    run("savedFlash", wireSavedFlash);
    run("shortcuts", mountKeyboardShortcuts);
    run("courseFilter", wireCourseTileFilter);
    run("courseSort", wireCourseProgressSort);
    run("tutorialFilter", wireTutorialFilter);
    run("quickFind", wireQuickFindShortcut);
    run("backTop", mountBackToTop);
    run("backTopKey", wireBackToTopHotkey);
    run("readProgress", mountReadingProgress);
    // Lesson/module UIs often hydrate after boot.
    window.setTimeout(() => {
      run("nextModules:deferred", highlightNextModules);
      run("hubRail:deferred", refreshCourseHubRails);
      run("externalLinks:deferred", enhanceExternalLinks);
      run("copyLink:deferred", mountCopyLinkButton);
      run("focusMode:deferred", mountLessonFocusMode);
      run("courseSort:deferred", wireCourseProgressSort);
      run("celebrate:deferred", wireCompletionCelebrate);
      run("press:deferred", enhancePressFeedback);
      run("quizKeys:deferred", wireQuizKeyboard);
      run("moduleKeys:deferred", wireModuleListKeys);
      run("pathCelebrate:deferred", wirePathCompleteCelebrate);
      run("quizStrip:deferred", mountQuizProgressStrip);
      run("finishNudge:deferred", mountLessonFinishNudge);
      run("savedFlash:deferred", wireSavedFlash);
      run("lessonOutline:deferred", mountLessonOutline);
      run("readingMeta:deferred", enhanceLessonReadingMeta);
    }, 200);
    window.setTimeout(() => {
      run("nextModules:late", highlightNextModules);
      run("hubRail:late", refreshCourseHubRails);
    }, 800);
    run("pageReady", markPageReady);
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
    SITE_YEAR,
    SITE_MAINTAINED_LABEL,
    COURSE_MODULE_MAP,
    ADVANCED_COURSES,
    PREMIUM_COURSES,
    PREMIUM_PATH_PREFIXES,
    isPremiumPath,
    isPremiumCourseName,
    canAccessPremium,
    ensurePremiumAccess,
    refreshPremiumEntitlements,
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
    highlightNextModules,
    enhanceCourseTiles,
    mountCourseHubRail,
    refreshCourseHubRails,
    mountLearningMomentum,
    wireQuizKeyboard,
    wireNextModuleHotkey,
    wireModuleListKeys,
    mountQuizProgressStrip,
    wireGoChords,
    mountConnectivityBanner,
    wireLessonIdlePresence,
    wireInPageAnchors,
    mountStudySessionChip,
    mountLessonFinishNudge,
    wireSavedFlash,
    mountLessonOutline,
    wireOutlineHotkey,
    enhanceInternalPrefetch,
    wireBackToTopHotkey,
    getStudyStreak,
    recordActivityDay,
    celebrateStreakMilestones,
    formatRelativeTime,
    showToast,
    mountKeyboardShortcuts,
    mountStickyResume,
    mountCopyLinkButton,
    mountLessonFocusMode,
    mountLessonScrollMemory,
    wireLessonNavKeys,
    wireCourseProgressSort,
    resetAllProgress,
    getDeviceProgressConsent,
    setDeviceProgressConsent,
    hasChosenDeviceProgressConsent,
    canPersistGuestProgress,
    exportGuestProgress,
    downloadGuestProgress,
    importGuestProgress,
    mountDeviceProgressNotice,
    dismissDeviceProgressNotice,
    mountDeviceProgressAftermath,
    dismissDeviceProgressAftermath,
    markNavCurrent,
    mountHeader,
    mountDonateSlots,
    mountBrandCredit,
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
