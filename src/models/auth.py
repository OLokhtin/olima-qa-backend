from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class UserModel(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_email: Mapped[str]
    user_password: Mapped[str]
    user_phone: Mapped[str]
    user_name: Mapped[str]
    user_surname: Mapped[str]
    user_birthday: Mapped[date]

