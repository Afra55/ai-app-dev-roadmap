"""Step 5: Full chat app with conversation history."""

from __future__ import annotations

import gradio as gr

from llm_utils import call_llm

SYSTEM_PROMPT = """You are a helpful and friendly AI assistant.
Always answer in Chinese unless the user asks in another language.
Be concise but informative."""


def _format_history(history: list | None) -> str:
    """Convert Gradio history into plain text for the prompt."""
    if not history:
        return ""

    lines: list[str] = []
    for turn in history:
        if isinstance(turn, dict):
            role = turn.get("role")
            content = turn.get("content", "")
            if role == "user":
                lines.append(f"User: {content}")
            elif role == "assistant":
                lines.append(f"Assistant: {content}")
            continue

        if isinstance(turn, (list, tuple)):
            if len(turn) >= 2:
                user_msg, assistant_msg = turn[0], turn[1]
                if user_msg:
                    lines.append(f"User: {user_msg}")
                if assistant_msg:
                    lines.append(f"Assistant: {assistant_msg}")
            elif len(turn) == 1 and turn[0]:
                lines.append(f"User: {turn[0]}")

    if lines:
        return "\n".join(lines) + "\n\n"
    return ""


def chat(message: str, history: list | None) -> str:
    history_text = _format_history(history)
    full_prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"{history_text}"
        f"User: {message}\n"
        "Assistant:"
    )
    return call_llm(full_prompt)


with gr.Blocks(title="第1周完整聊天应用") as demo:
    gr.Markdown(
        "# 第1周完整聊天应用\n"
        "带对话历史记录的简单 AI 聊天应用。"
    )
    gr.ChatInterface(
        fn=chat,
        type="messages",
        title="AI 助手",
        description="支持多轮对话",
        examples=["你好", "今天天气怎么样？", "简单介绍一下自己"],
    )

if __name__ == "__main__":
    demo.launch()
