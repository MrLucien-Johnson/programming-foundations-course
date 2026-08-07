#!/usr/bin/env bash
# Replace public donor course trees with stubs AFTER the private repo is serving content.
# Usage: ./scripts/stub_public_premium_content.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COURSES=(devops aws azure gcp kubernetes terraform)

for course in "${COURSES[@]}"; do
  dir="$ROOT/languages/$course"
  mkdir -p "$dir"
  # Remove module payloads from the public tip (history may still contain older copies).
  rm -rf "$dir/modules"
  cat > "$dir/README.md" <<EOF
# ${course} (private donor content)

Lesson markdown for this donor course is **not** stored in the public repository tip.

Signed-in donor / allowlisted accounts load it through the site API
(\`GET /api/content\`) from the private premium content repo configured on Render.

See \`docs/PREMIUM-CONTENT-PRIVATE.md\`.
EOF
  echo "stubbed languages/$course"
done

echo "Done. Commit this change only after Render premium content sync is healthy."
