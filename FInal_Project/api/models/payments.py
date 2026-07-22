from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), unique=True, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    payment_type = Column(String(30), nullable=False)  # Card | Cash | Digital Wallet
    transaction_status = Column(String(30), nullable=False, default="Pending")
    # Store a payment token/transaction reference from the payment gateway,
    # never a full card number (PCI compliance).
    transaction_id = Column(String(100), nullable=True)
    card_last4 = Column(String(4), nullable=True)
    amount = Column(DECIMAL(8, 2), nullable=False)

    order = relationship("Order", back_populates="payment")
    customer = relationship("Customer", back_populates="payments")
