from typing import Optional
from pydantic import BaseModel


class MenuItemIngredientBase(BaseModel):
    menu_item_id: int
    ingredient_id: int
    amount_required: float
    unit: str


class MenuItemIngredientCreate(MenuItemIngredientBase):
    pass


class MenuItemIngredientUpdate(BaseModel):
    amount_required: Optional[float] = None
    unit: Optional[str] = None


class MenuItemIngredient(MenuItemIngredientBase):
    class Config:
        from_attributes = True
