from flask import Flask, render_template, request, jsonify

from qna import ask_question
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_recommendations


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"answer": "Please enter a question."})

    return jsonify({
        "answer": ask_question(question)
    })


@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"answer": "Please enter a topic."})

    return jsonify({
        "answer": explain_topic(topic)
    })


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"answer": "Please enter some text."})

    return jsonify({
        "answer": summarize_text(text)
    })


@app.route("/quiz", methods=["POST"])
def quiz():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"answer": "Please enter a topic."})

    return jsonify({
        "answer": generate_quiz(topic)
    })


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"answer": "Please enter a topic."})

    return jsonify({
        "answer": get_recommendations(topic)
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
