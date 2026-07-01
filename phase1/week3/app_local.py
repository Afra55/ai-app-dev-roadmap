"""Gradio UI for Week 3 local on-device chat."""

from __future__ import annotations

import gradio as gr

from local_llm import get_local_llm

llm = get_local_llm("mock")


def chat(message: str, history: list) -> str:
    if not message.strip():
        return "请输入有效问题。"
    return llm.generate(message)


with gr.Blocks(title="Week 3 端侧聊天") as demo:
    gr.Markdown(
        "# Week 3 端侧聊天 Demo\n"
        "默认使用 Mock 端侧模型（无需下载）。"
        "真实 Qwen2.5 本地推理请使用 `python chat_local.py --backend qwen`。"
    )
    gr.ChatInterface(
        fn=chat,
        type="messages",
        title="端侧离线助手",
        examples=["你好", "什么是 RAG？", "端侧 AI 有什么优势？"],
    )

if __name__ == "__main__":
    demo.launch()
