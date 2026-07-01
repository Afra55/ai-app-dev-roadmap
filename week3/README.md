# 第3周：安卓端侧 AI（离线 Qwen2.5 聊天）

← [路线图](../README.md) · [第一阶段（第 1–4 周）](../week1-4/) · **Week 3**

## 学习目标

完成本周学习后，你将能够：

- 理解端侧 AI 的优势与适用场景
- 在 Python 中运行本地小模型（Qwen2.5-0.5B）或 Mock 端侧后端
- 搭建 Android 端侧聊天 App 骨架（Jetpack Compose）
- 设计 `OnDeviceLLM` 抽象，为接入 MLC LLM / LiteRT-LM 做准备
- 理解端侧与云端的能力边界

## 本周资源

- [Google AI Edge / LiteRT 文档](https://ai.google.dev/edge)
- [MLC LLM 文档](https://llm.mlc.ai/)
- [Qwen2.5 模型页](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)

---

## 快速开始（Python 端侧 Demo）

```text
week3/
├── requirements.txt
├── local_llm.py          # Mock / Qwen 本地推理
├── chat_local.py         # 命令行聊天
├── app_local.py          # Gradio 端侧聊天
├── verify_setup.py       # 环境检查
└── android-app/          # Android 工程骨架
```

### 1. 安装依赖

```bash
cd week3
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> `torch` 和 `transformers` 体积较大。若只想快速体验，可只安装 `gradio` 并使用默认 Mock 后端。

### 2. 运行检查

```bash
python verify_setup.py
```

### 3. 运行端侧聊天

```bash
# Mock 模式（无需下载模型，推荐先跑通）
python chat_local.py
python chat_local.py "你好"

# 真实 Qwen2.5 本地推理（首次会下载模型）
python chat_local.py --backend qwen "你好"

# Gradio 界面（默认 Mock）
python app_local.py
```

---

## 详细步骤

### Step 1: 理解端侧 AI

端侧 AI 的核心价值：

| 优势 | 说明 |
|------|------|
| 隐私 | 数据不出设备 |
| 低延迟 | 无网络往返 |
| 弱网可用 | 离线可响应 |
| 成本可控 | 减少 API 调用 |

适用场景：问候、简单指令、敏感数据预处理。  
不适合：大范围知识库检索、复杂推理（交给云端）。

---

### Step 2: Python 本地推理抽象

`local_llm.py` 提供两种后端：

| 后端 | 说明 |
|------|------|
| `mock` | 默认，无需 GPU/下载，适合学习与 CI |
| `qwen` | 真实 `Qwen2.5-0.5B-Instruct` CPU 推理 |

核心接口：

```python
from local_llm import get_local_llm

llm = get_local_llm("mock")
answer = llm.generate("你好")
```

---

### Step 3: 命令行与 Gradio 聊天

- `chat_local.py`：终端交互
- `app_local.py`：Web UI（默认 Mock）

---

### Step 4: Android 端侧 App 骨架

打开 Android Studio：

1. **Open** → 选择 `week3/android-app`
2. 等待 Gradle Sync 完成
3. 运行到模拟器或真机

工程结构：

```text
android-app/
└── app/src/main/java/com/ailearning/week3/
    ├── MainActivity.kt
    ├── llm/
    │   ├── OnDeviceLLM.kt       # 端侧模型接口
    │   └── MockOnDeviceLLM.kt     # 默认可运行实现
    └── ui/
        ├── ChatViewModel.kt
        └── ChatScreen.kt
```

当前默认使用 `MockOnDeviceLLM`，确保没有模型文件也能编译运行。

---

### Step 5: 接入真实 Qwen2.5（进阶）

在 Android 真机上集成真实离线模型，推荐路径：

1. **MLC LLM**：将 Qwen2.5 量化后打包进 App
2. **LiteRT-LM（Google AI Edge）**：面向 Android 的端侧推理方案

集成步骤（概览）：

1. 新建 `MlcOnDeviceLLM : OnDeviceLLM`
2. 将模型资产放入 `app/src/main/assets/` 或应用私有目录
3. 在 `MainActivity` 中替换 `MockOnDeviceLLM()`

```kotlin
// MainActivity.kt
val viewModel = ChatViewModel(MlcOnDeviceLLM(context))
```

> 模型文件通常 >500MB，不建议提交到 Git。请按官方文档下载到本地。

---

### Step 6: 端侧与云端边界

为第 4 周端云协同做准备，记住简单规则：

- **端侧**：问候、极短问答、隐私敏感输入
- **云端**：复杂推理、长文本生成
- **Agent+工具**：知识库检索、天气、计算等

---

## 本周验收清单

- [ ] `python verify_setup.py` 通过
- [ ] `python chat_local.py "你好"` 有端侧回复
- [ ] `python app_local.py` 可打开聊天界面
- [ ] Android 工程可在 Android Studio 成功 Sync
- [ ] App 可在模拟器发送消息并收到 Mock 回复
- [ ] 能解释 `OnDeviceLLM` 接口的作用
- [ ] 能说明端侧 AI 的优势与局限

---

## 常见问题

### 1. `torch` 安装慢或失败

先用 Mock 模式学习：`python chat_local.py --backend mock`

### 2. `--backend qwen` 首次很慢

需要下载 `Qwen2.5-0.5B-Instruct`（约 1GB），请耐心等待。

### 3. Android Studio Sync 失败

- 确认 JDK 17+
- 检查网络与 Gradle 仓库访问
- 使用 Android Studio 最新稳定版

### 4. 真机离线模型太大

优先在 Python 端验证流程，再按 MLC LLM 文档做 Android 集成。

---

## 与后续周次的衔接

| 周次 | 衔接点 |
|------|--------|
| 第 4 周 | 端侧 Mock 模型作为 `local` 路由后端 |
| 第 5-8 周 | 智能笔记 App 可复用 `OnDeviceLLM` 抽象 |

---

**最后更新**：2026 年 7 月
