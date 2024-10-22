from sqlalchemy import Column, Integer, Float, DateTime, func, String
from .database import Base

class TemperatureData(Base):
    __tablename__ = 'temperature_data'

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    node_id = Column(String, nullable=False)