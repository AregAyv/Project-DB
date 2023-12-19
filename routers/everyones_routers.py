from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from controllers.controllers_for_everyone import (
    get_join_of_cars_and_orders,
    get_orders_count_for_cars,
    get_cars_with_year_of_issue,
    update_brand,
    generate_cars_by_quantity,
    generate_orders_by_quantity,
    get_median_year_of_issue,
    get_cars_with_highest_orders,
    update_planned_end_date_for_auto_mechanics,
)

router = APIRouter()


# Cars and Orders
@router.get('/cars/orders', response_model=list)
async def join_of_cars_and_orders(per_page: int = 10, page: int = 1, db: Session = Depends(SessionLocal)):
    return get_join_of_cars_and_orders(db, per_page, page)


@router.get('/cars/orders/count', response_model=list)
async def orders_count_for_cars(per_page: int = 10, page: int = 1, db: Session = Depends(SessionLocal)):
    return get_orders_count_for_cars(db, per_page, page)


@router.get('/cars/with_year_of_issue', response_model=list)
async def cars_with_year_of_issue(year_of_issue: int, per_page: int = 10, page: int = 1,
                                  db: Session = Depends(SessionLocal)):
    return get_cars_with_year_of_issue(db, year_of_issue, per_page, page)


@router.put('/cars/update_brand')
async def update_car_brand(new_brand: str, db: Session = Depends(SessionLocal)):
    update_brand(db, new_brand)
    return {'message': 'Brand updated successfully'}


@router.post('/cars/generate', response_model=dict)
async def generate_cars(quantity: int, db: Session = Depends(SessionLocal)):
    result = generate_cars_by_quantity(db, quantity)
    return {'message': result}


@router.post('/orders/generate', response_model=dict)
async def generate_orders(quantity: int, db: Session = Depends(SessionLocal)):
    result = generate_orders_by_quantity(db, quantity)
    db.add_all(result)
    db.commit()
    return {'message': result}


@router.get('/cars/median_year_of_issue', response_model=int)
async def median_year_of_issue(db: Session = Depends(SessionLocal)):
    return get_median_year_of_issue(db)


@router.get('/cars/highest_orders', response_model=list)
async def cars_with_highest_orders(per_page: int = 10, page: int = 1, db: Session = Depends(SessionLocal)):
    return get_cars_with_highest_orders(db, per_page, page)


@router.put('/auto_mechanics/update_planned_end_date', response_model=dict)
async def update_planned_end_date_for_mechanics(threshold_order_count: int, new_planned_end_date: str,
                                                db: Session = Depends(SessionLocal)):
    update_planned_end_date_for_auto_mechanics(db, threshold_order_count, new_planned_end_date)
    return {'message': 'Planned end date updated successfully'}
