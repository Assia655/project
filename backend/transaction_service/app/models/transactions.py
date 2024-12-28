from sqlalchemy import Column, Integer, String, Float, ForeignKey,  Enum as SqlEnum, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum
from app.db.base import Base

# Enum  types_trans
class TransactionType(str, Enum):
    PAYMENT = "payment"
    VIREMENT = "virement"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, nullable=False) 
    buyer_id = Column(Integer, nullable=False)
    announcement_id = Column(Integer, ForeignKey("announcements.id"), nullable=True)  
    credit_amount = Column(Float, nullable=False)
    price_at_transaction = Column(Float, nullable=False) 
    total_price = Column(Float, nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="pending")

    announcement = relationship("Announcement", back_populates="transactions")





