# app/models/wallet.py
from sqlalchemy import Column, Float, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum

class WalletType(PyEnum):
    USD = "USD"
    ETH = "ETH"
    CARBON = "CARBON"

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, default=0.0)
    currency = Column(Enum(WalletType), nullable=False)  # USD, ETH, CARBON
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="wallets", lazy="joined")
