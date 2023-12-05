from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated

from models.order import Order
from controllers.controllers_for_Order import get_one, get_all,  update_, delete_
from database import get_db
import schemas

router = APIRouter()


@router.get("/orders", response_model=List[schemas.Order])
def get_order(id_: int, db: Session = Depends(get_db)):
    order = get_one(db, id_)
    return order

