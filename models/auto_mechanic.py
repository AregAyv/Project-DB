from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, Date
import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from models.order import Order
from typing import List

Base = declarative_base()


class AutoMechanic(Base):
    __tablename__ = "AutoMechanic"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Full_name: Mapped[str] = mapped_column()
    Experience: Mapped[int] = mapped_column()
    Discharge: Mapped[str] = mapped_column()
    Planned_end_date: Mapped[datetime] = mapped_column()
    Personnel_Number: Mapped[int] = mapped_column()

    orders: Mapped[List["Order"]] = relationship(back_populates='auto_mechanic')
