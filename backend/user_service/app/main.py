from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db.session import get_db
from schemas import (
    UserCreate,
    UserResponse,
    WalletCreate,
    WalletResponse,
    UserProfileCreate,
    UserProfileResponse,
)
from services.user import (
    authenticate_user,
    create_user,
    get_user_by_username,
)
from services.wallet import (
    create_wallet_service,
    get_user_wallet_balance,
    get_wallets_by_user_service,
    get_wallets_by_user_service_currency,
    update_wallet_balance_service,
    delete_wallet_service,
)
from services.user_profil import (
    create_user_profile_service,
    get_user_profile_service,
    update_user_profile_service,
    delete_user_profile_service,
)
from utils.jwt import create_access_token, verify_access_token
from db.initdb import create_tables

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup logic
#     print("Starting up...")
#     # Check database readiness
#     while True:
#         try:
#             conn = psycopg2.connect(
#                 dbname="user_service_db",
#                 user="postgres",
#                 password="1234",
#                 host="user_db",
#                 port="5432"
#             )
#             conn.close()
#             print("Database is ready!")
#             break
#         except psycopg2.OperationalError:
#             print("Database is not ready, waiting...")
#             time.sleep(5)
#     # Initialize tables
#     #create_tables()
#     yield  # Application runs here
#     # Shutdown logic
#     print("Shutting down...")
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.on_event("startup")
async def startup_event():
    create_tables()

# ====================================================
# Endpoint pour vérifier l'état de santé du service
# ====================================================
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# ====================================================
# Authentification & gestion des utilisateurs
# ====================================================
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer","user_id":user.id}

@app.post("/users/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """Créer un utilisateur et ses wallets par défaut."""
    new_user = create_user(db, user)
    # Création automatique des wallets pour l'utilisateur (EURO, ETH, CARBON)
    return new_user

@app.get("/users/me", response_model=UserResponse)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Vérifier et retourner l'utilisateur connecté via son token."""
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    username = payload.get("sub")
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user




# ====================================================
# Gestion des wallets
# ====================================================
@app.post("/wallets/", response_model=WalletResponse)
def create_wallet(wallet: WalletCreate, db: Session = Depends(get_db)):
    return create_wallet_service(db, wallet)

@app.get("/wallets/{user_id}", response_model=list[WalletResponse])
def get_wallets(user_id: int, db: Session = Depends(get_db)):
    wallets = get_wallets_by_user_service(db, user_id)
    return [WalletResponse.from_orm(wallet) for wallet in wallets]

@app.get("/wallets/{user_id}/{currency}", response_model=list[WalletResponse])
def get_wallets_currency(user_id: int,currency:str, db: Session = Depends(get_db)):
    wallets = get_wallets_by_user_service_currency(db, user_id, currency)
    return [WalletResponse.from_orm(wallet) for wallet in wallets]


@app.put("/wallets/{wallet_id}", response_model=WalletResponse)
def update_wallet_balance(wallet_id: int, balance: float, db: Session = Depends(get_db)):
    wallet = update_wallet_balance_service(db, wallet_id, balance)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@app.get("/wallet/balance/{user_id}/{currency}")
async def get_wallet_balance(user_id: int, currency: str, db: Session = Depends(get_db)):
    balance = get_user_wallet_balance(db, user_id, currency)
    if balance is not None:
        return {"user_id": user_id, "currency": currency, "balance": balance}
    raise HTTPException(status_code=404, detail="Wallet not found for this user and currency")


@app.delete("/wallets/{wallet_id}")
def delete_wallet(wallet_id: int, db: Session = Depends(get_db)):
    if not delete_wallet_service(db, wallet_id):
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"message": "Wallet deleted successfully"}



# ====================================================
# Gestion des profils utilisateurs
# ====================================================
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
