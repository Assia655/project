from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.base import Base
from datetime import datetime

class SmartContract(Base):
    __tablename__ = "smart_contracts"

    id = Column(Integer, primary_key=True, index=True)
    contract_hash = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)  # e.g., "carbon-credit-sale"
    status = Column(String, default="active")  # active, completed, cancelled
    metadata = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
