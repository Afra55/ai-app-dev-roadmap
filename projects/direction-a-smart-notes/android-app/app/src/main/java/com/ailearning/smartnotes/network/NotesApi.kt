package com.ailearning.smartnotes.network

import com.ailearning.smartnotes.data.ChatDto
import com.ailearning.smartnotes.data.NoteDto
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface NotesApi {
    @GET("notes")
    suspend fun listNotes(): List<NoteDto>

    @POST("notes")
    suspend fun createNote(@Body body: NoteCreateRequest): NoteDto

    @POST("chat")
    suspend fun chat(@Body body: ChatRequest): ChatDto
}

data class NoteCreateRequest(
    val title: String,
    val content: String,
    val tags: String = "",
)

data class ChatRequest(
    val question: String,
)
