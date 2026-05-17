#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

npx @google/design.md lint "$ROOT/examples/ai-devtool/DESIGN.md"
npx @google/design.md lint "$ROOT/examples/creator-commerce/DESIGN.md"
npx @google/design.md lint "$ROOT/examples/editorial-saas/DESIGN.md"
