from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import declarative_base
from datetime import datetime
from app.db.base import Base


class MarketPrice(Base):
    __tablename__ = "market_prices"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String, nullable=False, default="MCO2") 
    price = Column(Float, nullable=False)  
    timestamp = Column(DateTime, default=func.now())  

  

