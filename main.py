from flask import Flask, jsonify, request
from preprocessor import clean

import nltk

app = Flask(__name__)

print("Installing NLTK dependencies...")

# NLTK dependencies
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


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
        cleaned_text = clean("hello, world!")
        res = {
            "message": "Analyzed Sentiment.",
            "success": True,
            "code": 200,
            "payload": cleaned_text
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
