from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


# Schéma de base pour une annonce
class AnnouncementBase(BaseModel):
    credit_amount: float = Field(..., description="Quantité de crédits carbone à vendre")
    market_price_at_creation: float = Field(..., description="Prix du marché au moment de la création")
    currency: str = Field(..., description="Devise utilisée (ex: USD, ETH)")
    is_active: bool = Field(default=True, description="Statut de l'annonce")


# Schéma pour créer une annonce
class AnnouncementCreate(AnnouncementBase):
    seller_id: int = Field(..., description="ID du vendeur")


# Schéma pour afficher une annonce
class Announcement(AnnouncementBase):
    id: int
    created_at: datetime = Field(..., description="Date de création de l'annonce")

    class Config:
        from_attributes = True  # Pour SQLAlchemy ORM
