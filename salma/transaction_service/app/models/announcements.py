from sqlalchemy import Boolean, Column, Integer, ForeignKey, Float, Enum, DateTime, String
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime


class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, nullable=False)  
    credit_amount = Column(Float, nullable=False) 
    market_price_at_creation = Column(Float, nullable=False) 
    is_active = Column(Boolean, default=True) 
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relations
    transactions = relationship("Transaction", back_populates="announcement")

    

