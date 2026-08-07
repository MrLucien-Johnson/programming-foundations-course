# Learner tutorial videos

Two kinds of clips:
- **setup** — download/install/site orientation (kept short)
- **lesson** — teach module ideas with examples + practice prompts

Each clip includes: MP4, WebVTT captions, plain-text transcript, and audio.
Voice: en-US JennyNeural at -12%. Slides use the live parchment/gold brand.
Audio is volume-checked after mux so silent tracks cannot ship.
Policy: every shipped tutorial MP4 must be muxed with audible voiceover.
Rebuild with:

```bash
pip install edge-tts Pillow
python3 scripts/tutorials/generate_tutorials.py
# or a subset:
python3 scripts/tutorials/generate_tutorials.py 05-ai-foundations 06-python-basics
python3 scripts/assert_videos_muxed.py
```

| ID | Kind | Title | ~Length | Learning path |
|----|------|-------|---------|---------------|
| `01-get-started-download` | setup | Get started — browser & download | ~60s | start-here, help, courses |
| `02-python-setup` | setup | Python — download, install, first script | ~69s | python-course, module-01-setup |
| `03-csharp-setup` | setup | C# — install .NET and first project | ~63s | csharp-course, module-01-setup |
| `04-tips-tricks` | setup | Tips & tricks for this site | ~64s | help, start-here, account |
| `05-ai-foundations` | lesson | AI Module 1 — foundations lesson | ~112s | ai-course, 01-ai-foundations |
| `06-python-basics` | lesson | Python Module 2 — variables & input lesson | ~99s | python-course, module-02-basics |
| `07-csharp-basics` | lesson | C# Module 2 — variables & input lesson | ~102s | csharp-course, module-02-basics |
| `08-ai-prompting-basics` | lesson | AI Module 2 — prompting basics lesson | ~100s | ai-course, 02-prompting-basics |
| `09-python-control-flow` | lesson | Python Module 3 — decisions & loops lesson | ~101s | python-course, module-03-control-flow |
| `10-python-functions` | lesson | Python Module 4 — functions lesson | ~92s | python-course, module-04-functions |
| `11-python-collections` | lesson | Python Module 5 — collections lesson | ~79s | python-course, module-05-collections |
| `12-python-oop` | lesson | Python Module 6 — objects lesson | ~73s | python-course, module-06-oop |
| `13-python-task-tracker` | lesson | Python Module 7 — Task Tracker project lesson | ~81s | python-course, module-07-task-tracker |
| `14-csharp-control-flow` | lesson | C# Module 3 — decisions & loops lesson | ~75s | csharp-course, module-03-control-flow |
| `15-csharp-methods` | lesson | C# Module 4 — methods lesson | ~65s | csharp-course, module-04-methods |
| `16-csharp-collections` | lesson | C# Module 5 — collections lesson | ~56s | csharp-course, module-05-collections |
| `17-csharp-oop` | lesson | C# Module 6 — objects lesson | ~46s | csharp-course, module-06-oop-intro |
| `18-csharp-task-tracker` | lesson | C# Module 7 — Task Tracker project lesson | ~49s | csharp-course, module-07-task-tracker |
| `19-ai-prompt-patterns` | lesson | AI Module 3 — prompt patterns lesson | ~67s | ai-course, 03-prompt-patterns |
| `20-ai-evaluation` | lesson | AI Module 4 — evaluation lesson | ~54s | ai-course, 04-evaluation-and-iteration |
| `21-ai-safety` | lesson | AI Module 5 — safety basics lesson | ~53s | ai-course, 05-safety-and-policy-basics |
| `22-ai-workflows` | lesson | AI Module 6 — workflows lesson | ~50s | ai-course, 06-workflows-and-automation |
| `23-intermediate-modules-guide` | guide | How to study intermediate modules | ~54s | advanced courses, intermediate modules |
| `24-advanced-modules-guide` | guide | How to study advanced modules | ~52s | advanced courses, advanced modules |
| `25-premium-devops` | guide | DevOps Foundations — study guide | ~38s | devops-course, donor |
| `26-premium-aws` | guide | AWS Cloud — study guide | ~22s | aws-course, donor |
| `27-premium-azure` | guide | Azure Cloud — study guide | ~37s | azure-course, donor |
| `28-premium-gcp` | guide | GCP Cloud — study guide | ~36s | gcp-course, donor |
| `29-premium-kubernetes` | guide | Kubernetes — study guide | ~39s | kubernetes-course, donor |
| `30-premium-terraform` | guide | Terraform & IaC — study guide | ~37s | terraform-course, donor |

Prefer text? Enable captions on the video player, or open the on-page transcript / `.txt` download.

Play on site: `docs/tutorials.html`

