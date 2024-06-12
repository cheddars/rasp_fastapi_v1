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

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True