from typing import Union
from fastapi import FastAPI
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

engine = create_engine(f"sqlite:///Auto_repair_shop.db", echo=False)

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
