"""Chat orchestration for smart notes."""

from __future__ import annotations

from dataclasses import dataclass

from config import TOP_K
from indexer import search_notes
import settings  # noqa: F401
from week4.agent import EdgeCloudOrchestrator
from week4.llm_utils import get_cloud_llm


NOTES_PROMPT = """你是智能笔记助手。请优先根据以下笔记内容回答。
如果笔记中没有相关信息，请明确说明，不要编造。

笔记内容：
{context}

用户问题：{question}
"""


@dataclass
class ChatResult:
    route: str
    reason: str
    backend: str
    answer: str
    sources: list[str]


class NotesChatService:
    def __init__(self) -> None:
        self.orchestrator = EdgeCloudOrchestrator(local_backend="mock")

    def _answer_from_notes(self, question: str) -> ChatResult | None:
        docs = search_notes(question, top_k=TOP_K)
        if not docs:
            return None

        context_blocks = []
        sources: list[str] = []
        for index, doc in enumerate(docs, start=1):
            title = doc.metadata.get("title", "unknown")
            note_id = doc.metadata.get("note_id", "?")
            context_blocks.append(f"[{index}] {title}\n{doc.page_content}")
            sources.append(f"note-{note_id}:{title}")

        prompt = NOTES_PROMPT.format(context="\n\n".join(context_blocks), question=question)
        try:
            answer = str(get_cloud_llm().invoke(prompt).content)
        except ValueError:
            answer = (
                "（离线模式）根据笔记检索结果：\n"
                + docs[0].page_content[:400]
            )
        return ChatResult(
            route="notes-rag",
            reason="命中笔记知识库",
            backend="smart-notes-rag",
            answer=answer,
            sources=sources,
        )

    def chat(self, question: str) -> ChatResult:
        question = question.strip()
        if not question:
            raise ValueError("问题不能为空")

        note_keywords = ("笔记", "note", "rag", "端云", "标签")
        lower = question.lower()
        if any(keyword in lower for keyword in note_keywords) or "?" in question or "？" in question:
            notes_result = self._answer_from_notes(question)
            if notes_result is not None:
                return notes_result

        routed = self.orchestrator.run(question)
        return ChatResult(
            route=routed.route,
            reason=routed.reason,
            backend=routed.backend,
            answer=routed.answer,
            sources=[],
        )
