from fastapi import FastAPI
from database import engine
from Base import Base
from routers.order_router import router as order_router
from routers.car_router import router as car_router
from routers.auto_mechanic_router import router as auto_mechanic_router
from routers.everyones_routers import router as everyones_router
from models.order import Order
from models.car import Car
from models.auto_mechanic import AutoMechanic
from database import session

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    router=order_router,
    prefix='/orders',
)

app.include_router(
    router=car_router,
    prefix='/cars',
)

app.include_router(
    router=auto_mechanic_router,
    prefix='/auto_mechanics',
)

app.include_router(
    router=everyones_router,
    prefix='/everyones_router',
)

# usege od orm
new_car = Car(
    Owners_full_name='John Doe',
    Brand='Toyota',
    Number=123456,
    Year_of_issue=2020
)
session.add(new_car)
session.commit()


cars = session.query(Car).all()
for car in cars:
    print(car.Owners_full_name, car.Brand, car.Number)


car_to_update = session.query(Car).filter_by(Owners_full_name='John Doe').first()
car_to_update.Brand = 'Honda'
session.commit()


car_to_delete = session.query(Car).filter_by(Owners_full_name='John Doe').first()
session.delete(car_to_delete)
session.commit()
