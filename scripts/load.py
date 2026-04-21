import pandas as pd
from database.db_connection import get_engine
from database.models import create_tables

CLEAN_PATH = "data/cleaned_healthcare.csv"

def load_clean_data():
    engine = get_engine()
    create_tables(engine)

    df = pd.read_csv(CLEAN_PATH)
    print(f"[load] {len(df)} cleaned records to load")

    # Use INSERT IGNORE pattern: append only, rely on DB uniqueness or replace
    df.to_sql(
        "cleaned_patients",
        engine,
        if_exists="append",   # change to "replace" to start fresh
        index=False,
        method="multi",       # faster batch inserts
        chunksize=500
    )
    print("[load] Cleaned data loaded into 'cleaned_patients' ✓")

if __name__ == "__main__":
    load_clean_data()