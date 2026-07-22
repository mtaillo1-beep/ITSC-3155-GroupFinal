from datetime import datetime
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"), nullable=False)
    # Ties the review to a purchased item, verifying the customer actually ordered it
    order_item_id = Column(Integer, ForeignKey("order_items.order_item_id"), nullable=False)
    score = Column(Integer, nullable=False)  # 1-5
    review_text = Column(String(1000), nullable=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now)

    customer = relationship("Customer", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")
    order_item = relationship("OrderItem", back_populates="review")
