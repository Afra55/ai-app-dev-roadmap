"""Department-aware enterprise knowledge base."""

from __future__ import annotations

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from common.rag import (
    build_vectorstore,
    reset_chroma_dir,
    similarity_search,
    split_documents,
)
from config import CHROMA_DIR, COLLECTION_NAME, SAMPLE_DOCS_DIR


def _load_department_documents() -> list[Document]:
    documents: list[Document] = []
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
    if not documents:
        raise ValueError(f"在 {SAMPLE_DOCS_DIR} 中未找到部门文档")
    return documents


def rebuild_index() -> tuple[int, int]:
    reset_chroma_dir(CHROMA_DIR)
    documents = _load_department_documents()
    chunks = split_documents(documents, chunk_size=350, chunk_overlap=50)
    build_vectorstore(
        chunks,
        chroma_dir=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )
    return len(documents), len(chunks)


def search_knowledge(query: str, department: str | None = None, top_k: int = 3) -> list:
    where = {"department": department} if department else None
    return similarity_search(
        query,
        chroma_dir=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
        top_k=top_k,
        where=where,
    )
