# Portfolio 演示与录屏清单

## 录屏前准备

- [ ] 终端字体放大（演示用）
- [ ] 关闭无关通知
- [ ] 提前运行一次 `bash scripts/check_portfolio.sh`
- [ ] 若演示 cloud/agent 路径，确认 `week1/.env` 已配置 API Key
- [ ] 准备架构图（见 `project-highlights.md`）

---

## 必录场景（主项目 Direction A）

| # | 场景 | 命令/操作 | 时长 |
|---|------|-----------|------|
| 1 | 环境检查 | `python verify_setup.py` | 30s |
| 2 | 笔记问答 | `python demo_cli.py "我的 RAG 笔记说了什么"` | 60s |
| 3 | 端侧路由 | `python demo_cli.py "你好"` | 30s |
| 4 | API 文档 | `uvicorn api:app --port 8010` → 打开 `/docs` | 60s |
| 5 | 架构讲解 | 对照 README mermaid 图 | 60s |

可选：
- [ ] Android 模拟器连 `10.0.2.2:8010` 创建笔记并提问
- [ ] 配置 API Key 后演示 Agent 天气/计算工具（Week 4）

---

## Direction B 补充镜头（银行 Android 岗）

- [ ] 快捷问题按钮点击
- [ ] 展示脱敏后的 `masked_question` 字段
- [ ] 口述：Key 为何不能放在 App 里

---

## Direction C 补充镜头（国企 Agent 岗）

- [ ] `python verify_setup.py`
- [ ] `python app_admin.py` 提问 + 查看审计日志
- [ ] 口述：分部门检索与工具调用流程

---

## 录屏发布建议

- 标题示例：`Android 开发者转型 AI 应用 — 端云协同智能笔记 Demo`
- 简介附上仓库链接与「教学演示」声明（若含 Direction B）
- 将链接填入 GitHub 主 README 的「Demo 视频」一节

---

## Live Demo 应急预案

| 问题 | 应对 |
|------|------|
| 网络/API 失败 | 切换到离线演示：`你好`、笔记 RAG 离线模式 |
| Embedding 下载慢 | 提前跑过一次 `verify_setup.py` |
| Android 连不上后端 | 改用 CLI + Swagger 演示 |
| 检索无结果 | 先 `python demo_cli.py --init` 重建索引 |
