from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas import UserCreate
from app.utils.password import hash_password, verify_password


def get_user_by_username(db: Session, username: str) -> User:
    """Récupérer un utilisateur par son nom d'utilisateur."""
    return db.query(User).filter(User.username == username).first()

def get_user_by_id(db: Session, user_id: int) -> User:
    """Récupérer un utilisateur par son ID."""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate) -> User:
    """Créer un nouvel utilisateur."""
   
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)

    #new user creation
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=user.is_admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str) -> User:
    """Authentifier un utilisateur."""

    db_user = get_user_by_username(db, username)
    if not db_user:
        return None

    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user
