"""Reusable tools for Week 4 LangGraph agent."""

from __future__ import annotations

import ast
import operator

from langchain_core.tools import tool

from common.agent_utils import extract_agent_answer

try:
    from . import settings as _settings  # noqa: F401
except ImportError:
    import settings as _settings  # noqa: F401
from week2.rag_pipeline import RAGPipeline

_rag_pipeline: RAGPipeline | None = None


def _get_rag_pipeline() -> RAGPipeline:
    global _rag_pipeline
    if _rag_pipeline is None:
        _rag_pipeline = RAGPipeline()
    return _rag_pipeline


@tool
def search_knowledge_base(question: str) -> str:
    """Search indexed local documents and return an answer with sources."""
    try:
        result = _get_rag_pipeline().answer(question)
    except FileNotFoundError:
        return (
            "知识库尚未建立。请先在 week2 目录运行: "
            "python ingest.py --reindex"
        )
    except Exception as exc:
        return f"知识库检索失败: {exc}"

    if not result.sources:
        return result.answer

    sources = ", ".join(f"{item.file}#chunk-{item.chunk_id}" for item in result.sources)
    return f"{result.answer}\n\n来源: {sources}"


@tool
def get_weather(city: str) -> str:
    """Query current weather for a city."""
    from common.weather import fetch_weather

    return fetch_weather(city)


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def _eval_math(expression: str) -> float:
    node = ast.parse(expression, mode="eval").body

    def _evaluate(item):
        if isinstance(item, ast.Constant) and isinstance(item.value, (int, float)):
            return float(item.value)
        if isinstance(item, ast.BinOp):
            left = _evaluate(item.left)
            right = _evaluate(item.right)
            operator_func = _ALLOWED_OPERATORS.get(type(item.op))
            if operator_func is None:
                raise ValueError("仅支持 + - * / 运算")
            return operator_func(left, right)
        if isinstance(item, ast.UnaryOp) and isinstance(item.op, ast.USub):
            return -_evaluate(item.operand)
        raise ValueError("表达式包含不支持的语法")

    return _evaluate(node)


@tool
def calculator(expression: str) -> str:
    """Evaluate a basic math expression, e.g. (12 + 8) * 2."""
    try:
        value = _eval_math(expression.replace(" ", ""))
        return f"{expression} = {value}"
    except Exception as exc:
        return f"计算失败: {exc}"


ALL_TOOLS = [search_knowledge_base, get_weather, calculator]
