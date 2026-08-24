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
  const SITE_MAINTAINED_LABEL = "24 August 2026";

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

  const getCompletions = () =>
    safeParse(localStorage.getItem(KEYS.completions), []);

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

    if (showQuiz) {
      const when = formatRelativeTime(lastQuiz.ts);
      host.hidden = false;
      host.innerHTML = `
      <div class="resume-banner" role="region" aria-label="Resume learning">
        <div class="resume-banner-copy">
          <strong>Continue your last quiz</strong>
          <span>${escapeHtml(lastQuiz.title || "Quiz")}${
            when ? ` <em class="resume-when">· ${escapeHtml(when)}</em>` : ""
          }</span>
        </div>
        <div class="resume-banner-actions">
          <a class="btn btn-primary" href="quiz-viewer.html?quiz=${encodeURIComponent(lastQuiz.quiz)}">Open quiz</a>
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
    const label = done ? "Review last lesson" : "Continue where you left off";
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
          <a class="btn btn-primary" href="course-viewer.html?path=${encodeURIComponent(last.path)}">Open lesson</a>
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

  /** Thin reading progress bar under the sticky header. */
  const mountReadingProgress = () => {
    if (document.getElementById("pf-read-progress")) return;
    const bar = document.createElement("div");
    bar.id = "pf-read-progress";
    bar.className = "read-progress";
    bar.setAttribute("aria-hidden", "true");
    bar.innerHTML = '<div class="read-progress__fill"></div>';
    document.body.appendChild(bar);
    const fill = bar.querySelector(".read-progress__fill");
    const update = () => {
      const doc = document.documentElement;
      const max = Math.max(doc.scrollHeight - window.innerHeight, 1);
      const pct = Math.min(100, Math.max(0, (window.scrollY / max) * 100));
      if (fill) fill.style.width = `${pct}%`;
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
    document.querySelectorAll(".course-tile").forEach((tile) => {
      if (tile.querySelector(".course-tile-progress")) return;
      const heading = tile.querySelector("h3, h4");
      const name = (heading?.textContent || "").trim();
      const mapKey = resolveCourseMapKey(name);
      if (!mapKey || !COURSE_MODULE_MAP[mapKey]) return;
      const progress = courseProgress(mapKey);
      if (!progress.total) return;
      const chip = document.createElement("p");
      chip.className = "course-tile-progress";
      chip.setAttribute("aria-label", `${name} progress`);
      if (progress.done === 0) {
        chip.textContent = `${progress.total} modules · not started`;
      } else if (progress.done >= progress.total) {
        chip.innerHTML = `<strong>Complete</strong> · ${progress.total} modules`;
        tile.classList.add("is-complete");
      } else {
        chip.innerHTML = `<strong>${progress.percent}%</strong> · ${progress.done} of ${progress.total} modules`;
        tile.classList.add("is-in-progress");
      }
      const body = tile.querySelector(".course-tile-body") || tile;
      const buttons = body.querySelector(".button-row");
      if (buttons) body.insertBefore(chip, buttons);
      else body.appendChild(chip);
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
          <li><kbd>Ctrl</kbd> + <kbd>Enter</kbd> <span>Run playground (home)</span></li>
          <li><kbd>Esc</kbd> <span>Close dialogs and this sheet</span></li>
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
      meta.hidden = false;
      meta.textContent = `About ${minutes} min read · ${words.toLocaleString()} words`;
    };
    update();
    const mo = new MutationObserver(update);
    mo.observe(content, { childList: true, subtree: true, characterData: true });
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
    wireHeaderScroll();
    mountDonateSlots();
    mountBrandCredit();
    enhanceFooters();
    mountDeviceProgressNotice();
    mountResumeBanner();
    mountStickyResume();
    mountPersonaPicker();
    applyPersonaCopy();
    enhancePlaygroundChallenges();
    enhanceModuleLists();
    highlightNextModules();
    enhanceCourseTiles();
    enhanceScrollReveal();
    enhanceInteractiveSurfaces();
    enhanceHashTargets();
    enhancePathNodes();
    enhanceExternalLinks();
    enhanceLessonReadingMeta();
    mountCopyLinkButton();
    mountKeyboardShortcuts();
    wireCourseTileFilter();
    wireTutorialFilter();
    wireQuickFindShortcut();
    mountBackToTop();
    mountReadingProgress();
    // Lesson/module UIs often hydrate after boot.
    window.setTimeout(() => {
      highlightNextModules();
      enhanceExternalLinks();
      mountCopyLinkButton();
    }, 200);
    window.setTimeout(highlightNextModules, 800);
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
    formatRelativeTime,
    showToast,
    mountKeyboardShortcuts,
    mountStickyResume,
    mountCopyLinkButton,
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
