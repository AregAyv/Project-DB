import datetime
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from connect import Base


class Order(Base):
    __tablename__ = "Order"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Price: Mapped[int] = mapped_column(Numeric(10, 2), nullable=False)
    Type_of_work: Mapped[str] = mapped_column(String, nullable=False)
    Date_of_issue: Mapped[datetime.datetime] = Column(DateTime, nullable=False)
    Planned_end_date: Mapped[datetime.datetime] = Column(DateTime, nullable=False)
    Real_end_date: Mapped[datetime.datetime] = Column(DateTime, nullable=False)

    car_id: Mapped[int] = mapped_column(ForeignKey("Car.Id"))
    auto_mechanic_id: Mapped[int] = mapped_column(ForeignKey("AutoMechanic.Id"))

    # car: Mapped["Car"] = relationship(back_populates="orders")
    # auto_mechanic: Mapped["AutoMechanic"] = relationship(back_populates="orders")


