from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import declarative_base
from datetime import datetime
from db.base import Base


class MarketPrice(Base):
      __tablename__ = "market_prices"
      date = Column(String(50), primary_key=True, nullable=False)
      price = Column(Float, nullable=False)
      change_percent = Column(String(50), nullable=True)
      price_eth = Column(Float, nullable=False)
      timestamp = Column(DateTime, server_default=func.current_timestamp(), nullable=False)

class CarbonEmissionsData(Base):
  __tablename__ = "carbon_emissions_data"

  date = Column(String(50), primary_key=True, nullable=False)
  price = Column(Float, nullable=False)
  change_percent = Column(String(50), nullable=True)
  price_eth = Column(Float, nullable=False)
  timestamp = Column(DateTime, server_default=func.current_timestamp(), nullable=False)

