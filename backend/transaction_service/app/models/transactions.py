from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum
from db.base import Base

# Définir les types de transactions
class TransactionType(str, Enum):
    PAYMENT = "payment"
    VIREMENT = "virement"

# Modèle de la table transactions
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, nullable=False)
    seller_id = Column(Integer, nullable=True)
    announcement_id = Column(Integer, ForeignKey("announcements.id"), nullable=True)
    credit_amount = Column(Float, nullable=False)
    price_at_transaction = Column(Float, nullable=True)
    total_price = Column(Float, nullable=True)
    currency = Column(String, nullable=False)
    type = Column(String, nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")

    announcement = relationship("Announcement", back_populates="transactions")