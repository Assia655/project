
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
import os

DATABASE_URL = os.getenv('DATABASE_URL', "postgresql://postgres:1234@localhost:5431/carbon_prices")


#moteur BD
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
