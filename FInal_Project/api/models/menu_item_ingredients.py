from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItemIngredient(Base):
    __tablename__ = "menu_item_ingredients"

    # Composite primary key: each menu item / ingredient pairing is unique
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.ingredient_id"), primary_key=True)
    amount_required = Column(DECIMAL(10, 2), nullable=False)
    unit = Column(String(20), nullable=False)

    menu_item = relationship("MenuItem", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="menu_items")
