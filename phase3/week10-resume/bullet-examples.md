# 项目描述 Bullet 范例库

按目标岗位复制修改，每条控制在 **1–2 行**。

---

## Direction A：智能笔记（AI 应用岗 · 主推）

- 基于 **FastAPI + SQLite + Chroma** 实现智能笔记后端，笔记保存时自动分块向量化，支持语义检索与来源引用
- 设计 **端云协同路由**：问候类请求走端侧 Mock/Qwen，复杂推理走 DeepSeek，工具类请求走 **LangGraph ReAct Agent**
- 开发 **Android Compose** 客户端，使用 Retrofit 调用 REST API，实现笔记列表、创建与「问我的笔记」对话
- 实现离线降级策略：无 API Key 时端侧 Mock 与 RAG 检索片段仍可演示，保证 Portfolio 可复现
- 编写 `verify_setup.py` 与演示脚本，新环境可在 10 分钟内完成可运行性验证

---

## Direction B：银行客服（银行 Android 岗 · 辅推）

> 务必标注：**教学演示项目，虚构业务数据**

- 实现银行 FAQ **RAG 问答后端**，客户端通过 REST API 提问，**API Key 不进入 Android 安装包**
- 开发输入 **脱敏模块**，对日志中的手机号、身份证号进行掩码，降低敏感信息泄露风险
- Android 端提供 **快捷问题入口**与聊天界面，弱网时展示友好错误提示，支持后续扩展「转人工」流程
- 在 README 中说明安全基线与威胁模型，体现金融场景合规意识

---

## Direction C：企业助手（国企 Agent 岗 · 主推/辅推）

- 按 **HR / 财务 / IT** 分目录构建企业知识库，检索时支持部门 metadata 过滤
- 基于 **LangGraph** 实现 ReAct Agent，集成知识库检索、请假余额查询（Mock）、IT 工单提交（Mock）三类工具
- 设计 **SQLite 审计日志**，记录用户 ID、问题、路由路径与时间戳，满足企业内控追溯需求
- 提供 **FastAPI + Gradio** 双入口，支持 API 集成与管理界面演示

---

## 第一阶段基础（可合并进项目描述，不宜单独占一整段）

- 完成 4 周 AI 应用基础训练：LLM API、RAG、端侧推理抽象、LangGraph Agent 与端云路由
- 熟练使用 **Prompt 工程**（结构化输出、CoT、Tool Use）提升 LLM 应用稳定性

---

## 按岗位组合建议

| 岗位 | 主项目 bullets | 辅项目 bullets |
|------|----------------|----------------|
| AI 应用开发 | A 全部选 3–4 条 | C 选 2 条 |
| 银行 Android | B 全部选 3 条 | A 中选「Android + Key 不进客户端」1–2 条 |
| 国企 Agent | C 全部选 3–4 条 | A 中选 RAG/端云 1–2 条 |

---

## 动词参考

实现、设计、开发、集成、优化、封装、构建、编写、支持、降低、保证
