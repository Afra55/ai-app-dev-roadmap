"""FastAPI integration tests for Direction A."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest.mock import MagicMock

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "phase2" / "direction-a-smart-notes"


def _load_api():
    for name in list(sys.modules):
        if name in {"api", "database", "indexer", "settings", "config", "chat_service"}:
            sys.modules.pop(name, None)
    sys.path.insert(0, str(PROJECT))
    sys.path.insert(0, str(ROOT))

    fake_db = MagicMock()
    fake_indexer = MagicMock()
    sys.modules["database"] = fake_db
    sys.modules["indexer"] = fake_indexer
    sys.modules["settings"] = MagicMock()

    spec = importlib.util.spec_from_file_location("direction_a_api_test", PROJECT / "api.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_direction_a_health():
    api = _load_api()
    client = TestClient(api.app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["project"] == "direction-a-smart-notes"
    # Avoid polluting sys.modules for later integration tests
    for name in ("direction_a_api_test", "api", "database", "indexer", "settings", "config", "chat_service"):
        sys.modules.pop(name, None)
