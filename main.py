from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.wsgi import WSGIMiddleware

import models, schemas, crud
from database import SessionLocal, engine
from dashboard import app as dboard
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/dashboard", WSGIMiddleware(dboard.server))

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/humidity_temperature/", response_model=schemas.CommonResponse)
def create_humidity_temperture(humidity_temperature: schemas.HumidityTemperatureBase, db: Session = Depends(get_db)):
    crud.insert_humidity_temperature(db=db, humidity_temperature=humidity_temperature)
    return schemas.CommonResponse(status=200, message="Data inserted successfully")


