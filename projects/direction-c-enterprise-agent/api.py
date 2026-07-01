"""FastAPI for Direction C enterprise agent."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agent import EnterpriseAgentService
from audit import init_audit_db, list_audit
from knowledge import rebuild_index

service = EnterpriseAgentService()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_audit_db()
    rebuild_index()
    yield


app = FastAPI(title="Enterprise Agent API", version="1.0.0", lifespan=lifespan)


class ChatRequest(BaseModel):
    user_id: str = "U10001"
    question: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    route: str
    answer: str


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
