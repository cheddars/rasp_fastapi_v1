from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR, Float, DateTime, func, Index
from sqlalchemy.dialects.mysql import FLOAT
from database import Base


class HumidityTemperature(Base):
    __tablename__ = "humidity_temperature"
    id = Column(Integer, primary_key=True, autoincrement=True)
    yyyy = Column(CHAR(4))
    mm = Column(CHAR(2))
    dd = Column(CHAR(2))
    module = Column(String(50))
    humidity = Column(Float(2))
    temperature = Column(Float(2))
    latitude = Column(FLOAT(precision=17, scale=14))
    longitude = Column(FLOAT(precision=17, scale=14))
    svr_dt = Column(DateTime, server_default=func.now(), index=True)
    __table_args__ = (Index('humidity_ymd_idx', "yyyy", "mm", "dd"),)
