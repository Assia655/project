from pydantic import BaseModel
from datetime import datetime

class CarbonEmissionsDataCreate(BaseModel):
    date: str
    price: float
    change_percent: str
    price_eth: float

class CarbonEmissionsDataResponse(BaseModel):
    date: str
    price: float
    change_percent: str
    price_eth: float
    timestamp: datetime

class MarketPriceCreate(BaseModel):
    currency: str
    price: float

class MarketPriceResponse(BaseModel):
    id: int
    currency: str
    price: float
    timestamp: datetime

class Config:
    from_attributes = True
