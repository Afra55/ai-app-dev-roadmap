"""Shared weather tool implementation."""

from __future__ import annotations

import requests


def fetch_weather(city: str, *, timeout: int = 5) -> str:
    city = city.strip()
    if not city:
        return "城市名称不能为空。"
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3", timeout=timeout)
        if response.status_code == 200:
            return f"{city} 当前天气：{response.text.strip()}"
        return f"无法获取 {city} 的天气信息"
    except Exception as exc:
        return f"查询天气时出错：{exc}"
