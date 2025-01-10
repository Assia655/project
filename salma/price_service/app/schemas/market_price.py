from pydantic import BaseModel
from datetime import datetime

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
