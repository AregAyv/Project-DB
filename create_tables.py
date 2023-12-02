from models.order import Order
from models.car import Car
from models.auto_mechanic import AutoMechanic
from connect import engine
from connect import Base

Base.metadata.create_all(bind=engine)

