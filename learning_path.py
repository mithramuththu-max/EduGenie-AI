from qna import ask_gemini


def get_recommendations(topic):
    prompt = f"""
You are EduGenie, an AI tutor.

Create a learning path for a student who wants to learn:

{topic}

Provide:
1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Practice suggestions
5. Recommended order of learning
"""

    return ask_gemini(prompt)
