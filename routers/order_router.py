from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated

from models.order import Order
from controllers.controllers_for_Order import get_one, get_all, update_, delete_, create_
from database import get_db
import schemas

router = APIRouter()


@router.post("/orders)", response_model=schemas.Order)
def create_order(order_to_cr: schemas.OrderCreate, db: Session = Depends(get_db)):
    order = create_(db, order_to_cr)
    return order


@router.get("/orders/{order_id}", response_model=schemas.Order)
def get_order(id_: int, db: Session = Depends(get_db)):
    order = get_one(db, id_)
    return order


@router.get("/orders", response_model=List[schemas.Order])
def get_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    orders = get_all(db, skip, limit)
    return orders


@router.put("/orders/{order_id", response_model=schemas.Order)
def update_order(order_id: int, new_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    return update_(db, order_id, new_data)


@router.delete("/orders/{order_id")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return delete_(db, order_id)


@router.get("/order/", response_model=List[schemas.Order])
def get_orders_pagination(page: int = 0, per_page: int = 10, db: Session = Depends(get_db)):
    orders = db.query(Order).offset(page * per_page).limit(per_page).all()
    return orders
