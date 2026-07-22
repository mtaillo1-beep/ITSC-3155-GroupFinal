from datetime import datetime
from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.promotion_id"), nullable=True)
    order_date = Column(DATETIME, nullable=False, default=datetime.now)
    tracking_number = Column(String(50), unique=True, nullable=False)
    order_type = Column(String(20), nullable=False)  # Takeout | Delivery
    status = Column(String(30), nullable=False, default="Pending")
    total_price = Column(DECIMAL(8, 2), nullable=False, default=0.00)

    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)
