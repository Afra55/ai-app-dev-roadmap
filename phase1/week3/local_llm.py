"""Local on-device style LLM backends for Week 3."""

from __future__ import annotations

import re
from abc import ABC, abstractmethod

try:
    from .config import DEFAULT_MODEL_ID, MAX_NEW_TOKENS, TEMPERATURE
except ImportError:
    from config import DEFAULT_MODEL_ID, MAX_NEW_TOKENS, TEMPERATURE


class LocalLLM(ABC):
    """Abstract local inference backend."""

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_ready(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class MockLocalLLM(LocalLLM):
    """Deterministic mock backend for tests and quick demos without GPU."""

    @property
    def name(self) -> str:
        return "mock-qwen2.5"

    @property
    def is_ready(self) -> bool:
        return True

    def generate(self, prompt: str) -> str:
        text = prompt.strip()
        if not text:
            return "请输入有效问题。"

        if re.search(r"你好|hello|hi", text, flags=re.IGNORECASE):
            return "你好！我是端侧离线助手（Mock 模式）。真实设备上可替换为 Qwen2.5 本地模型。"

        if "RAG" in text.upper() or "检索" in text:
            return (
                "RAG 会先检索文档，再生成答案。端侧小模型适合简单问答，"
                "复杂知识库检索通常交给云端。"
            )

        if len(text) <= 12:
            return f"（端侧 Mock 回复）已收到：{text}"

        return (
            "这是端侧 Mock 模型的回复。"
            "如需真实离线推理，请运行：`python chat_local.py --backend qwen`。"
        )


class QwenLocalLLM(LocalLLM):
    """Run Qwen2.5 with transformers on CPU (first run downloads the model)."""

    def __init__(self, model_id: str = DEFAULT_MODEL_ID) -> None:
        self.model_id = model_id
        self._pipeline = None

    @property
    def name(self) -> str:
        return self.model_id

    @property
    def is_ready(self) -> bool:
        return self._pipeline is not None

    def _ensure_pipeline(self):
        if self._pipeline is not None:
            return
        try:
            from transformers import pipeline
        except ImportError as exc:
            raise RuntimeError(
                "未安装 transformers/torch。请执行: pip install -r requirements.txt"
            ) from exc

        self._pipeline = pipeline(
            "text-generation",
            model=self.model_id,
            device_map="cpu",
            torch_dtype="auto",
        )

    def generate(self, prompt: str) -> str:
        self._ensure_pipeline()
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Reply in Chinese."},
            {"role": "user", "content": prompt},
        ]

        outputs = self._pipeline(
            messages,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            do_sample=True,
            return_full_text=False,
        )
        result = outputs[0]["generated_text"]
        if isinstance(result, list):
            return str(result[-1].get("content", "")).strip()
        return str(result).strip()


def get_local_llm(backend: str = "mock") -> LocalLLM:
    backend = backend.lower().strip()
    if backend == "mock":
        return MockLocalLLM()
    if backend in {"qwen", "transformers", "hf"}:
        return QwenLocalLLM()
    raise ValueError(f"不支持的 backend: {backend}，可选 mock / qwen")
