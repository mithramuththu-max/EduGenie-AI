import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = "gemini-3.8-flash"

URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    f"models/{MODEL}:generateContent"
)


def ask_gemini(prompt):

    if not API_KEY:
        return "GEMINI_API_KEY is not set."

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=60
        )

        if response.status_code != 200:
            return "Gemini API Error: " + response.text

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:

        return "Error: " + str(e)


def ask_question(question):

    prompt = f"""
You are EduGenie, a friendly AI tutor.

Answer the student's question clearly
and in simple language.

Student question:
{question}

Give an educational and easy-to-understand answer.
"""

    return ask_gemini(prompt)
