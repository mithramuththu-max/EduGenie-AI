from qna import ask_gemini


def generate_quiz(topic):
    prompt = f"""
You are EduGenie, an AI tutor.

Create a short educational quiz about:

{topic}

Generate 5 multiple-choice questions.

For each question provide:
A, B, C, D options
Correct answer
Short explanation
"""

    return ask_gemini(prompt)
