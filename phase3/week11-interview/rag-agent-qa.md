# RAG 与 Agent 面试题

结合本仓库 `week2/`、`week4/`、`projects/` 回答。

---

## RAG 基础

### 1. 什么是 RAG？解决什么问题？

**答**：检索增强生成。先从知识库检索相关文档，再拼进 Prompt 让 LLM 生成答案。解决幻觉、知识过时、私有数据无法训练等问题。

**项目**：`week2/rag_pipeline.py` — 检索 Top-K 块 + RAG Prompt + 来源引用。

---

### 2. 为什么要做 Chunk？chunk_size 怎么选？

**答**：受上下文窗口限制，且检索需要合适粒度。太大检索粗、易带噪声；太小上下文不完整。本仓库默认 `chunk_size=500, overlap=80`（`week2/config.py`），智能笔记用 `400/60`（`direction-a/config.py`）。

**追问**：如何验证？→ 改参数后 `--reindex`，用同一问题对比答案。

---

### 3. 检索不准怎么办？

**答**：
- 调小 chunk 或调大 top_k
- 优化文档结构与标题（智能笔记在正文前加标题/标签）
- 后续可加 Hybrid Search、Rerank（本路线未深入）
- 检查 Embedding 模型是否与语言匹配（中文用 `bge-small-zh`）

---

### 4. 如何减少 RAG 幻觉？

**答**：Prompt 明确要求「仅根据参考资料回答，没有则说未找到」；返回来源引用；必要时降低 temperature。

**项目**：`week2/rag_pipeline.py` 的 `RAG_PROMPT`。

---

## Agent 基础

### 5. 什么是 ReAct Agent？

**答**：Reasoning + Acting。模型交替「思考 → 选工具 → 执行 → 再生成」，直到得出最终答案。

**项目**：`week4/agent.py` 使用 `langgraph.prebuilt.create_react_agent`。

---

### 6. Agent 和直接 Chat 有什么区别？

**答**：Chat 只靠模型参数知识；Agent 可调用外部工具（知识库、API、计算器）获取实时或私有数据。

**项目**：`week4/tools.py` — `search_knowledge_base`、`get_weather`、`calculator`。

---

### 7. Tool Use 的基本流程？

**答**：用户提问 → 模型判断是否调用工具 → 输出 tool_call → 执行工具 → 将结果作为 ToolMessage 回传 → 模型生成最终回答。

**项目**：`week1/app_with_tool.py`（入门）、`week4`（完整 Agent）。

---

### 8. Agent 失败常见原因？

**答**：工具描述不清、检索为空仍编造、多步推理超时、API 不稳定。应对：清晰 tool docstring、空结果显式处理、路由简单问题不走 Agent。

---

## 综合追问（高频）

| 问题 | 回答要点 |
|------|----------|
| 知识库更新后怎么办？ | 重新 ingest / 笔记保存时 `index_note` |
| 多轮对话怎么做？ | Week1 history；Agent 用 message 列表 |
| 如何评估 RAG 质量？ | 准备测试问题集，看召回与答案是否含来源 |
| LangGraph 和 LangChain Agent 关系？ | LangGraph 提供图式编排；`create_react_agent` 是预构建 ReAct |

---

## 自测题

1. 画出 RAG 数据流（5 个框以内）。
2. 说明 `search_knowledge_base` 工具如何复用 Week2。
3. 如果没有 API Key，Agent 路径如何降级？（见 `direction-c/agent.py`）
