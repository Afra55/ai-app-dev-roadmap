# Week 1: Python Basics + Prompt Engineering + DeepSeek API Practice

## Learning Objectives

By the end of this week, you will be able to:

- Quickly master Python asynchronous programming and type annotations
- Understand and apply core Prompt Engineering techniques (CoT, structured output, function calling)
- Use the DeepSeek API to build simple LLM-powered applications
- Understand basic API calling and encapsulation patterns
- Handle common errors in API calls

## Resources for This Week

- Datawhale: *Hands-on Large Model Application Development* (Task 1-2)
- Bilibili: Black Horse Programmer 2026 LLM Application Development series (first 10 videos)
- DeepSeek Official Documentation

---

## Detailed Steps

### Step 1: Set Up Python Virtual Environment and Obtain DeepSeek API Key

**Objective**: Create an isolated learning environment and securely manage your API credentials.

1. Open your terminal and create + activate the virtual environment:

```bash
conda create -n llm-dev python=3.10 -y
conda activate llm-dev
```

   After successful activation, your terminal prompt should show `(llm-dev)`.

2. Install the required packages for this week:

```bash
pip install python-dotenv gradio langchain-openai
```

3. Obtain your DeepSeek API Key:
   - Visit: https://platform.deepseek.com/api_keys
   - Log in and create a new API Key
   - Copy the key (starts with `sk-`)

4. Create a project folder (recommended location: Desktop or Documents):

```bash
mkdir ai-learning
cd ai-learning
```

5. Create a `.env` file in the `ai-learning` folder.

   **Important**: The filename must start with a dot (`.`). Use any text editor (VS Code, Notepad++, etc.) and paste the following content:

```env
DEEPSEEK_API_KEY=sk-your-actual-deepseek-api-key-here
```

   Save the file.

**How to Verify the `.env` File**

The `.env` file is **not** automatically loaded into your shell environment. It is designed to be read by Python applications using the `python-dotenv` library.

**Correct verification methods**:

- Check file content:
  ```bash
  cat .env
  ```

- Verify inside Python (recommended):
  ```bash
  python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Key loaded:', bool(os.getenv('DEEPSEEK_API_KEY'))); print('Key starts with:', os.getenv('DEEPSEEK_API_KEY')[:10] if os.getenv('DEEPSEEK_API_KEY') else 'Not found')"
  ```

If the output shows `Key loaded: True`, the setup is successful.

---

### Step 2: Create and Run Your First Structured Output Chat Application

**Objective**: Verify that the API call works and implement basic structured output.

1. In the `ai-learning` folder, create a new file named `test_chat.py` and paste the following code:

```python
import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0.7,
)

def chat(message, history):
    prompt = f"""Please answer the user's question strictly in JSON format with the following structure:
{{"answer": "Your detailed answer", "confidence": "high/medium/low"}}

User question: {message}"""
    
    response = llm.invoke(prompt)
    return response.content

demo = gr.ChatInterface(chat, title="DeepSeek Structured Chat Demo")
demo.launch()
```

2. Run the script in the terminal:

```bash
python test_chat.py
```

3. A browser window should open automatically. Test by entering questions and observe whether the output is in valid JSON format.

**Common Issues & Solutions**:
- **API Key error**: Double-check that the key in `.env` is correct and that `load_dotenv()` is called.
- **Model not found**: Confirm you are using `"deepseek-chat"`.

---

### Step 3: Prompt Engineering Practice (Structured Output + Chain-of-Thought)

**Objective**: Deeply understand and practice the two most important Prompt Engineering techniques.

**Detailed Exercises**:

1. **Structured Output Practice**
   - Open `test_chat.py`
   - Replace the `prompt` section with this improved template:

```python
prompt = f"""You are a helpful assistant. Please answer the user's question in the following strict JSON format:
{{"answer": "concise and accurate answer", "reasoning": "brief reasoning", "confidence": "high/medium/low"}}

User question: {message}"""
```

   - Test with different questions, for example:
     - "What are your advantages?"
     - "How to learn Python effectively?"
     - "What is the weather like today?"

2. **Chain-of-Thought (CoT) Practice**
   - Add "Let's think step by step." to your prompt.
   - Compare two versions:
     - Version A: Direct answer request
     - Version B: Require reasoning before answering
   - Observe which version produces better structured output.

3. **Design Your Own Prompts**
   - Create a prompt that makes the model output code examples.
   - Create a prompt that makes the model perform simple classification.

**Recommendation**: Test each prompt with at least 3 different questions and record your observations.

---

### Step 4: Encapsulate LLM Calling Functions

**Objective**: Learn basic code encapsulation patterns and prepare for future FastAPI development. Add basic error handling.

**Detailed Steps**:

1. Create a new file `llm_utils.py` in the `ai-learning` folder and paste the following code:

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    """Return a configured LLM instance."""
    return ChatOpenAI(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
        temperature=0.7,
    )

def call_llm(prompt: str) -> str:
    """Call the LLM with basic error handling."""
    llm = get_llm()
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error occurred: {str(e)}"
```

2. Modify `test_chat.py` to use the encapsulated function:

```python
from llm_utils import call_llm

def chat(message, history):
    prompt = f"""Please answer in JSON format... User question: {message}"""
    return call_llm(prompt)
```

3. Test error handling:
   - Temporarily put an incorrect API key in `.env` and observe the error message.
   - Restore the correct key afterward.

**Extension Exercise**:
- Add retry logic
- Add support for streaming output

---

### Step 5: Integrate Everything into a Complete Simple Application

**Objective**: Combine all components learned this week into a reusable module.

1. Create `app.py` that integrates all previous functionality.
2. Add basic conversation history support.
3. Test the complete workflow and document your results.

---

## Learning Outcomes After Completing Week 1

After finishing this week, you will be able to:

- Independently create and manage Python virtual environments
- Correctly call the DeepSeek API and manage API keys
- Quickly build simple chat interfaces using Gradio
- Apply core Prompt Engineering techniques (structured output, Chain-of-Thought)
- Encapsulate LLM calling logic with basic error handling
- Organize code into reusable modules

---

**Notes**:

This document will be continuously updated as learning progresses. After completing each step, you are encouraged to add your own notes, observations, or solutions to problems at the end of this file.
