from sqlalchemy import text
from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas
from .database import engine, Base, get_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.error")

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    try:
        body = await request.body()
        logger.info(f"Request body: {body.decode('utf-8')}")
    except Exception as e:
        logger.error(f"Error reading body: {str(e)}")
    
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

@app.post("/temperature", response_model=schemas.Temperature)
async def create_temperature(temp_data: schemas.TemperatureCreate, db: AsyncSession = Depends(get_db)):
    try:
        logger.info(f"Received temperature data: {temp_data}")
        new_temp = models.TemperatureData(temperature=temp_data.temperature)
        db.add(new_temp)
        await db.commit()
        await db.refresh(new_temp)
        logger.info(f"Temperature saved: {new_temp}")
        return new_temp
    except Exception as e:
        logger.error(f"Error saving temperature data: {str(e)}")
        raise HTTPException(status_code=500, detail="Error saving temperature data")

@app.get("/temperature/latest", response_model=schemas.Temperature)
async def get_latest_temperature(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT * FROM temperature_data ORDER BY id DESC LIMIT 1;"))
        latest_temp = result.fetchone()
        if latest_temp is None:
            logger.warning("No temperature data available")
            raise HTTPException(status_code=404, detail="No data available")
        logger.info(f"Latest temperature data: {latest_temp}")
        return latest_temp
    except Exception as e:
        logger.error(f"Error fetching latest temperature data: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching latest temperature data")

@app.get("/check_db")
async def check_db_connection(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1;"))
        logger.info("Database connection successful")
        return {"status": "Connected to the database successfully!"}
    except Exception as e:
        logger.error(f"Failed to connect to the database: {str(e)}")
        return {"status": "Failed to connect to the database.", "error": str(e)}