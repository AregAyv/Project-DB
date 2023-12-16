from fastapi import FastAPI
from database import engine
from Base import Base
from routers.order_router import router as order_router
from routers.car_router import router as car_router
from routers.auto_mechanic_router import router as auto_mechanic_router


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


