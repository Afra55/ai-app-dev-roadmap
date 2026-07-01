"""Integration tests for Direction A chat service."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

from langchain_core.documents import Document

PROJECT = Path(__file__).resolve().parents[1] / "phase2" / "direction-a-smart-notes"


def _reload_chat_modules():
  for name in ("chat_service", "database", "indexer", "settings", "config", "api"):
      sys.modules.pop(name, None)
  if str(PROJECT) not in sys.path:
      sys.path.insert(0, str(PROJECT))


def test_chat_greeting_routes_local():
    _reload_chat_modules()
    import settings  # noqa: F401
    from chat_service import NotesChatService
    service = NotesChatService()
    result = service.chat("你好")
    assert result.route == "local"
    assert result.backend == "mock-qwen2.5"


def test_chat_note_question_routes_notes_rag():
    _reload_chat_modules()
    import settings  # noqa: F401
    from chat_service import NotesChatService

    fake_docs = [
        Document(
            page_content="RAG 笔记内容示例",
            metadata={"note_id": 1, "title": "RAG 学习笔记"},
        )
    ]

    with (
        patch("chat_service.search_notes", return_value=fake_docs),
        patch("chat_service.get_cloud_llm", side_effect=ValueError("no key")),
    ):
        service = NotesChatService()
        result = service.chat("我的笔记里 RAG 写了什么？")

    assert result.route == "notes-rag"
    assert result.sources
    assert "离线模式" in result.answer or "RAG" in result.answer
