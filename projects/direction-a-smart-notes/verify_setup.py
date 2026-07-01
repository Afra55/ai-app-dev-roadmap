"""Smoke checks for Direction A."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    project_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(project_dir))

    import settings  # noqa: F401
    from database import init_db, list_notes, seed_demo_notes
    from indexer import rebuild_index, search_notes
    from chat_service import NotesChatService

    init_db()
    seed_demo_notes()
    note_count, chunk_count = rebuild_index()
    if note_count == 0 or chunk_count == 0:
        raise RuntimeError("笔记索引失败")

    docs = search_notes("RAG")
    if not docs:
        raise RuntimeError("笔记检索失败")

    service = NotesChatService()
    local = service.chat("你好")
    if local.route != "local":
        raise RuntimeError(f"端侧路由失败: {local.route}")

    notes = service.chat("我的 RAG 笔记说了什么")
    if notes.route != "notes-rag":
        raise RuntimeError(f"笔记 RAG 路由失败: {notes.route}")

    print(f"Direction A 检查通过：{note_count} 条笔记，{chunk_count} 个文本块")
    print(f"端侧回复: {local.answer[:40]}...")
    print(f"笔记问答后端: {notes.backend}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
