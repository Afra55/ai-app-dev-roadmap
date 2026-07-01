# 第二阶段：项目实战（第 5–8 周）

本目录对应路线中的 **第 5–8 周**。每周按所选方向推进一个 Portfolio 项目，而非单独的 `week5/` 代码目录。

## 周次与项目映射

| 周次 | 方向 A（AI 应用开发） | 方向 B（银行 Android） | 方向 C（企业 Agent） |
|------|----------------------|------------------------|----------------------|
| 5 | 笔记 CRUD + 向量索引 | FAQ 知识库 + 脱敏 | 部门知识库 + 权限 |
| 6 | 端云路由 + RAG 问答 | FastAPI 客服 API | LangGraph Agent 工具链 |
| 7 | Android 客户端联调 | Android 安全 UI | Streamlit 管理台 |
| 8 | 联调打磨 + README | 联调打磨 + README | 审计日志 + README |

## 项目入口

- [方向 A：端云协同智能笔记](direction-a-smart-notes/) — 端口 `8010`
- [方向 B：银行智能客服](direction-b-bank-assistant/) — 端口 `8020`
- [方向 C：企业内部智能助手](direction-c-enterprise-agent/) — 端口 `8030`

总览与选型说明见 [projects/README.md](README.md)。

## 快速验证

```bash
# 仓库根目录
pip install -e ".[dev]"
bash scripts/check_portfolio.sh
```

## 与第一阶段的关系

| 复用模块 | 来源 |
|----------|------|
| LLM 客户端 | `common/llm_utils.py`（源自 week1） |
| RAG 索引 | `common/rag.py`（源自 week2） |
| 端云路由 | `week4/router.py` |
| Agent 工具 | `week4/tools.py` |

架构说明见 [docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md)。

## 完成后

进入 [第三阶段：Portfolio 打磨](../phase3/)（第 9–12 周）。
