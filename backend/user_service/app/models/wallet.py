from sqlalchemy import Column, Float, ForeignKey, Integer, Enum, String
from sqlalchemy.orm import relationship
from db.base import Base
from enum import Enum as PyEnum

# Enum pour le type de monnaie
class WalletCurrency(PyEnum):
<<<<<<< HEAD
    EURO = "EURO"
=======
    USD = "USD"
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
    ETH = "ETH"
    CARBON = "CARBON"

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, default=0.0)
    currency = Column(Enum(WalletCurrency), nullable=False)  # USD, ETH, CARBON
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    address = Column(String, nullable=True)  # Colonne pour l'adresse du wallet (peut être NULL)

    owner = relationship("User", back_populates="wallets", lazy="joined")

    def set_address(self):
        """Logique pour définir l'adresse du wallet en fonction de la monnaie."""
        if self.currency == WalletCurrency.ETH:
            self.address = "adresse_unique_pour_ethereum"  # Exemple d'adresse pour ETH
        else:
            self.address = None  # Valeur NULL pour USD et CARBON
