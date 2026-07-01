"""Week 1 shared LLM utilities."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

WEEK1_DIR = Path(__file__).resolve().parent
load_dotenv(WEEK1_DIR / ".env")

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-flash"


def _get_api_key() -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "未找到 DEEPSEEK_API_KEY。请在 week1 目录创建 .env 文件，"
            "可参考 .env.example。"
        )
    return api_key


def get_llm(**kwargs: Any) -> ChatOpenAI:
    """Create a configured DeepSeek chat client."""
    params = {
        "model": DEFAULT_MODEL,
        "api_key": _get_api_key(),
        "base_url": DEEPSEEK_BASE_URL,
        "temperature": 0.7,
    }
    params.update(kwargs)
    return ChatOpenAI(**params)


def call_llm(prompt: str, **kwargs: Any) -> str:
    """Invoke the model with a plain-text prompt and return the response."""
    llm = get_llm(**kwargs)
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as exc:
        return f"Error: {exc}"
