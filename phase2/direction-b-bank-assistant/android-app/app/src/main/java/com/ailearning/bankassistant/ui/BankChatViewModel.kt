package com.ailearning.bankassistant.ui

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ailearning.bankassistant.network.ApiClient
import com.ailearning.bankassistant.network.AskRequest
import kotlinx.coroutines.launch

class BankChatViewModel : ViewModel() {
    var input by mutableStateOf("")
    var answer by mutableStateOf("")
    var status by mutableStateOf("教学演示 · 非真实银行业务")

    val quickQuestions = listOf("转账限额是多少？", "信用卡怎么还款？", "如何挂失银行卡？")

    fun ask(question: String = input) {
        val q = question.trim()
        if (q.isEmpty()) return
        viewModelScope.launch {
            status = "查询中..."
            try {
                val response = ApiClient.api.ask(AskRequest(q))
                answer = response.answer
                status = "已脱敏提问: ${response.masked_question}"
            } catch (_: Exception) {
                answer = "无法连接后端，请先启动 direction-b backend (8020)。"
                status = "连接失败"
            }
        }
    }
}
