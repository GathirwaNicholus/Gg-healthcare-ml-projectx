import pandas as pd
import joblib
from ml.preprocess import encode_features, TARGET_INVERSE

MODEL_PATH = "models/model.joblib"

def predict_single(input_dict: dict) -> str:
    """
    Takes a dict of patient features, returns predicted label.
    Example input:
    {
        "age": 45, "gender": "Male", "blood_type": "A+",
        "medical_condition": "Diabetes", "insurance_provider": "Medicare",
        "billing_amount": 25000.0, "room_number": 205,
        "admission_type": "Elective", "medication": "Aspirin",
        "length_of_stay": 5, "admission_month": 6, "admission_year": 2023
    }
    """
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([input_dict])
    df_encoded, _ = encode_features(df, fit=False)

    # Remove target column if accidentally included
    df_encoded = df_encoded.drop(columns=["test_results"], errors="ignore")

    prediction_int = model.predict(df_encoded)[0]
    return TARGET_INVERSE.get(int(prediction_int), "Unknown")