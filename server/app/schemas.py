from pydantic import BaseModel

class TemperatureCreate(BaseModel):
    temperature: float

class Temperature(BaseModel):
    id: int
    temperature: float

    class Config:
        orm_mode = True
