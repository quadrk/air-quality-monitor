# Description: FastAPI application for logging battery data
# main.py debug
from fastapi import FastAPI
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("battery_logger")

app = FastAPI()

# data model for battery data
class BatteryData(BaseModel):
    battery_level: float
    node_id: str

# endpoint for logging battery data
@app.post("/battery")
async def log_battery_data(battery_data: BatteryData):
    logger.info(f"Received battery data - Node ID: {battery_data.node_id}, Battery Level: {battery_data.battery_level}%")
    return {"status": "Battery data received and logged"}
