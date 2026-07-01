"""Week 2 shared LLM utilities (reuses week1 API key if available)."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

WEEK2_DIR = Path(__file__).resolve().parent
WEEK1_DIR = WEEK2_DIR.parent / "week1"

load_dotenv(WEEK2_DIR / ".env")
if not os.getenv("DEEPSEEK_API_KEY", "").strip():
    load_dotenv(WEEK1_DIR / ".env")

# Allow importing week1 llm_utils when running from repository root.
if str(WEEK1_DIR) not in sys.path:
    sys.path.insert(0, str(WEEK1_DIR))

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-flash"


def _get_api_key() -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "未找到 DEEPSEEK_API_KEY。请在 week2/ 或 week1/ 目录创建 .env 文件，"
            "可参考 week2/.env.example。"
        )
    return api_key


def get_llm(**kwargs: Any) -> ChatOpenAI:
    """Create a configured DeepSeek chat client."""
    params = {
        "model": DEFAULT_MODEL,
        "api_key": _get_api_key(),
        "base_url": DEEPSEEK_BASE_URL,
        "temperature": 0.2,
    }
    params.update(kwargs)
    return ChatOpenAI(**params)


def call_llm(prompt: str, **kwargs: Any) -> str:
    """Invoke the model with a plain-text prompt and return the response."""
    llm = get_llm(**kwargs)
    response = llm.invoke(prompt)
    return response.content
