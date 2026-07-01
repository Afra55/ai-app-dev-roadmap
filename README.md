# AI应用开发学习路线

**从 Android 开发者转型 AI 应用开发者**

**仓库地址**: https://github.com/Afra55/ai-app-dev-roadmap

为有 Android 开发经验的开发者设计的系统化、可落地的 12 周学习路线。重点突出端侧 AI、端云协同、RAG 与 AI Agent 能力。

---

## 30 分钟快速体验

```bash
git clone https://github.com/Afra55/ai-app-dev-roadmap.git
cd ai-app-dev-roadmap

# 1. 安装共享依赖（推荐）
pip install -e ".[dev]"

# 2. 配置 API Key（可选，无 Key 可走离线/Mock 模式）
cp .env.example week1/.env
# 编辑 week1/.env，填入 DEEPSEEK_API_KEY

# 3. 一键检查（pytest + 各周 verify_setup）
bash scripts/check_portfolio.sh
```

| 步骤 | 命令 | 说明 |
|------|------|------|
| Week 1 聊天 | `cd week1 && python demo_chat.py` | 结构化输出 + Gradio |
| Week 2 RAG | `cd week2 && python demo_rag.py "什么是 RAG？"` | 本地文档问答 |
| Week 4 Agent | `cd week4 && python app.py` | 端云路由 + LangGraph |
| 方向 A API | `cd projects/direction-a-smart-notes && uvicorn api:app --port 8010` | 智能笔记后端 |

---

## 作品集入口（求职用）

| 项目 | 路径 | 亮点 |
|------|------|------|
| 智能笔记（方向 A） | [projects/direction-a-smart-notes/](projects/direction-a-smart-notes/) | 端云协同 + 笔记 RAG + Android |
| 银行客服（方向 B） | [projects/direction-b-bank-assistant/](projects/direction-b-bank-assistant/) | 金融脱敏 + FAQ RAG |
| 企业 Agent（方向 C） | [projects/direction-c-enterprise-agent/](projects/direction-c-enterprise-agent/) | 部门权限 + 审计日志 |

**第三阶段材料**：[phase3/](phase3/)（简历模板、面试题、演示脚本）

**架构说明**：[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## Core Differentiators

本路线依托 Android 开发者的核心优势：

- **端侧 AI** (LiteRT-LM / MLC LLM)
- **端云协同**
- **RAG 与 AI Agent** (LangGraph)

这些能力使你相比纯 Python 转行者具有明显优势。

---

## 12 周路线概览

### 第一阶段：基础打牢（第 1-4 周）

| 周次 | 重点 | 核心产出 |
|------|-------|------------------|
| 1    | Python + Prompt 工程 + DeepSeek API | 结构化输出聊天应用 |
| 2    | RAG 实现 | 本地文档问答工具 + FastAPI |
| 3    | 安卓端侧 AI | 离线 Qwen2.5 聊天 App（Python Demo + Android 骨架） |
| 4    | 简单端云协同 + LangGraph Agent | ReAct Agent + 端云路由 |

### 第二阶段：分方向项目实战（第 5-8 周）

根据目标岗位选择主方向（导航见 [week5-8/](week5-8/)，代码见 [projects/](projects/)）：

- **方向 A** (岗位1 AI 应用软件开发工程师)：UX 工程化 + 高级端侧 AI → [端云协同智能笔记 App](projects/direction-a-smart-notes/)
- **方向 B** (岗位2 国有银行 Android 开发)：高级 Android + 安全开发 → [银行智能客服 App](projects/direction-b-bank-assistant/)
- **方向 C** (岗位3 国企 AI Agent 应用开发)：Python 全栈 + 高级 Agent → [企业内部智能助手 Agent](projects/direction-c-enterprise-agent/)

### 第三阶段：Portfolio 打磨 + 简历 + 面试准备（第 9-12 周）

详细指导见 [phase3/](phase3/)：

| 周次 | 主题 | 链接 |
|------|------|------|
| 9 | Portfolio 打磨 | [week9-portfolio](phase3/week9-portfolio/) |
| 10 | 简历优化 | [week10-resume](phase3/week10-resume/) |
| 11 | 面试准备 | [phase3/week11-interview](phase3/week11-interview/) |
| 12 | 投递收尾 | [phase3/week12-apply](phase3/week12-apply/) |

---

## 仓库结构

```
ai-app-dev-roadmap/
├── README.md                 # 本文件：导航与快速体验
├── pyproject.toml            # 统一依赖，pip install -e ".[dev]"
├── common/                   # 共享包：LLM、RAG、Embedding、天气
├── docs/ARCHITECTURE.md      # 架构说明
├── tests/                    # pytest 回归测试
├── scripts/
│   └── check_portfolio.sh    # 一键检查（pytest + verify_setup）
├── week1/ … week4/           # 第一阶段
├── week5-8/                  # 第二阶段导航（项目代码在 projects/）
├── projects/                 # 第二阶段 A/B/C 三方向
├── phase3/                   # 第三阶段：作品集、简历、面试、投递
└── .github/workflows/ci.yml  # GitHub Actions CI
```

---

## 如何使用本仓库

1. Star 并 Fork 本仓库
2. `pip install -e ".[dev]"` 安装共享依赖
3. 复制 `.env.example` → `week1/.env`，配置 `DEEPSEEK_API_KEY`（可选）
4. 进入对应 `weekX/` 目录，按 `README.md` 完成每周任务
5. 第 5–8 周进入 `projects/` 对应方向
6. 第 9–12 周使用 `phase3/` 打磨求职材料
7. 通过 Issues 追踪问题

**建议**：主要参考各周 `README.md` 进行学习；贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 每周详细指导

- [Week 1: Python + Prompt + DeepSeek API](week1/README.md)
- [Week 2: RAG 实现（本地文档问答 + FastAPI）](week2/README.md)
- [Week 3: 安卓端侧 AI（离线 Qwen2.5 聊天）](week3/README.md)
- [Week 4: 端云协同与 LangGraph Agent](week4/README.md)
- [Week 5–8: 项目实战导航](week5-8/README.md)

### 第三阶段

- [Phase 3 总览](phase3/README.md)
- [Week 9: Portfolio 打磨](phase3/week9-portfolio/README.md)
- [Week 10: 简历优化](phase3/week10-resume/README.md)
- [Week 11: 面试准备](phase3/week11-interview/README.md)
- [Week 12: 投递收尾](phase3/week12-apply/README.md)

---

## 推荐资源

**主要资源（免费且集中）**：

- Datawhale 《动手学大模型应用开发》
- Google AI Edge: LiteRT-LM 官方文档
- LangGraph 官方教程
- LlamaIndex 官方文档
- B站黑马程序员 2026 大模型应用开发系列

**API 提供商**：
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

完成 12 周学习后，你将拥有：

- 完整的 AI 应用 Portfolio（包含端侧 AI 和端云协同项目）
- 突出端侧 AI 与端云协同优势的简历内容
- 面试准备就绪的 RAG、Agent 和端侧部署知识
- 系统化的 AI 学习方法

---

## 备注

本仓库持续更新中。变更记录见 [CHANGELOG.md](CHANGELOG.md)。

如有问题请提交 Issue。

**最后更新时间**：2026 年 7 月

---

## 作品集快速检查

```bash
bash scripts/check_portfolio.sh
```

包含 `pytest` 单元测试与各周 `verify_setup.py` 冒烟检查。
