from sqlite3 import Date

from fastapi import FastAPI, HTTPException, Depends

from models.order import Order
from sqlalchemy.orm import Session
from sqlalchemy import update, delete


def create_order(db: Session, order: Order):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.Id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()


def update_order(db: Session, order_id: int, new_data: Order):
    stmt = (
        update(Order).
        where(Order.Id == order_id).
        values(
            Price=new_data.Price,
            Type_of_work=new_data.Type_of_work,
            Date_of_issue=new_data.Date_of_issue,
            Planned_end_date=new_data.Planned_end_date,
            Real_end_date=new_data.Real_end_date,
            car_id=new_data.car_id,
            auto_mechanic_id=new_data.auto_mechanic_id
        )
    )

    db.execute(stmt)
    db.commit()

    updated_order = db.query(Order).filter(Order.Id == order_id).first()
    return updated_order


def delete_order(db: Session, order_id: int):
    stmt = delete(Order).where(Order.Id == order_id)

    deleted_order = db.execute(stmt)
    db.commit()

    return deleted_order