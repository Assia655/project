from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class BlockchainHistory(Base):
    __tablename__ = "blockchain_history"

    id = Column(Integer, primary_key=True, index=True)
    user_address = Column(String, nullable=False) 
    contract_name = Column(String, nullable=False)  
    function_name = Column(String, nullable=False)  
    amount = Column(Float, nullable=True)  
    tx_hash = Column(String, nullable=False) 
    status = Column(String, default="pending")  
    timestamp = Column(DateTime, default=func.now())  
