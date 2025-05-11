from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


@dataclass
class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, default=0.00, nullable=False)


@dataclass
class Role(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(10), unique=True, nullable=False)
    user: Mapped[list["User"]] = relationship(back_populates="role")


@dataclass
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(sa.String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey("role.id"))
    role: Mapped["Role"] = relationship(back_populates="user")
