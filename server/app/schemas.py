from pydantic import BaseModel
from datetime import datetime

class TemperatureCreate(BaseModel):
    temperature: float

class Temperature(BaseModel):
    id: int
    temperature: float
    timestamp: datetime

    class Config:
        orm_mode = True
