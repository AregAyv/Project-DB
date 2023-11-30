from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Car(Base):
    __tablename__ = "Car"

    Id = Column("Id", Integer, primary_key=True)
    Owners_full_name = Column("Owners_full_name", String)
    Brand = Column("Brand", String)
    Number = Column("Number", Integer)
    Year_of_issue = Column("Year_of_issue", Integer)


