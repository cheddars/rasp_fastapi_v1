from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR, Float, DateTime, func, Index
from sqlalchemy.orm import relationship

from database import Base


class HumidityTemperture(Base):
    __tablename__ = "humidity_temperture"
    id = Column(Integer, primary_key=True, autoincrement=True)
    yyyy = Column(CHAR(4))
    mm = Column(CHAR(2))
    dd = Column(CHAR(2))
    module = Column(String(50))
    humidity = Column(Float(2))
    temperture = Column(Float(2))
    latitude = Column(Float(10))
    longitude = Column(Float(10))
    sensor_dt = Column(DateTime)
    svr_dt = Column(DateTime, server_default=func.now(), index=True)
    __table_args__ = (Index('humidity_ymd_idx', "yyyy", "mm", "dd"),)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")