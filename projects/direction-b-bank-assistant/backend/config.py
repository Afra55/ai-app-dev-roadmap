"""Direction B backend settings."""

from __future__ import annotations

import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BACKEND_DIR.parent
REPO_ROOT = PROJECT_DIR.parent.parent
SAMPLE_DOCS_DIR = BACKEND_DIR / "sample_docs"
CHROMA_DIR = BACKEND_DIR / "data" / "chroma_db"
COLLECTION_NAME = "bank_faq"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
