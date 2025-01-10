from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.blockchain import LinkWalletRequest, RegisterUserRequest


from app.services.blockchain import (
    register_user_service,
    link_wallet_service,
    pay_for_credits_service,
    stake_carbon_service
)
from app.utils.auth import get_current_user  

app = FastAPI()

# Route protégée pour valider les utilisateurs
@app.get("/protected-route")
def protected_route(user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {user['username']}!"}

# Enregistrer un utilisateur sur la blockchain
@app.post("/blockchain/register")
async def register_user_endpoint(
    request: RegisterUserRequest, user: dict = Depends(get_current_user)
):
    """Endpoint pour enregistrer un utilisateur sur la blockchain."""
    try:
        username = user.get("username")
        print(f"User {username} is registering address {request.user_address}")
        return await register_user_service(request.user_address)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")
    
@app.post("/blockchain/link_wallet")
async def link_wallet_endpoint(
    request: LinkWalletRequest,  
    user: dict = Depends(get_current_user),
):
    user_address = request.user_address
    wallet_address = request.wallet_address
    username = user.get("username")
    return await link_wallet_service(user_address, wallet_address)

# Payer pour des crédits carbone
@app.post("/blockchain/pay")
async def pay_for_credits_endpoint(
    to_address: str, amount: float, user: dict = Depends(get_current_user)
):
    username = user.get("username")  
    return await pay_for_credits_service(to_address, amount)

# Staker des crédits carbone
@app.post("/blockchain/stake")
async def stake_carbon_endpoint(amount: float, user: dict = Depends(get_current_user)):
    username = user.get("username")  
    return await stake_carbon_service(amount)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vous pouvez spécifier des domaines précis au lieu de "*"
    allow_credentials=True,
    allow_methods=["*"],  # Permet tous les types de requêtes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permet tous les en-têtes
)