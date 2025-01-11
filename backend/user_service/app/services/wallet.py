from sqlalchemy.orm import Session
from models.wallet import Wallet
from schemas import WalletCreate, WalletCurrency
from models.wallet import Wallet
from schemas import WalletCreate, WalletCurrency

def create_wallet_service(db: Session, wallet_create: WalletCreate):
    db_wallet = Wallet(
        user_id=wallet_create.user_id,
        balance=wallet_create.balance,
        currency=WalletCurrency(wallet_create.currency) 
    )

    if db_wallet.currency == "ETH": 
        db_wallet.address = "adresse_unique_pour_ethereum"  
    else:
        db_wallet.address = None  # Pour USD et CARBON
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)

    return db_wallet

def get_wallets_by_user_service(db: Session, user_id: int):
    """Récupérer les wallets d'un utilisateur."""
    return db.query(Wallet).filter(Wallet.user_id == user_id).all()

def get_wallets_by_user_service_currency(db: Session, user_id: int, currency:str):
    """Récupérer les wallets d'un utilisateur."""
    return db.query(Wallet).filter((Wallet.user_id == user_id),(Wallet.currency==currency)).all()

def get_user_wallet_balance(db: Session, user_id: int):
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id, Wallet.currency == currency).first()
    if wallet:
        return wallet.balance
    return None


def update_wallet_balance_service(db: Session, wallet_id: int, new_balance: float):
    """Mettre à jour le solde d'un wallet."""
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        return None
    wallet.balance = new_balance
    db.commit()
    db.refresh(wallet)
    return wallet

def delete_wallet_service(db: Session, wallet_id: int):
    """Supprimer un wallet."""
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if wallet:
        db.delete(wallet)
        db.commit()
        return True
    return False
