from app.services.user import create_user
from app.schemas import UserCreate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User
from app.db.session import get_db

# Configuration de la base de données pour le test
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/user_service_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crée une session DB pour l'exécution de test
db = SessionLocal()

# Créer un utilisateur de test
new_user_data = UserCreate(
    username="testuser",
    email="testuser@example.com",
    password="secur123",
    is_admin=False
)

# Appel de la fonction create_user pour tester
new_user = create_user(db, new_user_data)

# Affichage du résultat
print(f"User created: {new_user.username}")
