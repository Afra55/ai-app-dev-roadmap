"""Department-aware enterprise knowledge base."""

from __future__ import annotations

import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHROMA_DIR, COLLECTION_NAME, SAMPLE_DOCS_DIR
from week2.embeddings import get_embeddings


def rebuild_index() -> tuple[int, int]:
    if CHROMA_DIR.exists():
        shutil.rmtree(CHROMA_DIR)

    documents = []
    for dept_dir in sorted(SAMPLE_DOCS_DIR.iterdir()):
        if not dept_dir.is_dir():
            continue
        department = dept_dir.name
        for path in sorted(dept_dir.rglob("*.md")):
            loader = TextLoader(str(path), encoding="utf-8")
            for doc in loader.load():
                doc.metadata["department"] = department
                doc.metadata["source"] = path.name
                documents.append(doc)

    splitter = RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
    )
    return len(documents), len(chunks)


def search_knowledge(query: str, department: str | None = None, top_k: int = 3) -> list:
    if not CHROMA_DIR.exists():
        return []

    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=str(CHROMA_DIR),
    )

    if department:
        try:
            return store.similarity_search(
                query,
                k=top_k,
                filter={"department": department},
            )
        except Exception:
            pass
    return store.similarity_search(query, k=top_k)
