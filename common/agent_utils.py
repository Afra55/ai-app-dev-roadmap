"""Shared LangGraph / agent helpers."""

from __future__ import annotations

from typing import Any

from langchain_core.messages import AIMessage


def extract_agent_answer(result: dict[str, Any]) -> str:
    messages = result.get("messages", [])
    for message in reversed(messages):
        if isinstance(message, AIMessage) and message.content:
            return str(message.content)
    return "Agent 未返回有效答案。"
