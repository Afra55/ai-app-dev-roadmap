"""Vector indexing for smart notes."""

from __future__ import annotations

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHROMA_DIR, CHUNK_OVERLAP, CHUNK_SIZE, COLLECTION_NAME
from database import Note, list_notes
from week2.embeddings import get_embeddings


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


def _get_store() -> Chroma:
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=str(CHROMA_DIR),
    )


def delete_note_vectors(note_id: int) -> None:
    if not CHROMA_DIR.exists():
        return
    store = _get_store()
    # Chroma metadata filter delete
    try:
        store._collection.delete(where={"note_id": note_id})  # noqa: SLF001
    except Exception:
        pass


def index_note(note: Note) -> int:
    delete_note_vectors(note.id)
    docs = _split_note(note)
    if not docs:
        return 0

    Chroma.from_documents(
        documents=docs,
        embedding=get_embeddings(),
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
    )
    return len(docs)


def rebuild_index() -> tuple[int, int]:
    if CHROMA_DIR.exists():
        import shutil

        shutil.rmtree(CHROMA_DIR)

    notes = list_notes()
    chunk_total = 0
    for note in notes:
        chunk_total += index_note(note)
    return len(notes), chunk_total


def search_notes(query: str, top_k: int = 4) -> list[Document]:
    if not CHROMA_DIR.exists():
        return []
    store = _get_store()
    return store.similarity_search(query, k=top_k)
