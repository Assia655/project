from typing import TYPE_CHECKING, List, Optional
from pydantic import BaseModel, EmailStr
from enum import Enum

if TYPE_CHECKING:
    from app.models.user import UserProfile
    from app.models.wallet import Wallet

# Enum pour Wallet
class WalletCurrency(str, Enum):
    USD = "USD"
    ETH = "ETH"
    CARBON = "CARBON"

# Schéma pour Wallet
class WalletCreate(BaseModel):
    user_id: int
    balance: float
    currency: WalletCurrency  

class WalletResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    currency: WalletCurrency  # Représente la valeur sous forme de chaîne de caractères
    address: Optional[str] = None  # Champ adresse pour le wallet

    class Config:
        orm_mode = True
        use_enum_values = True
        
      

# Schéma pour UserProfile
class UserProfileCreate(BaseModel):
    user_id: int
    is_seller: bool
    is_buyer: bool

class UserProfileResponse(BaseModel):
    id: int
    user_id: int
    is_seller: bool
    is_buyer: bool

    class Config:
        orm_mode = True

# Schéma de base pour l'utilisateur
class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_admin: bool = False

class UserCreate(UserBase):
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool
    profile: Optional[UserProfileResponse]
    wallets: List[WalletResponse]

    class Config:
        orm_mode = True

# Schéma pour la réponse utilisateur
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    profile: Optional[UserProfileResponse]
    wallets: List[WalletResponse]

    class Config:
        orm_mode = True
