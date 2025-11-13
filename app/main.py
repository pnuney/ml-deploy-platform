from fastapi import FastAPI
from pydantic import BaseModel
from .model_utils import load_model, predict_proba

app = FastAPI()

#Load model once at startup
model = load_model()


class PredictionRequest(BaseModel):
    features: list[float]


class PredictionResponse(BaseModel):
    probability: float
    label: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest):
    probability = predict_proba(model, payload.features)
    label = 1 if probability >= 0.5 else 0
    return PredictionResponse(probability=probability, label=label)
