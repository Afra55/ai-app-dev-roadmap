#!/usr/bin/env bash
# Direction A: 智能笔记演示脚本
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
DIR="$ROOT/phase2/direction-a-smart-notes"

echo "=== Direction A: Smart Notes ==="
cd "$DIR"
python3 verify_setup.py
python3 demo_cli.py --init
echo ""
echo "--- 端侧路由（无需 API Key）---"
python3 demo_cli.py "你好"
echo ""
echo "--- 笔记 RAG（无 Key 时走离线模式）---"
python3 demo_cli.py "我的 RAG 笔记说了什么"
echo ""
echo "启动 API: uvicorn api:app --port 8010"
echo "Swagger: http://127.0.0.1:8010/docs"
