import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "Missing API key. Add GOOGLE_API_KEY or GEMINI_API_KEY to your environment or .env file."
    )

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="I want to learn about lang chains. Can you explain it to me in simple terms?",
)
print(response.text)