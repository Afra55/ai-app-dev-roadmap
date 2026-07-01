"""Direction C settings."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROJECT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data"
CHROMA_DIR = DATA_DIR / "chroma_db"
AUDIT_DB = DATA_DIR / "audit.db"
SAMPLE_DOCS_DIR = PROJECT_DIR / "sample_docs"
COLLECTION_NAME = "enterprise_kb"

from common.paths import ensure_repo_on_path

ensure_repo_on_path()

DEPARTMENTS = ("hr", "finance", "it")
