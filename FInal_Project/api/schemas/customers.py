from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True
