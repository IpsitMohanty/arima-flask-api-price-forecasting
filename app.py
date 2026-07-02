import os
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

model = pickle.load(open("arima_model.pkl", "rb"))


@app.route("/")
def home():
    return "ARIMA Price Forecasting API"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        steps = int(data.get("steps", 1))
        if steps < 1 or steps > 365:
            return jsonify({"error": "steps must be between 1 and 365"}), 400
        prediction = model.forecast(steps=steps)
        return jsonify({"prediction": prediction.tolist(), "steps": steps})
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug)
