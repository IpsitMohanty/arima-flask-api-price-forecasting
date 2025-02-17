from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the pre-trained ARIMA model
model = pickle.load(open('arima_model.pkl', 'rb'))

# Define the home route for testing
@app.route('/')
def home():
    return "Welcome to the ARIMA model prediction API!"

# Define a route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the POST request (assumed to be JSON)
        input_data = request.get_json()
        
        # Example: Assume the input_data contains a feature 'price' as a list
        price_data = input_data['price']

        # Convert the input data to a pandas DataFrame for the model
        input_df = pd.DataFrame(price_data, columns=['price'])

        # Make the prediction using the model
        prediction = model.forecast(steps=len(input_df))

        # Return the prediction as a JSON response
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
