from typing import List, Union
from datetime import datetime
from pydantic import BaseModel


class CommonResponse(BaseModel):
    status: int
    message: str

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class HumidityTemperatureBase(BaseModel):
    module: str
    humidity: float
    temperature: float
    latitude: float
    longitude: float
    date_time: datetime









