from sqlalchemy import Column, Integer, String, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(DECIMAL(6, 2), nullable=False)
    calories = Column(Integer, nullable=True)
    category = Column(String(50), nullable=False)
    is_available = Column(Boolean, nullable=False, default=True)

    order_items = relationship("OrderItem", back_populates="menu_item")
    ingredients = relationship("MenuItemIngredient", back_populates="menu_item")
    reviews = relationship("Review", back_populates="menu_item")
