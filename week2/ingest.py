"""Document loading and vector store indexing."""

from __future__ import annotations

import argparse
from pathlib import Path

from langchain_chroma import Chroma

from common.rag import build_vectorstore, load_documents, reset_chroma_dir, split_documents

try:
    from .config import (
        CHROMA_DIR,
        CHUNK_OVERLAP,
        CHUNK_SIZE,
        COLLECTION_NAME,
        SAMPLE_DOCS_DIR,
    )
except ImportError:
    from config import (
        CHROMA_DIR,
        CHUNK_OVERLAP,
        CHUNK_SIZE,
        COLLECTION_NAME,
        SAMPLE_DOCS_DIR,
    )


def split_documents_with_ids(documents: list) -> list:
    """Split documents into chunks for retrieval."""
    chunks = split_documents(
        documents,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = index
    return chunks


def reset_vector_store() -> None:
    """Clear the existing collection or remove the persisted directory."""
    reset_chroma_dir(CHROMA_DIR)


def ingest_documents(
    docs_dir: Path,
    *,
    reindex: bool = False,
) -> tuple[Chroma, int, int]:
    """Load, split, embed, and persist documents into Chroma."""
    if reindex:
        reset_vector_store()

    documents = load_documents(docs_dir)
    chunks = split_documents_with_ids(documents)
    vectorstore = build_vectorstore(
        chunks,
        chroma_dir=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
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
