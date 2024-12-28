from sqlalchemy.orm import Session
from app.models.transactions import Transaction
from app.schemas.transaction import TransactionCreate
from app.utils.user_service_api import get_wallet_balance, update_wallet_balance
from app.services.marcket_price import get_market_price

def create_transaction(db: Session, transaction_data: TransactionCreate):
    """Créer une transaction."""
    # Valider les utilisateurs
    seller_balance = get_wallet_balance(transaction_data.seller_id, "CARBON")
    buyer_balance = get_wallet_balance(transaction_data.buyer_id, transaction_data.currency)

    if seller_balance is None or buyer_balance is None:
        raise ValueError("Invalid wallet information")

    # Récupérer le prix actuel du marché pour la devise spécifiée
    market_price = get_market_price(transaction_data.currency)
    total_price = transaction_data.credit_amount * market_price

    if buyer_balance < total_price:
        raise ValueError("Insufficient funds in buyer's wallet")

    # Mettre à jour les balances dans les wallets
    update_wallet_balance(transaction_data.seller_id, transaction_data.credit_amount, is_seller=True)
    update_wallet_balance(transaction_data.buyer_id, -total_price, is_seller=False)

    # Enregistrer la transaction dans la base de données
    transaction = Transaction(
        seller_id=transaction_data.seller_id,
        buyer_id=transaction_data.buyer_id,
        credit_amount=transaction_data.credit_amount,
        market_price_at_time=market_price,
        type=transaction_data.type,
        total_price=total_price,
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_transaction_by_id(db: Session, transaction_id: int):
    """Récupérer une transaction par ID."""
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def get_all_transactions(db: Session):
    """Récupérer toutes les transactions."""
    return db.query(Transaction).all()
