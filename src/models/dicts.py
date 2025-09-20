from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class DictModel(Base):
    __tablename__ = "dicts"
    id: Mapped[int] = mapped_column(primary_key=True)
    dict_key: Mapped[str]
    self_id: Mapped[int]
    value: Mapped[str]
    description: Mapped[str]