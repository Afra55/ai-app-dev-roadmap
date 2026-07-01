"""Enterprise agent tools."""

from __future__ import annotations

from langchain_core.tools import tool

from knowledge import search_knowledge

_MOCK_LEAVE_BALANCE = {"U10001": 3, "U10002": 7}


@tool
def search_department_kb(question: str, department: str = "hr") -> str:
    """Search enterprise knowledge base by department: hr/finance/it."""
    department = department.lower().strip()
    docs = search_knowledge(question, department=department, top_k=3)
    if not docs:
        return f"{department} 知识库中未找到相关信息。"

    blocks = []
    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        blocks.append(f"[{source}] {doc.page_content}")
    return "\n\n".join(blocks)


@tool
def query_leave_balance(user_id: str = "U10001") -> str:
    """Query remaining annual leave days for an employee (mock data)."""
    days = _MOCK_LEAVE_BALANCE.get(user_id, 0)
    return f"用户 {user_id} 剩余年假 {days} 天（Mock 数据）。"


@tool
def submit_it_ticket(issue: str) -> str:
    """Submit an IT support ticket (mock)."""
    issue = issue.strip()
    if not issue:
        return "工单内容不能为空。"
    return f"IT 工单已提交（Mock）：{issue[:120]}"


ALL_TOOLS = [search_department_kb, query_leave_balance, submit_it_ticket]
