import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.session import engine
from db.base import Base

def create_tables():
    from db.base import Base
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
