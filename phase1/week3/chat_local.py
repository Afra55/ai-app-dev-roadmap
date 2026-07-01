"""Command-line local chat for Week 3."""

from __future__ import annotations

import argparse
import sys

from local_llm import get_local_llm


def run_interactive(llm) -> int:
    print(f"Week 3 端侧聊天（backend={llm.name}，输入 exit 退出）")
    while True:
        try:
            message = input("\n你> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            return 0

        if not message:
            continue
        if message.lower() in {"exit", "quit", "q"}:
            print("再见！")
            return 0

        print(f"\n助手> {llm.generate(message)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Week 3 端侧本地聊天")
    parser.add_argument("message", nargs="?", help="单次提问（不提供则进入交互模式）")
    parser.add_argument(
        "--backend",
        choices=["mock", "qwen"],
        default="mock",
        help="mock=无需下载模型；qwen=真实 Qwen2.5-0.5B 本地推理",
    )
    args = parser.parse_args()

    try:
        llm = get_local_llm(args.backend)
        if args.message:
            print(llm.generate(args.message))
            return 0
        return run_interactive(llm)
    except Exception as exc:
        print(f"运行失败: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
