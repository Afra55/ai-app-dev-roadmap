"""Bank FAQ indexing and retrieval."""

from __future__ import annotations

from common.rag import (
    build_vectorstore,
    load_documents,
    reset_chroma_dir,
    similarity_search,
    split_documents,
)
from config import CHROMA_DIR, COLLECTION_NAME, SAMPLE_DOCS_DIR


def rebuild_index() -> tuple[int, int]:
    reset_chroma_dir(CHROMA_DIR)
    documents = load_documents(SAMPLE_DOCS_DIR)
    chunks = split_documents(documents, chunk_size=300, chunk_overlap=40)
    build_vectorstore(
        chunks,
        chroma_dir=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )
    return len(documents), len(chunks)


def search(query: str, top_k: int = 3):
    return similarity_search(
        query,
        chroma_dir=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
        top_k=top_k,
    )
