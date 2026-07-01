package com.ailearning.week3.llm

/**
 * On-device LLM abstraction.
 *
 * Replace [MockOnDeviceLLM] with MLC LLM / LiteRT-LM integration for real
 * offline Qwen2.5 inference on Android devices.
 */
interface OnDeviceLLM {
    val name: String
    val isReady: Boolean

    suspend fun generate(prompt: String): String
}
