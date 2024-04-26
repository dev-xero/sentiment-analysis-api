from flask import Flask, jsonify, request

app = Flask(__name__)


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
        res = {
            "message": "Analyzed Sentiment.",
            "success": True,
            "code": 200
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
def not_found(e):
    res = {
        "message": "Request method not allowed.",
        "success": False,
        "code": 405
    }
    return jsonify(res), 405


if __name__ == "__main__":
    app.run()
