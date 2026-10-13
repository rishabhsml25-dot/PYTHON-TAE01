from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import re

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

SENTENCES = {
    "easy": [
        "Practice makes progress every single day.",
        "Small steps can lead to big results.",
        "Python helps us solve problems with code.",
        "Stay focused and keep learning new things."
    ],
    "medium": [
        "Consistent practice improves both typing speed and accuracy.",
        "Writing clean code makes software easier to understand.",
        "A good developer learns from mistakes and keeps improving.",
        "Technology becomes powerful when people use it thoughtfully."
    ],
    "hard": [
        "Reliable software is built through careful testing, clear thinking, and continuous improvement.",
        "Programming challenges teach us to break complex problems into smaller, manageable steps.",
        "Accuracy matters because a tiny mistake can sometimes change the behaviour of an entire program.",
        "Great solutions balance performance, readability, maintainability, and the needs of real users."
    ]
}

@app.get("/")
def home():
    return jsonify({
        "name": "CodeStrength Python API",
        "status": "running",
        "endpoints": ["/api/health", "/api/challenge?level=easy", "/api/score"]
    })

@app.get("/api/health")
@app.get("/health")
def health():
    # Keep a simple health response for Render and browser-side connection checks.
    return jsonify({
        "status": "ok",
        "message": "Python backend is running",
        "service": "CodeStrength Python API",
        "api_version": 1
    })

@app.get("/api/challenge")
def challenge():
    level = request.args.get("level", "easy").strip().lower()
    if level not in SENTENCES:
        return jsonify({"error": "Difficulty must be easy, medium, or hard."}), 400
    return jsonify({
        "difficulty": level.title(),
        "sentence": random.choice(SENTENCES[level])
    })

@app.post("/api/score")
def score():
    data = request.get_json(silent=True) or {}
    target = data.get("target", "")
    typed = data.get("typed", "")
    try:
        elapsed = float(data.get("elapsed_seconds", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "elapsed_seconds must be a number."}), 400
    difficulty = str(data.get("difficulty", "easy")).title()

    if not isinstance(target, str) or not target or not isinstance(typed, str):
        return jsonify({"error": "A target sentence and typed text are required."}), 400
    if elapsed <= 0:
        return jsonify({"error": "Elapsed time must be greater than zero."}), 400

    # Compare character-by-character, counting correct characters at matching positions.
    correct = sum(1 for a, b in zip(target, typed) if a == b)
    total = max(len(target), len(typed), 1)
    wrong = total - correct
    accuracy = round((correct / total) * 100, 1)
    minutes = elapsed / 60
    wpm = round((len(typed) / 5) / minutes) if minutes > 0 else 0
    seconds = round(elapsed, 1)

    if accuracy >= 95:
        feedback = "Excellent accuracy! Keep it up."
    elif accuracy >= 80:
        feedback = "Good effort. Slow down slightly to improve accuracy."
    else:
        feedback = "Keep practising. Focus on matching the sentence carefully."

    return jsonify({
        "difficulty": difficulty,
        "wpm": max(wpm, 0),
        "accuracy": accuracy,
        "correct_characters": correct,
        "wrong_characters": wrong,
        "time_seconds": seconds,
        "feedback": feedback
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
