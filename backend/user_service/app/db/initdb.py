
import os
import sys
# repertoire `user_service/app` l chemin Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import engine
from app.db.base import Base 
from app.models.user import User, UserProfile
from app.models.wallet import Wallet


def create_tables():
    from db.base import Base
    Base.metadata.create_all(bind=engine)
