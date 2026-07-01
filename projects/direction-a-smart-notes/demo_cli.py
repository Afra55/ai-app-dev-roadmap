"""CLI demo for Direction A smart notes."""

from __future__ import annotations

import argparse
import json
import sys

import settings  # noqa: F401
from chat_service import NotesChatService
from database import create_note, init_db, list_notes, seed_demo_notes
from indexer import rebuild_index


def main() -> int:
    parser = argparse.ArgumentParser(description="Direction A 智能笔记 CLI")
    parser.add_argument("question", nargs="?", help="提问内容")
    parser.add_argument("--init", action="store_true", help="初始化示例笔记与索引")
    parser.add_argument("--list", action="store_true", help="列出笔记")
    args = parser.parse_args()

    init_db()
    if args.init:
        created = seed_demo_notes()
        note_count, chunk_count = rebuild_index()
        print(f"初始化完成：新增 {created} 条笔记，索引 {note_count} 条 / {chunk_count} 块")
        return 0

    if args.list:
        notes = list_notes()
        print(json.dumps([note.__dict__ for note in notes], ensure_ascii=False, indent=2))
        return 0

    if not list_notes():
        seed_demo_notes()
        rebuild_index()

    if not args.question:
        print("请提供 question，或使用 --init / --list", file=sys.stderr)
        return 1

    service = NotesChatService()
    result = service.chat(args.question)
    print(
        json.dumps(
            {
                "route": result.route,
                "reason": result.reason,
                "backend": result.backend,
                "answer": result.answer,
                "sources": result.sources,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
