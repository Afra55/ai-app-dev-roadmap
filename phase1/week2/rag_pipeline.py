"""RAG retrieval and answer generation."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

try:
    from .config import CHROMA_DIR, COLLECTION_NAME, TOP_K
    from .embeddings import get_embeddings
    from .llm_utils import call_llm
except ImportError:
    from config import CHROMA_DIR, COLLECTION_NAME, TOP_K
    from embeddings import get_embeddings
    from llm_utils import call_llm

RAG_PROMPT = """你是文档问答助手。请仅根据以下参考资料回答用户问题。
如果资料中没有相关信息，请明确回答「资料中未找到相关信息」，不要编造。

参考资料：
{context}

用户问题：{question}

请用中文回答，并在结尾列出引用来源（文件名）。"""


@dataclass
class Source:
    file: str
    chunk_id: int
    snippet: str


@dataclass
class RAGAnswer:
    answer: str
    sources: list[Source]


class RAGPipeline:
    """End-to-end RAG pipeline: retrieve relevant chunks and generate an answer."""

    def __init__(self, top_k: int = TOP_K) -> None:
        self.top_k = top_k
        self._vectorstore: Chroma | None = None

    def reset(self) -> None:
        """Drop cached vector store client after reindex."""
        self._vectorstore = None

    def _get_vectorstore(self) -> Chroma:
        if not CHROMA_DIR.exists():
            raise FileNotFoundError(
                f"向量库不存在: {CHROMA_DIR}。请先运行 `python ingest.py`。"
            )

        if self._vectorstore is None:
            self._vectorstore = Chroma(
                collection_name=COLLECTION_NAME,
                embedding_function=get_embeddings(),
                persist_directory=str(CHROMA_DIR),
            )
        return self._vectorstore

    def retrieve(self, question: str) -> list[Document]:
        vectorstore = self._get_vectorstore()
        return vectorstore.similarity_search(question, k=self.top_k)

    @staticmethod
    def _format_context(documents: list[Document]) -> str:
        blocks: list[str] = []
        for index, doc in enumerate(documents, start=1):
            source = doc.metadata.get("source", "unknown")
            chunk_id = doc.metadata.get("chunk_id", index)
            blocks.append(
                f"[{index}] 文件: {source} | chunk: {chunk_id}\n{doc.page_content.strip()}"
            )
        return "\n\n".join(blocks)

    @staticmethod
    def _to_sources(documents: list[Document]) -> list[Source]:
        sources: list[Source] = []
        for doc in documents:
            snippet = doc.page_content.strip().replace("\n", " ")
            if len(snippet) > 160:
                snippet = snippet[:160] + "..."
            sources.append(
                Source(
                    file=str(doc.metadata.get("source", "unknown")),
                    chunk_id=int(doc.metadata.get("chunk_id", -1)),
                    snippet=snippet,
                )
            )
        return sources

    def answer(self, question: str) -> RAGAnswer:
        question = question.strip()
        if not question:
            raise ValueError("问题不能为空")

        documents = self.retrieve(question)
        if not documents:
            return RAGAnswer(
                answer="资料中未找到相关信息。",
                sources=[],
            )

        context = self._format_context(documents)
        prompt = RAG_PROMPT.format(context=context, question=question)
        response = call_llm(prompt)
        return RAGAnswer(answer=response, sources=self._to_sources(documents))
