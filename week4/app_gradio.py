"""Gradio UI for Week 4 edge-cloud orchestration."""

from __future__ import annotations

import gradio as gr

from agent import EdgeCloudOrchestrator, preview_route

orchestrator = EdgeCloudOrchestrator(local_backend="mock")


def respond(message: str, history: list) -> str:
    if not message.strip():
        return "请输入有效问题。"

    decision = preview_route(message)
    try:
        result = orchestrator.run(message)
    except Exception as exc:
        return f"路由: {decision.route}\n错误: {exc}"

    return (
        f"**路由**: {result.route}\n\n"
        f"**原因**: {result.reason}\n\n"
        f"**后端**: {result.backend}\n\n"
        f"**回答**:\n{result.answer}"
    )


with gr.Blocks(title="Week 4 端云协同 Agent") as demo:
    gr.Markdown(
        "# Week 4 端云协同 + LangGraph Agent\n"
        "- 简单问候 → 端侧 Mock 模型\n"
        "- 复杂推理 → 云端 DeepSeek\n"
        "- 工具任务 → LangGraph ReAct Agent（知识库/天气/计算）"
    )
    gr.ChatInterface(
        fn=respond,
        type="messages",
        title="端云协同助手",
        examples=[
            "你好",
            "什么是 RAG？",
            "北京现在天气怎么样？",
            "计算 (12 + 8) * 2",
        ],
    )

if __name__ == "__main__":
    demo.launch()
