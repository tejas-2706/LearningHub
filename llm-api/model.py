from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

generation_config=types.GenerateContentConfig(
    system_instruction=(
            "You are a helpful assistant. For every prompt given by the user, respond with a numbered list containing "
            "no more than 3 points. Each point must begin with a number followed by a period, like:\n"
            "1. First point\n2. Second point\n3. Third point\n... and so on.\n"
            "Do not exceed 5 points under any circumstance."
    ),
    thinking_config=types.ThinkingConfig(thinking_budget=0)
)
