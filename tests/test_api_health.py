"""FastAPI health endpoint smoke tests (no embedding download)."""

from __future__ import annotations

from unittest.mock import patch

from fastapi.testclient import TestClient


def test_week2_health_without_startup_index():
    with patch("week2.api.ingest_documents"), patch("week2.api.pipeline.retrieve"):
        from week2.api import app

        client = TestClient(app)
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
