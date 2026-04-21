from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
import numpy as np

TARGET_NAMES = ["Normal", "Abnormal", "Inconclusive"]

def evaluate_model(model, X_test, y_test, model_name: str = "") -> dict:
    y_pred = model.predict(X_test)

    accuracy  = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted", zero_division=0)
    recall    = recall_score(y_test, y_pred, average="weighted", zero_division=0)
    f1_w      = f1_score(y_test, y_pred, average="weighted", zero_division=0)
    cm        = confusion_matrix(y_test, y_pred)

    print(f"\n{'='*50}")
    print(f"  Model: {model_name}")
    print(f"{'='*50}")
    print(f"  Accuracy  : {accuracy:.4f}")
    print(f"  Precision : {precision:.4f}")
    print(f"  Recall    : {recall:.4f}")
    print(f"  F1 (wt'd) : {f1_w:.4f}")
    print(f"\nConfusion Matrix:\n{cm}")
    print(f"\nClassification Report:\n"
          f"{classification_report(y_test, y_pred, target_names=TARGET_NAMES, zero_division=0)}")

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_weighted": f1_w,
        "confusion_matrix": cm.tolist(),
    }