from sqlalchemy.ext.declarative import declarative_base

# Classe de base pour tous les modèles SQLAlchemy
Base = declarative_base()


# Importer tous les modèles ici pour Alembic
from app.models.announcements import Announcement
from app.models.transactions import Transaction
from app.models.marcket_prices import MarketPrice
