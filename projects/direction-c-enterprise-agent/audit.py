"""Audit log storage."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

from config import AUDIT_DB, DATA_DIR


def _connect() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(AUDIT_DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_audit_db() -> None:
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                question TEXT NOT NULL,
                route TEXT NOT NULL,
                tools TEXT DEFAULT '',
                created_at TEXT NOT NULL
            )
            """
        )


def write_audit(user_id: str, question: str, route: str, tools: str = "") -> None:
    with _connect() as conn:
        conn.execute(
            "INSERT INTO audit_logs (user_id, question, route, tools, created_at) VALUES (?, ?, ?, ?, ?)",
            (
                user_id,
                question,
                route,
                tools,
                datetime.now(timezone.utc).isoformat(),
            ),
        )


def list_audit(limit: int = 20) -> list[dict]:
    with _connect() as conn:
        rows = conn.execute(
            "SELECT id, user_id, question, route, tools, created_at FROM audit_logs ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]
