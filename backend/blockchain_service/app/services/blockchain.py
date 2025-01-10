from fastapi import HTTPException
from app.utils.transaction_helper import (
    register_user,
    link_wallet,
    pay_for_carbon_credits,
    stake_carbon,
    approve_token
)

def register_user_service(user_address: str):
    try:
        receipt = register_user(user_address)
        return {"status": "success", "transaction_hash": receipt.transactionHash.hex()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")

def link_wallet_service(user_address: str, wallet_address: str):
    try:
        receipt = link_wallet(user_address, wallet_address)
        return {"status": "success", "transaction_hash": receipt.transactionHash.hex()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to link wallet: {str(e)}")

def pay_for_credits_service(to_address: str, amount: float):
    try:
        receipt = pay_for_carbon_credits(to_address, amount)
        return {"status": "success", "transaction_hash": receipt.transactionHash.hex()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to pay for credits: {str(e)}")

def stake_carbon_service(amount: float):
    try:
        receipt = stake_carbon(amount)
        return {"status": "success", "transaction_hash": receipt.transactionHash.hex()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to stake carbon credits: {str(e)}")
