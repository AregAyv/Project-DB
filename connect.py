from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import text

engine = create_engine(f"sqlite:///Auto_repair_shop.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))


class Base(DeclarativeBase):
    pass


print(result.all())
