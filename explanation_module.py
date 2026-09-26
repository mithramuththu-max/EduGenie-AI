from qna import ask_gemini


def explain_topic(topic):
    prompt = f"""
You are EduGenie, an AI tutor.

Explain the following topic in simple student-friendly language.

Topic:
{topic}

Include:
1. Simple definition
2. Main points
3. Easy example
4. Short conclusion
"""

    return ask_gemini(prompt)
