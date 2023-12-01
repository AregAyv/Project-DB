from sqlite3 import Date

from fastapi import FastAPI, HTTPException, Depends

from models.order import Order
from sqlalchemy.orm import Session


def create_order(db: Session, order: Order):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.Id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()


def update_orders(db: Session, order_id: int, price: float, type_of_work: str, date_of_issue: Date,
                  planned_end_date: Date, real_end_date: Date, car_id: int, auto_mechanic_id: int):
    order = db.query(Order).filter(Order.Id == order_id).first()
    if order:
        order.Price = price
        order.Type_of_work = type_of_work
        order.Date_of_issue = date_of_issue
        order.Planned_end_date = planned_end_date
        order.Real_end_date = real_end_date
        order.car_id = car_id
        order.auto_mechanic_id = auto_mechanic_id
        db.commit()
        db.refresh(order)
        return order
    return None


def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.Id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        return order
    return None
