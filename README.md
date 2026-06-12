# AI应用开发学习路线（从Android转型AI App Dev）

**GitHub Repo**: https://github.com/Afra55/ai-app-dev-roadmap

这个仓库用于存放完整的3个月学习路线 + 以后所有测试代码、项目代码。

由Grok为你定制，项目名称自己决定为 `ai-app-dev-roadmap`。

---

## 🎯 核心竞争力

- **端侧AI** (LiteRT-LM / MLC LLM)
- **端云协同**
- **RAG + Agent**

这是你作为Android开发者最大的区别于纯Python转行者的杀手锐。

---

## 📊 3个月路线概览

### 第一阶段（第1-4周）：基础打牢
- **第1周**：Python速通 + Prompt + 国内LLM API（DeepSeek优先）
- **第2周**：RAG核心实现（推荐 LlamaIndex）
- **第3周**：安卓端侧AI（LiteRT-LM + Qwen2.5）
- **第4周**：简单端云协同 + LangGraph Agent入门

### 第二阶段（第5-8周）：分方向项目实战
根据目标岗位选主方向（A/B/C），做具体App项目。

### 第三阶段（第9-12周）：Portfolio打磨 + 简历 + 面试准备

---

## 📝 详细路线（完整版）

### 第一阶段：基础打牢（第1-4周）

** 第1周：Python速通 + Prompt + 国内LLM API **
- 只学：Python异步/await、类型注解 + Prompt技巧（CoT、结构化输出、function calling） + 国内API封装
- **必做产出**：FastAPI统一LLM调用接口 + Gradio支持JSON结构化输出的聊天应用（用DeepSeek）
- **资源**：Datawhale《动手学大模型应用开发》Task 1-2 + B站黑马程序员视频

** 第2周：RAG核心实现 **
- 只学：完整RAG流程 + 分块策略、嵌入模型、重排器
- **必做产出**：LlamaIndex本地文档问答工具（支持PDF） + FastAPI接口
- **资源**：Datawhale RAG部分 + LlamaIndex官方quickstart

** 第3周：安卓端侧AI（你的核心竞争力） **
- 只学：LiteRT-LM Kotlin API + Qwen2.5-1.5B-INT4部署 + GPU/NPU加速
- **必做产出**：Android App集成Qwen2.5-1.5B-INT4，实现纯离线聊天，记录中端设备推理速度
- **资源**：Google官方 LiteRT-LM 文档 + B站端侧AI视频

** 第4周：简单端云协同 + LangGraph Agent入门 **
- 只学：LangGraph状态/节点/边 + 简单ReAct Agent + 端云判断逻辑
- **必做产出**：端云协同智能助手 + 能调用计算器的简单Agent
- **资源**：LangGraph官方tutorial

---

### 第二阶段：分方向深化 + 项目实战（第5-8周）

** 方向A（岗位1 AI应用软件开发工程师） **
- UX工程化 + 高级端侧AI
- 项目：端云协同智能笔记App

** 方向B（岗位2 国有银行Android开发） **
- 高级Android强化
- 项目：银行智能客服App

** 方向C（岗位3 国企AI Agent应用开发） **
- Python全栈进阶 + 高级Agent
- 项目：企业内部智能助手Agent

** 通用要求 **：所有项目上传GitHub，写README（架构图 + 技术栈 + 量化成果 + 演示视频）。后端Docker化。

---

### 第三阶段：简历优化 + 面试准备 + 投递（第9-12周）

- 第9-10周：简历优化（突出端侧AI、端云协同、量化成果）
- 第11周：面试准备（RAG流程、Agent原理、端侧AI优劣势、Android性能优化）
- 第12周：项目打磨 + 模拟面试 + 投递

---

## 📦 仓库结构（未来代码放这里）

```
ai-app-dev-roadmap/
├── README.md          # 完整学习路线
├── week1/             # 第1周代码
├── week2/             # 第2周代码
├── projects/          # 项目代码
├── docs/              # 额外资料
└── .gitignore
```

---

## 📚 资源列表（完全免费主干）

- **Datawhale** 《动手学大模型应用开发》：https://datawhalechina.github.io/llm-universe/
- **LiteRT-LM官方** ：https://ai.google.dev/edge/litert-lm/overview
- **LangGraph官方** ：https://langchain-ai.github.io/langgraph/
- **LlamaIndex官方** ：https://docs.llamaindex.ai/
- **B站黑马程序员** 2026大模型应用开发视频
- DeepSeek API：https://platform.deepseek.com

---

## ❌ 绝对不要学的内容

- 数学与底层理论
- 大模型训练（预训练、SFT、RLHF等）
- 底层系统优化（CUDA kernel等）
- 重型MLOps
- 非核心多模态训练

---

## 🚀 如何使用这个仓库

1. Star 并 Fork 到自己账号
2. Clone 到本地
3. 每周按路线完成任务
4. 每周代码提交到对应文件夹
5. README 会随时更新

** 接下来行动 **：
今天开始第1周第1步！

有任何问题直接在Issues或评论区提出。

---

** 由Grok为你创建并维护 **
** 最后更新时间 **：2026年6月12日
