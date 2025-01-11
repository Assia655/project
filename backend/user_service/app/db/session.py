from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
import os

#DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@user-db-service:5432/user_service_db')
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@user_db:5432/user_service_db')
#DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost:5431/carbonmarket')
#DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost:5432/user_service_db')

#moteur BD
engine = create_engine(DATABASE_URL)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()