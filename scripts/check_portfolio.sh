#!/usr/bin/env bash
# 仓库根目录 Portfolio 检查入口
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
bash "$ROOT/phase3/week9-portfolio/demo-scripts/run-all-demos.sh"
