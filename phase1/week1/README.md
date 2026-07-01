# 第1周：Python 基础 + Prompt 工程 + DeepSeek API 实践

← [路线图](../../README.md) · [第一阶段](../README.md) · **Week 1**

## 学习目标

完成本周学习后，你将能够：

- 快速掌握 Python 虚拟环境与依赖管理
- 掌握 Prompt 工程的核心技巧和实际应用
- 使用 DeepSeek API 构建简单的 LLM 应用
- 封装 LLM 调用逻辑并处理常见错误
- 初步了解 Tool Use（工具调用）的基本流程

## 本周资源

- [Datawhale《动手学大模型应用开发》](https://github.com/datawhalechina/llm-universe)
- B站黑马程序员《2026 大模型应用开发》前 10 集
- [DeepSeek 官方 API 文档](https://api-docs.deepseek.com/)

---

## 快速开始（推荐）

本目录已包含可直接运行的示例代码：

```text
week1/
├── .env.example          # API Key 配置模板
├── requirements.txt      # Python 依赖
├── llm_utils.py          # 共享 LLM 封装（Step 4）
├── demo_chat.py          # 结构化输出聊天（Step 2，原 test_chat.py）
├── app.py                # 带历史记录的完整应用（Step 5）
├── app_with_tool.py      # Tool Use 入门（Step 6）
└── verify_setup.py       # 本地环境检查脚本
```

### 1. 进入目录并安装依赖

```bash
cd phase1/week1
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

> 如果你使用 conda，也可以执行：
>
> ```bash
> conda create -n llm-dev python=3.10 -y
> conda activate llm-dev
> pip install -r requirements.txt
> ```

### 2. 配置 API Key

```bash
cp .env.example .env
```

编辑 `.env`，填入你的 DeepSeek API Key（以 `sk-` 开头）：

```env
DEEPSEEK_API_KEY=sk-你的DeepSeekAPIKey
```

获取地址：https://platform.deepseek.com/api_keys

> **安全提示**：`.env` 已被 `.gitignore` 忽略，请勿将 API Key 提交到 Git 仓库。

### 3. 运行环境检查

```bash
python verify_setup.py
```

看到「依赖检查通过，已检测到 DEEPSEEK_API_KEY」即可继续。

### 4. 按步骤运行示例

```bash
python demo_chat.py        # Step 2
python app.py              # Step 5
python app_with_tool.py    # Step 6
```

浏览器会自动打开 Gradio 界面。若端口被占用，可在代码中将 `demo.launch()` 改为 `demo.launch(server_port=7861)`。

### 模型说明

本仓库默认使用官方推荐的 **`deepseek-v4-flash`**（见 [DeepSeek API 文档](https://api-docs.deepseek.com/)）。

- 旧别名 `deepseek-chat` / `deepseek-reasoner` 将于 **2026-07-24** 停用，请勿在新代码中使用。
- 如需更强推理能力，可在 `llm_utils.py` 中将 `DEFAULT_MODEL` 改为 `deepseek-v4-pro`。

---

## 详细步骤

### Step 1: 搭建 Python 虚拟环境并获取 DeepSeek API Key

**目标**：创建独立的学习环境，安全管理 API Key。

请直接按照上方「快速开始」完成环境搭建。完成后用以下命令验证 `.env` 是否生效：

```bash
python -c "from llm_utils import _get_api_key; print('Key prefix:', _get_api_key()[:8])"
```

若输出 `Key prefix: sk-xxxxx`，说明配置成功。

---

### Step 2: 创建并运行第一个结构化输出聊天应用

**目标**：验证 API 调用正常，并实现结构化输出功能。

**运行**：

```bash
python demo_chat.py
```

**代码说明**（`demo_chat.py`）：

1. 通过 `llm_utils.get_llm()` 创建 DeepSeek 客户端
2. 在 Prompt 中要求模型严格返回 JSON
3. 使用 Gradio `ChatInterface` 快速生成 Web 聊天界面

**为什么返回 JSON？**

这是 Prompt 工程中的 **Structured Output（结构化输出）** 技巧。固定输出格式后，程序更容易解析模型结果，也是后续 RAG 和 Agent 的基础。

**核心代码片段**：

```python
from llm_utils import get_llm

llm = get_llm()
prompt = """Please answer strictly in JSON:
{"answer": "...", "confidence": "high/medium/low"}
User question: ..."""
response = llm.invoke(prompt)
```

---

### Step 3: Prompt 工程核心技巧实践

**目标**：理解 Prompt 工程的作用，掌握实际工作中最常用的核心技巧。

#### Prompt 工程是做什么的？

**Prompt Engineering（提示词工程）** 是通过设计、优化提示词，使大模型输出更准确、更符合预期、更安全的技能。简单说，就是「教会 AI 怎么思考和回答」。

#### 主要用途

| 目的 | 说明 | 常见场景 |
|------|------|----------|
| 提升答案质量 | 减少错误、幻觉、偏差 | 问答、总结、分析 |
| 控制输出格式 | 让模型按固定格式输出 | 结构化输出、Agent 工具调用 |
| 步骤推理 | 提升复杂任务正确率 | 数学、逻辑、多步问题 |
| 控制风格 | 指定角色、语气 | 客服、写作、教学 |
| 减少幻觉 | 通过限制和验证减少编造 | 业务安全场景 |

#### Week 1 必须掌握的 6 个技巧

1. **角色设定（Role / Persona）**
   ```text
   You are a senior software architect with 15 years of experience.
   ```

2. **明确指令 + 限制（Clear Instructions + Constraints）**
   ```text
   Please answer in Chinese. Keep the answer within 150 words.
   ```

3. **思维链（Chain-of-Thought, CoT）**
   ```text
   Think step by step before giving the final answer.
   ```

4. **结构化输出（Structured Output）**
   ```text
   Respond strictly in JSON: {"answer": "...", "confidence": "high/medium/low"}
   ```

5. **示例引导（Few-shot Prompting）**：给出 1~3 个示例让模型模仿

6. **分隔符与格式化**：使用 `"""`、`<task>` 等分隔不同部分

#### Prompt 必须用英文吗？

不一定。DeepSeek、Qwen 等模型中文能力很强，业务场景用中文完全可行。英文在复杂推理、最新研究技巧、国际项目中有时更精准。建议两者都能掌握。

#### Step 3 实践建议

1. 每次写 Prompt 尝试组合：**角色 + 明确指令 + CoT + 结构化输出**
2. 做 A/B 对比（加 CoT vs 不加 CoT）
3. 把效果好的 Prompt 保存成自己的 Prompt 库

---

### Step 4: 封装 LLM 调用函数

**目标**：学会代码封装思路，并添加错误处理。

本步骤对应 `llm_utils.py`，所有示例脚本都复用该模块：

```python
from llm_utils import get_llm, call_llm

# 方式一：直接获取客户端
llm = get_llm()
response = llm.invoke("你好")

# 方式二：封装好的调用函数（含错误处理）
answer = call_llm("你好")
```

**设计要点**：

- API Key 从 `.env` 读取，不硬编码
- `get_llm()` 统一模型名、`base_url`、`temperature`
- `call_llm()` 捕获异常并返回可读错误信息

**自测**：故意把 `.env` 中的 Key 改错，运行 `python -c "from llm_utils import call_llm; print(call_llm('hi'))"`，应看到 `Error: ...` 而非程序崩溃。

---

### Step 5: 集成完整简单应用（带对话历史记录）

**目标**：将前面所学集成到完整可复用应用，并支持多轮对话。

**运行**：

```bash
python app.py
```

**代码说明**（`app.py`）：

- `SYSTEM_PROMPT`：控制系统提示词与回答风格
- `_format_history()`：兼容 Gradio 5 的 `messages` 格式历史记录
- `call_llm()`：统一调用入口

**建议练习**：

1. 多轮对话，观察模型是否记住上下文
2. 修改 `SYSTEM_PROMPT`，体验不同回答风格
3. 尝试加入 CoT 提示词，对比回答质量

---

### Step 6: 简单工具调用（Tool Use）入门

**目标**：让模型能够调用外部工具（以查询天气为例），理解 Tool Use 基本流程。

**运行**：

```bash
python app_with_tool.py
```

输入「北京现在天气怎么样？」测试工具调用。

> **说明**：这是简化的入门示例，用于理解「模型判断 → 调用工具 → 返回结果 → 生成回答」的流程。完整的 Agent 设计（多工具协作、错误重试、并行调用等）将在第 4 周用 LangGraph 系统学习。

#### 为什么需要 Tool Use？

模型本身没有实时数据。当用户问天气时，需要调用外部 API 获取信息，再基于结果生成回答。

#### 核心流程

1. 模型判断需要调用工具
2. 输出工具调用请求（Tool Call）
3. 执行工具并获取结果
4. 将工具结果返回给模型
5. 模型生成最终回答

#### 实现要点（`app_with_tool.py`）

- 使用 `@tool` 装饰器定义 `get_weather`（基于免费 `wttr.in` 接口，无需额外 API Key）
- 使用 `bind_tools()` 将工具绑定到 LLM
- 使用 LangChain 的 `HumanMessage` / `ToolMessage` 传递工具结果

**当前版本的限制**：

- 仅演示单工具、单轮工具调用
- 未覆盖完整多轮 Agent 状态管理

这些会在后续 Agent 章节深入学习。

---

## 本周验收清单

完成以下检查项，即表示第 1 周学习达标：

- [ ] 成功创建虚拟环境并安装 `requirements.txt` 中的依赖
- [ ] `python verify_setup.py` 通过，且能检测到 API Key
- [ ] `python demo_chat.py` 能打开页面并返回 JSON 风格回答
- [ ] 能解释 Prompt 工程中至少 4 种核心技巧
- [ ] `python app.py` 支持多轮对话且上下文连贯
- [ ] `python app_with_tool.py` 能正确查询城市天气
- [ ] 理解 `llm_utils.py` 的封装作用，能独立修改 `SYSTEM_PROMPT`

---

## 常见问题

### 1. `未找到 DEEPSEEK_API_KEY`

- 确认在 `phase1/week1/` 目录下创建了 `.env` 文件（不是 `.env.example`）
- 确认变量名为 `DEEPSEEK_API_KEY`，无多余空格或引号
- 在 `phase1/week1/` 目录内运行脚本，或依赖 `llm_utils.py` 自动从本目录加载 `.env`

### 2. 模型不存在 / 404

- 确认使用 `deepseek-v4-flash` 或 `deepseek-v4-pro`
- 查阅 [官方文档](https://api-docs.deepseek.com/) 获取最新模型列表

### 3. API Key 无效 / 401

- 检查 Key 是否完整复制（以 `sk-` 开头）
- 确认 DeepSeek 账户有余额且 Key 未过期

### 4. Gradio 页面打不开

- 检查终端是否有报错
- 尝试换端口：`demo.launch(server_port=7861)`
- 若在远程服务器上运行，使用：`demo.launch(server_name="0.0.0.0")`

### 5. 天气工具查询失败

- 检查网络是否能访问 `https://wttr.in`
- 尝试英文城市名，如 `Beijing` 而非「北京」（模型通常会自动转换）

### 6. `python3 -m venv` 报错 ensurepip

在 Ubuntu/Debian 上可安装：

```bash
sudo apt install python3-venv
```

或改用 conda 创建环境。

---

## 可选练习

1. 在 `demo_chat.py` 中加入 CoT 提示词，对比 JSON 输出质量
2. 给 `app.py` 增加「回答字数限制」或「专业术语解释模式」
3. 新增第二个工具（如获取当前时间），观察模型如何选择工具
4. 将 `DEFAULT_MODEL` 改为 `deepseek-v4-pro`，对比回答差异

---

## 本周完成后将掌握的内容

- 独立创建和管理 Python 虚拟环境
- 正确调用 DeepSeek API 并安全管理 API Key
- 使用 Gradio 快速构建聊天界面
- 掌握 Prompt 工程的核心技巧
- 封装 LLM 调用逻辑并处理常见错误
- 具备基本的代码组织和模块化能力
- 初步了解 Tool Use 的基本概念和流程

---

**说明**：建议每完成一个 Step 后，在本文件末尾记录自己的心得和笔记。

**最后更新**：2026 年 7 月
