#!/usr/bin/env python3
"""Generate donor-gated DevOps & cloud course markdown, quizzes, and hub HTML."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LANG = ROOT / "languages"
sys.path.insert(0, str(ROOT / "scripts"))
from premium_module_content import MODULES  # noqa: E402

COURSES = [
    {
        "id": "devops",
        "name": "DevOps Foundations Course",
        "page": "devops-course.html",
        "hub_title": "DevOps Foundations",
        "blurb": "CI/CD, containers, observability, and delivery habits used in real teams.",
        "best_for": "Developers and career changers moving into platform / DevOps roles.",
        "build": "A sample delivery pipeline, containerised app, and ops checklist.",
        "modules": [
            ("01-devops-mindset", "DevOps mindset & value stream"),
            ("02-git-branching-for-teams", "Git branching for teams"),
            ("03-ci-pipelines", "Continuous integration pipelines"),
            ("04-cd-and-releases", "Continuous delivery & releases"),
            ("05-containers-basics", "Containers basics"),
            ("06-compose-and-local-envs", "Compose & local environments"),
            ("07-observability-basics", "Observability basics"),
            ("08-incident-response", "Incident response habits"),
            ("09-security-in-the-pipeline", "Security in the pipeline"),
            ("10-capstone-delivery", "Capstone: ship a small service"),
        ],
    },
    {
        "id": "aws",
        "name": "AWS Cloud Course",
        "page": "aws-course.html",
        "hub_title": "AWS Cloud",
        "blurb": "Practical AWS building blocks: IAM, VPC, compute, storage, and serverless.",
        "best_for": "Learners preparing for cloud roles or shipping on Amazon Web Services.",
        "build": "A secure VPC sketch, EC2/S3 lab notes, and a serverless starter.",
        "modules": [
            ("01-aws-foundations", "AWS foundations & accounts"),
            ("02-iam-and-security", "IAM & security basics"),
            ("03-vpc-networking", "VPC & networking"),
            ("04-ec2-and-compute", "EC2 & compute choices"),
            ("05-s3-and-storage", "S3 & storage"),
            ("06-rds-and-data", "RDS & managed data"),
            ("07-lambda-serverless", "Lambda & serverless"),
            ("08-monitoring-cloudwatch", "Monitoring with CloudWatch"),
            ("09-cost-and-well-architected", "Cost & Well-Architected"),
            ("10-capstone-aws-app", "Capstone: deploy a small AWS app"),
        ],
    },
    {
        "id": "azure",
        "name": "Azure Cloud Course",
        "page": "azure-course.html",
        "hub_title": "Azure Cloud",
        "blurb": "Microsoft Azure fundamentals: identity, networking, compute, and App Service.",
        "best_for": "Teams already on Microsoft 365 / .NET, or aiming at Azure roles.",
        "build": "Resource group design, App Service notes, and an Azure Monitor checklist.",
        "modules": [
            ("01-azure-foundations", "Azure foundations & subscriptions"),
            ("02-entra-id-and-rbac", "Entra ID & RBAC"),
            ("03-vnet-networking", "VNet & networking"),
            ("04-compute-options", "Compute options"),
            ("05-storage-and-blobs", "Storage & blobs"),
            ("06-app-service", "App Service"),
            ("07-azure-sql-and-data", "Azure SQL & data"),
            ("08-monitor-and-insights", "Monitor & Application Insights"),
            ("09-governance-and-cost", "Governance & cost"),
            ("10-capstone-azure-app", "Capstone: host a small Azure app"),
        ],
    },
    {
        "id": "gcp",
        "name": "GCP Cloud Course",
        "page": "gcp-course.html",
        "hub_title": "Google Cloud (GCP)",
        "blurb": "GCP foundations: projects, IAM, VPC, Compute Engine, GKE intro, and Cloud Run.",
        "best_for": "Builders targeting Google Cloud or multi-cloud fluency.",
        "build": "Project/IAM map, Cloud Run service notes, and billing alerts checklist.",
        "modules": [
            ("01-gcp-foundations", "GCP foundations & projects"),
            ("02-iam-and-org-policy", "IAM & org policy"),
            ("03-vpc-networking", "VPC networking"),
            ("04-compute-engine", "Compute Engine"),
            ("05-gcs-and-data", "Cloud Storage & data"),
            ("06-cloud-run", "Cloud Run"),
            ("07-gke-intro", "GKE introduction"),
            ("08-ops-and-logging", "Ops & Cloud Logging"),
            ("09-billing-and-cost", "Billing & cost control"),
            ("10-capstone-gcp-service", "Capstone: ship on Cloud Run"),
        ],
    },
    {
        "id": "kubernetes",
        "name": "Kubernetes Course",
        "page": "kubernetes-course.html",
        "hub_title": "Kubernetes",
        "blurb": "Cluster mental model, workloads, services, config, and safe rollouts.",
        "best_for": "DevOps and backend engineers running containers in production.",
        "build": "A sample Deployment/Service manifest set and rollout checklist.",
        "modules": [
            ("01-k8s-mental-model", "Kubernetes mental model"),
            ("02-pods-and-workloads", "Pods & workloads"),
            ("03-services-and-ingress", "Services & Ingress"),
            ("04-configmaps-secrets", "ConfigMaps & Secrets"),
            ("05-storage-and-pv", "Storage & persistent volumes"),
            ("06-deployments-rollouts", "Deployments & rollouts"),
            ("07-autoscaling-basics", "Autoscaling basics"),
            ("08-observability-on-k8s", "Observability on Kubernetes"),
            ("09-security-basics", "Kubernetes security basics"),
            ("10-capstone-k8s-app", "Capstone: deploy an app to a cluster"),
        ],
    },
    {
        "id": "terraform",
        "name": "Terraform & IaC Course",
        "page": "terraform-course.html",
        "hub_title": "Terraform & Infrastructure as Code",
        "blurb": "Write, plan, and apply infrastructure safely with Terraform modules and state.",
        "best_for": "Cloud and DevOps learners who want repeatable infrastructure.",
        "build": "A starter module, remote state notes, and a plan/apply runbook.",
        "modules": [
            ("01-iac-why-terraform", "Why IaC & Terraform"),
            ("02-providers-and-resources", "Providers & resources"),
            ("03-state-and-backends", "State & backends"),
            ("04-variables-outputs", "Variables & outputs"),
            ("05-modules", "Modules"),
            ("06-workspaces-environments", "Workspaces & environments"),
            ("07-plan-apply-destroy", "Plan, apply, destroy"),
            ("08-testing-and-policy", "Testing & policy"),
            ("09-ci-for-terraform", "CI for Terraform"),
            ("10-capstone-module", "Capstone: ship a reusable module"),
        ],
    },
]


def content_for(course_id: str, slug: str) -> dict | None:
    return MODULES.get(f"{course_id}/{slug}") or MODULES.get(slug)


def lesson_md(course: dict, slug: str, title: str, index: int, total: int) -> str:
    spec = content_for(course["id"], slug)
    if not spec:
        raise KeyError(f"Missing premium content for {course['id']}/{slug}")

    goals = "\n".join(f"- {g}" for g in spec["goals"])
    ideas = "\n".join(f"{i}. {idea}" for i, idea in enumerate(spec["ideas"], start=1))
    practice = "\n".join(f"{i}. {p}" for i, p in enumerate(spec["practice"], start=1))
    mistakes = "\n".join(f"- {m}" for m in spec["mistakes"])

    return f"""# {title}

**Course:** {course['name']} (donor / allowlist access)  
**Module:** {index} of {total}

## Learning goals

By the end of this lesson you will be able to:

{goals}

## Why this matters

{spec['why']}

## Core ideas

{ideas}

## Worked example

{spec['example']}

## Practice

{practice}

## Common mistakes

{mistakes}

## Stretch goal

{spec['stretch']}

## Before you mark complete

- [ ] Learning goals feel true
- [ ] Practice notes saved (secrets redacted)
- [ ] Quiz attempted

## Next

Continue to the next module in order, or revisit the
[course hub]({course['page']}) for the full path.
"""


LETTERS = "ABCD"


def quiz_md(course_id: str, slug: str, title: str) -> str:
    spec = content_for(course_id, slug)
    if not spec:
        raise KeyError(f"Missing premium quiz for {course_id}/{slug}")
    blocks = [f"# Quiz — {title}", ""]
    for i, (question, choices, _correct) in enumerate(spec["quiz"], start=1):
        blocks.append(f"{i}. {question}")
        for letter, choice in zip(LETTERS, choices):
            blocks.append(f"   - {letter}. {choice}")
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def quiz_answers_md(course_id: str, slug: str, title: str) -> str:
    spec = content_for(course_id, slug)
    if not spec:
        raise KeyError(f"Missing premium answers for {course_id}/{slug}")
    lines = [f"# Answers — {title}", ""]
    for i, (_q, _choices, correct) in enumerate(spec["quiz"], start=1):
        lines.append(f"{i}. {LETTERS[correct]}")
    lines.append("")
    lines.append(
        "**Teaching note:** Prefer reasoning about outcomes, blast radius, and evidence over trivia."
    )
    lines.append("")
    return "\n".join(lines)


def hub_html(course: dict) -> str:
    modules = course["modules"]
    paths = [f"languages/{course['id']}/modules/{slug}.md" for slug, _ in modules]
    lis = "\n".join(
        f"""          <li>
            {title} —
            <a href="course-viewer.html?path=languages/{course['id']}/modules/{slug}.md">Lesson</a>
            ·
            <a href="quiz-viewer.html?quiz=languages/{course['id']}/modules/{slug}.quiz.md">Quiz</a>
            ·
            <a href="tutorials.html#premium-{course['id']}">Voiceover guide</a>
          </li>"""
        for slug, title in modules
    )
    first = paths[0]
    progress_id = f"{course['id']}-premium"
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{course['hub_title']} (Donor) - Programming Foundations</title>
    <link rel="stylesheet" href="styles.css?v=ux39" />
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to main content</a>
    <div data-pf-header></div>
    <script src="config.js"></script>
    <script src="site.js?v=ux39"></script>

    <main id="main" class="container">
      <div id="pf-resume-host" hidden></div>
      <section class="hero">
        <p class="pill">Donor / allowlist course</p>
        <h2>{course['hub_title']}</h2>
        <p>
          {course['blurb']} This path sits behind a free account that has donated, or an email
          allowlisted by the site owner. Free beginner courses stay open for everyone.
        </p>
        <div id="premium-gate" class="note" hidden></div>
        <div class="button-row" id="premium-actions">
          <a class="btn btn-primary" href="course-viewer.html?path={first}">Start Module 1</a>
          <a class="btn btn-secondary" href="tutorials.html#premium-{course['id']}">Voiceover guide</a>
          <a class="btn btn-secondary" href="support.html#donor-courses">Support / donate</a>
          <a class="btn btn-secondary" href="courses.html#donor-courses">All donor courses</a>
        </div>
        <p class="pill" id="{progress_id}-progress-text">Progress: 0 of {len(modules)} complete</p>
        <div class="progress-bar">
          <div class="progress-fill" id="{progress_id}-progress-fill"></div>
        </div>
      </section>

      <section class="section">
        <h3>Modules</h3>
        <p class="note">
          Work in order. Each lesson includes goals, practice, and a quiz. Media guides open from
          <a href="tutorials.html#premium-{course['id']}">Tutorials</a>.
        </p>
        <ol class="card">
{lis}
        </ol>
      </section>
    </main>

    <footer class="footer container">
      <a href="courses.html#donor-courses">Donor courses</a>
      ·
      <a href="support.html#donor-courses">How access works</a>
      ·
      <a href="account.html">Account</a>
      ·
      <a href="privacy.html">Privacy</a>
      ·
      <a href="help.html">Help</a>
    </footer>

    <script>
      const modules = {json.dumps(paths)};
      const gate = document.getElementById("premium-gate");
      const actions = document.getElementById("premium-actions");
      (async function () {{
        const ok = window.PF && (await window.PF.ensurePremiumAccess({{ soft: true }}));
        if (!ok) {{
          if (gate) {{
            gate.hidden = false;
            gate.innerHTML =
              'This course is for donor / allowlisted accounts. <a href="account.html">Sign in</a>, ' +
              '<a href="support.html#donor-courses">donate</a>, or ask the owner to allowlist your email.';
          }}
          if (actions) {{
            actions.querySelectorAll('a[href*="course-viewer"], a[href*="tutorials.html#premium"]').forEach((a) => {{
              a.classList.add("is-disabled");
              a.setAttribute("aria-disabled", "true");
              a.addEventListener("click", (event) => {{
                event.preventDefault();
              }});
            }});
          }}
          return;
        }}
        window.PF.bindProgressUI({{
          modules,
          textEl: "{progress_id}-progress-text",
          fillEl: "{progress_id}-progress-fill",
        }});
      }})();
    </script>
  </body>
</html>
"""


def main() -> None:
    index_courses = []
    for course in COURSES:
        mod_dir = LANG / course["id"] / "modules"
        mod_dir.mkdir(parents=True, exist_ok=True)
        total = len(course["modules"])
        index_modules = []
        for i, (slug, title) in enumerate(course["modules"], start=1):
            lesson = mod_dir / f"{slug}.md"
            quiz = mod_dir / f"{slug}.quiz.md"
            answers = mod_dir / f"{slug}.quiz-answers.md"
            lesson.write_text(lesson_md(course, slug, title, i, total), encoding="utf-8")
            quiz.write_text(quiz_md(course["id"], slug, title), encoding="utf-8")
            answers.write_text(quiz_answers_md(course["id"], slug, title), encoding="utf-8")
            index_modules.append(
                {
                    "title": title,
                    "path": f"languages/{course['id']}/modules/{slug}.md",
                    "quiz": f"languages/{course['id']}/modules/{slug}.quiz.md",
                    "tutorial": f"tutorials.html#premium-{course['id']}",
                    "tutorialId": f"premium-{course['id']}",
                }
            )
        (DOCS / course["page"]).write_text(hub_html(course), encoding="utf-8")
        index_courses.append(
            {
                "id": course["id"],
                "name": course["name"],
                "page": course["page"],
                "level": "Donor / cloud & DevOps",
                "premium": True,
                "modules": index_modules,
            }
        )
        print("wrote", course["id"], total, "modules + hub")

    # Merge into course-index.json
    index_path = DOCS / "course-index.json"
    data = json.loads(index_path.read_text(encoding="utf-8"))
    existing = {c["id"]: c for c in data.get("courses", [])}
    for course in index_courses:
        existing[course["id"]] = course
    # Keep stable-ish order: non-premium first, then premium
    free = [c for c in existing.values() if not c.get("premium")]
    premium = [c for c in existing.values() if c.get("premium")]
    data["courses"] = free + premium
    index_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print("updated course-index.json")


if __name__ == "__main__":
    main()
