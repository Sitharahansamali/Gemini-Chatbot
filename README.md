# Gemini Chatbot (Python)

A simple Python chatbot project that uses the Google Gemini API.

## Features

- Loads environment variables from a .env file
- Uses google-genai SDK
- Sends a prompt to Gemini and prints the response

## Project Structure

- chatbot.py: Main script
- .env: Local environment variables (not committed)
- .venv/: Local virtual environment (not committed)

## Requirements

- Python 3.11 recommended
- A Gemini API key from Google AI Studio

## Setup

1. Clone the repository.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment.

Windows (PowerShell):

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Windows (Git Bash):

python -m venv .venv
source .venv/Scripts/activate

4. Install dependencies:

pip install google-genai python-dotenv

5. Create a .env file with your key:

GEMINI_API_KEY=your_api_key_here

You can also use GOOGLE_API_KEY instead of GEMINI_API_KEY.

## Run

python chatbot.py

## Notes

- Do not commit your .env file.
- If you see quota errors (429), enable billing/quota for your Gemini project or use another key.
- If you use Python 3.14 alpha, some packages may fail. Use Python 3.11 for stability.
