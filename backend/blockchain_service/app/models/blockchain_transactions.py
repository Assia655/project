from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.base import Base
from datetime import datetime

class BlockchainTransaction(Base):
    __tablename__ = "blockchain_transactions"

    id = Column(Integer, primary_key=True, index=True)
    tx_hash = Column(String, unique=True, nullable=False)
    sender = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    confirmations = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
