"""Repository path helpers."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PHASE1_DIR = REPO_ROOT / "phase1"
PHASE2_DIR = REPO_ROOT / "phase2"
PHASE3_DIR = REPO_ROOT / "phase3"


def ensure_repo_on_path() -> Path:
    """Ensure repository root and phase dirs are importable."""
    for path in (REPO_ROOT, PHASE1_DIR, PHASE2_DIR):
        entry = str(path)
        if entry not in sys.path:
            sys.path.insert(0, entry)
    return REPO_ROOT


def week_dir(name: str) -> Path:
    return PHASE1_DIR / name


def project_dir(*parts: str) -> Path:
    return PHASE2_DIR.joinpath(*parts)
