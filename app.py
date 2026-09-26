from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    answer = f"You asked: {question}\n\nThis is your EduGenie answer."

    return jsonify({"answer": answer})


@app.route("/explain", methods=["POST"])
def explain():
    data = request.json
    topic = data.get("topic", "")

    answer = (
        f"{topic}\n\n"
        f"Let's understand {topic} in a simple way.\n"
        f"This topic can be learned step by step with examples."
    )

    return jsonify({"answer": answer})


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"answer": "Please enter some text."})

    words = text.split()

    if len(words) > 40:
        summary = " ".join(words[:40]) + "..."
    else:
        summary = text

    return jsonify({"answer": summary})


@app.route("/quiz", methods=["POST"])
def quiz():
    data = request.json
    topic = data.get("topic", "")

    quiz = f"""Quiz: {topic}

1. What is {topic}?

A) Option A
B) Option B
C) Option C
D) Option D

2. Which statement is related to {topic}?

A) Option A
B) Option B
C) Option C
D) Option D
"""

    return jsonify({"answer": quiz})


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    topic = data.get("topic", "")

    recommendations = f"""Learning Recommendations for {topic}

• Learn the basic concepts
• Study important terminology
• Practice simple examples
• Solve practice questions
• Move to advanced concepts
"""

    return jsonify({"answer": recommendations})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
