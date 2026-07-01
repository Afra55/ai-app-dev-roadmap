"""Shared utilities for ai-app-dev-roadmap."""

from common.paths import REPO_ROOT, ensure_repo_on_path

ensure_repo_on_path()

__all__ = ["REPO_ROOT", "ensure_repo_on_path"]
