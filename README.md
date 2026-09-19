This is my Ai-agent project, I'm using the boot.dev course to build it! :)

## Description
A Python-based AI Code Assistant that interacts with LLMs via the OpenRouter API. It allows users to send prompts directly from the command line and receive intelligent responses, with an optional verbose mode for debugging token usage.

## Features
- **CLI Interface**: Send prompts as command-line arguments.
- **OpenRouter Integration**: Access various models (defaults to `openrouter/free`).
- **Environment Management**: Uses `python-dotenv` to keep API keys secure.
- **Verbose Mode**: Track prompt and completion tokens for performance monitoring.

## Prerequisites
- Python 3.x
- An [OpenRouter](https://openrouter.ai/) API Key

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Chnopfli/AI-agent.git
   cd AI-agent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install openai python-dotenv
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory and add your API key:
   ```text
   OPENROUTER_API_KEY=your_api_key_here
   ```
   
5. **Set a system prompt under prompts.py**:
   ```text
   system_prompt = """
   your text here
   """
   ```

## Usage
Run the assistant by passing your prompt as a string:
```bash
python main.py "Explain how a for loop works in Python"
```
or
```bash
uv run main.py "Explain how a for loop works in Python"
```

To see token usage and extra details, use the `--verbose` flag:
```bash
python main.py "What is a decorator?" --verbose
```

## Project Structure
- `main.py`: The entry point of the application.
- `prompts.py`: Contains the `system_prompt` logic.
- `calculator` is just a test "Project"
 
