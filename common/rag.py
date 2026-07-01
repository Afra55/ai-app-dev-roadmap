"""Shared RAG indexing utilities."""

from __future__ import annotations

import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from common.embeddings import get_embeddings

SUPPORTED_SUFFIXES = {".txt", ".md", ".pdf"}


def load_documents(docs_dir: Path) -> list[Document]:
    if not docs_dir.exists():
        raise FileNotFoundError(f"文档目录不存在: {docs_dir}")

    documents: list[Document] = []
    for path in sorted(docs_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        loader = PyPDFLoader(str(path)) if path.suffix.lower() == ".pdf" else TextLoader(
            str(path), encoding="utf-8"
        )
        for doc in loader.load():
            doc.metadata.setdefault("source", path.name)
            documents.append(doc)

    if not documents:
        raise ValueError(f"在 {docs_dir} 中未找到支持的文档（txt/md/pdf）")
    return documents


def split_documents(
    documents: list[Document],
    *,
    chunk_size: int,
    chunk_overlap: int,
) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "。", "！", "？", " ", ""],
    )
    return splitter.split_documents(documents)


def reset_chroma_dir(chroma_dir: Path) -> None:
    if chroma_dir.exists():
        shutil.rmtree(chroma_dir)


def delete_by_metadata(
    chroma_dir: Path,
    collection_name: str,
    where: dict,
) -> None:
    if not chroma_dir.exists():
        return
    import chromadb

    client = chromadb.PersistentClient(path=str(chroma_dir))
    try:
        collection = client.get_collection(collection_name)
        collection.delete(where=where)
    except Exception:
        pass


def build_vectorstore(
    documents: list[Document],
    *,
    chroma_dir: Path,
    collection_name: str,
) -> Chroma:
    return Chroma.from_documents(
        documents=documents,
        embedding=get_embeddings(),
        collection_name=collection_name,
        persist_directory=str(chroma_dir),
    )


def get_vectorstore(*, chroma_dir: Path, collection_name: str) -> Chroma:
    return Chroma(
        collection_name=collection_name,
        embedding_function=get_embeddings(),
        persist_directory=str(chroma_dir),
    )


def similarity_search(
    query: str,
    *,
    chroma_dir: Path,
    collection_name: str,
    top_k: int = 4,
    where: dict | None = None,
) -> list[Document]:
    if not chroma_dir.exists():
        return []
    store = get_vectorstore(chroma_dir=chroma_dir, collection_name=collection_name)
    if where:
        try:
            return store.similarity_search(query, k=top_k, filter=where)
        except Exception:
            pass
    return store.similarity_search(query, k=top_k)
