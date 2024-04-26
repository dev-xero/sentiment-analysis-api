from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    res = {
        "message": "Welcome to the API",
        "success": True,
        "code": 200
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run()
