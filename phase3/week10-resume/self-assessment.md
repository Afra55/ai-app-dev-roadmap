# 技能自评表

请诚实填写，用于对齐 JD 和面试准备。**熟练** = 能独立做项目；**了解** = 能看懂并小改；**计划** = 仅概念或未实践。

---

## 填写说明

| 等级 | 含义 |
|------|------|
| 熟练 | 仓库里有可运行代码，能答追问 |
| 了解 | 跟过教程，需查文档才能写 |
| 计划 | 知道概念，尚未动手 |

---

## AI 应用开发

| 技能 | 自评 | 证据（仓库路径） |
|------|------|------------------|
| Prompt 工程 | 熟练 / 了解 / 计划 | `week1/` |
| DeepSeek / OpenAI 兼容 API | 熟练 / 了解 / 计划 | `week1/llm_utils.py` |
| RAG（分块、Embedding、检索） | 熟练 / 了解 / 计划 | `week2/`、`projects/direction-a-smart-notes/` |
| FastAPI 服务化 | 熟练 / 了解 / 计划 | `week2/api.py`、各 project API |
| 端侧模型（Mock / 本地小模型） | 熟练 / 了解 / 计划 | `week3/` |
| 端云协同路由 | 熟练 / 了解 / 计划 | `week4/router.py` |
| LangGraph Agent | 熟练 / 了解 / 计划 | `week4/agent.py`、`direction-c/` |
| Tool Use / 多工具协作 | 熟练 / 了解 / 计划 | `week4/tools.py` |

---

## Android

| 技能 | 自评 | 证据 |
|------|------|------|
| Jetpack Compose UI | 熟练 / 了解 / 计划 | `week3/android-app`、`projects/*/android-app` |
| Retrofit 网络层 | 熟练 / 了解 / 计划 | `direction-a` NotesApi |
| ViewModel 状态管理 | 熟练 / 了解 / 计划 | 各 Android ViewModel |
| 端侧 AI 集成（MLC/LiteRT） | 熟练 / 了解 / 计划 | `week3/README` Step 5 |

---

## 安全与工程（银行/国企岗加分）

| 技能 | 自评 | 证据 |
|------|------|------|
| API Key 服务端管理 | 熟练 / 了解 / 计划 | 所有 backend |
| 输入脱敏 | 熟练 / 了解 / 计划 | `direction-b/security.py` |
| 审计日志 | 熟练 / 了解 / 计划 | `direction-c/audit.py` |
| `.env` / 密钥不提交 Git | 熟练 / 了解 / 计划 | `.gitignore` |

---

## 建议跳过的简历表述（除非真会）

- [ ] 大模型预训练 / SFT / RLHF
- [ ] CUDA kernel 优化
- [ ] 「精通」Transformer 数学推导
- [ ] 未部署过的 K8s / 重型 MLOps

---

## 自评后的行动

| 若多数为「计划」 | 行动 |
|------------------|------|
| RAG | 重跑 `week2/verify_setup.py` + 改 chunk 参数实验 |
| Agent | 重跑 `week4/app.py` 三个路由用例 |
| Android | 在模拟器跑通 Direction A App |
| 端侧真实模型 | 试 `week3/chat_local.py --backend qwen` |

---

**填写日期**：________  
**目标岗位**：________
