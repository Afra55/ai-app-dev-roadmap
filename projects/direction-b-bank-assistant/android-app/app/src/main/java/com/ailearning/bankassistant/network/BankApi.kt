package com.ailearning.bankassistant.network

import retrofit2.http.Body
import retrofit2.http.POST

interface BankApi {
    @POST("ask")
    suspend fun ask(@Body body: AskRequest): AskResponse
}

data class AskRequest(val question: String)
data class AskResponse(val answer: String, val masked_question: String, val sources: List<String>)
