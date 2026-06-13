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

** 目标 **：验证 API 调用正常，并实现结构化输出功能。

### 代码解释（重要）

这段代码做以下几件事：

1. **加载环境变量** (`load_dotenv()`)：从 `.env` 文件中读取 `DEEPSEEK_API_KEY`。
2. **创建 LLM 客户端** (`ChatOpenAI`)：使用 LangChain 封装的客户端调用 DeepSeek API。
3. **Gradio 创建网页界面** (`gr.ChatInterface`)：快速生成一个简单的聊天 Web UI。
4. **强制 JSON 输出** (在 Prompt 中)：通过 Prompt 让模型回答时严格按照 JSON 格式输出。

** 为什么会出现网页？**

`demo.launch()` 会启动一个简易的 Web 服务器，并自动打开浏览器。这是 Gradio 提供的功能，用来快速测试聊天应用。

** 为什么返回的是 JSON？**

我们在 `prompt` 里面明确要求了模型严格按照 JSON 格式回答。这是 Prompt 工程的一种常见技巧，叫做 **Structured Output**。

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

3. 浏览器会自动打开界面。输入问题测试，观察输出是否为有效 JSON 格式。

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

** 为什么你加了“一步一步思考”结果没变？**

很多斶候直接加 `Let’s think step by step` 对简单问题效果不明显，因为：
- 模型本身已经很强（特别是 deepseek-v4-flash）
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

### Step 5: 集成完整简单应用

** 目标 **：将前面所学内容集成到一个可复用的模块中。

1. 创建 `app.py` 集成所有功能。
2. 添加基本对话历史记录。
3. 测试完整流程并记录结果。

---

## 本周完成后将掌揣的内容

完成第1周后，你将能够：

- 独立创建和管理 Python 虚拟环境
- 正确调用 DeepSeek API 并管理 API Key
- 使用 Gradio 快速构建简单聊天界面
- 掌握 Prompt 工程核心技巧
- 初步封装 LLM 调用逻辑
- 处理 API 调用中的常见错误
- 具备基本的代码组练和模块化能力

---

** 说明 **：
本文档会随着学习进度持续更新。
每完成一个 Step 后，建议在本文件末尾添加自己的心得和笔记。
