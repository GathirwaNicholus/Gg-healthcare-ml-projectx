from database.db_connection import get_engine
from sqlalchemy import text # 1. Import text

engine = get_engine()

with engine.connect() as conn:
    # 2. Wrap your raw SQL string in text()
    result = conn.execute(text("SELECT 1;")) 
    print(result.fetchall())  # Should print [(1,)]