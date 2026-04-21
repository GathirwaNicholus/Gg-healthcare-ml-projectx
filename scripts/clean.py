import pandas as pd
import numpy as np

RAW_PATH = "data/raw/healthcare_dataset.csv"
CLEAN_PATH = "data/cleaned_healthcare.csv"

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    print(f"[clean] Starting shape: {df.shape}")

    # 1. Standardise column names 
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Drop PII / irrelevant columns 
    df = df.drop(columns=["name", "doctor"], errors="ignore")

    #  3. Remove duplicates 
    before = len(df)
    df = df.drop_duplicates()
    print(f"[clean] Removed {before - len(df)} duplicate rows")

    #  4. Handle missing values
    print(f"[clean] Missing values:\n{df.isnull().sum()}")
    # Numeric: fill with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    # Categorical: fill with mode
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    #  5. Standardise categorical string values 
    for col in cat_cols:
        df[col] = df[col].str.strip().str.title()

    #  6. Convert date columns 
    df["date_of_admission"] = pd.to_datetime(df["date_of_admission"], errors="coerce")
    df["discharge_date"]    = pd.to_datetime(df["discharge_date"],    errors="coerce")

    # Drop rows where dates couldn't be parsed
    df = df.dropna(subset=["date_of_admission", "discharge_date"])

    #  7. Feature Engineering 
    df["length_of_stay"]  = (df["discharge_date"] - df["date_of_admission"]).dt.days
    df["admission_month"] = df["date_of_admission"].dt.month
    df["admission_year"]  = df["date_of_admission"].dt.year

    # Drop raw date columns (not needed for ML)
    df = df.drop(columns=["date_of_admission", "discharge_date"])

    #  8. Validate target variable 
    valid_targets = {"Normal", "Abnormal", "Inconclusive"}
    df = df[df["test_results"].isin(valid_targets)]

    #  9. Remove invalid numeric values
    df = df[df["age"] > 0]
    df = df[df["billing_amount"] >= 0]
    df = df[df["length_of_stay"] >= 0]

    print(f"[clean] Final shape: {df.shape}")
    return df

if __name__ == "__main__":
    df_raw = pd.read_csv(RAW_PATH)
    df_clean = clean_data(df_raw)
    df_clean.to_csv(CLEAN_PATH, index=False)
    print(f"[clean] Saved to {CLEAN_PATH} ")