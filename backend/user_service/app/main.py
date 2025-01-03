from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.db.session import get_db
from app.schemas import UserCreate, User, UserProfileCreate, UserProfileResponse, UserResponse, WalletCreate, WalletResponse
from app.services.user import authenticate_user, create_user, get_user_by_id
from app.utils.jwt import create_access_token, verify_access_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="user_service")

# Endpoint pour créer un utilisateur
@app.post("/users/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """Créer un utilisateur directement."""
    return create_user(db, user)

# Endpoint pour récupérer un utilisateur par ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """Récupérer un utilisateur par son ID."""
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Endpoint pour l'inscription (register)
@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """Créer un nouvel utilisateur."""
    return create_user(db, user)

# Endpoint pour la connexion (login)
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint protégé pour vérifier l'utilisateur connecté
@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": payload["sub"]}

# ENDPOINTS POUR LES WALLETS
# ===========================
from app.services.wallet import (
    create_wallet_service,
    get_wallets_by_user_service,
    update_wallet_balance_service,
    delete_wallet_service,
)

@app.post("/wallets/", response_model=WalletResponse)
def create_wallet(wallet: WalletCreate, db: Session = Depends(get_db)):
    return create_wallet_service(db, wallet)

@app.get("/wallets/{user_id}", response_model=list[WalletResponse])
def get_wallets(user_id: int, db: Session = Depends(get_db)):
    return get_wallets_by_user_service(db, user_id)

@app.put("/wallets/{wallet_id}", response_model=WalletResponse)
def update_wallet_balance(wallet_id: int, balance: float, db: Session = Depends(get_db)):
    wallet = update_wallet_balance_service(db, wallet_id, balance)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@app.delete("/wallets/{wallet_id}")
def delete_wallet(wallet_id: int, db: Session = Depends(get_db)):
    if not delete_wallet_service(db, wallet_id):
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"message": "Wallet deleted successfully"}


# ================================
# ENDPOINTS POUR LES USER PROFILES
# ================================

from app.services.user_profil import (
    create_user_profile_service,
    get_user_profile_service,
    update_user_profile_service,
    delete_user_profile_service,
)
@app.post("/user_profiles/", response_model=UserProfileResponse)
def create_user_profile(profile: UserProfileCreate, db: Session = Depends(get_db)):
    return create_user_profile_service(db, profile)

@app.get("/user_profiles/{user_id}", response_model=UserProfileResponse)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    profile = get_user_profile_service(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile

@app.put("/user_profiles/{user_profile_id}", response_model=UserProfileResponse)
def update_user_profile(user_profile_id: int, is_seller: bool, is_buyer: bool, db: Session = Depends(get_db)):
    profile = update_user_profile_service(db, user_profile_id, is_seller, is_buyer)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile

@app.delete("/user_profiles/{user_profile_id}")
def delete_user_profile(user_profile_id: int, db: Session = Depends(get_db)):
    if not delete_user_profile_service(db, user_profile_id):
        raise HTTPException(status_code=404, detail="User profile not found")
    return {"message": "User profile deleted successfully"}
