# AI 应用开发学习路线

> **从 Android 开发者转型 AI 应用开发者**  
> 仓库：https://github.com/Afra55/ai-app-dev-roadmap

为有 Android 开发经验的开发者设计的 **12 周**系统化学习路线，覆盖端侧 AI、端云协同、RAG 与 AI Agent。

---

## 目录

- [快速开始](#快速开始)
- [12 周导航](#12-周导航)
- [作品集入口](#作品集入口)
- [仓库结构](#仓库结构)
- [核心优势](#核心优势)
- [使用说明](#使用说明)
- [推荐资源](#推荐资源)

---

## 快速开始

```bash
git clone https://github.com/Afra55/ai-app-dev-roadmap.git
cd ai-app-dev-roadmap

pip install -e ".[dev]"                              # 安装共享依赖
cp .env.example week1/.env                           # 可选：配置 API Key
bash scripts/check_portfolio.sh                      # pytest + 各周冒烟检查
```

| 体验项 | 目录 | 命令 |
|--------|------|------|
| Week 1 聊天 | [week1/](week1/) | `cd week1 && python demo_chat.py` |
| Week 2 RAG | [week2/](week2/) | `cd week2 && python demo_rag.py "什么是 RAG？"` |
| Week 3 端侧 | [week3/](week3/) | `cd week3 && python chat_local.py` |
| Week 4 Agent | [week4/](week4/) | `cd week4 && python app.py` |
| 方向 A API | [projects/direction-a-smart-notes/](projects/direction-a-smart-notes/) | `uvicorn api:app --port 8010` |

---

## 12 周导航

### 第一阶段 · 基础打牢（第 1–4 周）

阶段总览：[week1-4/README.md](week1-4/README.md)

| 周次 | 主题 | 代码目录 | 学习指南 |
|------|------|----------|----------|
| 1 | Python + Prompt + DeepSeek API | [week1/](week1/) | [week1/README.md](week1/README.md) |
| 2 | RAG 本地文档问答 + FastAPI | [week2/](week2/) | [week2/README.md](week2/README.md) |
| 3 | 安卓端侧 AI（Qwen2.5 / Mock） | [week3/](week3/) | [week3/README.md](week3/README.md) |
| 4 | 端云协同 + LangGraph Agent | [week4/](week4/) | [week4/README.md](week4/README.md) |

### 第二阶段 · 项目实战（第 5–8 周）

阶段总览：[week5-8/README.md](week5-8/README.md) · 项目索引：[projects/README.md](projects/README.md)

| 方向 | 适合岗位 | 代码目录 | 学习指南 |
|------|----------|----------|----------|
| **A** 智能笔记 | AI 应用开发 / 端云协同 | [projects/direction-a-smart-notes/](projects/direction-a-smart-notes/) | [README](projects/direction-a-smart-notes/README.md) |
| **B** 银行客服 | 银行 Android + 安全合规 | [projects/direction-b-bank-assistant/](projects/direction-b-bank-assistant/) | [README](projects/direction-b-bank-assistant/README.md) |
| **C** 企业 Agent | 国企 Agent / Python 全栈 | [projects/direction-c-enterprise-agent/](projects/direction-c-enterprise-agent/) | [README](projects/direction-c-enterprise-agent/README.md) |

### 第三阶段 · 求职准备（第 9–12 周）

阶段总览：[phase3/README.md](phase3/README.md)

| 周次 | 主题 | 代码目录 | 学习指南 |
|------|------|----------|----------|
| 9 | Portfolio 打磨 | [phase3/week9-portfolio/](phase3/week9-portfolio/) | [README](phase3/week9-portfolio/README.md) |
| 10 | 简历优化 | [phase3/week10-resume/](phase3/week10-resume/) | [README](phase3/week10-resume/README.md) |
| 11 | 面试准备 | [phase3/week11-interview/](phase3/week11-interview/) | [README](phase3/week11-interview/README.md) |
| 12 | 投递收尾 | [phase3/week12-apply/](phase3/week12-apply/) | [README](phase3/week12-apply/README.md) |

---

## 作品集入口

| 项目 | 亮点 | 演示脚本 |
|------|------|----------|
| [Direction A 智能笔记](projects/direction-a-smart-notes/) | 端云协同 + 笔记 RAG + Android | [direction-a-demo.sh](phase3/week9-portfolio/demo-scripts/direction-a-demo.sh) |
| [Direction B 银行客服](projects/direction-b-bank-assistant/) | 金融脱敏 + FAQ RAG | [direction-b-demo.sh](phase3/week9-portfolio/demo-scripts/direction-b-demo.sh) |
| [Direction C 企业 Agent](projects/direction-c-enterprise-agent/) | 部门权限 + 审计日志 | [direction-c-demo.sh](phase3/week9-portfolio/demo-scripts/direction-c-demo.sh) |

架构说明：[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md) · 变更记录：[CHANGELOG.md](CHANGELOG.md)

---

## 仓库结构

```
ai-app-dev-roadmap/
│
├── README.md                      # 本文件：总导航
├── pyproject.toml                 # pip install -e ".[dev]"
├── common/                        # 共享包（LLM / RAG / Embedding）
├── docs/ARCHITECTURE.md           # 架构说明
├── tests/                         # pytest 回归测试
├── scripts/check_portfolio.sh     # 一键检查
│
├── week1-4/                       # 第一阶段导航（第 1–4 周）
├── week1/  week2/  week3/  week4/  # 第一阶段代码与教程
│
├── week5-8/                       # 第二阶段导航（第 5–8 周）
├── projects/                      # 第二阶段 A / B / C 项目
│   ├── direction-a-smart-notes/
│   ├── direction-b-bank-assistant/
│   └── direction-c-enterprise-agent/
│
└── phase3/                        # 第三阶段（第 9–12 周）
    ├── week9-portfolio/
    ├── week10-resume/
    ├── week11-interview/
    └── week12-apply/
```

---

## 核心优势

本路线依托 Android 开发者的差异化能力：

| 能力 | 对应周次 / 项目 |
|------|----------------|
| **端侧 AI**（LiteRT-LM / MLC LLM） | [week3/](week3/) · [Direction A](projects/direction-a-smart-notes/) |
| **端云协同** | [week4/](week4/) · [Direction A](projects/direction-a-smart-notes/) |
| **RAG** | [week2/](week2/) · 三方向项目 |
| **AI Agent**（LangGraph） | [week4/](week4/) · [Direction C](projects/direction-c-enterprise-agent/) |

---

## 使用说明

1. Fork 本仓库，按 [12 周导航](#12-周导航) 顺序学习
2. 每周进入**代码目录**，跟随对应 **README** 完成任务
3. 第 5–8 周在 [projects/](projects/) 中选一个方向主攻
4. 第 9–12 周用 [phase3/](phase3/) 打磨简历与面试材料
5. 定期运行 `bash scripts/check_portfolio.sh` 确保可复现

---

## 推荐资源

- [Datawhale《动手学大模型应用开发》](https://github.com/datawhalechina/llm-universe)
- [Google AI Edge / LiteRT](https://ai.google.dev/edge)
- [LangGraph 官方教程](https://langchain-ai.github.io/langgraph/)
- [DeepSeek API 文档](https://api-docs.deepseek.com/)

**建议跳过**：大模型训练、数学推导、CUDA 底层优化、重型 MLOps——前 3 个月聚焦应用开发。

---

## 期望学习成果

- 可演示的 AI 应用 Portfolio（含端侧 + 端云协同）
- 突出差异化优势的简历与项目描述
- 面试就绪的 RAG / Agent / 端侧部署知识

---

**最后更新**：2026 年 7 月 · 问题反馈请提交 [Issue](https://github.com/Afra55/ai-app-dev-roadmap/issues)
