"""Smoke checks for Week 4 setup."""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


def check_import(module_name: str) -> None:
    if importlib.util.find_spec(module_name) is None:
        raise RuntimeError(f"缺少依赖: {module_name}")


def main() -> int:
    week4_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(week4_dir))

    import settings  # noqa: F401

    for module in (
        "dotenv",
        "gradio",
        "langchain_openai",
        "langgraph",
        "requests",
    ):
        check_import(module)

    import agent  # noqa: F401
    import router  # noqa: F401
    import tools  # noqa: F401

    local_cases = [
        ("你好", "local"),
        ("请分析微服务架构的设计步骤", "cloud"),
        ("北京天气怎么样", "agent"),
    ]
    for query, expected in local_cases:
        decision = router.route_query(query)
        if decision.route != expected:
            raise RuntimeError(
                f"路由不符合预期: query={query}, expected={expected}, got={decision.route}"
            )

    print("路由规则检查通过。")

    orchestrator = agent.EdgeCloudOrchestrator(local_backend="mock")
    local_result = orchestrator.run("你好")
    if local_result.route != "local":
        raise RuntimeError("端侧路由执行失败")

    print(f"端侧执行通过: {local_result.answer}")

    calc_result = tools.calculator.invoke({"expression": "(12+8)*2"})
    if "40" not in calc_result:
        raise RuntimeError(f"计算器工具异常: {calc_result}")
    print(f"计算器工具通过: {calc_result}")

    from dotenv import load_dotenv

    load_dotenv(week4_dir / ".env")
    load_dotenv(week4_dir.parent / "week1" / ".env")
    has_key = bool(os.getenv("DEEPSEEK_API_KEY", "").strip())

    week2_chroma = week4_dir.parent / "week2" / "chroma_db"
    if not week2_chroma.exists():
        print("提示: week2 向量库尚未建立，Agent 知识库工具需要先运行 week2/ingest.py。")
    else:
        print("检测到 week2 向量库，Agent 知识库工具可用。")

    if has_key:
        print("已检测到 DEEPSEEK_API_KEY，可运行 cloud/agent 路径。")
    else:
        print("提示: 未配置 DEEPSEEK_API_KEY，cloud/agent 路径暂不可用。")

    print("Week 4 基础检查完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
