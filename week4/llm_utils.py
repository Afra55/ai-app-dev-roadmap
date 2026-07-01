"""Week 4 shared LLM utilities."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

try:
    from .settings import WEEK1_DIR, WEEK4_DIR
except ImportError:
    from settings import WEEK1_DIR, WEEK4_DIR

load_dotenv(WEEK4_DIR / ".env")
if not os.getenv("DEEPSEEK_API_KEY", "").strip():
    load_dotenv(WEEK1_DIR / ".env")

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-flash"


def _get_api_key() -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "未找到 DEEPSEEK_API_KEY。请在 week4/ 或 week1/ 目录配置 .env。"
        )
    return api_key


def get_cloud_llm(**kwargs: Any) -> ChatOpenAI:
    params = {
        "model": DEFAULT_MODEL,
        "api_key": _get_api_key(),
        "base_url": DEEPSEEK_BASE_URL,
        "temperature": 0.2,
    }
    params.update(kwargs)
    return ChatOpenAI(**params)
