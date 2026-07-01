"""FastAPI backend for Direction A smart notes."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import settings  # noqa: F401
from chat_service import NotesChatService
from database import (
    Note,
    create_note,
    delete_note,
    get_note,
    init_db,
    list_notes,
    seed_demo_notes,
    update_note,
)
from indexer import index_note, rebuild_index

app = FastAPI(title="Smart Notes API", version="1.0.0")
chat_service = NotesChatService()


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    tags: str = ""


class NoteUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    tags: str = ""


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    route: str
    reason: str
    backend: str
    answer: str
    sources: list[str]


def _to_dict(note: Note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "tags": note.tags,
        "updated_at": note.updated_at,
    }


@app.on_event("startup")
def on_startup() -> None:
    init_db()
    seed_demo_notes()
    rebuild_index()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": "direction-a-smart-notes"}


@app.get("/notes")
def notes_list() -> list[dict]:
    return [_to_dict(note) for note in list_notes()]


@app.post("/notes")
def notes_create(payload: NoteCreate) -> dict:
    note = create_note(payload.title, payload.content, payload.tags)
    index_note(note)
    return _to_dict(note)


@app.get("/notes/{note_id}")
def notes_get(note_id: int) -> dict:
    note = get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="笔记不存在")
    return _to_dict(note)


@app.put("/notes/{note_id}")
def notes_update(note_id: int, payload: NoteUpdate) -> dict:
    note = update_note(note_id, payload.title, payload.content, payload.tags)
    if note is None:
        raise HTTPException(status_code=404, detail="笔记不存在")
    index_note(note)
    return _to_dict(note)


@app.delete("/notes/{note_id}")
def notes_delete(note_id: int) -> dict[str, str]:
    note = get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="笔记不存在")
    delete_note(note_id)
    from indexer import delete_note_vectors

    delete_note_vectors(note_id)
    return {"message": "deleted"}


@app.post("/index/rebuild")
def index_rebuild() -> dict[str, int]:
    note_count, chunk_count = rebuild_index()
    return {"note_count": note_count, "chunk_count": chunk_count}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    try:
        result = chat_service.chat(payload.question)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"聊天失败: {exc}") from exc

    return ChatResponse(
        route=result.route,
        reason=result.reason,
        backend=result.backend,
        answer=result.answer,
        sources=result.sources,
    )
