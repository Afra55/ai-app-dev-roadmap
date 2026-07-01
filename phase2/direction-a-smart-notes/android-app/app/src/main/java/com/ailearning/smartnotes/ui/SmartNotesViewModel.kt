package com.ailearning.smartnotes.ui

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ailearning.smartnotes.data.ChatDto
import com.ailearning.smartnotes.data.NoteDto
import com.ailearning.smartnotes.data.NotesRepository
import kotlinx.coroutines.launch

class SmartNotesViewModel(
    private val repository: NotesRepository,
) : ViewModel() {
    var notes by mutableStateOf<List<NoteDto>>(emptyList())
        private set
    var question by mutableStateOf("")
    var chatResult by mutableStateOf<ChatDto?>(null)
    var status by mutableStateOf("就绪")
    var newTitle by mutableStateOf("")
    var newContent by mutableStateOf("")

    init {
        refreshNotes()
    }

    fun refreshNotes() {
        viewModelScope.launch {
            status = "加载笔记中..."
            notes = repository.loadNotes()
            status = if (notes.isEmpty()) "未连接后端或暂无笔记" else "已加载 ${notes.size} 条笔记"
        }
    }

    fun createNote() {
        val title = newTitle.trim()
        val content = newContent.trim()
        if (title.isEmpty() || content.isEmpty()) return

        viewModelScope.launch {
            status = "创建笔记中..."
            val created = repository.createNote(title, content)
            if (created != null) {
                newTitle = ""
                newContent = ""
                refreshNotes()
            } else {
                status = "创建失败，请确认后端已启动"
            }
        }
    }

    fun ask() {
        val q = question.trim()
        if (q.isEmpty()) return
        viewModelScope.launch {
            status = "提问中..."
            chatResult = repository.ask(q)
            status = chatResult?.let { "路由: ${it.route}" } ?: "提问失败，请确认后端已启动"
        }
    }
}
