from sqlalchemy import Column, Integer, String, DECIMAL, Date, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    promotion_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_amount = Column(DECIMAL(6, 2), nullable=False)
    expiration_date = Column(Date, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    orders = relationship("Order", back_populates="promotion")
