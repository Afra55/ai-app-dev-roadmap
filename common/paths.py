"""Repository path helpers."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def ensure_repo_on_path() -> Path:
    """Ensure repository root is importable (for `common` and `week*` packages)."""
    root = str(REPO_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)
    return REPO_ROOT


def week_dir(name: str) -> Path:
    return REPO_ROOT / name


def project_dir(*parts: str) -> Path:
    return REPO_ROOT.joinpath("projects", *parts)
