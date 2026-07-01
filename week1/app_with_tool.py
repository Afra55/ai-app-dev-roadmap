"""Step 6: Simple tool-use demo with a weather lookup tool."""

from __future__ import annotations

import gradio as gr
import requests
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool

from llm_utils import get_llm


@tool
def get_weather(city: str) -> str:
    """Query current weather information for a specified city."""
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"{city} 当前天气：{response.text.strip()}"
        return f"无法获取 {city} 的天气信息"
    except Exception as exc:
        return f"查询天气时出错：{exc}"


def _get_tool_llm():
    return get_llm().bind_tools([get_weather])


def chat_with_tool(message: str, history: list | None) -> str:
    """Let the model decide whether to call the weather tool."""
    llm = _get_tool_llm()
    messages = [HumanMessage(content=message)]
    response = llm.invoke(messages)

    if not response.tool_calls:
        return response.content

    messages.append(response)
    for tool_call in response.tool_calls:
        if tool_call["name"] != "get_weather":
            continue
        tool_result = get_weather.invoke(tool_call["args"])
        messages.append(
            ToolMessage(
                content=tool_result,
                tool_call_id=tool_call["id"],
            )
        )

    final_response = llm.invoke(messages)
    return final_response.content


with gr.Blocks(title="Step 6: Tool Use 示例") as demo:
    gr.Markdown(
        "# Step 6: 简单 Tool Use 示例\n"
        "模型可以自动调用工具查询天气。这是入门演示，完整 Agent 会在第 4 周学习。"
    )
    gr.ChatInterface(
        fn=chat_with_tool,
        type="messages",
        title="AI 助手（可查天气）",
        examples=["北京现在天气怎么样？", "上海今天会下雨吗？"],
    )

if __name__ == "__main__":
    demo.launch()
