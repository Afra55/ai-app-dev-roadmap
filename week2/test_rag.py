"""Command-line RAG Q&A for Week 2."""

from __future__ import annotations

import argparse
import json
import sys

try:
    from .config import SAMPLE_DOCS_DIR
    from .ingest import ingest_documents
    from .rag_pipeline import RAGPipeline
except ImportError:
    from config import SAMPLE_DOCS_DIR
    from ingest import ingest_documents
    from rag_pipeline import RAGPipeline


def run_interactive(pipeline: RAGPipeline) -> int:
    print("Week 2 文档问答（输入 exit 退出）")
    while True:
        try:
            question = input("\n问题> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            return 0

        if not question:
            continue
        if question.lower() in {"exit", "quit", "q"}:
            print("再见！")
            return 0

        result = pipeline.answer(question)
        print("\n回答:")
        print(result.answer)
        if result.sources:
            print("\n来源:")
            for source in result.sources:
                print(f"- {source.file}#chunk-{source.chunk_id}: {source.snippet}")


def run_once(pipeline: RAGPipeline, question: str) -> int:
    result = pipeline.answer(question)
    payload = {
        "answer": result.answer,
        "sources": [
            {
                "file": source.file,
                "chunk_id": source.chunk_id,
                "snippet": source.snippet,
            }
            for source in result.sources
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Week 2 本地文档问答")
    parser.add_argument("question", nargs="?", help="直接提问（不提供则进入交互模式）")
    parser.add_argument(
        "--reindex",
        action="store_true",
        help="提问前先重建索引",
    )
    args = parser.parse_args()

    if args.reindex:
        print("正在重建索引...")
        ingest_documents(SAMPLE_DOCS_DIR, reindex=True)

    pipeline = RAGPipeline()

    try:
        if args.question:
            return run_once(pipeline, args.question)
        return run_interactive(pipeline)
    except FileNotFoundError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        print("请先运行: python ingest.py", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"运行失败: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
