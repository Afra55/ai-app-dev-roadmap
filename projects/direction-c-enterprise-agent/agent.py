"""Enterprise LangGraph agent service."""

from __future__ import annotations

from typing import Any

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.prebuilt import create_react_agent

from audit import write_audit
from tools import ALL_TOOLS
from week4.llm_utils import get_cloud_llm


class EnterpriseAgentService:
    def __init__(self) -> None:
        self._agent = None

    def _get_agent(self):
        if self._agent is None:
            self._agent = create_react_agent(get_cloud_llm(), ALL_TOOLS)
        return self._agent

    @staticmethod
    def _extract_answer(result: dict[str, Any]) -> str:
        messages = result.get("messages", [])
        for message in reversed(messages):
            if isinstance(message, AIMessage) and message.content:
                return str(message.content)
        return "Agent 未返回有效答案。"

    def run(self, user_id: str, question: str) -> dict[str, str]:
        question = question.strip()
        if not question:
            raise ValueError("问题不能为空")

        # Offline fallback when API key is unavailable.
        try:
            result = self._get_agent().invoke({"messages": [HumanMessage(content=question)]})
            answer = self._extract_answer(result)
            route = "agent"
        except ValueError:
            from knowledge import search_knowledge

            docs = search_knowledge(question, department=None, top_k=2)
            if docs:
                answer = f"（离线模式）{docs[0].page_content[:400]}"
            else:
                answer = "（离线模式）未找到知识库内容，且未配置 API Key。"
            route = "offline-rag"

        write_audit(user_id=user_id, question=question, route=route, tools="")
        return {"route": route, "answer": answer}
