from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from .order_items import OrderItem


class OrderBase(BaseModel):
    customer_id: int
    tracking_number: str
    order_type: str  # Takeout | Delivery
    status: str = "Pending"
    total_price: float = 0.00
    promotion_id: Optional[int] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    promotion_id: Optional[int] = None
    tracking_number: Optional[str] = None
    order_type: Optional[str] = None
    status: Optional[str] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    order_id: int
    order_date: datetime
    order_items: List[OrderItem] = []

    class Config:
        from_attributes = True
