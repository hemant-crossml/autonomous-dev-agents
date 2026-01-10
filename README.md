# autonomous-dev-agents

An intelligent Python development assistant powered by Google's Gemini 2.5 Flash Lite, LangChain, and SerpAPI. This tool helps developers write code, generate comprehensive test cases, execute terminal commands safely, and research technical information through web searches.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Tools & Capabilities](#tools--capabilities)

## ✨ Features

- 🔧 **Terminal Command Execution**: Safely execute shell commands with proper error handling
- 🔍 **Web Search Integration**: Search the web for technical documentation and solutions using SerpAPI
- ✅ **Test Case Generation**: Automatically generate comprehensive Python test cases (pytest/unittest)
- 💡 **Code Generation**: Write clean, well-documented code following best practices
- 📝 **Comprehensive Logging**: Detailed logging with rotating file handlers for debugging
- 🎯 **Non-Interactive Mode**: Run predefined examples for demonstration purposes

## 📖 Learning Outcomes

By working with this project, you will learn:

- **LangChain Framework**: Build AI agents with tool integration and orchestration
- **API Integration**: Connect multiple APIs (Gemini, SerpAPI) in a unified system
- **Prompt Engineering**: Design effective system prompts for AI assistants
- **Error Handling**: Implement robust error handling and logging strategies
- **Environment Management**: Securely manage API keys and configuration
- **Python Best Practices**: Write clean, modular, and maintainable code

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- API keys for:
  - Google Gemini API
  - SerpAPI

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-development-assistant.git
cd ai-development-assistant
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create .env File

Create a `.env` file in the project root:

```bash
touch .env
```

Add your API keys to `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
```

**Important**: Never commit your `.env` file to version control!

## 🔑 Configuration

### Getting API Keys

#### Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

#### SerpAPI Key

1. Visit [SerpAPI](https://serpapi.com/)
2. Sign up for a free account (100 searches/month)
3. Get your API key from the dashboard
4. Copy the key to your `.env` file

### Model Configuration

The default model is `gemini-2.5-flash-lite`. You can modify settings in `client.py`:

```python
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.2,      # Adjust for creativity (0.0 - 1.0)
    top_p=0.9,           # Nucleus sampling
    top_k=40,            # Top-k sampling
    max_output_tokens=512 # Maximum response length
)
```

## 🚀 Usage

### Running the Application

```bash
python main.py
```

The application will run three predefined examples:

1. **Example 1**: Web search for Python best practices
2. **Example 2**: Generate pytest test cases for a function
3. **Example 3**: Execute terminal commands (Python version check)

## 🛠️ Tools & Capabilities

### 1. Execute Terminal Command

Safely execute shell commands with timeout and error handling.

**Security Features**:
- Command timeout (30 seconds)
- No shell injection (uses `split()`)
- Error capture and logging

### 2. Web Search Tool

Search the web using SerpAPI's Google search integration.

**Features**:
- Top 5 results by default (configurable)
- Structured output with title, URL, and snippet
- Error handling for API failures

### 3. Generate Test Cases

Generate comprehensive Python test cases using pytest or unittest.

**Features**:
- Positive test cases
- Edge case testing
- Negative test scenarios
- Configurable test framework

## 📚 Dependencies

```
langchain>=0.1.0
langchain-google-genai>=1.0.0
langchain-core>=0.1.0
google-generativeai>=0.3.0
serpapi>=0.1.5
python-dotenv>=1.0.0
```
