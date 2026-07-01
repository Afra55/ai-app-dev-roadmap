package com.ailearning.week3

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.ailearning.week3.llm.MockOnDeviceLLM
import com.ailearning.week3.ui.ChatScreen
import com.ailearning.week3.ui.ChatViewModel

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        val viewModel = ChatViewModel(MockOnDeviceLLM())
        setContent {
            ChatScreen(viewModel = viewModel)
        }
    }
}
