# Android 开发者转 AI 应用开发笔记

## 与 Android 开发的相似点

| Android 概念 | AI 应用开发对应 |
|-------------|----------------|
| 网络请求层（Retrofit） | LLM API 调用封装（如 `llm_utils.py`） |
| 本地数据库（Room） | 向量数据库（Chroma） |
| Repository 模式 | RAG Pipeline 封装 |
| 依赖注入 | 配置与环境变量管理 |

## 端侧 AI 的优势

有 Android 背景的开发者在做 AI 应用时有独特优势：

- **端侧部署**：可以在设备上运行小模型，保护隐私、降低延迟
- **端云协同**：简单任务本地处理，复杂任务上云
- **用户体验**：更熟悉移动端交互设计

## 学习路线建议

1. 第 1 周：Python + Prompt + API 调用
2. 第 2 周：RAG 实现（当前周）
3. 第 3 周：安卓端侧 AI
4. 第 4 周：LangGraph Agent

## Chunk 分块注意事项

- `chunk_size` 太大：检索粒度粗，容易带入无关内容
- `chunk_size` 太小：上下文不完整，答案可能片面
- `chunk_overlap` 用于保持段落之间的语义连续性
