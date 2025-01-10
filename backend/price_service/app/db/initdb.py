from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# URL de la base de données
DATABASE_URL = os.getenv('DATABASE_URL', "postgresql://postgres:1234@localhost:5432/price_service_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

