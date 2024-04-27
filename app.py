from flask import Flask, jsonify, request
from preprocessor import clean
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

import pickle
import tensorflow as tf
import nltk
import os

app = Flask(__name__)

# NLTK directory
os.makedirs("nltk", exist_ok=True)

print("Installing NLTK dependencies...")

# NLTK dependencies
nltk.download('averaged_perceptron_tagger', download_dir='nltk')
nltk.download('wordnet', download_dir='nltk')
nltk.download('omw-1.4', download_dir='nltk')
nltk.download('stopwords', download_dir='nltk')
nltk.download('punkt', download_dir='nltk')

# Load model
model = load_model(os.path.join('model', 'SentimentAnalyser.keras'))
print("Loaded model.")

# Load tokenizer
with open(os.path.join("tokenizers", "tokenizer.pkl"), "rb") as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

MAX_LEN: int = 50
THRESHOLD: float = 0.20


@app.route("/")
def home():
    res = {
        "message": "Welcome to the API",
        "success": True,
        "code": 200
    }
    return jsonify(res)


@app.route("/analyze", methods=['POST'])
def analyze():
    if request.method == 'POST':
        req_data = request.json
        text = req_data.get('review')

        if text == None:
            return jsonify({
                "message": "Provide some text for analysis.",
                "success": False,
                "code": 400
            }), 400

        cleaned_text = clean(text)
        tokenized_text = tokenizer.texts_to_sequences([cleaned_text])
        padded_text = pad_sequences(tokenized_text, MAX_LEN)

        analysis = model.predict(padded_text)
        sentiment = 1

        print("PROMPT:", text, "\nANALYSIS:", analysis)

        if 0.1 <= analysis <= THRESHOLD:
            sentiment = 0

        elif analysis < 0.1:
            sentiment = -1

        res = {
            "message": "Analyzed Sentiment.",
            "success": True,
            "code": 200,
            "payload": sentiment
        }

        return jsonify(res)


@app.errorhandler(404)
def not_found(e):
    res = {
        "message": "Invalid endpoint accessed.",
        "success": False,
        "code": 404
    }
    return jsonify(res), 404


@app.errorhandler(405)
def not_allowed(e):
    res = {
        "message": "Request method not allowed.",
        "success": False,
        "code": 405
    }
    return jsonify(res), 405


@app.errorhandler(500)
def server_error(e):
    res = {
        "message": "Internal server error.",
        "success": False,
        "code": 500
    }
    return jsonify(res), 500


if __name__ == "__main__":
    app.run()
