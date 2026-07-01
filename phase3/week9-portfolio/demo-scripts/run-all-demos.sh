#!/usr/bin/env bash
# 一键跑通各阶段 verify_setup（Portfolio 可运行性检查）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"

echo "========================================"
echo " AI App Dev Roadmap - Portfolio Check"
echo "========================================"

run_check() {
  local name="$1"
  local dir="$2"
  echo ""
  echo ">>> $name"
  if [ ! -d "$dir" ]; then
    echo "SKIP: 目录不存在 $dir"
    return 0
  fi
  cd "$dir"
  if [ -f "verify_setup.py" ]; then
    python3 verify_setup.py
  else
    echo "SKIP: 无 verify_setup.py"
  fi
  cd "$ROOT"
}

run_check "Week 1" "$ROOT/week1"
run_check "Week 2" "$ROOT/week2"
run_check "Week 3" "$ROOT/week3"
run_check "Week 4" "$ROOT/week4"
run_check "Direction A" "$ROOT/projects/direction-a-smart-notes"
run_check "Direction B" "$ROOT/projects/direction-b-bank-assistant/backend"
run_check "Direction C" "$ROOT/projects/direction-c-enterprise-agent"

echo ""
echo "========================================"
echo " 全部检查完成"
echo "========================================"
