from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from models.order import Order
from typing import List

Base = declarative_base()


class Car(Base):
    __tablename__ = "Car"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Owners_full_name: Mapped[str] = mapped_column()
    Brand: Mapped[str] = mapped_column()
    Number: Mapped[int] = mapped_column()
    Year_of_issue: Mapped[int] = mapped_column()

    orders: Mapped[List["Order"]] = relationship(back_populates="car")


