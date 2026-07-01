package com.ailearning.bankassistant

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.ailearning.bankassistant.ui.BankChatScreen
import com.ailearning.bankassistant.ui.BankChatViewModel

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { BankChatScreen(BankChatViewModel()) }
    }
}
