# 第1周：Python 基础 + Prompt 工程 + DeepSeek API 实践

## 学习目标

本周将帮助你：
- 快速掌握 Python 异步编程、类型注解等基础知识
- 学会 Prompt 工程核心技巧（CoT、结构化输出、function calling）
- 能够使用 DeepSeek API 实现简单的 LLM 聊天应用
- 了解基本的 API 调用封装思路
- 初步建立错误处理和代码组织能力

## 本周资源

- Datawhale 《动手学大模型应用开发》 Task 1-2
- B站黑马程序员《2026 大模型应用开发》前 10 集
- DeepSeek 官方文档

---

## 详细操作步骤

### Step 1: 搭建 Python 虚拟环境并获取 DeepSeek API Key

** 目标 **：创建独立的学习环境，避免与其他项目冲突。

1. 打开终端，执行以下命令创建并激活环境：
```bash
conda create -n llm-dev python=3.10 -y
conda activate llm-dev
```

   - 成功后终端前面会显示 `(llm-dev)`。

2. 安装本周必要的基础库：
```bash
pip install python-dotenv gradio langchain-openai
```

3. 注册 DeepSeek API Key：
   - 访问 https://platform.deepseek.com/api_keys
   - 登录并点击创建新的 API Key
   - 复制 Key（以 `sk-` 开头）

4. 在本地新建文件夹 `ai-learning`（建议放在 Desktop 或 Documents）。

5. 在该文件夹中新建一个名为 `.env` 的文件（注意前面有一个点），用文本编辑器打开并粘贴以下内容：
```env
DEEPSEEK_API_KEY=sk-你的DeepSeek API Key
```
   - 保存文件。

** 验证 **：在终端中输入 `echo $DEEPSEEK_API_KEY` （Mac/Linux）或 `echo %DEEPSEEK_API_KEY%` （Windows），能看到 key 即为成功。

---

### Step 2: 创建并运行第一个结构化输出聊天脚本

** 目标 **：验证 API 调用是否正常，并实现简单的结构化输出功能。

1. 在 `ai-learning` 文件夹中新建一个 Python 文件 `test_chat.py`，粘贴以下代码：
```python
import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
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

2. 在终端中运行：
```bash
python test_chat.py
```

3. 浏览器会自动打开一个网页界面。
   - 输入任意问题测试
   - 观察输出是否为 JSON 格式

** 常见问题解决 **：
- API Key 错误：检查 `.env` 文件是否正确保存
- 模型不存在：确认使用 `"deepseek-chat"`

---

### Step 3: Prompt 技巧实践（结构化输出与 CoT）

** 目标 **：深入理解并实践 Prompt 工程中最常用的两种技巧，能够自己设计有效的 Prompt。

** 详细操作 **：

1. **基础结构化输出练习**
   - 打开 `test_chat.py`
   - 将 `prompt` 替换为下面这个模板，测试不同问题：
```python
prompt = f"""You are a helpful assistant. Please answer the user's question in the following strict JSON format:
{{"answer": "concise and accurate answer", "reasoning": "brief reasoning", "confidence": "high/medium/low"}}

User question: {message}"""
```
   - 测试问题示例：
     - “说一下你的优点”
     - “如何学习 Python?”
     - “今天天气如何？”

2. **CoT 思维链练习**
   - 在 prompt 中添加“Let’s think step by step.”
   - 尝试两种版本对比：
     - 版本A：直接要求回答
     - 版本B：先让模型思考再回答
   - 观察哪种版本的结构化输出更准确。

3. **自己设计 Prompt 练习**
   - 设计一个让模型输出代码例子的 Prompt
   - 设计一个让模型进行简单分类的 Prompt

** 建议 **：每个 Prompt 至少测试 3 个不同问题，并在注释中记录你发现的差异。

---

### Step 4: 封装简单的 LLM 调用函数

** 目标 **：学会基本的代码封装思路，为后续 FastAPI 做准备，并添加基本错误处理。

** 详细操作 **：

1. 在 `ai-learning` 文件夹中新建一个文件 `llm_utils.py`，粘贴以下代码：
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    return ChatOpenAI(
        model="deepseek-chat",
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

2. 修改 `test_chat.py`，引入并使用上面的函数：
```python
from llm_utils import call_llm

def chat(message, history):
    prompt = f"""Please answer in JSON format... User question: {message}"""
    return call_llm(prompt)
```

3. 测试错误处理：
   - 故意输入错误的 API Key 测试异常捕获
   - 观察错误信息是否友好

** 扩展练习 **：
- 添加流式输出支持
- 添加重试机制

---

### Step 5: 完整的简单应用封装（扩展）

** 目标 **：将以上所学集成为一个可复用的模块。

1. 创建 `app.py`，集成以上所有功能。
2. 添加基本的对话历史记录功能。
3. 测试完整流程并记录结果。

---

## 本周完成后将掌握的内容

完成第1周后，你将能够：

- 独立创建和管理 Python 虚拟环境
- 正确调用 DeepSeek API 并处理 API Key
- 使用 Gradio 快速构建简单的聊天界面
- 掌握 Prompt 工程的基本方法（结构化输出、CoT）
- 初步封装 LLM 调用逻辑
- 了解 API 调用中常见的错误处理方式
- 具备基本的代码组织和模块化能力

---

** 说明 **：
本文档会随着学习进度持续更新。
每完成一个 Step 后，建议在本文件末尾添加自己的心得或问题解决记录。
