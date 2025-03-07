from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)

@dataclass
class Dish(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(20), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(sa.String(30), nullable=False)
    price: Mapped[float] = mapped_column(sa.Float, default=0.00, nullable=False)
