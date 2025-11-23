# predict.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import joblib
import pandas as pd
import numpy as np
import os


# Path to your trained model
MODEL_PATH = "./content/best_model.pkl"

# Enable CORS so any website can call the API
app = FastAPI(title="Polymer Weight Loss Predictor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Allow ALL origins
    allow_credentials=True,
    allow_methods=["*"],     # Allow all methods
    allow_headers=["*"],     # Allow all headers
)

# Request body
class PredictRequest(BaseModel):
    Polymer_Type: str
    Molecular_Weight: float
    Crystallinity: float
    Thickness_mm: float
    Temperature_C: float
    pH: float
    Porosity: float
    Enzyme: float
    Days: float

# Response body
class PredictResponse(BaseModel):
    prediction: float
    prediction_array: list
    model_path: Optional[str] = None

# Load model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Train the model first.")

model = joblib.load(MODEL_PATH)

if not hasattr(model, "predict"):
    raise RuntimeError("Loaded model is invalid. Ensure you saved the pipeline with joblib.")

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        # Convert input to DataFrame
        X = pd.DataFrame([req.dict()])

        # Make prediction
        preds = model.predict(X)
        preds_list = np.array(preds).tolist()
        pred_value = float(preds_list[0])

        return PredictResponse(
            prediction=pred_value,
            prediction_array=preds_list,
            model_path=MODEL_PATH
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/")
def root():
    return {"status": "ok", "message": "Send POST request to /predict"}

"""
TEST WITH CURL:

curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{
  "Polymer_Type": "PLA",
  "Molecular_Weight": 15000,
  "Crystallinity": 32.5,
  "Thickness_mm": 1.0,
  "Temperature_C": 37,
  "pH": 7.4,
  "Porosity": 12.8,
  "Enzyme": 1.2,
  "Days": 28
}'

TEST WITH JAVASCRIPT (FROM ANY WEBSITE):

fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    Polymer_Type: "PLA",
    Molecular_Weight: 15000,
    Crystallinity: 32.5,
    Thickness_mm: 1.0,
    Temperature_C: 37,
    pH: 7.4,
    Porosity: 12.8,
    Enzyme: 1.2,
    Days: 28
  })
})
.then(res => res.json())
.then(data => console.log(data));
"""
