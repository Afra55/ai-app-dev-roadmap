"""Bank FAQ indexing and retrieval."""

from __future__ import annotations

import shutil

from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHROMA_DIR, COLLECTION_NAME, SAMPLE_DOCS_DIR
from week2.embeddings import get_embeddings


def rebuild_index() -> tuple[int, int]:
    if CHROMA_DIR.exists():
        shutil.rmtree(CHROMA_DIR)

    documents = []
    for path in sorted(SAMPLE_DOCS_DIR.rglob("*.md")):
        loader = TextLoader(str(path), encoding="utf-8")
        for doc in loader.load():
            doc.metadata["source"] = path.name
            documents.append(doc)

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=40)
    chunks = splitter.split_documents(documents)
    Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
    )
    return len(documents), len(chunks)


def search(query: str, top_k: int = 3):
    if not CHROMA_DIR.exists():
        return []
    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=str(CHROMA_DIR),
    )
    return store.similarity_search(query, k=top_k)
