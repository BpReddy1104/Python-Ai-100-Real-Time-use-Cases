from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from nrclex import NRCLex
from langdetect import detect
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Load HuggingFace model
classifier = pipeline("sentiment-analysis")

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def translate_text(text):
    lang = detect_language(text)
    if lang != "en":
        try:
            return GoogleTranslator(source='auto', target='en').translate(text)
        except:
            return text
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        text = request.form["text"]
        translated_text = translate_text(text)

        sentiment_result = classifier(translated_text)[0]
        sentiment = sentiment_result["label"]
        score = round(sentiment_result["score"] * 100, 2)

        emotions = NRCLex(translated_text)
        emotion_scores = emotions.raw_emotion_scores

        result = {
            "original_text": text,
            "translated_text": translated_text,
            "sentiment": sentiment,
            "score": score,
            "language": detect_language(text),
            "emotion_scores": emotion_scores
        }

    return render_template("index.html", result=result)

@app.route("/api/sentiment", methods=["POST"])
def api_sentiment():
    text = request.json.get("text", "")
    translated = translate_text(text)
    sentiment_result = classifier(translated)[0]
    emotions = NRCLex(translated)
    return jsonify({
        "sentiment": sentiment_result["label"],
        "confidence": round(sentiment_result["score"], 4),
        "emotions": emotions.raw_emotion_scores
    })

if __name__ == "__main__":
    app.run(debug=True)
