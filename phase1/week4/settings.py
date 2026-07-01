"""Week 4 settings and repository path bootstrap."""

from __future__ import annotations

import sys
from pathlib import Path

WEEK4_DIR = Path(__file__).resolve().parent
PHASE1_DIR = WEEK4_DIR.parent
REPO_ROOT = PHASE1_DIR.parent
WEEK1_DIR = PHASE1_DIR / "week1"
WEEK2_DIR = PHASE1_DIR / "week2"
WEEK3_DIR = PHASE1_DIR / "week3"

for path in (REPO_ROOT, PHASE1_DIR):
    entry = str(path)
    if entry not in sys.path:
        sys.path.insert(0, entry)

LOCAL_MAX_CHARS = 24
LOCAL_KEYWORDS = ("你好", "hello", "hi", "谢谢", "再见")
AGENT_KEYWORDS = ("天气", "计算", "资料", "文档", "知识库", "检索", "rag")
COMPLEX_KEYWORDS = ("分析", "为什么", "比较", "设计", "架构", "步骤", "方案")
