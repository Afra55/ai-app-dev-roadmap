"""Vector indexing for smart notes."""

from __future__ import annotations

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from common.embeddings import get_embeddings
from common.rag import build_vectorstore, delete_by_metadata, reset_chroma_dir, similarity_search
from config import CHROMA_DIR, CHUNK_OVERLAP, CHUNK_SIZE, COLLECTION_NAME
from database import Note, list_notes


def _split_note(note: Note) -> list[Document]:
    header = f"标题: {note.title}\n标签: {note.tags}\n\n"
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", "。", " ", ""],
    )
    chunks = splitter.split_text(header + note.content)
    documents: list[Document] = []
    for index, chunk in enumerate(chunks):
        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "note_id": note.id,
                    "title": note.title,
                    "chunk_id": index,
                    "source": f"note-{note.id}",
                },
            )
        )
    return documents


def delete_note_vectors(note_id: int) -> None:
    delete_by_metadata(CHROMA_DIR, COLLECTION_NAME, {"note_id": note_id})


def index_note(note: Note) -> int:
    delete_note_vectors(note.id)
    docs = _split_note(note)
    if not docs:
        return 0

    build_vectorstore(
        docs,
        chroma_dir=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )
    return len(docs)


def rebuild_index() -> tuple[int, int]:
    reset_chroma_dir(CHROMA_DIR)

    notes = list_notes()
    chunk_total = 0
    for note in notes:
        chunk_total += index_note(note)
    return len(notes), chunk_total


def search_notes(query: str, top_k: int = 4) -> list[Document]:
    return similarity_search(
        query,
        chroma_dir=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
        top_k=top_k,
    )
