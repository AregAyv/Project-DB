from models.order import Order
from models.car import Car
from models.auto_mechanic import AutoMechanic
from faker import Faker
import random
import requests
fake = Faker()
BASE_URL = "http://localhost:8000"


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


def generate_orders_gen(quantity: int):
    return [generate_order_() for i in range(quantity)]


def generate_cars_gen(quantity: int):
    return [generate_car_() for i in range(quantity)]


def generate_auto_mechanic_gen(quantity: int):
    return [generate_auto_mechanic_() for i in range(quantity)]


def populate_orders(num_orders):
    for _ in range(num_orders):
        order_data = generate_order_()
        requests.post(f"{BASE_URL}/orders/", json=order_data)


def populate_cars(num_cars):
    for _ in range(num_cars):
        car_data = generate_car_()
        requests.post(f"{BASE_URL}/cars/", json=car_data)


def populate_auto_mechanics(num_auto_mechanics):
    for _ in range(num_auto_mechanics):
        auto_mechanic_data = generate_auto_mechanic_()
        requests.post(f"{BASE_URL}/auto_mechanics/", json=auto_mechanic_data)


if __name__ == "__main__":
    num_orders_to_create = 100
    populate_orders(num_orders_to_create)

    num_cars_to_create = 100
    populate_cars(num_cars_to_create)

    num_auto_mechanics_to_create = 100
    populate_auto_mechanics(num_auto_mechanics_to_create)

    print('/Population completed/')
