package com.ailearning.bankassistant.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun BankChatScreen(viewModel: BankChatViewModel) {
    Column(Modifier.fillMaxSize().padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
        Text("银行智能客服（Direction B）")
        Text(viewModel.status)
        LazyRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            items(viewModel.quickQuestions) { q ->
                Button(onClick = { viewModel.ask(q) }) { Text(q) }
            }
        }
        OutlinedTextField(
            value = viewModel.input,
            onValueChange = { viewModel.input = it },
            modifier = Modifier.fillMaxWidth(),
            label = { Text("请输入问题") },
        )
        Button(onClick = { viewModel.ask() }) { Text("发送") }
        Card(Modifier.fillMaxWidth()) {
            Text(viewModel.answer, modifier = Modifier.padding(12.dp))
        }
    }
}
