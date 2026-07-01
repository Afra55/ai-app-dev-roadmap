"""Week 4 settings and repository path bootstrap."""

from __future__ import annotations

import sys
from pathlib import Path

WEEK4_DIR = Path(__file__).resolve().parent
REPO_ROOT = WEEK4_DIR.parent
WEEK1_DIR = REPO_ROOT / "week1"
WEEK2_DIR = REPO_ROOT / "week2"
WEEK3_DIR = REPO_ROOT / "week3"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

LOCAL_MAX_CHARS = 24
LOCAL_KEYWORDS = ("你好", "hello", "hi", "谢谢", "再见")
AGENT_KEYWORDS = ("天气", "计算", "资料", "文档", "知识库", "检索", "rag")
COMPLEX_KEYWORDS = ("分析", "为什么", "比较", "设计", "架构", "步骤", "方案")
