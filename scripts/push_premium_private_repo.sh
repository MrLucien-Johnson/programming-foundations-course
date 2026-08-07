#!/usr/bin/env bash
# Push donor course markdown into a PRIVATE GitHub repo (same path layout).
# Usage:
#   export PREMIUM_CONTENT_GIT_URL='https://github.com/YOU/programming-foundations-premium.git'
#   export PREMIUM_CONTENT_GIT_TOKEN='ghp_...'   # PAT with Contents: Read/Write on that private repo
#   ./scripts/push_premium_private_repo.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
URL="${PREMIUM_CONTENT_GIT_URL:-}"
TOKEN="${PREMIUM_CONTENT_GIT_TOKEN:-}"

if [[ -z "$URL" || -z "$TOKEN" ]]; then
  echo "Set PREMIUM_CONTENT_GIT_URL and PREMIUM_CONTENT_GIT_TOKEN first." >&2
  exit 1
fi

COURSES=(devops aws azure gcp kubernetes terraform)
for course in "${COURSES[@]}"; do
  if [[ ! -d "$ROOT/languages/$course/modules" ]]; then
    echo "Missing languages/$course/modules — generate courses first." >&2
    exit 1
  fi
done

AUTH_URL="$(python3 - <<'PY' "$URL" "$TOKEN"
from urllib.parse import urlparse, urlunparse
import sys
url, token = sys.argv[1], sys.argv[2]
p = urlparse(url)
if p.scheme != "https":
    raise SystemExit("URL must be https")
netloc = f"x-access-token:{token}@{p.hostname}"
if p.port:
    netloc += f":{p.port}"
print(urlunparse((p.scheme, netloc, p.path, "", "", "")))
PY
)"

WORKDIR="$(mktemp -d)"
cleanup() { rm -rf "$WORKDIR"; }
trap cleanup EXIT

echo "Cloning / preparing private repo…"
if git ls-remote "$AUTH_URL" HEAD &>/dev/null; then
  git clone --depth 1 "$AUTH_URL" "$WORKDIR/repo"
else
  mkdir -p "$WORKDIR/repo"
  git -C "$WORKDIR/repo" init -b main
  git -C "$WORKDIR/repo" remote add origin "$AUTH_URL"
fi

mkdir -p "$WORKDIR/repo/languages"
for course in "${COURSES[@]}"; do
  rm -rf "$WORKDIR/repo/languages/$course"
  cp -a "$ROOT/languages/$course" "$WORKDIR/repo/languages/$course"
done

cat > "$WORKDIR/repo/README.md" <<'EOF'
# Programming Foundations — private donor content

Private markdown for DevOps / cloud donor courses.

The public site never loads these files from raw GitHub. The Render API clones this
repo and serves files only to allowlisted / donor accounts via `GET /api/content`.

Layout (keep stable):

```
languages/<course>/modules/*.md
languages/<course>/modules/*.quiz.md
languages/<course>/modules/*.quiz-answers.md
```
EOF

git -C "$WORKDIR/repo" add -A
if git -C "$WORKDIR/repo" diff --cached --quiet; then
  echo "No content changes to push."
  exit 0
fi

git -C "$WORKDIR/repo" -c user.email="premium-content-bot@local" -c user.name="Premium Content Bot" \
  commit -m "Sync donor DevOps and cloud course content"
git -C "$WORKDIR/repo" push -u origin HEAD:main

echo "Pushed donor content to private repo."
echo "Next: set the same URL + token (read-only is enough) on Render, redeploy, then remove public languages/{devops,aws,azure,gcp,kubernetes,terraform}."
