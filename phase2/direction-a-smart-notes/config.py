"""Direction A: smart notes project settings."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROJECT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data"

DB_PATH = DATA_DIR / "notes.db"
CHROMA_DIR = DATA_DIR / "chroma_db"
COLLECTION_NAME = "smart_notes"

CHUNK_SIZE = 400
CHUNK_OVERLAP = 60
TOP_K = 4

from common.paths import ensure_repo_on_path

ensure_repo_on_path()
