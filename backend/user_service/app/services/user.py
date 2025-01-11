from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.user import User
# from models.wallet import 
from schemas import UserCreate, WalletCreate
from services.wallet import create_wallet_service 
from models.wallet import WalletCurrency
from utils.password import hash_password, verify_password
from models.user import User
from models.wallet import WalletCurrency
from schemas import UserCreate, WalletCreate
from services.wallet import create_wallet_service 
from utils.password import hash_password, verify_password

def get_user_by_username(db: Session, username: str) -> User:
    """Récupérer un utilisateur par son nom d'utilisateur."""
    return db.query(User).filter(User.username == username).first()

def get_user_by_id(db: Session, user_id: int) -> User:
    """Récupérer un utilisateur par son ID."""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate) -> User:
    """Créer un nouvel utilisateur."""
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Nom d'utilisateur déjà utilisé")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email déjà utilisé")

    hashed_password = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=user.is_admin,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        wallet_types = [WalletCurrency.EURO, WalletCurrency.ETH, WalletCurrency.CARBON]
        for currency in WalletCurrency:  # Iterate through enum directly
            print(f"Creating wallet for {currency}")
            wallet_data = WalletCreate(
                user_id=db_user.id,
                balance=0.0,
                currency=currency  # Use the enum directly
            )
            create_wallet_service(db,wallet_data)

        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

def authenticate_user(db: Session, username: str, password: str) -> User:
    """Authentifier un utilisateur."""
    db_user = get_user_by_username(db, username)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user
