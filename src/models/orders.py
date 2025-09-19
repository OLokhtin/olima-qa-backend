from datetime import datetime, date

from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class OrderModel(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    customer_full_name: Mapped[str]
    customer_phone: Mapped[str]
    customer_email: Mapped[str]
    delivery_address: Mapped[str]
    delivery_date: Mapped[date]
    total_amount: Mapped[int]