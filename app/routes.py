from fastapi import APIRouter, HTTPException
from app.schemas import PatientInput, PredictionResponse
from ml.predict import predict_single

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Healthcare ML API is running"}

@router.post("/predict", response_model=PredictionResponse)
def predict(patient: PatientInput):
    try:
        result = predict_single(patient.model_dump())
        return PredictionResponse(prediction=result)
    except FileNotFoundError:
        raise HTTPException(
            status_code=503,
            detail="Model not yet trained. Run ml/train.py first."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/model-info")
def model_info():
    import joblib, os
    path = os.getenv("MODEL_PATH", "models/model.joblib")
    if not os.path.exists(path):
        return {"status": "no model found"}
    model = joblib.load(path)
    return {
        "model_type": type(model).__name__,
        "model_path": path,
    }