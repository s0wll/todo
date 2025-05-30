from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Integer, String, Boolean

from backend.src.database import Base


class TasksORM(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
