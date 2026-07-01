package com.ailearning.smartnotes.data

import com.ailearning.smartnotes.BuildConfig
import com.ailearning.smartnotes.network.ApiClient
import com.ailearning.smartnotes.network.ChatRequest
import com.ailearning.smartnotes.network.NoteCreateRequest

class NotesRepository {
    private val api = ApiClient.create(BuildConfig.API_BASE_URL)

    suspend fun loadNotes(): List<NoteDto> = try {
        api.listNotes()
    } catch (_: Exception) {
        emptyList()
    }

    suspend fun createNote(title: String, content: String): NoteDto? = try {
        api.createNote(NoteCreateRequest(title, content, ""))
    } catch (_: Exception) {
        null
    }

    suspend fun ask(question: String): ChatDto? {
        return try {
            api.chat(ChatRequest(question))
        } catch (_: Exception) {
            localOfflineFallback(question)
        }
    }

    private fun localOfflineFallback(question: String): ChatDto? {
        val text = question.trim()
        if (text.isEmpty()) return null

        val lower = text.lowercase()
        if (GREETING_REGEX.containsMatchIn(lower)) {
            return ChatDto(
                route = "local",
                reason = "端侧离线兜底（未连接后端）",
                backend = "mock-qwen2.5",
                answer = "你好！我是端侧离线助手（Mock 模式）。真实设备上可替换为 Qwen2.5 本地模型。",
                sources = emptyList(),
            )
        }

        if (text.length <= 12) {
            return ChatDto(
                route = "local",
                reason = "端侧离线兜底（未连接后端）",
                backend = "mock-qwen2.5",
                answer = "（端侧 Mock 回复）已收到：$text",
                sources = emptyList(),
            )
        }

        return ChatDto(
            route = "local",
            reason = "端侧离线兜底（未连接后端）",
            backend = "mock-qwen2.5",
            answer = "后端未连接。请启动 Smart Notes API（默认 http://10.0.2.2:8010）后重试。",
            sources = emptyList(),
        )
    }

    companion object {
        private val GREETING_REGEX = Regex("你好|hello|hi")
    }
}

data class NoteDto(
    val id: Int,
    val title: String,
    val content: String,
    val tags: String,
    val updated_at: String,
)

data class ChatDto(
    val route: String,
    val reason: String,
    val backend: String,
    val answer: String,
    val sources: List<String>,
)
