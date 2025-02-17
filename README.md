# AI Enterprise Capstone Project

This project demonstrates the development of an ARIMA-based time-series forecasting model deployed via a Flask API, with Docker for easy containerization.

## Project Highlights
- **ARIMA Model**: Time-series forecasting using ARIMA.
- **Flask API**: A RESTful API that serves the trained ARIMA model.
- **Docker**: Containerized Flask app for easy deployment.

## Setup Instructions
Install dependencies
- pip install -r requirements.txt
  
Run the Flask Application
- python app.py

API Endpoints
- GET /: Welcome message for testing the API.
- POST /predict: Accepts JSON data for predictions.

Docker
- docker build -t arima-flask-api .
- docker run -p 5000:5000 arima-flask-api



### Clone the repository

```bash
git clone https://github.com/IpsitMohanty/arima-flask-api-price-forecasting.git
