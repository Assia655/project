from db.session import engine
from db.base import Base

def create_tables():
    """Créer les tables dans la base de données."""
    Base.metadata.create_all(bind=engine)
    print("Tables créées dans la base de données.")

if __name__ == "__main__":
    create_tables()
