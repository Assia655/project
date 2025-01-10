from fastapi import FastAPI, Depends
from app.services.blockchain import (
    register_user_service,
    link_wallet_service,
    pay_for_credits_service,
    stake_carbon_service
)
from app.utils.auth import get_current_user  # Validation du token JWT

app = FastAPI()

@app.post("/blockchain/register")
async def register_user_endpoint(user_address: str, user: dict = Depends(get_current_user)):
    """Enregistrer un utilisateur sur la blockchain."""
    # Vérification utilisateur à partir du token
    username = user.get("username")
    return await register_user_service(user_address)

@app.post("/blockchain/link_wallet")
async def link_wallet_endpoint(user_address: str, wallet_address: str, user: dict = Depends(get_current_user)):
    """Lier un portefeuille à un utilisateur."""
    # Vérification utilisateur à partir du token
    username = user.get("username")
    return await link_wallet_service(user_address, wallet_address)

@app.post("/blockchain/pay")
async def pay_for_credits_endpoint(to_address: str, amount: float, user: dict = Depends(get_current_user)):
    """Payer pour des crédits carbone."""
    # Vérification utilisateur à partir du token
    username = user.get("username")
    return await pay_for_credits_service(to_address, amount)

@app.post("/blockchain/stake")
async def stake_carbon_endpoint(amount: float, user: dict = Depends(get_current_user)):
    """Staker des crédits carbone."""
    # Vérification utilisateur à partir du token
    username = user.get("username")
    return await stake_carbon_service(amount)
