# models/__init__.py
from app.models.user import User, UserProfile
from app.models.wallet import Wallet

from app.db.base import Base  # Base doit être importée ici pour collecter toutes les métadonnées
