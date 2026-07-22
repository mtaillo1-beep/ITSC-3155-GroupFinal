from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    ingredient_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    amount_on_hand = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    unit = Column(String(20), nullable=False)  # e.g. grams, oz, count

    menu_items = relationship("MenuItemIngredient", back_populates="ingredient")
