import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

ENCODER_PATH = "models/label_encoders.joblib"

CATEGORICAL_COLS = [
    "gender", "blood_type", "medical_condition",
    "insurance_provider", "admission_type", "medication"
]

TARGET_COL = "test_results"
TARGET_MAP = {"Normal": 0, "Abnormal": 1, "Inconclusive": 2}
TARGET_INVERSE = {v: k for k, v in TARGET_MAP.items()}

# Drop these columns before training
DROP_COLS = ["hospital"]  # high cardinality, optional to keep

def encode_features(df: pd.DataFrame, fit: bool = True):
    """
    Encode categorical features.
    fit=True  → fit new encoders and save (training time).
    fit=False → load saved encoders and transform (inference time).
    """
    df = df.copy()

    # Drop irrelevant columns
    df = df.drop(columns=[c for c in DROP_COLS if c in df.columns], errors="ignore")

    if fit:
        encoders = {}
        for col in CATEGORICAL_COLS:
            if col in df.columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                encoders[col] = le
        os.makedirs("models", exist_ok=True)
        joblib.dump(encoders, ENCODER_PATH)
    else:
        encoders = joblib.load(ENCODER_PATH)
        for col in CATEGORICAL_COLS:
            if col in df.columns:
                le = encoders[col]
                # Handle unseen labels gracefully
                df[col] = df[col].astype(str).apply(
                    lambda x: le.transform([x])[0]
                    if x in le.classes_ else -1
                )

    # Encode target
    if TARGET_COL in df.columns:
        df[TARGET_COL] = df[TARGET_COL].map(TARGET_MAP)

    return df, encoders if fit else joblib.load(ENCODER_PATH)


def get_X_y(df: pd.DataFrame):
    """Split into features and target."""
    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]
    return X, y