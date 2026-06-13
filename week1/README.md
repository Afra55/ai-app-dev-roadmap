# 第1周：Python 基础 + Prompt 工程 + DeepSeek API 实践

## 学习目标

完成本周学习后，你将能够：

- 快速掌握 Python 异步编程和类型注解
- 掌握 Prompt 工程核心技巧（CoT、结构化输出、function calling）
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

### Step 3: Prompt 技巧实践（结构化输出与 CoT）

** 目标 **：深入理解并实践 Prompt 工程中最重要的两种技巧。

### 1. 结构化输出练习

将 prompt 替换为以下模板，测试不同问题：

```python
prompt = f"""You are a helpful assistant. Please answer the user's question in the following strict JSON format:
{{"answer": "concise and accurate answer", "reasoning": "brief reasoning", "confidence": "high/medium/low"}}

User question: {message}"""
```

** 测试题目建议 **：
- “说一下你的优点”
- “如何有效学习 Python?”
- “一个人如何提升写作能力？”

### 2. Chain-of-Thought (CoT) 思维链练习（重点）

** 为什义你加了“一步一步思考”结果没变？**

很多时候直接加 `Let’s think step by step` 对简单问题效果不明显，因为：
- 模型本身已绌很强（特别是 deepseek-v4-flash）
- 任务太简单，模型不需要明显的 CoT 也能答好

** 正确的 CoT 练习方式 **：

1. **使用更复杂的问题**
   选择需要多步推理的问题，例如：
   - “一个人月薪 8000 元，每月花费3000元，剩下的钱用来投资，假设每年投资收益 12%，5 年后他能有多少钱？”
   - “有 3 个盒子，第一个盒子里有 2 个球，第二个盒子里有 3 个球，第三个盒子里有 4 个球。从每个盒子里各取出 1 个球，剩下多少个球？”

2. **在 JSON 中输出思考过程**
   修改 prompt ，让模型在 `reasoning` 字段里写出思考过程：

```python
prompt = f"""You are a helpful assistant. Please answer the user's question in the following strict JSON format. Think step by step before giving the final answer.
{{"answer": "final answer", "reasoning": "detailed step-by-step reasoning", "confidence": "high/medium/low"}}

User question: {message}"""
```

3. **对比实验**
   - 版本 A：不加 CoT，直接要求回答
   - 版本 B：加上 `Think step by step before giving the final answer`
   - 用同一个复杂问题测试两个版本，对比 `reasoning` 字段的质量和 `answer` 的准确性。

** 建议 **：CoT 在简单问题上效果并不明显，但在需要逻辑推理、计算、多步解决的问题上效果很明显。

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
- 依然能体现 Tool Use 的核心思想：模型自动判断需要工具 → 执行工具 → 把结果反馈给模型

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
- 掌揣 Prompt 工程核心技巧
- 初步封装 LLM 调用逻辑
- 处理 API 调用中的常见错误
- 具备基本的代码组练和模块化能力
- 初步了解 Tool Use 的基本概念和流程

---

** 说明 **：
本文档会随着学习进度持续更新。
每完成一个 Step 后，建议在本文件末尾添加自己的心得和笔记。
