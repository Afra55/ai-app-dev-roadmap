package com.ailearning.week3.ui

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ailearning.week3.llm.OnDeviceLLM
import kotlinx.coroutines.launch

data class ChatMessage(
    val role: String,
    val content: String,
)

class ChatViewModel(
    private val onDeviceLLM: OnDeviceLLM,
) : ViewModel() {
    var messages by mutableStateOf<List<ChatMessage>>(emptyList())
        private set

    var input by mutableStateOf("")
    var isGenerating by mutableStateOf(false)
        private set

    val modelName: String
        get() = onDeviceLLM.name

    fun updateInput(value: String) {
        input = value
    }

    fun sendMessage() {
        val question = input.trim()
        if (question.isEmpty() || isGenerating) {
            return
        }

        messages = messages + ChatMessage(role = "user", content = question)
        input = ""
        isGenerating = true

        viewModelScope.launch {
            val answer = onDeviceLLM.generate(question)
            messages = messages + ChatMessage(role = "assistant", content = answer)
            isGenerating = false
        }
    }
}
