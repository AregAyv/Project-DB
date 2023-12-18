from sqlalchemy.orm import Session
from sqlalchemy import func, select
from models.order import Order
from models.car import Car
from models.auto_mechanic import AutoMechanic
from generator import generate_orders, generate_cars, generate_auto_mechanic


def get_join_of_cars_and_orders(db: Session, per_page: int, page: int) -> list:
    data = (
        db.query(Car)
        .join(Order, Car.Id == Order.car_id)
        .order_by(Car.Id)
        .slice(page * per_page, page * per_page + per_page)
        .all()
    )
    result = []
    for car in data:
        result.append(
            {
                "id": car.Id,
                "owners_full_name": car.Owners_full_name,
                "brand": car.Brand,
                "number": car.Number,
                "year_of_issue": car.Year_of_issue,
            }
        )
    return result


def get_orders_count_for_cars(db: Session, per_page: int, page: int) -> list:
    data = (
        db.query(Car, func.count(Order.Id).label("order_count"))
        .join(Order)
        .group_by(Car.Id)
        .slice(page * per_page, page * per_page + per_page)
    )
    result = []
    for car, order_count in data:
        result.append(
            {
                "id": car.Id,
                "owners_full_name": car.Owners_full_name,
                "brand": car.Brand,
                "number": car.Number,
                "year_of_issue": car.Year_of_issue,
                "orders_count": order_count,
            }
        )
    return result


def get_cars_with_year_of_issue(db: Session, date_of_issue: int, per_page: int, page: int) -> list:
    # You may adjust or remove this condition based on your actual data model
    # For example, if there's no Year_of_issue in Order, you might use another condition.
    subquery = (
        db.query(Order.car_id)
        .filter(Order.Date_of_issue >= date_of_issue)  # Replace with a relevant condition
        .subquery()
    )
    query = (
        db.query(Car)
        .join(subquery, Car.Id == subquery.c.car_id)
        .slice(page * per_page, page * per_page + per_page)
    )
    result = []
    for car in query:
        result.append(
            {
                "id": car.Id,
                "owners_full_name": car.Owners_full_name,
                "brand": car.Brand,
                "number": car.Number,
                "year_of_issue": car.Year_of_issue,
            }
        )
    return result


def update_brand(db: Session, new_brand: str) -> None:
    subquery = (
        db.query(Order.car_id)
        .filter(Order.Real_end_date <= Order.Planned_end_date)
        .subquery()
    )
    db.query(Car).filter(Car.Id.in_(select(subquery))).update(
        {"Brand": new_brand}
    )
    db.commit()


def generate_cars_by_quantity(db: Session, quantity: int) -> str:
    data = generate_cars(quantity)
    db.add_all(data)
    db.commit()
    return "Create cars was successful"


def generate_orders_by_quantity(db: Session, quantity: int) -> str:
    data = generate_orders(quantity)
    db.add_all(data)
    db.commit()
    return "Create orders was successful"


def get_median_year_of_issue(db: Session) -> int:
    data = db.query(func.round(func.avg(Car.Year_of_issue))).scalar()
    return data


def get_cars_with_highest_orders(db: Session, per_page: int, page: int) -> list:
    subquery = (
        db.query(Order.car_id, func.count(Order.Id).label("order_count"))
        .group_by(Order.car_id)
        .order_by(func.count(Order.Id).desc())
        .limit(per_page)
        .offset(page * per_page)
        .subquery()
    )
    query = (
        db.query(Car, subquery.c.order_count)
        .join(subquery, Car.Id == subquery.c.car_id)
        .order_by(subquery.c.order_count.desc())
        .all()
    )
    result = []
    for car, order_count in query:
        result.append(
            {
                "id": car.Id,
                "owners_full_name": car.Owners_full_name,
                "brand": car.Brand,
                "number": car.Number,
                "year_of_issue": car.Year_of_issue,
                "order_count": order_count,
            }
        )
    return result


def update_planned_end_date_for_auto_mechanics(db: Session, threshold_order_count: int,
                                               new_planned_end_date: str) -> None:
    subquery = (
        db.query(Order.auto_mechanic_id, func.count(Order.Id).label("order_count"))
        .group_by(Order.auto_mechanic_id)
        .filter(func.count(Order.Id) >= threshold_order_count)
        .subquery()
    )
    db.query(AutoMechanic).filter(AutoMechanic.Id.in_(select(subquery))).update(
        {"Planned_end_date": new_planned_end_date}, synchronize_session=False
    )
    db.commit()
