# Direction A 智能笔记 · 3 分钟演示脚本

> 配合 `demo-scripts/direction-a-record-demo.sh` 录制。目标时长 **3:00**，适合 B 站 / 面试投屏。

---

## 时间轴

| 时间 | 画面 | 口述（参考） |
|------|------|--------------|
| 0:00–0:20 | 打开 GitHub 仓库 README，指向 Phase 2 | 「这是一个 Android 开发者转型 AI 应用的 12 周路线，我主攻 Direction A 端云协同智能笔记。」 |
| 0:20–0:50 | 终端：`bash demo-scripts/direction-a-record-demo.sh` 前半段 | 「先看离线能力：问候语走端侧 Mock，不需要联网。」 |
| 0:50–1:30 | 终端：笔记 RAG 问答输出 | 「问笔记相关内容时，系统先检索向量库，再生成答案，并返回 sources。」 |
| 1:30–2:10 | 启动 `uvicorn api:app --port 8010`，打开 `/docs` | 「后端是 FastAPI，提供笔记 CRUD 和 /chat 端云路由。」 |
| 2:10–2:40 | Android 模拟器 / 或说明架构图 | 「Android 端用 Compose，模拟器通过 10.0.2.2 访问宿主机 API；离线时端侧 Mock 兜底。」 |
| 2:40–3:00 | 总结架构：SQLite + Chroma + Week4 路由 | 「技术栈：Week2 RAG、Week3 端侧、Week4 Agent，整合成一个可演示的 Portfolio。」 |

---

## 录制前检查

```bash
pip install -e ".[dev]"
python phase2/direction-a-smart-notes/verify_setup.py
```

- [ ] 终端字体 ≥ 14pt，配色清晰
- [ ] 关闭通知，隐藏敏感 API Key
- [ ] 若演示 cloud 路径，确认 `phase1/week1/.env` 已配置 Key
- [ ] 预演一遍，控制在 3 分钟内

---

## 上传后

将视频链接填入 [demo-video-links.md](demo-video-links.md) 和根 README「作品集」章节。
