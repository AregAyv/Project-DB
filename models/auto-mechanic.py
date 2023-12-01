from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()


class AutoMechanic(Base):
    __tablename__ = "AutoMechanic"

    Id = Column("Id", Integer, primary_key=True)
    Full_name = Column("Full_name", String)
    Experience = Column("Experience", Integer)
    Discharge = Column("Discharge", String)
    Planned_end_date = Column("Planned_end_date", Date)
    Personnel_Number = Column("Personnel_Number", Integer)

    orders = relationship('Order', back_populates='auto_mechanic')
