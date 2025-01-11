from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
import os

# Récupérer l'URL de la base de données à partir des variables d'environnement ou définir par défaut
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@transaction_db:5432/transaction_service_db')

# Créer l'engine SQLAlchemy
engine = create_engine(DATABASE_URL)

# Sessionmaker pour gérer les sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
