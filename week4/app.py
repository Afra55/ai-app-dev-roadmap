"""CLI demo for Week 4 edge-cloud orchestration."""

from __future__ import annotations

import argparse
import json
import sys

from agent import EdgeCloudOrchestrator, preview_route


def run_interactive(orchestrator: EdgeCloudOrchestrator) -> int:
    print("Week 4 端云协同助手（输入 exit 退出）")
    print("示例: 你好 | 什么是RAG | 北京天气 | 计算 (12+8)*2")
    while True:
        try:
            query = input("\n问题> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            return 0

        if not query:
            continue
        if query.lower() in {"exit", "quit", "q"}:
            print("再见！")
            return 0

        result = orchestrator.run(query)
        print(f"\n路由: {result.route} ({result.reason})")
        print(f"后端: {result.backend}")
        print(f"回答: {result.answer}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Week 4 端云协同 + Agent 演示")
    parser.add_argument("question", nargs="?", help="单次提问")
    parser.add_argument(
        "--route-only",
        action="store_true",
        help="仅预览路由决策，不实际调用模型",
    )
    parser.add_argument(
        "--local-backend",
        choices=["mock", "qwen"],
        default="mock",
        help="端侧模型后端",
    )
    args = parser.parse_args()

    try:
        if args.route_only:
            if not args.question:
                print("请提供 question 参数", file=sys.stderr)
                return 1
            decision = preview_route(args.question)
            print(json.dumps(decision.__dict__, ensure_ascii=False, indent=2))
            return 0

        orchestrator = EdgeCloudOrchestrator(local_backend=args.local_backend)
        if args.question:
            result = orchestrator.run(args.question)
            print(
                json.dumps(
                    {
                        "route": result.route,
                        "reason": result.reason,
                        "backend": result.backend,
                        "answer": result.answer,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 0
        return run_interactive(orchestrator)
    except Exception as exc:
        print(f"运行失败: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
