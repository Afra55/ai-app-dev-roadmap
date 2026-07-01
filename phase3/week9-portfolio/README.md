# 第 9 周：Portfolio 打磨

## 本周目标

把第二阶段项目变成**可演示、可讲解、可复现**的作品集，面试时 5 分钟内讲清价值与技术亮点。

---

## 任务清单

- [ ] 阅读 [project-highlights.md](project-highlights.md)，选定主项目（建议 Direction A）
- [ ] 按 [demo-checklist.md](demo-checklist.md) 完成录屏或 live demo 排练
- [ ] 运行 [demo-scripts/run-all-demos.sh](demo-scripts/run-all-demos.sh) 确保命令可用
- [ ] 更新 GitHub 仓库 README 顶部的「作品集入口」说明
- [ ] 准备 1 分钟 / 3 分钟两版项目口述稿

---

## 5 分钟演示结构（推荐）

| 时间 | 内容 |
|------|------|
| 0:00–0:30 | 问题背景：为什么做智能笔记 / 客服 / 企业助手 |
| 0:30–1:30 | 架构图：端云协同、RAG、Agent 如何分工 |
| 1:30–3:30 | Live Demo：按演示脚本操作 |
| 3:30–4:30 | 技术难点：检索、路由、安全（按方向选 1–2 个） |
| 4:30–5:00 | 总结 + 可扩展方向 |

---

## 演示脚本

详见 [demo-scripts/](demo-scripts/)：

- `run-all-demos.sh`：一键检查各模块（无需 API Key 部分）
- `direction-a-demo.sh`：智能笔记专项演示
- `direction-b-demo.sh`：银行客服专项演示
- `direction-c-demo.sh`：企业 Agent 专项演示

---

## GitHub 仓库整理建议

1. **Pin 本仓库**到你的 GitHub 主页
2. 根 README 写清学习路径：`phase1` → `projects` → `phase3`
3. 主项目 README 顶部增加：
   - 演示命令
   - 架构图（已有 mermaid 可复用）
   - 录屏链接占位（上传 B 站 / YouTube 后填入）
4. 确认 `.env` 未提交，`git log` 中无密钥

---

## 本周验收

- [ ] 演示脚本在本机跑通
- [ ] 能不看稿讲完架构图
- [ ] 能解释「为什么简单问题走端侧、复杂问题走云端」
- [ ] 准备好回答「如果检索结果为空怎么办」

---

**下一步**：[Week 10 简历优化](../week10-resume/README.md)
