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

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

DEPARTMENTS = ("hr", "finance", "it")
