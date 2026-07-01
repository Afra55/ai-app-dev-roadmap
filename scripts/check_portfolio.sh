#!/usr/bin/env bash
# 仓库根目录 Portfolio 检查入口
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo ">>> 运行 pytest 单元测试"
if ! python3 -m pip show ai-app-dev-roadmap &>/dev/null; then
  python3 -m pip install -e ".[dev]" -q
fi
python3 -m pytest tests/ -q --tb=short

bash "$ROOT/phase3/week9-portfolio/demo-scripts/run-all-demos.sh"
