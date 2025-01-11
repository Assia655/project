from sqlalchemy.orm import Session
from models.transactions import Transaction, TransactionType
from models.announcements import Announcement
from schemas.transaction import TransactionCreate
from utils.user_service_api import get_wallet_balance, update_wallet_balance
from utils.price_service_api import get_price


def create_transaction(db: Session, transaction_data: TransactionCreate):
    """Créer une transaction (payment ou virement)."""

    if transaction_data.type == TransactionType.PAYMENT:
        # Vérification que la devise est USD pour les transactions PAYMENT
        if transaction_data.currency != "EURO":
            raise ValueError("Only EURO is allowed for transactions involving MCO2")

        # Vérifier si l'annonce existe et est active
        announcement = db.query(Announcement).filter(Announcement.id == transaction_data.announcement_id).first()
        if not announcement or not announcement.is_active:
            raise ValueError("Invalid or inactive announcement")

        # Valider les portefeuilles des utilisateurs
        seller_balance = get_wallet_balance(announcement.seller_id, "EURO")
        buyer_balance = get_wallet_balance(transaction_data.buyer_id, "EURO")

        if seller_balance is None:
            raise ValueError(f"Seller with ID {announcement.seller_id} does not have a EURO wallet")
        if buyer_balance is None:
            raise ValueError(f"Buyer with ID {transaction_data.buyer_id} does not have a EURO wallet")

        # Récupérer le prix du marché via le service de prix
        try:
            market_price = get_price("ETH")
        except Exception as e:
            raise ValueError(f"Failed to fetch market price: {e}")

        # Calculer le prix total et vérifier le solde de l'acheteur
        total_price = transaction_data.credit_amount * market_price
        if buyer_balance < total_price:
            raise ValueError("Insufficient funds in buyer's wallet")

        # Mettre à jour les portefeuilles
        update_wallet_balance(
            wallet_id=announcement.seller_id,
            new_balance=seller_balance + transaction_data.credit_amount,
            user_id=announcement.seller_id,
            currency="EURO"
        )
        update_wallet_balance(
            wallet_id=transaction_data.buyer_id,
            new_balance=buyer_balance - total_price,
            user_id=transaction_data.buyer_id,
            currency="EURO"
        )

        # Créer et enregistrer la transaction
        transaction = Transaction(
            seller_id=announcement.seller_id,
            buyer_id=transaction_data.buyer_id,
            announcement_id=transaction_data.announcement_id,
            credit_amount=transaction_data.credit_amount,
            price_at_transaction=market_price,
            total_price=total_price,
            type=transaction_data.type,
        )
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction

    elif transaction_data.type == TransactionType.VIREMENT:
        # Valider les portefeuilles pour le virement
        sender_balance = get_wallet_balance(transaction_data.buyer_id, transaction_data.currency)
        recipient_balance = get_wallet_balance(transaction_data.recipient_id, transaction_data.currency)

        if sender_balance is None:
            raise ValueError(f"Sender with ID {transaction_data.buyer_id} does not have a {transaction_data.currency} wallet")
        if recipient_balance is None:
            raise ValueError(f"Recipient with ID {transaction_data.recipient_id} does not have a {transaction_data.currency} wallet")

        # Vérifier que l'expéditeur a un solde suffisant
        if sender_balance < transaction_data.credit_amount:
            raise ValueError("Insufficient funds in sender's wallet")

        # Mettre à jour les portefeuilles pour le virement
        update_wallet_balance(
            wallet_id=transaction_data.buyer_id,
            new_balance=sender_balance - transaction_data.credit_amount,
            user_id=transaction_data.buyer_id,
            currency=transaction_data.currency
        )
        update_wallet_balance(
            wallet_id=transaction_data.recipient_id,
            new_balance=recipient_balance + transaction_data.credit_amount,
            user_id=transaction_data.recipient_id,
            currency=transaction_data.currency
        )

        # Créer et enregistrer la transaction
        transaction = Transaction(
            buyer_id=transaction_data.buyer_id,
            seller_id=transaction_data.recipient_id,
            credit_amount=transaction_data.credit_amount,
            currency=transaction_data.currency,
            type=transaction_data.type,
        )
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction

    else:
        raise ValueError("Invalid transaction type")



def get_transaction_by_id(db: Session, transaction_id: int):
    """Récupérer une transaction par ID."""
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def get_all_transactions(db: Session):
    """Récupérer toutes les transactions."""
    return db.query(Transaction).all()

def get_transactions_by_user(db: Session, seller_id: int):
    """Récupérer les transactions pour un utilisateur spécifique"""
    return db.query(Transaction).filter(Transaction.seller_id == seller_id).all()

def get_transaction_by_user(db: Session, user_id: int):
    """Récupérer une transaction par buyer_id ou seller_id"""
    return db.query(Transaction).filter(
        (Transaction.buyer_id == user_id) | (Transaction.seller_id == user_id)
    ).first()