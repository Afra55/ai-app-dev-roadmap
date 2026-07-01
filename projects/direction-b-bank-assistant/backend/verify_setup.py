"""Smoke checks for Direction B backend."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    backend_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(backend_dir))

    from knowledge import rebuild_index, search
    from security import mask_sensitive_text

    _, chunks = rebuild_index()
    if chunks == 0:
        raise RuntimeError("FAQ 索引失败")

    docs = search("转账限额")
    if not docs:
        raise RuntimeError("FAQ 检索失败")

    masked = mask_sensitive_text("我的手机号是13812345678")
    if "13812345678" in masked:
        raise RuntimeError("脱敏失败")

    print(f"Direction B 检查通过：{chunks} 个 FAQ 块")
    print(f"脱敏示例: {masked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
