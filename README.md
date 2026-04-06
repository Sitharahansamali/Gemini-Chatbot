# Gemini Chatbot (Python)

A lightweight Python chatbot that sends prompts to Google Gemini and prints the response.

## Overview

This project:
- Loads environment variables from `.env`
- Uses the `google-genai` SDK
- Sends a prompt to a Gemini model and prints output

## Project Structure

```text
.
|-- chatbot.py
|-- .env
|-- .gitignore
|-- README.md
`-- .venv/
```

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

## Troubleshooting

### Quota error (429 RESOURCE_EXHAUSTED)

- Your API key/project has no available quota.
- Enable billing/quota in Google AI Studio / Google Cloud, or use another key with quota.

### Model not found (404 NOT_FOUND)

- The selected model is unavailable for your key or API version.
- Update the model name in `chatbot.py` to a supported one.

### DLL load failed for `pydantic_core`

- Usually caused by incompatible Python versions (for example Python 3.14 alpha).
- Recreate environment with Python 3.11 and reinstall dependencies.

## Publish to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Security Note

- Never commit `.env`.
- If a key is exposed, rotate/regenerate it immediately.
