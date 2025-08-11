import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from dotenv import load_dotenv

load_dotenv()
DB_HOST=os.getenv("DB_HOST")
DB_PASS=os.getenv("DB_PASS")
DB_USER=os.getenv("DB_USER")
DB_NAME=os.getenv("DB_NAME")
DB_PORT=os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    """
    Dependency to get a database session for each request.

    This function is a generator that will:
    1. Create a new database session (`db`) from the SessionLocal factory.
    2. `yield` this session to the API endpoint that depends on it.
    3. The code in the endpoint will run.
    4. Once the endpoint is finished, the code here resumes.
    5. The `finally` block ensures that the session is always closed,
       even if an error occurred in the endpoint. This prevents
       leaving open connections to the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()