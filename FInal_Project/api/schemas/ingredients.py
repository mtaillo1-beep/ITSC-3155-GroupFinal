from typing import Optional
from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str
    amount_on_hand: float = 0.00
    unit: str


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    amount_on_hand: Optional[float] = None
    unit: Optional[str] = None


class Ingredient(IngredientBase):
    ingredient_id: int

    class Config:
        from_attributes = True
