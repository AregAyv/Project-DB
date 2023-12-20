from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
# from typing import List
from Base import Base


class Car(Base):
    __tablename__ = "Car"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Owners_full_name: Mapped[str] = mapped_column(String, nullable=False)
    Brand: Mapped[str] = mapped_column(String, nullable=False)
    Number: Mapped[int] = mapped_column(Integer, nullable=False)
    Year_of_issue: Mapped[int] = mapped_column(Integer, nullable=False)


