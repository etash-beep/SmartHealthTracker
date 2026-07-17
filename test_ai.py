from ai_coach import askGemini
import os

response = askGemini(
    "Say hello in one sentence."
)

print(response)
print(os.getenv("GEMINI_API_KEY"))