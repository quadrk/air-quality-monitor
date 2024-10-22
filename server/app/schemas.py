from pydantic import BaseModel
from datetime import datetime

class TemperatureCreate(BaseModel):
    temperature: float
    node_id: str

class Temperature(BaseModel):
    id: int
    temperature: float
    timestamp: datetime
    node_id: str

    class Config:
        orm_mode = True
