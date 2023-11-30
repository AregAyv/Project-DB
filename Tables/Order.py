from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()


class Order(Base):
    __tablename__ = "Order"

    Id = Column("Id", Integer, primary_key=True)
    Price = Column("Price", Numeric(10, 2))
    Type_of_work = Column("Type_of_work", String)
    Date_of_issue = Column("Date_of_issue", Date)
    Planned_end_date = Column("Planned_end_date", Date)
    Real_end_date = Column("Real_end_date", Date)

    car_id = Column(Integer, ForeignKey('Car.Id'))
    auto_mechanic_id = Column(Integer, ForeignKey('Auto_Mechanic.Id'))

    car = relationship('Car', back_populates='orders')
    auto_mechanic = relationship('AutoMechanic', back_populates='orders')
