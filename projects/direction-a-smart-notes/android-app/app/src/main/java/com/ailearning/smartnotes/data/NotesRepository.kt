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

    suspend fun ask(question: String): ChatDto? = try {
        api.chat(ChatRequest(question))
    } catch (_: Exception) {
        null
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
