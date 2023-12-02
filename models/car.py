from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import List
from connect import Base


class Car(Base):
    __tablename__ = "Car"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Owners_full_name: Mapped[str] = mapped_column(String, nullable=False)
    Brand: Mapped[str] = mapped_column(String, nullable=False)
    Number: Mapped[int] = mapped_column(Integer, nullable=False)
    Year_of_issue: Mapped[int] = mapped_column(Integer, nullable=False)

    # orders: Mapped[List["Order"]] = relationship(back_populates="car")
