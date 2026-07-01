"""Backward-compatible alias for week4.settings."""

try:
    from .settings import *  # noqa: F403
except ImportError:
    from settings import *  # noqa: F403
