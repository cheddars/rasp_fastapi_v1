from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def insert_humidity_temperature(db: Session, humidity_temperature: schemas.HumidityTemperatureBase):
    sensor_dt = humidity_temperature.date_time
    yyyy = sensor_dt.strftime('%Y')
    mm = sensor_dt.strftime('%m')
    dd = sensor_dt.strftime('%d')
    db_humidity_temperature = models.HumidityTemperature(
                                yyyy=yyyy, mm=mm,  dd=dd,
                                module=humidity_temperature.module,
                                humidity=humidity_temperature.humidity,
                                temperature=humidity_temperature.temperature,
                                latitude=humidity_temperature.latitude,
                                longitude=humidity_temperature.longitude,
                                sensor_dt=humidity_temperature.date_time)
    db.add(db_humidity_temperature)
    db.commit()
    db.refresh(db_humidity_temperature)

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