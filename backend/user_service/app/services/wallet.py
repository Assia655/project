from sqlalchemy.orm import Session
from app.models.wallet import Wallet
from app.schemas import WalletCreate

def create_wallet_service(db: Session, wallet_data: WalletCreate):
    """Créer un wallet pour un utilisateur."""
    wallet = Wallet(
        user_id=wallet_data.user_id,
        balance=wallet_data.balance,
        currency=wallet_data.currency
    )
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet

def get_wallets_by_user_service(db: Session, user_id: int):
    """Récupérer les wallets d'un utilisateur."""
    return db.query(Wallet).filter(Wallet.user_id == user_id).all()

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
