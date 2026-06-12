# 第1周：Python 基础 + Prompt 工程 + DeepSeek API 实践

## 学习目标

本周将帮助你：
- 快速掌握 Python 异步编程、类型注解等基础知识
- 学会 Prompt 工程核心技巧（CoT、结构化输出、function calling）
- 能够使用 DeepSeek API 实现简单的 LLM 聊天应用
- 了解基本的 API 调用封装思路

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

** 目标 **：掌握 CoT 和结构化输出的实际应用。

1. 修改 `test_chat.py` 中的 `prompt` 部分，尝试不同的 Prompt 模板：
   - 添加角色设定（You are a helpful assistant...)
   - 使用 CoT：“Let’s think step by step...”

2. 重新运行脚本并测试不同 Prompt 的效果差异。

** 建议练习 **：
- 让模型输出 JSON
- 让模型先思考再回答

---

### Step 4: 封装简单的 LLM 调用函数

** 目标 **：学会基本的 API 封装思路，为后续 FastAPI 做准备。

1. 创建新文件 `llm_utils.py`，封装一个简单的调用函数。
2. 将其引入到 `test_chat.py` 中使用。

---

## 本周完成后将掌握的内容

完成第1周后，你将能够：

- 独立创建和管理 Python 虚拟环境
- 正确调用 DeepSeek API 并处理 API Key
- 使用 Gradio 快速构建简单的聊天界面
- 掌握 Prompt 工程的基本方法（结构化输出、CoT）
- 初步封装 LLM 调用逻辑
- 了解 API 调用中常见的错误处理方式

---

** 说明 **：
本文档会随着学习进度持续更新。
每完成一个 Step 后，建议在本文件末尾添加自己的心得或问题解决记录。
