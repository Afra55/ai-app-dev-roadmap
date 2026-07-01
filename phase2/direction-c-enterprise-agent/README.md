# 企业内部智能助手（Direction C · 精简版）

← [路线图](../../README.md) · [第二阶段](../README.md) · **Direction C**

## 功能

- 分部门知识库检索（HR / Finance / IT）
- LangGraph ReAct Agent：知识库 + 请假余额(Mock) + 工单(Mock)
- 审计日志
- Gradio 管理/演示界面

## 快速开始

```bash
cd phase2/direction-c-enterprise-agent
pip install -r requirements.txt
python verify_setup.py
uvicorn api:app --reload --port 8030
python app_admin.py
```

## 示例问题

- 「年假还剩几天？」（HR + 工具）
- 「报销流程是什么？」（Finance 知识库）
- 「VPN 连不上怎么办？」（IT 知识库）
