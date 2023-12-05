from pydantic import BaseModel
from typing import List
import datetime


class OrderBase(BaseModel):
    Price: int
    Type_of_work: str
    Date_of_issue: datetime.date
    Planned_end_date: datetime.date
    Real_end_date: datetime.date


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    Id: int

    class Config:
        from_attributes = True


class CarBase(BaseModel):
    Owners_full_name: str
    Brand: str
    Number: int
    Year_of_issue: datetime.date


class CarCreate(CarBase):
    pass


class Car(CarBase):
    Id: int

    class Config:
        from_attributes = True


class AutoMechanicBase(BaseModel):
    Full_name: str
    Experience: int
    Discharge: str
    Planned_end_date: datetime.date
    Personnel_Number: int


class AutoMechanicCreate(AutoMechanicBase):
    pass


class AutoMechanic(AutoMechanicBase):
    Id: int

    class Config:
        from_attributes = True
