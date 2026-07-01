"""Week 2 configuration."""

from pathlib import Path

WEEK2_DIR = Path(__file__).resolve().parent
SAMPLE_DOCS_DIR = WEEK2_DIR / "sample_docs"
CHROMA_DIR = WEEK2_DIR / "chroma_db"
UPLOAD_DIR = WEEK2_DIR / "uploaded_docs"

EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"
COLLECTION_NAME = "week2_docs"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 80
TOP_K = 4

SUPPORTED_SUFFIXES = {".txt", ".md", ".pdf"}
