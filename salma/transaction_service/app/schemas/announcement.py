from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AnnouncementBase(BaseModel):
    seller_id: int
    credit_amount: float
    market_price_at_creation: float
    is_active: Optional[bool] = True


class AnnouncementCreate(AnnouncementBase):
    pass


class AnnouncementUpdate(BaseModel):
    credit_amount: Optional[float]
    is_active: Optional[bool]


class AnnouncementResponse(BaseModel):
    id: int
    seller_id: int
    credit_amount: float
    market_price_at_creation: float
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True




        

