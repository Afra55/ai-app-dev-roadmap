"""Smoke checks for Week 2 setup."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def check_import(module_name: str) -> None:
    if importlib.util.find_spec(module_name) is None:
        raise RuntimeError(f"缺少依赖: {module_name}")


def main() -> int:
    week2_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(week2_dir))

    for module in (
        "dotenv",
        "chromadb",
        "fastapi",
        "langchain_chroma",
        "langchain_community",
        "langchain_huggingface",
        "langchain_text_splitters",
        "pypdf",
        "sentence_transformers",
        "uvicorn",
    ):
        check_import(module)

    import config  # noqa: F401
    import embeddings  # noqa: F401
    import ingest  # noqa: F401
    import rag_pipeline  # noqa: F401

    print("依赖检查通过，开始构建示例索引（首次运行会下载 Embedding 模型）...")
    _, doc_count, chunk_count = ingest.ingest_documents(
        config.SAMPLE_DOCS_DIR,
        reindex=True,
    )
    print(f"索引完成：{doc_count} 个文档，{chunk_count} 个文本块")

    pipeline = rag_pipeline.RAGPipeline()
    docs = pipeline.retrieve("什么是 RAG？")
    if not docs:
        raise RuntimeError("检索失败：未返回任何文档块")

    print(f"检索测试通过，返回 {len(docs)} 个相关块")
    print(f"示例来源: {docs[0].metadata.get('source')}")

    from dotenv import load_dotenv
    import os

    load_dotenv(week2_dir / ".env")
    load_dotenv(week2_dir.parent / "week1" / ".env")
    if os.getenv("DEEPSEEK_API_KEY", "").strip():
        print("已检测到 DEEPSEEK_API_KEY，可运行 demo_rag.py 或 api.py 进行完整问答。")
    else:
        print("提示: 尚未配置 DEEPSEEK_API_KEY，检索功能可用，生成回答前请配置 API Key。")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
