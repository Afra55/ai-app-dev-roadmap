# 简历模板（中文）

> 复制本模板到 Notion / 语雀 / Word，删除说明性文字后使用。

---

## 张三

- 手机：138-xxxx-xxxx
- 邮箱：your@email.com
- GitHub：https://github.com/yourname
- 城市：北京
- 求职意向：**AI 应用开发工程师** / Android 开发（AI 方向）

---

## 技能摘要

- **AI 应用**：Prompt 工程、RAG（Chroma）、LangGraph Agent、DeepSeek API
- **端云协同**：端侧模型抽象（Mock/Qwen）、路由策略（local/cloud/agent）
- **后端**：Python、FastAPI、SQLite、向量检索
- **Android**：Kotlin、Jetpack Compose、Retrofit、ViewModel
- **工程习惯**：环境隔离、API Key 管理、基础安全脱敏

---

## 项目经历

### 端云协同智能笔记 App（个人项目）| 2026.01 – 2026.02

*技术栈：Python、FastAPI、Chroma、LangGraph、Android Compose*

- 实现笔记 SQLite 存储与保存时自动向量索引，支持「问我的笔记」RAG 问答并返回答案来源
- 集成端云路由：短问候走端侧 Mock 模型，复杂问题走云端 DeepSeek，工具任务走 LangGraph Agent
- 开发 Android Compose 客户端，通过 Retrofit 调用后端 API，API Key 仅部署于服务端
- 仓库：`github.com/xxx/ai-app-dev-roadmap`（含可运行 `verify_setup` 与演示脚本）

### 企业内部智能助手 Agent（个人项目）| 2026.02

*技术栈：LangGraph、FastAPI、Chroma、Gradio*

- 按 HR/财务/IT 分部门构建知识库，实现 ReAct Agent 多工具协作（检索、请假 Mock、工单 Mock）
- 设计审计日志记录用户问答与路由路径，支持 Gradio 管理界面演示
- 无 API Key 时降级为离线 RAG 片段模式，保证 Demo 可复现

---

## 工作经历

### XX 公司 | Android 开发工程师 | 20XX – 20XX

- 负责 XX App 核心模块开发与性能优化（可写具体指标）
- 具备客户端架构、网络层封装、本地存储经验，为转型 AI 应用开发打下基础

---

## 教育背景

- XX 大学 | 本科 | 计算机相关专业 | 20XX

---

## 自我评价（可选，控制在 3 行内）

有 X 年 Android 开发经验，系统完成 AI 应用开发学习路线（RAG、Agent、端云协同），具备从原型到可演示项目的全流程能力。
