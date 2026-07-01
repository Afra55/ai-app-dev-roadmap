"""Tests for Direction B security helpers."""

from __future__ import annotations

import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1] / "phase2" / "direction-b-bank-assistant" / "backend"
sys.path.insert(0, str(BACKEND))

from security import mask_sensitive_text  # noqa: E402


def test_mask_phone_number():
    result = mask_sensitive_text("我的手机号是13812345678")
    assert "13812345678" not in result
    assert "1**********" in result


def test_mask_id_card():
    result = mask_sensitive_text("身份证110101199001011234")
    assert "110101199001011234" not in result
