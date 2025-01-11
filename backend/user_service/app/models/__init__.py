# models/__init__.py
from models.user import User
from models.wallet import Wallet
from db.base import Base  # Base doit être importée ici pour collecter toutes les métadonnées
