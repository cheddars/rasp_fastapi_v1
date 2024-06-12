from sqlalchemy.orm import Session

import models, schemas


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
                                longitude=humidity_temperature.longitude)
    db.add(db_humidity_temperature)
    db.commit()
    db.refresh(db_humidity_temperature)
