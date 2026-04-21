import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

def get_engine():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in your .env file.")

    # Switch to psycopg v3 driver for SQLAlchemy
    url = DATABASE_URL.replace(
        "postgresql://", "postgresql+psycopg://"
    )
    return create_engine(url, echo=False)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()