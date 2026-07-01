"""Step 2: Structured JSON output chat demo."""

import gradio as gr

from llm_utils import get_llm

STRUCTURED_PROMPT = """Please answer the user's question strictly in JSON format with the following structure:
{{"answer": "Your detailed answer", "confidence": "high/medium/low"}}

User question: {message}"""


def chat(message: str, history: list) -> str:
    response = get_llm().invoke(STRUCTURED_PROMPT.format(message=message))
    return response.content


demo = gr.ChatInterface(
    fn=chat,
    type="messages",
    title="DeepSeek Structured Chat Demo",
    description="模型会尽量按 JSON 格式返回答案。",
    examples=["什么是 Prompt 工程？", "用一句话解释 RAG"],
)

if __name__ == "__main__":
    demo.launch()
