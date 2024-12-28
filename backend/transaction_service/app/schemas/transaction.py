from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime


class TransactionType(str, Enum):
    PAYMENT = "payment"
    VIREMENT = "virement"


class TransactionCreate(BaseModel):
    buyer_id: int
    announcement_id: int
    credit_amount: float
    currency: str
    type: TransactionType


class TransactionResponse(BaseModel):
    id: int
    seller_id: int
    buyer_id: int
    announcement_id: int
    credit_amount: float
    market_price_at_time: float  # Nouveau champ pour le prix au moment de la transaction
    total_price: float
    type: TransactionType
    transaction_date: datetime

    class Config:
        from_attributes = True
