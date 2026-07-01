# 银行智能客服（Direction B · 精简版）

← [路线图](../../README.md) · [第二阶段](../README.md) · **Direction B**

> 教学演示项目，非真实金融业务。

## 功能

- 银行 FAQ 知识库 RAG 问答
- 输入脱敏与审计日志
- Android 客户端：快捷问题 + 聊天（API Key 仅在后端）

## 快速开始

```bash
cd phase2/direction-b-bank-assistant/backend
pip install -r requirements.txt
python verify_setup.py
uvicorn api:app --reload --port 8020
```

Android Studio 打开 `android-app/`，模拟器访问 `http://10.0.2.2:8020`。

## 安全要点

- API Key 不进入 Android 客户端
- 日志中对手机号/身份证做脱敏
- 示例数据均为虚构
