"""Unit tests for common.rag document loading."""

from __future__ import annotations

from pathlib import Path

import pytest

from common.rag import load_documents, split_documents

REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DOCS = REPO_ROOT / "phase1" / "week2" / "sample_docs"


def test_load_documents_finds_sample_files():
    documents = load_documents(SAMPLE_DOCS)
    assert documents
    sources = {doc.metadata.get("source") for doc in documents}
    assert any(source.endswith(".md") for source in sources)


def test_split_documents_respects_chunk_size():
    documents = load_documents(SAMPLE_DOCS)
    chunks = split_documents(documents, chunk_size=100, chunk_overlap=10)
    assert chunks
    assert all(len(chunk.page_content) <= 200 for chunk in chunks)


def test_load_documents_missing_dir_raises():
    with pytest.raises(FileNotFoundError):
        load_documents(Path("/nonexistent/docs"))
