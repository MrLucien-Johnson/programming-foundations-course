# Private donor course content

Donor DevOps & cloud lessons must not rely on public `raw.githubusercontent.com`.

## How it works

1. **Private GitHub repo** holds `languages/{devops,aws,azure,gcp,kubernetes,terraform}/…`
2. **Render API** clones that repo at boot using:
   - `PREMIUM_CONTENT_GIT_URL` — https clone URL of the private repo
   - `PREMIUM_CONTENT_GIT_TOKEN` — PAT with **Contents: Read** on that repo only
3. **Site** loads donor lessons/quizzes via `GET /api/content?path=…` (auth + donor/allowlist required)
4. Free language courses still use the public repo

Owner emails in `ORG_CREATOR_EMAILS` (and `PREMIUM_ACCESS_EMAILS`) always unlock; other learners need a donor grant on Account.

## One-time setup

1. Create a **private** repo (suggested name: `programming-foundations-premium`).
2. From this public repo checkout, push the seed:

```bash
export PREMIUM_CONTENT_GIT_URL='https://github.com/YOU/programming-foundations-premium.git'
export PREMIUM_CONTENT_GIT_TOKEN='ghp_…'
chmod +x scripts/push_premium_private_repo.sh
./scripts/push_premium_private_repo.sh
```

3. On Render → `programming-foundations-api` → Environment, set the same URL + token, plus `ORG_CREATOR_EMAILS=your@email`.
4. Redeploy the API. Check `/api/health` → `premiumContent.ready` should be `true` and `configured` true.
5. After that works, remove public copies of the donor trees:

```bash
chmod +x scripts/stub_public_premium_content.sh
./scripts/stub_public_premium_content.sh
git add languages && git commit -m "Remove public donor course markdown (served privately)"
```

## Local development

Without the private repo env vars, the API falls back to the local `languages/` folder in this checkout (`PREMIUM_CONTENT_ROOT` overrides the root).

## Limits

- Git **history** of the public repo may still contain older copies until history is rewritten (optional hard scrub).
- Until step 5, determined users can still clone donor markdown from the public tip — the site itself will not fetch it via raw GitHub.
