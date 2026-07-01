"""Document loading and vector store indexing."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

try:
    from .config import (
        CHROMA_DIR,
        CHUNK_OVERLAP,
        CHUNK_SIZE,
        COLLECTION_NAME,
        SAMPLE_DOCS_DIR,
        SUPPORTED_SUFFIXES,
    )
    from .embeddings import get_embeddings
except ImportError:
    from config import (
        CHROMA_DIR,
        CHUNK_OVERLAP,
        CHUNK_SIZE,
        COLLECTION_NAME,
        SAMPLE_DOCS_DIR,
        SUPPORTED_SUFFIXES,
    )
    from embeddings import get_embeddings


def load_documents(docs_dir: Path) -> list[Document]:
    """Load supported documents from a directory."""
    if not docs_dir.exists():
        raise FileNotFoundError(f"文档目录不存在: {docs_dir}")

    documents: list[Document] = []
    for path in sorted(docs_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue

        if path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(path))
        else:
            loader = TextLoader(str(path), encoding="utf-8")

        for doc in loader.load():
            doc.metadata["source"] = path.name
            documents.append(doc)

    if not documents:
        raise ValueError(f"在 {docs_dir} 中未找到支持的文档（txt/md/pdf）")

    return documents


def split_documents(documents: list[Document]) -> list[Document]:
    """Split documents into chunks for retrieval."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", "。", "！", "？", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = index
    return chunks


def reset_vector_store() -> None:
    """Clear the existing collection or remove the persisted directory."""
    if not CHROMA_DIR.exists():
        return

    try:
        import chromadb

        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        try:
            client.delete_collection(COLLECTION_NAME)
            return
        except Exception:
            pass
    except Exception:
        pass

    shutil.rmtree(CHROMA_DIR)


def ingest_documents(
    docs_dir: Path,
    *,
    reindex: bool = False,
) -> tuple[Chroma, int, int]:
    """Load, split, embed, and persist documents into Chroma."""
    if reindex:
        reset_vector_store()

    documents = load_documents(docs_dir)
    chunks = split_documents(documents)
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
    )
    return vectorstore, len(documents), len(chunks)


def main() -> None:
    parser = argparse.ArgumentParser(description="索引本地文档到 Chroma 向量库")
    parser.add_argument(
        "--docs",
        type=Path,
        default=SAMPLE_DOCS_DIR,
        help="待索引的文档目录，默认 sample_docs/",
    )
    parser.add_argument(
        "--reindex",
        action="store_true",
        help="清空旧索引后重新构建",
    )
    args = parser.parse_args()

    print(f"正在索引文档目录: {args.docs}")
    _, doc_count, chunk_count = ingest_documents(args.docs, reindex=args.reindex)
    print(f"索引完成：{doc_count} 个文档，{chunk_count} 个文本块")
    print(f"向量库路径: {CHROMA_DIR}")


if __name__ == "__main__":
    main()
