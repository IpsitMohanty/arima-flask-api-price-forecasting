# ARIMA Flask API Price Forecasting

Applied time-series forecasting project that serves a pre-trained **ARIMA** model through a lightweight **Flask API** and Docker container.

This repository combines exploratory notebook work, a serialized forecasting model, and a small REST endpoint for local prediction experiments.

## What This Project Does

The project exposes a simple Flask service that loads a pickled ARIMA model and returns forecast values through an HTTP endpoint.

It includes:

- a notebook used during the capstone workflow
- a saved ARIMA model in `arima_model.pkl`
- a Flask app for local predictions
- a Dockerfile for containerized execution

## Repository Structure

- `AI_Enterprise_Capstone.ipynb`
  Notebook used for the broader forecasting workflow and experimentation.

- `app.py`
  Flask API that loads the serialized model and serves predictions.

- `arima_model.pkl`
  Saved trained ARIMA model used by the API.

- `requirements.txt`
  Python dependencies.

- `Dockerfile`
  Container setup based on `python:3.9-slim`.

## API Endpoints

- `GET /`
  Simple health / welcome response.

- `POST /predict`
  Accepts a `steps` integer and returns that many forecast periods from the pre-trained model.
  `steps` must be between 1 and 365.

## Example Request

```json
{
  "steps": 4
}
```

## Example Response

```json
{
  "steps": 4,
  "prediction": [106.2, 106.8, 107.1, 107.4]
}
```

The ARIMA model forecasts forward from its training end-date. `steps` controls how many future periods to return.

## Debug Mode

Debug mode is off by default. To enable it locally:

```bash
FLASK_DEBUG=true python app.py
```

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask app:

```bash
python app.py
```

Typical local URL:

- `http://127.0.0.1:5000`

## Docker

Build the image:

```bash
docker build -t arima-flask-api .
```

Run the container:

```bash
docker run -p 5000:5000 arima-flask-api
```

## Notes

This is a small applied prototype rather than a production forecasting platform.

The current API is intentionally simple and assumes the serialized model and expected input format are already compatible with the forecasting task.
