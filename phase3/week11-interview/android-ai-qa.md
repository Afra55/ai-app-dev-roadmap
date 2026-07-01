# Android + AI 面试题

结合 `week3/android-app`、`projects/direction-a`、`projects/direction-b`。

---

## 架构与安全

### 1. API Key 应该放在哪里？

**答**：**仅后端**。Android 通过 HTTPS 调自己的 FastAPI；客户端不含 `sk-` 密钥。若必须直连第三方，应用端用短期 Token + 后端代理。

**项目**：Direction A/B 均为后端持有 Key。

---

### 2. 模拟器如何访问本机后端？

**答**：Android 模拟器用 `10.0.2.2` 映射宿主机 `localhost`。本仓库 Direction A：`http://10.0.2.2:8010/`（`BuildConfig.API_BASE_URL`）。

---

### 3. 银行场景如何做输入脱敏？

**答**：日志与上报前对手机号、身份证等正则替换。不在客户端日志打印完整用户输入。

**项目**：`direction-b/backend/security.py` — `mask_sensitive_text`。

---

### 4. 弱网或后端不可用怎么办？

**答**：Retrofit 捕获异常，展示友好提示；可缓存最近 FAQ；端侧 Mock 处理极简交互。

**项目**：`NotesRepository` / `BankChatViewModel` 的 try-catch。

---

## Android 工程

### 5. 为什么用 ViewModel + Compose？

**答**：配置变更存活、状态与 UI 分离、便于测试。聊天/笔记列表状态放 ViewModel。

---

### 6. Retrofit 在本项目中的角色？

**答**：声明式 API（`NotesApi`、`BankApi`）， Gson 解析 JSON，协程 `suspend` 异步请求。

---

### 7. 端侧 AI 与云端 API 在 App 里如何共存？

**答**：简单 UI 可本地 `OnDeviceLLM`；知识库问答必须走后端 RAG；由产品策略决定，非所有请求都上云。

---

## 行为面（银行/Android 岗）

### 8. 为什么从 Android 转 AI 应用？

**参考答**：已有客户端工程与用户体验经验；端侧 AI 是差异化优势；系统学习 RAG/Agent 后能把移动端与 AI 能力结合。

### 9. 如何保证金融场景合规？（教学项目）

**参考答**：虚构数据、Key 不进客户端、脱敏、审计日志（Direction C）、README 明确演示性质。

---

## 自测题

1. 说明 Direction A App 从点击「提问」到显示答案的调用链。
2. 若面试官质疑「包体太大」如何放模型？→ 量化、按需下载、仅端侧小模型。
