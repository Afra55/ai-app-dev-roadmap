"""Gradio admin/demo UI for Direction C."""

from __future__ import annotations

import gradio as gr

from agent import EnterpriseAgentService
from audit import list_audit

service = EnterpriseAgentService()


def chat(user_id: str, question: str) -> str:
    if not question.strip():
        return "请输入问题。"
    result = service.run(user_id=user_id or "U10001", question=question)
    return f"**路由**: {result['route']}\n\n{result['answer']}"


def show_audit() -> str:
    rows = list_audit(10)
    if not rows:
        return "暂无审计日志。"
    lines = []
    for row in rows:
        lines.append(
            f"- [{row['created_at']}] {row['user_id']} | {row['route']} | {row['question']}"
        )
    return "\n".join(lines)


with gr.Blocks(title="Enterprise Agent Admin") as demo:
    gr.Markdown("# Direction C · 企业内部智能助手")
    user_id = gr.Textbox(label="用户 ID", value="U10001")
    question = gr.Textbox(label="问题", placeholder="例如：年假还剩几天？")
    answer = gr.Markdown()
    ask_btn = gr.Button("提问")
    audit_btn = gr.Button("查看审计日志")
    audit_box = gr.Markdown()

    ask_btn.click(chat, inputs=[user_id, question], outputs=answer)
    audit_btn.click(show_audit, outputs=audit_box)

if __name__ == "__main__":
    demo.launch()
