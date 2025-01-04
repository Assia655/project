from pydantic import BaseModel, field_validator
from typing import Literal, Optional
from enum import Enum
from datetime import datetime


class TransactionType(str, Enum):
    PAYMENT = "payment"
    VIREMENT = "virement"
    FAILED = "failed"    

class TransactionCreate(BaseModel):
    buyer_id: int
    announcement_id: Optional[int] = None
    recipient_id: Optional[int] = None
    credit_amount: float
    currency: Literal["USD"]  # Restreint aux devises supportées
    type: TransactionType

    @field_validator("*", mode="after")
    def check_transaction_fields(cls, values):
        credit_amount = values.get('credit_amount')
        if credit_amount <= 0:
            raise ValueError("credit_amount must be greater than 0")
        transaction_type = values.get('type')
        announcement_id = values.get('announcement_id')
        recipient_id = values.get('recipient_id')

        if transaction_type == TransactionType.PAYMENT and not announcement_id:
            raise ValueError("announcement_id is required for PAYMENT transactions")
        if transaction_type == TransactionType.VIREMENT and not recipient_id:
            raise ValueError("recipient_id is required for VIREMENT transactions")

        return values
    class Config:
        schema_extra = {
    
            "examples": {
                "payment": {
                    "buyer_id": 3,
                    "announcement_id": 5,
                    "credit_amount": 100.0,
                    "currency": "USD",
                    "type": "payment"
                },
                "virement": {
                    "buyer_id": 3,
                    "recipient_id": 7,
                    "credit_amount": 50.0,
                    "currency": "CARBON",
                    "type": "virement"
                }
            }
    
        }


class TransactionResponse(BaseModel):
    id: int  # Identifiant unique de la transaction
    buyer_id: int  # L'utilisateur qui a initié la transaction
    seller_id: Optional[int] = None  # Le vendeur ou destinataire
    announcement_id: Optional[int] = None  # L'annonce associée à la transaction (si applicable)
    credit_amount: float  # Montant de la transaction
    price_at_transaction: Optional[float] = None  # Prix du marché (pour les PAYMENT)
    total_price: Optional[float] = None  # Prix total calculé (pour les PAYMENT)
    currency: str  # Devise ou actif (USD, CARBON, MCO2, etc.)
    type: TransactionType  # Type de la transaction
    transaction_date: datetime  # Date de la transaction
    status: str  # Statut de la transaction (ex. pending, completed)
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "buyer_id": 3,
                "seller_id": 5,
                "announcement_id": 5,
                "credit_amount": 100.0,
                "price_at_transaction": 0.372777,
                "total_price": 37.28,
                "currency": "USD",
                "type": "payment",
                "transaction_date": "2025-01-01T12:00:00",
                "status": "completed"
            }
        }
        from_attributes = True
