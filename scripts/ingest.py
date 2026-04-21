import pandas as pd
from database.db_connection import get_engine

RAW_CSV_PATH = "data/raw/healthcare_dataset.csv"

def ingest_raw_data():
    engine = get_engine()
    df = pd.read_csv(RAW_CSV_PATH)
    print(f"[ingest] Loaded {len(df)} rows from {RAW_CSV_PATH}")
    print(f"[ingest] Columns: {list(df.columns)}")
    # Write to raw_patients table; replace on re-run
    df.to_sql("raw_patients", engine, if_exists="replace", index=False)
    print("[ingest] Raw data loaded into 'raw_patients' table ")

if __name__ == "__main__":
    ingest_raw_data()