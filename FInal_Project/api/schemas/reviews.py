from typing import Optional
from datetime import datetime
from pydantic import BaseModel, conint


class ReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    order_item_id: int
    score: conint(ge=1, le=5)
    review_text: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    score: Optional[conint(ge=1, le=5)] = None
    review_text: Optional[str] = None


class Review(ReviewBase):
    review_id: int
    created_at: datetime

    class Config:
        from_attributes = True
