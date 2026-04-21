import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib
import os

from database.db_connection import get_engine
from ml.preprocess import encode_features, get_X_y
from ml.evaluate import evaluate_model

MODEL_PATH = "models/model.joblib"

def load_data_from_db():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM cleaned_patients", engine)
    print(f"[train] Loaded {len(df)} records from DB")
    return df

def train():
    os.makedirs("models", exist_ok=True)

    # 1. Load data
    df = load_data_from_db()
    df = df.drop(columns=["id"], errors="ignore")

    # 2. Preprocess
    df_encoded, _ = encode_features(df, fit=True)
    X, y = get_X_y(df_encoded)

    # 3. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 4. Define models
    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=1000, random_state=42
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=100, random_state=42, n_jobs=-1
        ),
        "XGBoost": XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            use_label_encoder=False,
            eval_metric="mlogloss",
            random_state=42,
            n_jobs=-1,
        ),
    }

    # 5. Train and evaluate all models
    results = {}
    for name, model in models.items():
        print(f"\n[train] Training {name}...")
        model.fit(X_train, y_train)
        metrics = evaluate_model(model, X_test, y_test, name)
        results[name] = {"model": model, "f1": metrics["f1_weighted"]}

    # 6. Select the best model by weighted F1
    best_name = max(results, key=lambda k: results[k]["f1"])
    best_model = results[best_name]["model"]

    print(f"\n[train] Best model: {best_name} "
          f"(F1={results[best_name]['f1']:.4f})")

    # 7. Save the best model
    joblib.dump(best_model, MODEL_PATH)
    print(f"[train] Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()