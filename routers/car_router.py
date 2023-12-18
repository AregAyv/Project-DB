from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated

from models.car import Car
from controllers.controllers_Car import get_one, get_all, update_, delete_, create_
from database import get_db
import schemas

router = APIRouter()


@router.post("/cars", response_model=schemas.Order)
def create_car(car_to_create: schemas.CarCreate, db: Session = Depends(get_db)):
    car = create_(db, car_to_create)
    return car


@router.get("/cars/{car_id}", response_model=schemas.Order)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = get_one(db, car_id)
    return car


@router.get("/cars", response_model=List[schemas.Order])
def get_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    car = get_all(db, skip, limit)
    return car


@router.put("/cars/{car_id}", response_model=schemas.Order)
def update_car(car_id: int, new_data: schemas.CarCreate, db: Session = Depends(get_db)):
    return update_(db, car_id, new_data)


@router.delete("/cars/{car_id}")
def delete_order(car_id: int, db: Session = Depends(get_db)):
    return delete_(db, car_id)
