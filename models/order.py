import datetime
from sqlalchemy import ForeignKey, Column, String, Integer, DateTime
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from Base import Base


class Order(Base):
    __tablename__ = "Order"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Price: Mapped[int] = mapped_column(int, nullable=False)
    Type_of_work: Mapped[str] = mapped_column(String, nullable=False)
    Date_of_issue: Mapped[datetime.date] = Column(DateTime, nullable=False)
    Planned_end_date: Mapped[datetime.date] = Column(DateTime, nullable=False)
    Real_end_date: Mapped[datetime.date] = Column(DateTime, nullable=False)

    car_id: Mapped[int] = mapped_column(ForeignKey("Car.Id"))
    auto_mechanic_id: Mapped[int] = mapped_column(ForeignKey("AutoMechanic.Id"))

    # car: Mapped["Car"] = relationship(back_populates="orders")
    # auto_mechanic: Mapped["AutoMechanic"] = relationship(back_populates="orders")
