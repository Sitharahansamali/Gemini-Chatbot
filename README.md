# Gemini Chatbot (Python)

A lightweight Python chatbot that sends prompts to Google Gemini and prints the response.

## Overview

This project:
- Loads environment variables from `.env`
- Uses the `google-genai` SDK
- Sends a prompt to a Gemini model and prints output

## Project Structure

```text
chatbot/
├── chatbot.py          # Main chatbot script
├── .env                # API key configuration
├── .venv/              # Local Python virtual environment
├── .gitignore          # Ignored local and generated files
└── README.md           # Project overview and setup instructions
```

Local files such as `.env` and `.venv/` are shown here for clarity, even though they are usually ignored in git.

## Prerequisites

- Python 3.11 (recommended)
- A Gemini API key from Google AI Studio

## Quick Start

### 1. Create and activate virtual environment

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 2. Install dependencies

```bash
pip install google-genai python-dotenv
```

### 3. Add API key

Create `.env` in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

`GOOGLE_API_KEY` is also supported by the script.

## Run the Project

```bash
python chatbot.py
```
## Security Note

- Never commit `.env`.
- If a key is exposed, rotate/regenerate it immediately.
