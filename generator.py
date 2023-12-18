from models.order import Order
from models.car import Car
from models.auto_mechanic import AutoMechanic
from faker import Faker
import random

fake = Faker()


def generate_order_():
    date_of_issue_ = fake.date_this_decade()
    planned_end_date_ = fake.date_between(start_date=date_of_issue_, end_date='+30d')
    return Order(
        Price=random.randint(1, 100),
        Type_of_work=fake.job(),
        date_of_issue=date_of_issue_,
        planned_end_date=planned_end_date_,
        real_end_date=fake.date_between(start_date=planned_end_date_, end_date='+15d')
    )


def generate_car_():
    return Car(
        Owners_full_name=fake.name(),
        Brand=fake.car_make(),
        Number=fake.license_plate(),
        Year_of_issue=random.randint(1980, 2023)
    )


def generate_auto_mechanic_():
    return AutoMechanic(
        Full_name=fake.name(),
        Experience=random.randint(1, 20),
        Discharge=fake.job(),
        Planned_end_date=fake.date_this_decade(),
        Personnel_Number=fake.random_number(digits=6)
    )


def generate_orders(quantity: int):
    return [generate_order_() for i in range(quantity)]


def generate_cars(quantity: int):
    return [generate_car_() for i in range(quantity)]


def generate_auto_mechanic(quantity: int):
    return [generate_auto_mechanic_() for i in range(quantity)]
