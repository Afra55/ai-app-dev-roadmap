"""Smoke checks for Week 1 setup without calling the DeepSeek API."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def check_import(module_name: str) -> None:
    if importlib.util.find_spec(module_name) is None:
        raise RuntimeError(f"缺少依赖: {module_name}")


def main() -> int:
    week1_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(week1_dir))

    for module in ("dotenv", "gradio", "langchain_openai", "langchain_core", "requests"):
        check_import(module)

    import llm_utils  # noqa: F401
    import test_chat  # noqa: F401
    import app  # noqa: F401
    import app_with_tool  # noqa: F401

    env_file = week1_dir / ".env"
    if not env_file.exists():
        print("依赖检查通过。")
        print("提示: 尚未创建 .env，运行聊天应用前请先配置 DEEPSEEK_API_KEY。")
        return 0

    from dotenv import load_dotenv
    import os

    load_dotenv(env_file)
    if os.getenv("DEEPSEEK_API_KEY", "").strip():
        print("依赖检查通过，已检测到 DEEPSEEK_API_KEY。")
    else:
        print("依赖检查通过，但 .env 中未设置有效的 DEEPSEEK_API_KEY。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
