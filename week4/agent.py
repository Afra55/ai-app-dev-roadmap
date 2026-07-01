"""LangGraph ReAct agent and edge-cloud orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.prebuilt import create_react_agent

from llm_utils import get_cloud_llm
from router import RouteDecision, route_query
from tools import ALL_TOOLS
from week3.local_llm import get_local_llm


@dataclass
class OrchestratorResult:
    route: str
    reason: str
    answer: str
    backend: str


class EdgeCloudOrchestrator:
    """Route queries across local model, cloud LLM, and LangGraph agent."""

    def __init__(self, local_backend: str = "mock") -> None:
        self.local_llm = get_local_llm(local_backend)
        self.cloud_llm = None
        self.agent = None

    def _get_cloud_llm(self):
        if self.cloud_llm is None:
            self.cloud_llm = get_cloud_llm()
        return self.cloud_llm

    def _get_agent(self):
        if self.agent is None:
            self.agent = create_react_agent(self._get_cloud_llm(), ALL_TOOLS)
        return self.agent

    @staticmethod
    def _extract_agent_answer(result: dict[str, Any]) -> str:
        messages = result.get("messages", [])
        for message in reversed(messages):
            if isinstance(message, AIMessage) and message.content:
                return str(message.content)
        return "Agent 未返回有效答案。"

    def run(self, query: str) -> OrchestratorResult:
        decision = route_query(query)

        if decision.route == "local":
            answer = self.local_llm.generate(query)
            return OrchestratorResult(
                route=decision.route,
                reason=decision.reason,
                answer=answer,
                backend=self.local_llm.name,
            )

        if decision.route == "cloud":
            response = self._get_cloud_llm().invoke(
                [
                    HumanMessage(
                        content=(
                            "你是智能助手，请用中文简洁回答用户问题。\n"
                            f"用户问题: {query}"
                        )
                    )
                ]
            )
            return OrchestratorResult(
                route=decision.route,
                reason=decision.reason,
                answer=str(response.content),
                backend="deepseek-v4-flash",
            )

        agent_result = self._get_agent().invoke(
            {"messages": [HumanMessage(content=query)]}
        )
        return OrchestratorResult(
            route=decision.route,
            reason=decision.reason,
            answer=self._extract_agent_answer(agent_result),
            backend="langgraph-react-agent",
        )


def preview_route(query: str) -> RouteDecision:
    return route_query(query)
