# AI应用开发学习路线

**从 Android 开发者转型 AI 应用开发者**

**仓库地址**: https://github.com/Afra55/ai-app-dev-roadmap

为有 Android 开发经验的开发者设计的系统化、可落地的 3 个月学习路线。重点突出端侧 AI、端云协同、RAG 与 AI Agent 能力。

---

## 目录

- [Core Differentiators](#core-differentiators)
- [3 个月路线概览](#3%E4%B8%AA%E6%9C%88%E8%B7%AF%E7%BA%BF%E6%A6%82%E8%A7%88)
- [仓库结构](#%E4%BB%93%E5%BA%93%E7%BB%93%E6%9E%84)
- [如何使用本仓库](#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%9C%AC%E4%BB%93%E5%BA%93)
- [每周详细指导](#%E6%AF%8F%E5%91%A8%E8%AF%A6%E7%BB%86%E6%8C%87%E5%AF%BC)
- [推荐资源](#%E6%8E%A8%E8%8D%90%E8%B5%84%E6%BA%90)
- [建议跳过的内容](#%E5%BB%BA%E8%AE%AE%E8%B7%B3%E8%BF%87%E7%9A%84%E5%86%85%E5%AE%B9)
- [期望学习成果](#%E6%9C%9F%E6%9C%9B%E5%AD%A6%E4%B9%A0%E6%88%90%E6%9E%9C)

---

## Core Differentiators

本路线依托 Android 开发者的核心优势：

- **端侧 AI** (LiteRT-LM / MLC LLM)
- **端云协同**
- **RAG 与 AI Agent** (LangGraph)

这些能力使你相比纯 Python 转行者具有明显优势。

---

## 3 个月路线概览

### 第一阶段：基础打牢（第 1-4 周）

| 周次 | 重点 | 核心产出 |
|------|-------|------------------|
| 1    | Python + Prompt 工程 + DeepSeek API | 结构化输出聊天应用 |
| 2    | RAG 实现 | 本地文档问答工具 + FastAPI |
| 3    | 安卓端侧 AI | 离线 Qwen2.5 聊天 App |
| 4    | 简单端云协同 + LangGraph Agent | ReAct Agent + 端云逻辑 |

### 第二阶段：分方向项目实战（第 5-8 周）

根据目标岗位选择主方向：

- **方向 A** (岗位1 AI 应用软件开发工程师)：UX 工程化 + 高级端侧 AI → 端云协同智能笔记 App
- **方向 B** (岗位2 国有银行 Android 开发)：高级 Android + 安全开发 → 银行智能客服 App
- **方向 C** (岗位3 国企 AI Agent 应用开发)：Python 全栈 + 高级 Agent → 企业内部智能助手 Agent

### 第三阶段：Portfolio 打磨 + 简历 + 面试准备（第 9-12 周）

- Portfolio 打磨
- 简历优化（突出端侧 AI 与 端云协同优势）
- 面试准备
- 投递岗位

---

## 仓库结构

```
ai-app-dev-roadmap/
├── README.md                 # 高层概览与导航
├── week1/
│   ├── README.md             # 第1周详细步骤
│   ├── requirements.txt      # 第1周 Python 依赖
│   ├── llm_utils.py          # LLM 封装
│   ├── test_chat.py          # 结构化输出示例
│   ├── app.py                # 完整聊天应用
│   └── app_with_tool.py      # Tool Use 示例
├── week2/
│   ├── README.md             # 第2周详细步骤
│   ├── requirements.txt      # 第2周 Python 依赖
│   ├── ingest.py             # 文档索引
│   ├── rag_pipeline.py       # RAG 检索与生成
│   ├── api.py                # FastAPI 服务
│   └── sample_docs/          # 示例文档
├── projects/                 # 项目代码与文档
├── docs/                     # 附加参考资料
└── .gitignore
```

---

## 如何使用本仓库

1. Star 并 Fork 本仓库
2. Clone 到本地
3. 进入 `week1/` 或 `week2/` 目录，按对应 `README.md` 的「快速开始」安装依赖并配置 API Key
4. 按照 `weekX/README.md` 完成每周详细任务
5. 每周提交代码与笔记
6. 通过 Issues 追踪问题

** 建议 **：主要参考 `weekX/README.md` 进行学习。

---

## 每周详细指导

详细步骤、代码示例和练习请查看对应周的 README：

- [Week 1: Python + Prompt + DeepSeek API](week1/README.md)
- [Week 2: RAG 实现（本地文档问答 + FastAPI）](week2/README.md)
- Week 3: 安卓端侧 AI（即将更新）
- Week 4: 端云协同与 LangGraph（即将更新）

---

## 推荐资源

** 主要资源（免费且集中） **：

- Datawhale 《动手学大模型应用开发》
- Google AI Edge: LiteRT-LM 官方文档
- LangGraph 官方教程
- LlamaIndex 官方文档
- B站黑马程序员 2026 大模型应用开发系列

**API 提供商** ：
- DeepSeek Platform

---

## 建议跳过的内容

为保持效率，前 3 个月建议避免以下内容：

- 数学与底层理论（Transformer 细节、注意力公式等）
- 大模型训练（预训练、SFT、RLHF、LoRA 等）
- 底层系统优化（CUDA kernel 等）
- 重型 MLOps 工具
- 非核心多模态训练

---

## 期望学习成果

完成 3 个月学习后，你将拥有：

- 完整的 AI 应用 Portfolio（包含端侧 AI 和 端云协同项目）
- 突出端侧 AI 与 端云协同优势的简历内容
- 面试准备就绪的 RAG、Agent 和 端侧部署知识
- 系统化的 AI 学习方法

---

## 备注

本仓库正在持续更新中。每周详细指导会随着学习进度不断完善。

如有问题请提交 Issue。

** 最后更新时间 **：2026 年 6 月
