from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated

from models.auto_mechanic import AutoMechanic
from controllers.controllers_Auto_Mechanic import get_one, get_all, update_, delete_, create_
from database import get_db
import schemas

router = APIRouter()


@router.post("/auto_mechanics", response_model=schemas.AutoMechanic)
def create_auto_mechanic(mechanic_to_create: schemas.AutoMechanicCreate, db: Session = Depends(get_db)):
    mechanic = create_(db, mechanic_to_create)
    return mechanic


@router.get("/auto_mechanics/{mechanic_id}", response_model=schemas.AutoMechanic)
def get_auto_mechanic(mechanic_id: int, db: Session = Depends(get_db)):
    mechanic = get_one(db, mechanic_id)
    return mechanic


@router.get("/auto_mechanics", response_model=List[schemas.AutoMechanic])
def get_auto_mechanics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    mechanics = get_all(db, skip, limit)
    return mechanics


@router.put("/auto_mechanics/{mechanic_id}", response_model=schemas.AutoMechanic)
def update_auto_mechanic(mechanic_id: int, new_data: schemas.AutoMechanicCreate, db: Session = Depends(get_db)):
    return update_(db, mechanic_id, new_data)


@router.delete("/auto_mechanics/{mechanic_id}")
def delete_auto_mechanic(mechanic_id: int, db: Session = Depends(get_db)):
    return delete_(db, mechanic_id)


@router.get("/auto_mechanic/", response_model=List[schemas.AutoMechanic])
def get_auto_mechanics_pagination(page: int = 0, per_page: int = 10, sort_by: str = "id", db: Session = Depends(get_db)):
    auto_mechanics = db.query(AutoMechanic).order_by(getattr(AutoMechanic, sort_by)).offset(page * per_page).limit(
        per_page).all()
    return auto_mechanics
