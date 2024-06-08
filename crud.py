from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def insert_humidity_temperture(db: Session, humidity_temperture: schemas.HumidityTempertureBase):
    sensor_dt = humidity_temperture.date_time
    yyyy = sensor_dt.strftime('%Y')
    mm = sensor_dt.strftime('%m')
    dd = sensor_dt.strftime('%d')
    db_humidity_temperture = models.HumidityTemperture(
                                yyyy=yyyy, mm=mm,  dd=dd,
                                module=humidity_temperture.module,
                                humidity=humidity_temperture.humidity,
                                temperture=humidity_temperture.temperature,
                                latitude=humidity_temperture.latitude,
                                longitude=humidity_temperture.longitude,
                                sensor_dt=humidity_temperture.date_time)
    db.add(db_humidity_temperture)
    db.commit()
    db.refresh(db_humidity_temperture)

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item