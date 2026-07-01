"""FastAPI for Direction C enterprise agent."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agent import EnterpriseAgentService
from audit import init_audit_db, list_audit
from knowledge import rebuild_index

app = FastAPI(title="Enterprise Agent API", version="1.0.0")
service = EnterpriseAgentService()


class ChatRequest(BaseModel):
    user_id: str = "U10001"
    question: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    route: str
    answer: str


@app.on_event("startup")
def startup() -> None:
    init_audit_db()
    rebuild_index()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": "direction-c-enterprise-agent"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    try:
        result = service.run(payload.user_id, payload.question)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return ChatResponse(**result)


@app.get("/audit")
def audit(limit: int = 20) -> list[dict]:
    return list_audit(limit=limit)
