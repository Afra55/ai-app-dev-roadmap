"""Unit tests for week4 edge-cloud router."""

from __future__ import annotations

from week4.router import route_query


def test_greeting_routes_local():
    decision = route_query("你好")
    assert decision.route == "local"


def test_weather_routes_agent():
    decision = route_query("今天北京天气怎么样")
    assert decision.route == "agent"


def test_long_analysis_routes_cloud():
    decision = route_query("请详细分析 Android 开发者转型 AI 应用开发的优势与挑战，并给出分步骤学习方案")
    assert decision.route == "cloud"
