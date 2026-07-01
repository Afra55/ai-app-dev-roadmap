"""Smoke checks for Week 3 setup."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def check_import(module_name: str) -> None:
    if importlib.util.find_spec(module_name) is None:
        raise RuntimeError(f"缺少依赖: {module_name}")


def main() -> int:
    week3_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(week3_dir))

    for module in ("gradio",):
        check_import(module)

    import local_llm  # noqa: F401

    llm = local_llm.get_local_llm("mock")
    answer = llm.generate("你好")
    if not answer.strip():
        raise RuntimeError("Mock 端侧模型未返回有效答案")

    print("依赖检查通过。")
    print(f"Mock 端侧回复示例: {answer}")

    android_dir = week3_dir / "android-app"
    required_files = [
        android_dir / "settings.gradle.kts",
        android_dir / "app" / "build.gradle.kts",
        android_dir / "app" / "src" / "main" / "AndroidManifest.xml",
    ]
    missing = [str(path) for path in required_files if not path.exists()]
    if missing:
        raise RuntimeError(f"Android 工程文件缺失: {missing}")

    print("Android 工程骨架检查通过。")
    print("提示: 真实 Qwen2.5 本地推理可运行 `python chat_local.py --backend qwen`。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
