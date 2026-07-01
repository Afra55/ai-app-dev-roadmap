#!/usr/bin/env bash
# Direction A 3 分钟演示录制脚本（带旁白提示，适合边录边讲）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
DIR="$ROOT/phase2/direction-a-smart-notes"
PAUSE="${PAUSE:-2}"

say() {
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  🎬 $1"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  sleep "$PAUSE"
}

cd "$DIR"

say "【0:20】环境检查 — 证明项目可复现"
python3 verify_setup.py

say "【0:35】初始化示例笔记 + 向量索引"
python3 demo_cli.py --init

say "【0:50】端侧路由演示 — 输入「你好」（无需 API Key）"
python3 demo_cli.py "你好"

say "【1:10】笔记 RAG — 问「我的 RAG 笔记说了什么」"
python3 demo_cli.py "我的 RAG 笔记说了什么"

say "【1:30】列出笔记 — 证明 CRUD + 索引已就绪"
python3 demo_cli.py --list

say "【1:50】启动 API 服务（录制时可另开终端）"
echo "  uvicorn api:app --host 0.0.0.0 --port 8010"
echo "  Swagger: http://127.0.0.1:8010/docs"
echo ""
echo "  示例请求:"
echo '  curl -s -X POST http://127.0.0.1:8010/chat -H "Content-Type: application/json" -d "{\"question\":\"你好\"}"'

say "【2:30】演示完成 — 口述架构图（SQLite / Chroma / 端云路由）"
echo "  详细脚本见: phase3/week9-portfolio/direction-a-demo-3min.md"
echo "  上传录屏后更新: phase3/week9-portfolio/demo-video-links.md"
