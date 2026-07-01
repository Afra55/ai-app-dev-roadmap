"""Unified DeepSeek LLM client for the whole repository."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from common.paths import REPO_ROOT, project_dir, week_dir

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-flash"

_ENV_LOADED = False


def _load_env_files() -> None:
    global _ENV_LOADED
    if _ENV_LOADED:
        return
    for env_path in (
        REPO_ROOT / ".env",
        week_dir("week1") / ".env",
        week_dir("week2") / ".env",
        week_dir("week4") / ".env",
        project_dir("direction-a-smart-notes") / ".env",
        project_dir("direction-c-enterprise-agent") / ".env",
    ):
        if env_path.exists():
            load_dotenv(env_path)
    _ENV_LOADED = True


def _get_api_key() -> str:
    _load_env_files()
    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "未找到 DEEPSEEK_API_KEY。请在 phase1/week1/.env 或仓库根目录 .env 中配置，"
            "可参考 phase1/week1/.env.example。"
        )
    return api_key


def get_llm(*, temperature: float = 0.7, **kwargs: Any) -> ChatOpenAI:
    params = {
        "model": DEFAULT_MODEL,
        "api_key": _get_api_key(),
        "base_url": DEEPSEEK_BASE_URL,
        "temperature": temperature,
    }
    params.update(kwargs)
    return ChatOpenAI(**params)


def get_cloud_llm(**kwargs: Any) -> ChatOpenAI:
    """Lower temperature default for RAG / Agent."""
    kwargs.setdefault("temperature", 0.2)
    return get_llm(**kwargs)


def call_llm(prompt: str, *, temperature: float = 0.7, **kwargs: Any) -> str:
    llm = get_llm(temperature=temperature, **kwargs)
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as exc:
        return f"Error: {exc}"
