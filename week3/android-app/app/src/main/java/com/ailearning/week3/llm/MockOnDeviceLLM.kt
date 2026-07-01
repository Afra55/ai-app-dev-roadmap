package com.ailearning.week3.llm

/**
 * Mock on-device model for emulator and CI-friendly development.
 */
class MockOnDeviceLLM : OnDeviceLLM {
    override val name: String = "mock-qwen2.5"
    override val isReady: Boolean = true

    override suspend fun generate(prompt: String): String {
        val text = prompt.trim()
        if (text.isEmpty()) {
            return "请输入有效问题。"
        }

        return when {
            text.contains("你好", ignoreCase = true) ||
                text.contains("hello", ignoreCase = true) ->
                "你好！我是端侧离线助手（Mock 模式）。"

            text.contains("RAG", ignoreCase = true) || text.contains("检索") ->
                "RAG 适合云端知识库检索；端侧模型更适合隐私敏感和弱网场景。"

            text.length <= 12 ->
                "（端侧 Mock 回复）已收到：$text"

            else ->
                "这是 Mock 端侧模型回复。请按 week3/README.md 集成真实 Qwen2.5 本地模型。"
        }
    }
}
