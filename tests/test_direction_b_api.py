"""FastAPI integration tests for Direction B."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest.mock import MagicMock

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "phase2" / "direction-b-bank-assistant" / "backend"


def _load_api():
    for name in list(sys.modules):
        if name in {"api", "knowledge", "security", "config"}:
            sys.modules.pop(name, None)
    sys.path.insert(0, str(BACKEND))
    sys.path.insert(0, str(ROOT))
    sys.modules["knowledge"] = MagicMock()

    spec = importlib.util.spec_from_file_location("direction_b_api_test", BACKEND / "api.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_direction_b_health():
    api = _load_api()
    client = TestClient(api.app)
    response = client.get("/health")
    assert response.status_code == 200
    assert "bank" in response.json()["project"]
