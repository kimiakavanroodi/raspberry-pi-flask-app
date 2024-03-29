from flask import Flask, jsonify, request
from CountingPeoplePyTorch import getpredictions


app = Flask(__name__)


@app.route("/faster", methods=["POST"])

def faster():
    predictions = getpredictions(request)

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)