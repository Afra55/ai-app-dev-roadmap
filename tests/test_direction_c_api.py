"""FastAPI integration tests for Direction C."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest.mock import MagicMock

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "phase2" / "direction-c-enterprise-agent"


def _load_api():
    for name in list(sys.modules):
        if name in {"api", "knowledge", "audit", "agent", "config"}:
            sys.modules.pop(name, None)
    sys.path.insert(0, str(PROJECT))
    sys.path.insert(0, str(ROOT))
    sys.modules["knowledge"] = MagicMock()
    sys.modules["audit"] = MagicMock()
    sys.modules["agent"] = MagicMock()
    agent_mod = sys.modules["agent"]
    agent_mod.EnterpriseAgentService = MagicMock(return_value=MagicMock())

    spec = importlib.util.spec_from_file_location("direction_c_api_test", PROJECT / "api.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_direction_c_health():
    api = _load_api()
    client = TestClient(api.app)
    response = client.get("/health")
    assert response.status_code == 200
    assert "enterprise" in response.json()["project"]
