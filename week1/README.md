# 第1周：Python速通 + Prompt + DeepSeek API

** 本周目标 **：
- 快速掌握Python基础（异步、类型注解）
- 学会Prompt技巧（结构化输出、CoT）
- 能用DeepSeek API实现简单聊天应用

** 本周资源 **：
- Datawhale 《动手学大模型应用开发》 Task 1-2
- B站黑马程序员 2026大模型应用开发视频

---

## 📥 每日详细步骤（持续更新）

### Day 1 （今天）

** 第一步：搭建Python环境 + 获取 DeepSeek API Key **

1. 打开终端，执行：
```bash
conda create -n llm-dev python=3.10 -y
conda activate llm-dev
```

2. 安装基础库：
```bash
pip install python-dotenv gradio langchain-openai
```

3. 去 https://platform.deepseek.com/api_keys 注册并获取 API Key（以 `sk-` 开头）

4. 在电脑新建文件夹 `ai-learning`，里面新建 `.env` 文件，内容：
```env
DEEPSEEK_API_KEY=sk-你的key
```

** 完成后请回复我“第一步完成了” **，我会继续给你第二步。

---

** 说明 **：
每完成一步我都会把详细内容补充到这个文件。
你可以在每日结束后自己在这里记录心得或报错解决方案。

** 下一步 **：等你完成第一步后回复我。
