package com.ailearning.smartnotes.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun SmartNotesScreen(viewModel: SmartNotesViewModel) {
    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(10.dp),
    ) {
        Text("Direction A · 智能笔记")
        Text(viewModel.status)

        OutlinedTextField(
            value = viewModel.newTitle,
            onValueChange = { viewModel.newTitle = it },
            modifier = Modifier.fillMaxWidth(),
            label = { Text("新笔记标题") },
        )
        OutlinedTextField(
            value = viewModel.newContent,
            onValueChange = { viewModel.newContent = it },
            modifier = Modifier.fillMaxWidth(),
            label = { Text("新笔记内容") },
        )
        Button(onClick = viewModel::createNote) { Text("创建笔记") }
        Button(onClick = viewModel::refreshNotes) { Text("刷新笔记") }

        LazyColumn(modifier = Modifier.weight(1f)) {
            items(viewModel.notes) { note ->
                Card(modifier = Modifier.fillMaxWidth().padding(bottom = 8.dp)) {
                    Column(modifier = Modifier.padding(10.dp)) {
                        Text(note.title)
                        Text(note.content)
                    }
                }
            }
        }

        OutlinedTextField(
            value = viewModel.question,
            onValueChange = { viewModel.question = it },
            modifier = Modifier.fillMaxWidth(),
            label = { Text("问笔记") },
        )
        Button(onClick = viewModel::ask) { Text("提问") }
        viewModel.chatResult?.let { result ->
            Card(modifier = Modifier.fillMaxWidth()) {
                Column(modifier = Modifier.padding(10.dp)) {
                    Text("路由: ${result.route} / ${result.backend}")
                    Text(result.answer)
                }
            }
        }
    }
}
