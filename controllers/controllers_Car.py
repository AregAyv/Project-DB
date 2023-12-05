from sqlite3 import Date

from fastapi import FastAPI, HTTPException, Depends

from models.car import Car
from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from schemas import CarCreate


def create_(db: Session, car: CarCreate):
    db.add(car)
    db.commit()
    db.refresh(car)
    return car


def get_one(db: Session, car_id: int):
    return db.query(Car).filter(Car.Id == car_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Car).offset(skip).limit(limit).all()


def update_(db: Session, car_id: int, new_data: CarCreate):
    stmt = (
        update(Car).
        where(Car.Id == car_id).
        values(
            Owners_full_name=new_data.Owners_full_name,
            Brand=new_data.Brand,
            Number=new_data.Number,
            Year_of_issue=new_data.Year_of_issue
        )
    )

    db.execute(stmt)
    db.commit()

    updated_car = db.query(Car).filter(Car.Id == car_id).first()
    return updated_car


def delete_(db: Session, car_id: int):
    stmt = delete(Car).where(Car.Id == car_id)

    deleted_car = db.execute(stmt)
    db.commit()

    return deleted_car
