"""Smoke checks for Direction C."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    project_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(project_dir))

    import config  # noqa: F401

    from audit import init_audit_db, list_audit
    from knowledge import rebuild_index, search_knowledge
    from tools import query_leave_balance, search_department_kb
    from agent import EnterpriseAgentService

    init_audit_db()
    _, chunks = rebuild_index()
    if chunks == 0:
        raise RuntimeError("企业知识库索引失败")

    docs = search_knowledge("报销", department="finance")
    if not docs:
        raise RuntimeError("分部门检索失败")

    leave = query_leave_balance.invoke({"user_id": "U10001"})
    if "3" not in leave:
        raise RuntimeError(f"请假 Mock 工具异常: {leave}")

    service = EnterpriseAgentService()
    result = service.run("U10001", "年假还剩几天")
    if not result["answer"]:
        raise RuntimeError("Agent/离线回答失败")

    logs = list_audit(5)
    if not logs:
        raise RuntimeError("审计日志未写入")

    print(f"Direction C 检查通过：{chunks} 个知识块，最近路由={result['route']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
