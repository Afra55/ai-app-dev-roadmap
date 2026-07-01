"""FastAPI service for Week 2 RAG."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

try:
    from .config import SAMPLE_DOCS_DIR, SUPPORTED_SUFFIXES, UPLOAD_DIR
    from .ingest import ingest_documents
    from .rag_pipeline import RAGPipeline, Source
except ImportError:
    from config import SAMPLE_DOCS_DIR, SUPPORTED_SUFFIXES, UPLOAD_DIR
    from ingest import ingest_documents
    from rag_pipeline import RAGPipeline, Source

app = FastAPI(
    title="Week 2 RAG API",
    description="本地文档问答服务",
    version="1.0.0",
)
pipeline = RAGPipeline()


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, description="用户问题")


class SourceItem(BaseModel):
    file: str
    chunk_id: int
    snippet: str


class AskResponse(BaseModel):
    answer: str
    sources: list[SourceItem]


class IngestResponse(BaseModel):
    message: str
    document_count: int
    chunk_count: int


def _to_source_items(sources: list[Source]) -> list[SourceItem]:
    return [
        SourceItem(file=item.file, chunk_id=item.chunk_id, snippet=item.snippet)
        for item in sources
    ]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    try:
        result = pipeline.answer(request.question)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"生成回答失败: {exc}") from exc

    return AskResponse(
        answer=result.answer,
        sources=_to_source_items(result.sources),
    )


@app.post("/ingest/reindex", response_model=IngestResponse)
def reindex_sample_docs() -> IngestResponse:
    """Rebuild the vector index from bundled sample documents."""
    pipeline.reset()
    try:
        _, doc_count, chunk_count = ingest_documents(SAMPLE_DOCS_DIR, reindex=True)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"索引失败: {exc}") from exc

    return IngestResponse(
        message="示例文档索引完成",
        document_count=doc_count,
        chunk_count=chunk_count,
    )


@app.post("/ingest/upload", response_model=IngestResponse)
async def ingest_upload(files: list[UploadFile] = File(...)) -> IngestResponse:
    """Upload documents and rebuild the vector index."""
    if not files:
        raise HTTPException(status_code=400, detail="请至少上传一个文件")

    if UPLOAD_DIR.exists():
        shutil.rmtree(UPLOAD_DIR)
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    pipeline.reset()

    saved_count = 0
    for upload in files:
        suffix = Path(upload.filename or "").suffix.lower()
        if suffix not in SUPPORTED_SUFFIXES:
            raise HTTPException(
                status_code=400,
                detail=f"不支持的文件类型: {upload.filename}，仅支持 txt/md/pdf",
            )

        target = UPLOAD_DIR / Path(upload.filename).name
        with target.open("wb") as output:
            shutil.copyfileobj(upload.file, output)
        saved_count += 1

    if saved_count == 0:
        raise HTTPException(status_code=400, detail="没有有效文件被保存")

    try:
        _, doc_count, chunk_count = ingest_documents(UPLOAD_DIR, reindex=True)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"索引失败: {exc}") from exc

    return IngestResponse(
        message=f"已上传并索引 {saved_count} 个文件",
        document_count=doc_count,
        chunk_count=chunk_count,
    )


@app.on_event("startup")
def startup_ingest_if_needed() -> None:
    """Auto-build the index on first startup when vector store is missing."""
    try:
        pipeline.retrieve("RAG")
    except FileNotFoundError:
        ingest_documents(SAMPLE_DOCS_DIR, reindex=True)
