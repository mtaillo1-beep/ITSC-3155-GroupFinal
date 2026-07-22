from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    customer_id: int
    payment_type: str  # Card | Cash | Digital Wallet
    transaction_status: str = "Pending"
    transaction_id: Optional[str] = None
    card_last4: Optional[str] = None
    amount: float


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    transaction_id: Optional[str] = None
    card_last4: Optional[str] = None
    amount: Optional[float] = None


class Payment(PaymentBase):
    payment_id: int

    class Config:
        from_attributes = True
