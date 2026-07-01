package com.ailearning.smartnotes

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.ailearning.smartnotes.data.NotesRepository
import com.ailearning.smartnotes.ui.SmartNotesScreen
import com.ailearning.smartnotes.ui.SmartNotesViewModel

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val viewModel = SmartNotesViewModel(NotesRepository())
        setContent { SmartNotesScreen(viewModel) }
    }
}
