from sqlalchemy.ext.declarative import declarative_base

# Classe de base pour tous les modèles SQLAlchemy
Base = declarative_base()


# Importer tous les modèles ici pour Alembic
from app.models.announcements import Announcement
def get_transaction():
    from app.models.transactions import Transaction  # Importation différée
    return Transaction
from app.models.marcket_prices import MarketPrice
