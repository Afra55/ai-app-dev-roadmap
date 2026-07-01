"""Unit tests for common agent and weather helpers."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from langchain_core.messages import AIMessage

from common.agent_utils import extract_agent_answer
from common.weather import fetch_weather


def test_extract_agent_answer_from_messages():
    payload = {
        "messages": [
            AIMessage(content="最终答案"),
        ]
    }
    assert extract_agent_answer(payload) == "最终答案"


@patch("common.weather.requests.get")
def test_fetch_weather_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "Beijing: +22°C"
    mock_get.return_value = mock_response
    result = fetch_weather("Beijing")
    assert "22" in result
