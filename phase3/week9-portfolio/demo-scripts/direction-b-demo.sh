#!/usr/bin/env bash
# Direction B: 银行智能客服演示脚本
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
DIR="$ROOT/phase2/direction-b-bank-assistant/backend"

echo "=== Direction B: Bank Assistant（教学演示）==="
cd "$DIR"
python3 verify_setup.py
echo ""
echo "启动 API: uvicorn api:app --port 8020"
echo "测试: curl -X POST http://127.0.0.1:8020/ask -H 'Content-Type: application/json' -d '{\"question\":\"转账限额是多少？\"}'"
echo "Android 模拟器基址: http://10.0.2.2:8020/"
