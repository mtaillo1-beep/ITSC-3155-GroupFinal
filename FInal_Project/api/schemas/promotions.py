from typing import Optional
from datetime import date
from pydantic import BaseModel


class PromotionBase(BaseModel):
    code: str
    discount_amount: float
    expiration_date: date
    is_active: bool = True


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount_amount: Optional[float] = None
    expiration_date: Optional[date] = None
    is_active: Optional[bool] = None


class Promotion(PromotionBase):
    promotion_id: int

    class Config:
        from_attributes = True
