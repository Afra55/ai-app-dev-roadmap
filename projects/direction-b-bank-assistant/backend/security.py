"""Security helpers for Direction B."""

from __future__ import annotations

import re


_PHONE_RE = re.compile(r"1\d{10}")
_ID_RE = re.compile(r"\d{17}[\dXx]")


def mask_sensitive_text(text: str) -> str:
    masked = _PHONE_RE.sub("1**********", text)
    masked = _ID_RE.sub("******************", masked)
    return masked
