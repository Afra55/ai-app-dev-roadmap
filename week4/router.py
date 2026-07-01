"""Edge-cloud routing logic for Week 4."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

try:
    from .settings import AGENT_KEYWORDS, COMPLEX_KEYWORDS, LOCAL_KEYWORDS, LOCAL_MAX_CHARS
except ImportError:
    from settings import AGENT_KEYWORDS, COMPLEX_KEYWORDS, LOCAL_KEYWORDS, LOCAL_MAX_CHARS

RouteType = Literal["local", "cloud", "agent"]


@dataclass
class RouteDecision:
    route: RouteType
    reason: str


def route_query(query: str) -> RouteDecision:
    """Pick local, cloud, or agent execution based on simple heuristics."""
    text = query.strip()
    lower = text.lower()

    if not text:
        return RouteDecision(route="local", reason="空输入由端侧兜底")

    if any(keyword in text for keyword in AGENT_KEYWORDS) or any(
        keyword in lower for keyword in ("weather", "rag")
    ):
        return RouteDecision(route="agent", reason="需要工具调用（知识库/天气/计算）")

    if len(text) <= LOCAL_MAX_CHARS and any(keyword in lower for keyword in LOCAL_KEYWORDS):
        return RouteDecision(route="local", reason="短问候语，适合端侧快速响应")

    if len(text) > 80 or any(keyword in text for keyword in COMPLEX_KEYWORDS):
        return RouteDecision(route="cloud", reason="复杂问题交给云端大模型")

    if len(text) <= LOCAL_MAX_CHARS:
        return RouteDecision(route="local", reason="短问题默认端侧处理")

    return RouteDecision(route="cloud", reason="默认走云端以保证质量")
