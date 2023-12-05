from typing import Union
from fastapi import FastAPI
from models.database import engine
# from models.order import Order

from routers.order_router import router as order_router

app = FastAPI()

app.include_router(
    router=order_router,
    prefix='/orders',
)

# Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/orders/", response_model=Order)
# def create_order_api(order: Order, db: Session = Depends(get_db)):
#     return create_order(db, order)
#
#
# @app.get("/orders/{order_id}", response_model=Order)
# def read_order(order_id: int, db: Session = Depends(get_db)):
#     return get_order(db, order_id)
#
#
# @app.put("/orders/{order_id}", response_model=Order)
# def update_order_api(order_id: int, new_data: Order, db: Session = Depends(get_db)):
#     updated_order = update_order(db, order_id, new_data)
#     if updated_order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return updated_order
#
#
# @app.delete("/orders/{order_id}", response_model=Order)
# def delete_order_api(order_id: int, db: Session = Depends(get_db)):
#     deleted_order = delete_order(db, order_id)
#     if deleted_order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return deleted_order

# Base = declarative_base()
#
# engin = create_engine("sqlite:///mydb.db, echo=True")
# Base.metadata.create_all(bind=engin)
#
# Session = sessionmaker(bind=engin)
# session = Session()
#
#
#
# Base.metadata.create_all(bind=engine)
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
