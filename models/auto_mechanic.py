from sqlalchemy import String, Integer, DateTime
import datetime
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
# from typing import List
from Base import Base


class AutoMechanic(Base):
    __tablename__ = "AutoMechanic"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Full_name: Mapped[str] = mapped_column(String, nullable=False)
    Experience: Mapped[int] = mapped_column(Integer, nullable=False)
    Discharge: Mapped[str] = mapped_column(String, nullable=False)
    Planned_end_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    Personnel_Number: Mapped[int] = mapped_column(Integer, nullable=False)

    # orders: Mapped[List["Order"]] = relationship(back_populates='auto_mechanic')
