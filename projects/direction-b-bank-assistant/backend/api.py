"""FastAPI backend for Direction B bank assistant."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from knowledge import rebuild_index, search
from security import mask_sensitive_text

try:
    from week4.llm_utils import get_cloud_llm
except Exception:
    get_cloud_llm = None

app = FastAPI(title="Bank Assistant API", version="1.0.0")

PROMPT = """你是银行智能客服（教学演示）。仅根据 FAQ 资料回答，资料没有则说明无法回答。
资料：
{context}
用户问题：{question}
"""


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)


class AskResponse(BaseModel):
    answer: str
    masked_question: str
    sources: list[str]


@app.on_event("startup")
def startup() -> None:
    rebuild_index()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": "direction-b-bank-assistant"}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    masked = mask_sensitive_text(payload.question)
    docs = search(payload.question)
    if not docs:
        return AskResponse(answer="资料中未找到相关信息。", masked_question=masked, sources=[])

    context = "\n\n".join(doc.page_content for doc in docs)
    sources = [str(doc.metadata.get("source", "unknown")) for doc in docs]

    if get_cloud_llm is None:
        answer = f"（离线模式）{docs[0].page_content[:300]}"
    else:
        try:
            answer = str(get_cloud_llm().invoke(PROMPT.format(context=context, question=payload.question)).content)
        except ValueError:
            answer = f"（离线模式）{docs[0].page_content[:300]}"
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    return AskResponse(answer=answer, masked_question=masked, sources=sources)
