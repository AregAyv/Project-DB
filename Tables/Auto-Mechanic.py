from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Auto_Mechanic(Base):
    __tablename__ = "Auto_Mechanic"

    Id = Column("Id", Integer, primary_key=True)
    Full_name = Column("Full_name", String)
    Experience = Column("Experience", Integer)
    Discharge = Column("Discharge", String)
    Planned_end_date = Column("Planned_end_date", Date)
    Personnel_Number = Column("Personnel_Number", Integer)