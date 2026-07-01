#!/usr/bin/env bash
# Direction C: 企业 Agent 演示脚本
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
DIR="$ROOT/phase2/direction-c-enterprise-agent"

echo "=== Direction C: Enterprise Agent ==="
cd "$DIR"
python3 verify_setup.py
echo ""
echo "启动 API: uvicorn api:app --port 8030"
echo "管理界面: python app_admin.py"
echo "测试: curl -X POST http://127.0.0.1:8030/chat -H 'Content-Type: application/json' -d '{\"user_id\":\"U10001\",\"question\":\"年假还剩几天？\"}'"
