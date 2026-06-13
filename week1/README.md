# 第1周：Python 基础 + Prompt 工程 + DeepSeek API 实践

## 学习目标

完成本周学习后，你将能够：

- 快速掌握 Python 异步编程和类型注解
- 掌握 Prompt 工程的核心技巧和实际应用
- 使用 DeepSeek API 构建简单的 LLM 应用
- 初步封装 LLM 调用逻辑
- 处理 API 调用中的常见错误

## 本周资源

- Datawhale 《动手学大模型应用开发》 Task 1-2
- B站黑马程序员《2026 大模型应用开发》前 10 集
- DeepSeek 官方文档

---

## 详细步骤

### Step 1: 搭建 Python 虚拟环境并获取 DeepSeek API Key

** 目标 **：创建独立的学习环境，安全管理 API Key。

1. 打开终端，执行以下命令创建并激活环境：
```bash
conda create -n llm-dev python=3.10 -y
conda activate llm-dev
```

   成功后终端前面会显示 `(llm-dev)`。

2. 安装本周必要的库：
```bash
pip install python-dotenv gradio langchain-openai
```

3. 获取 DeepSeek API Key：
   - 访问 https://platform.deepseek.com/api_keys
   - 登录并创建新的 API Key
   - 复制 Key（以 `sk-` 开头）

4. 在本地新建文件夹 `ai-learning`（建议放在 Desktop 或 Documents）。

5. 在该文件夹中新建 `.env` 文件（文件名必须以点开头），用文本编辑器打开并粘贴以下内容：
```env
DEEPSEEK_API_KEY=sk-你的 DeepSeek API Key
```

   保存文件。

** 验证 `.env` 文件 **：

`.env` 文件不会自动加载到 shell 环境中，它是供 Python 程序通过 `python-dotenv` 读取的。

** 推荐验证方式 **：

- 查看文件内容：
  ```bash
  cat .env
  ```

- 用 Python 验证（最准确）：
  ```bash
  python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Key loaded:', bool(os.getenv('DEEPSEEK_API_KEY'))); print('Key prefix:', os.getenv('DEEPSEEK_API_KEY')[:8] if os.getenv('DEEPSEEK_API_KEY') else 'Not found')"
  ```

如果输出显示 `Key loaded: True`，则说明设置成功。

---

### Step 2: 创建并运行第一个结构化输出聊天应用

** 目标 **：验诉 API 调用正常，并实现结构化输出功能。

### 代码解释（重要）

这段代码做以下几件事：

1. **加载环境变量** (`load_dotenv()`)：从 `.env` 文件中读取 `DEEPSEEK_API_KEY`。
2. **创建 LLM 客户端** (`ChatOpenAI`)：使用 LangChain 封装的客户端调用 DeepSeek API。
3. **Gradio 创建网页界面** (`gr.ChatInterface`)：快速生成一个简单的聊天 Web UI。
4. **强制 JSON 输出** (在 Prompt 中)：通过 Prompt 让模型回答时严格按照 JSON 格式输出。

** 为什义返回的是 JSON？**

我们在 `prompt` 里面明确要求严格按照 JSON 格式回答。这是 Prompt 工程的一种常见技巧，叫做 **Structured Output**。

### 代码（已更新为 deepseek-v4-flash）

```python
import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0.7,
)

def chat(message, history):
    prompt = f"""Please answer the user's question strictly in JSON format with the following structure:
{{"answer": "Your detailed answer", "confidence": "high/medium/low"}}

User question: {message}"""
    
    response = llm.invoke(prompt)
    return response.content

demo = gr.ChatInterface(chat, title="DeepSeek Structured Chat Demo")
demo.launch()
```

2. 在终端运行：
```bash
python test_chat.py
```

3. 浏览器会自动打开界面。输入问题测试，观寏输出是否为有效 JSON 格式。

** 常见问题解决 **：
- API Key 错误：检查 `.env` 文件是否正确保存
- 模型不存在：确认使用 `"deepseek-v4-flash"`

---

### Step 3: Prompt 工程核心技巧实践

** 目标 **：理解 Prompt 工程的作用和价值，掌握实际工作中最常用、最有效的核心技巧。

### Prompt 工程是做什么的？

**Prompt Engineering（提示词工程）** 是指通过设计、优化、组合提示词（Prompt），使大模型输出更准确、更符合预期、更安全的技能。

简单来说，就是“** 教会 AI 怎么思考和回答 **”。

### Prompt 工程主要用来做什么？

| 目的               | 说明                                   | 常见场景               |
|-----------------------|---------------------------------------------|----------------------------------|
| 提升答案质量   | 减少错误、假象、偏差           | 问答、总结、分析     |
| 控制输出格式   | 让模型按固定格式输出（JSON等） | 结构化输出、Agent工具调用 |
| 让模型步骤推理 | 提升复杂任务的正确率           | 数学、逻辑、多步解决 |
| 控制风格和要求 | 让 AI 按指定角色、语气回答     | 客服、写作、教学等     |
| 减少幻觉           | 通过限制和验证减少编造内容     | 业务场景安全性要求   |

### 必须掌握的 Prompt 核心技巧（Week 1 重点）

#### 1. **角色设定（Role / Persona）**
给 AI 定义一个具体角色，能大大提升回答质量。

```text
You are a senior software architect with 15 years of experience in backend systems.
```

#### 2. **明确指令 + 限制（Clear Instructions + Constraints）**
要求越具体越好，并给出明确的限制条件。

```text
Please answer the question in Chinese. Keep the answer within 150 words. Do not mention that you are an AI.
```

#### 3. **思维链（Chain-of-Thought, CoT）**
让模型先思考再回答，对复杂问题效果显著。

```text
Think step by step before giving the final answer.
```

#### 4. **结构化输出（Structured Output）**
强制模型按 JSON、列表等固定格式输出，是做 Agent 和 RAG 的基础。

```text
Please respond strictly in the following JSON format:
{"answer": "...", "confidence": "high/medium/low"}
```

#### 5. **示例引导（Few-shot Prompting）**
给出 1~3 个示例，让模型模仿格式和逻辑。

#### 6. **分隔符与格式化**
使用 ``` 、""" 、<task> 等分隔符，让模型更容易区分不同部分。

### Prompt 必须用英文吗？

**不一定必须用英文**。

- 现在的主流模型（DeepSeek、Qwen、GPT-4o 等）对中文的理解和生成能力已经很强。
- 用中文写 Prompt 完全可以，特别是做业务场景时更方便。
- 但是，英文 Prompt 在以下情况下更有优势：
  - 需要更精准的控制和复杂推理时
  - 使用最新的技术技巧（很多研究是英文）
  - 做国际项目或与外国模型交互时

** 建议 **：
- 日常使用中文 Prompt 就可以
- 重要任务或需要高质量输出时，尝试用英文 Prompt
- 最理想状态是两者都能掌握

### Step 3 实践建议

1. 每次写 Prompt 都尝试加上 **角色 + 明确指令 + CoT + 结构化输出**
2. 多做 A/B 对比实验（加 CoT vs 不加 CoT）
3. 把好的 Prompt 保存起来，形成自己的 Prompt 库

---

### Step 4: 封装 LLM 调用函数

** 目标 **：学会基本的代码封装思路，并添加错误处理。

** 详细操作 **：

1. 新建 `llm_utils.py`，粘贴以下代码：
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    return ChatOpenAI(
        model="deepseek-v4-flash",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
        temperature=0.7,
    )

def call_llm(prompt: str) -> str:
    llm = get_llm()
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"
```

2. 修改 `test_chat.py` 引入并使用该函数。

3. 测试错误处理：故意输入错误 Key 观察错误信息。

---

### Step 5: 集成完整简单应用（带对话历史记录）

** 目标 **：将前面所学内容集成到一个完整的可复用应用中，并添加对话历史记录功能。

** Step 5 详细实施步骤 **：

1. **创建 `app.py` 文件**
2. **引入之前的 `llm_utils.py`**
3. **使用 Gradio 支持对话历史**
4. **添加系统提示词**
5. **测试完整功能**

### 完整示例代码（带详细注释 + 兼容新版 Gradio）

```python
# app.py - 第1周最终集成应用

import os                                   # 导入 os 模块，用于读取环境变量
from dotenv import load_dotenv             # 导入 dotenv，用于加载 .env 文件
import gradio as gr                         # 导入 Gradio，用于快速构建 Web 界面
from llm_utils import call_llm             # 导入我们自己封装的 LLM 调用函数

# 加载 .env 文件中的环境变量（包含 API Key）
load_dotenv()

# 定义系统提示词（让模型知道自己的角色）
SYSTEM_PROMPT = """You are a helpful and friendly AI assistant. 
Always answer in Chinese unless the user asks in another language.
Be concise but informative."""

# 主聊天函数
def chat(message, history):
    """
    用户发送消息时调用的主函数
    
    Args:
        message: 用户当前输入的消息
        history: Gradio 自动传入的对话历史
    
    Returns:
        模型的回答
    """
    
    # 1. 构建完整的 Prompt，包含系统提示词和历史对话
    full_prompt = SYSTEM_PROMPT + "\n\n"
    
    # 2. 安全处理 history（兼容新版 Gradio）
    if history:
        for turn in history:
            if isinstance(turn, (list, tuple)):
                if len(turn) >= 2:
                    user_msg = turn[0]
                    assistant_msg = turn[1]
                    full_prompt += f"User: {user_msg}\nAssistant: {assistant_msg}\n\n"
                elif len(turn) == 1:
                    full_prompt += f"User: {turn[0]}\n\n"
    
    # 3. 添加当前用户问题
    full_prompt += f"User: {message}\nAssistant:"
    
    # 4. 调用 LLM 获取回答
    response = call_llm(full_prompt)
    
    # 5. 返回模型的回答
    return response

# 创建 Gradio 界面
with gr.Blocks(title="第1周完整聊天应用") as demo:
    gr.Markdown("# 第1周完整聊天应用\n带对话历史记录的简单 AI 聊天应用")
    
    # 创建聊天组件
    chatbot = gr.ChatInterface(
        fn=chat,                           # 使用上面定义的 chat 函数
        title="AI 助手", 
        description="支持多轮对话",
        examples=["你好", "今天天气怎么样？", "简单介绍一下自己"]
    )

# 启动应用
demo.launch()
```

### 代码重点解释：

- `history` 参数：Gradio 会自动传入之前的对话历史
- **兼容处理**：新版 Gradio 中 `history` 可能是 tuple 或 list，元素数量可能不是固定 2 个，所以采用 `if len(turn) >= 2` 进行安全解包
- `SYSTEM_PROMPT`：系统提示词，用来控制模型的行为风格
- `gr.ChatInterface`：Gradio 提供的高级聊天组件，自动支持历史记录和显示

** 建议 **：
- 先运行以上代码，体验对话历史功能
- 尝试多轮对话，观寏模型是否能记住之前的内容
- 可以尝试修改 `SYSTEM_PROMPT` 来改变 AI 的回答风格

---

### Step 6: 简单工具调用（Tool Use / Function Calling）入门

** 目标 **：让模型能够主加调用外部工具（以查询天气为例），体验 Tool Use 的基本流程。

** 重要说明 **：

这个 Step **只是一个非常简化的入门示例**，目的是让你理解 Tool Use（工具调用）的基本概念和流程。

- 后面几周（特别是 Agent 部分）我们会系统学习如何设计工具、处理并行调用、多工具协作、错误处理等更高级的内容。
- 当前版本仅做演示，实际生产环境还需要更多工程化处理。

### 为什么需要 Tool Use？

当用户问“今天北京天气怎么样？”时，模型本身没有实时数据。它需要一个**工具**去获取信息，然后再基于工具返回的结果生成回答。

Tool Use 的核心流程是：
1. 模型判断需要调用工具
2. 输出工具调用请求（Tool Call）
3. 我们执行工具并获取结果
4. 把工具结果返回给模型
5. 模型基于工具结果生成最终回答

### Step 6 实现思路

我们将实现一个简单的“查天气”工具，并让模型能够自动调用它。

**实现步骤**：

1. **定义工具函数**（使用 `wttr.in` 免费接口，无需 API Key）
2. **使用 LangChain 的 `@tool` 装饰器**
3. **绑定工具到 LLM**
4. **处理工具调用并返回结果**

### 完整示例代码 (app_with_tool.py) - 已修复版

```python
# app_with_tool.py - Step 6 最终修复版（推荐）

import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests

load_dotenv()

# 1. 定义工具
@tool
def get_weather(city: str) -> str:
    """Query current weather information for a specified city."""
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        return f"{city} 当前天气：{response.text}" if response.status_code == 200 else f"无法获取 {city} 的天气信息"
    except Exception as e:
        return f"查询天气时出错：{str(e)}"

# 2. 初始化模型并绑定工具
llm = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0.7,
).bind_tools([get_weather])


def chat_with_tool(message: str, history: list):
    # 第一次调用，让模型判断是否需要使用工具
    response = llm.invoke(message)

    # 如果模型决定调用工具
    if response.tool_calls:
        tool_call = response.tool_calls[0]
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        if tool_name == "get_weather":
            tool_result = get_weather.invoke(tool_args)

            # 重新构造 Prompt，把工具结果告诉模型
            final_prompt = f"""User question: {message}

Tool result: {tool_result}

Please give the final answer based on the tool result."""

            final_response = llm.invoke(final_prompt)
            return final_response.content

    return response.content


# 创建界面
with gr.Blocks(title="Step 6: Tool Use 示例") as demo:
    gr.Markdown("# Step 6: 简单 Tool Use 示例\n模型可以自动调用工具查询天气")

    chatbot = gr.ChatInterface(
        fn=chat_with_tool,
        title="AI 助手（可查天气）",
        examples=["北京现在天气怎么样？", "上海今天会下雨吗？"]
    )

# 启动
demo.launch()
```

### 代码重点解释

- 这个版本更稳定、更容易理解
- 避免了复杂的消息历史管理
- 依然能体现 Tool Use 的核心思想：模型自动判断需要工具 → 执行工具 → 把结果反馈结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果结果

** 这个版本的限制 **：
- 工具调用逻辑是简化的
- 没有完整的多轮对话历史支持

这些高级功能会在后面几周的 Agent 学习中详细讳解。

---

## 本周完成后将掌握的内容

完成第1周后，你将能够：

- 独立创建和管理 Python 虚拟环境
- 正确调用 DeepSeek API 并管理 API Key
- 使用 Gradio 快速构建简单聊天界面
- 掌揣 Prompt 工程的核心技巧
- 初步封装 LLM 调用逻辑
- 处理 API 调用中的常见错误
- 具备基本的代码组练和模块化能力
- 初步了解 Tool Use 的基本概念和流程

---

** 说明 **：
本文档会随着学习进度持续更新。
每完成一个 Step 后，廚议在本文件末尾添加自己的心得和笔记。
