from sqlalchemy.orm import Session
from models.auto_mechanic import AutoMechanic
from sqlalchemy import update, delete
from schemas import AutoMechanicCreate


def create_(db: Session, auto_mechanic: AutoMechanicCreate):
    db.add(auto_mechanic)
    db.commit()
    db.refresh(auto_mechanic)
    return auto_mechanic


def get_one(db: Session, auto_mechanic_id: int):
    return db.query(AutoMechanic).filter(AutoMechanic.Id == auto_mechanic_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AutoMechanic).offset(skip).limit(limit).all()


def update_(db: Session, auto_mechanic_id: int, new_data: AutoMechanicCreate):
    stmt = (
        update(AutoMechanic).
        where(AutoMechanic.Id == auto_mechanic_id).
        values(
            Full_name=new_data.Full_name,
            Experience=new_data.Experience,
            Discharge=new_data.Discharge,
            Planned_end_date=new_data.Planned_end_date,
            Personnel_Number=new_data.Personnel_Number
        )
    )

    db.execute(stmt)
    db.commit()

    updated_auto_mechanic = db.query(AutoMechanic).filter(AutoMechanic.Id == auto_mechanic_id).first()
    return updated_auto_mechanic


def delete_(db: Session, auto_mechanic_id: int):
    stmt = delete(AutoMechanic).where(AutoMechanic.Id == auto_mechanic_id)

    deleted_auto_mechanic = db.execute(stmt)
    db.commit()

    return deleted_auto_mechanic
