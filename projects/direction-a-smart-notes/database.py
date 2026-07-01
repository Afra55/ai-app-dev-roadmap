"""SQLite storage for smart notes."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from config import DATA_DIR, DB_PATH


@dataclass
class Note:
    id: int
    title: str
    content: str
    tags: str
    updated_at: str


def _connect() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT DEFAULT '',
                updated_at TEXT NOT NULL
            )
            """
        )


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def list_notes() -> list[Note]:
    with _connect() as conn:
        rows = conn.execute(
            "SELECT id, title, content, tags, updated_at FROM notes ORDER BY updated_at DESC"
        ).fetchall()
    return [Note(**dict(row)) for row in rows]


def get_note(note_id: int) -> Note | None:
    with _connect() as conn:
        row = conn.execute(
            "SELECT id, title, content, tags, updated_at FROM notes WHERE id = ?",
            (note_id,),
        ).fetchone()
    return Note(**dict(row)) if row else None


def create_note(title: str, content: str, tags: str = "") -> Note:
    updated_at = _now()
    with _connect() as conn:
        cursor = conn.execute(
            "INSERT INTO notes (title, content, tags, updated_at) VALUES (?, ?, ?, ?)",
            (title.strip(), content.strip(), tags.strip(), updated_at),
        )
        note_id = int(cursor.lastrowid)
    return Note(id=note_id, title=title.strip(), content=content.strip(), tags=tags.strip(), updated_at=updated_at)


def update_note(note_id: int, title: str, content: str, tags: str = "") -> Note | None:
    if get_note(note_id) is None:
        return None
    updated_at = _now()
    with _connect() as conn:
        conn.execute(
            "UPDATE notes SET title = ?, content = ?, tags = ?, updated_at = ? WHERE id = ?",
            (title.strip(), content.strip(), tags.strip(), updated_at, note_id),
        )
    return get_note(note_id)


def delete_note(note_id: int) -> bool:
    with _connect() as conn:
        cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    return cursor.rowcount > 0


def seed_demo_notes() -> int:
    """Insert demo notes when database is empty."""
    if list_notes():
        return 0

    samples = [
        (
            "RAG 学习笔记",
            "RAG 通过检索增强生成，适合私有知识库问答。关键步骤：分块、向量化、检索、Prompt。",
            "rag,ai",
        ),
        (
            "端云协同策略",
            "简单问候走端侧，复杂推理走云端，需要工具时走 Agent。",
            "edge,cloud",
        ),
    ]
    for title, content, tags in samples:
        create_note(title, content, tags)
    return len(samples)
