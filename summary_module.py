from qna import ask_gemini


def summarize_text(text):
    prompt = f"""
You are EduGenie, an AI tutor.

Summarize the following educational text.

Text:
{text}

Give:
- Key points
- Important concepts
- Short and easy-to-understand summary
"""

    return ask_gemini(prompt)
