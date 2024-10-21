This project is a simple air quality monitoring system that uses Libelium Waspmote Plug & Sense sensors to collect air quality data and a FastAPI server to store and display the collected data in a PostgreSQL database. 
The project is divided into two parts: 
- **Server**: A FastAPI application that manages the backend for receiving, storing, and managing the sensor data.
- **Sketch**: A Waspmote sketch that collects temperature data from the sensor and transmits it to the server over Wi-Fi.


# Project Structure

- **Air-Quality-Monitor/**
  - **server/** - Server-side application code
    - **app/**
      - **database.py** - Database connection and configuration
      - **main.py** - FastAPI routes and app logic
      - **models.py** - Database models for temperature data
      - **schemas.py** - Pydantic models for data validation
    - **requirements.txt** - Python dependencies for the server
    - **.env** - Environment variables for database connection
  - **sketch/** - Waspmote sketch code
    - **libraries/** - Required libraries for sensors and communication
    - **waspmote-api/** - Waspmote API code
    - **main.pde** - Main sketch file for the Waspmote device
  - **.gitignore** - Files to be ignored by Git
  - **README.md** - General project README (this file)
 

# Getting Started

1. **Install Dependencies**: Navigate to the `server/` directory and install the required Python packages by running:
    ```bash
    pip install -r requirements.txt
    ```

2. **Setup Environment**: Create a `.env` file in the `server/` directory and add your database connection settings like this:
    ```bash
    DATABASE_URL="user:pass@host/database"
    ```

3. **Upload Sketch**: Open the `sketch/main.pde` in the Waspmote IDE v04 (Latest supported version for old Libelium Waspmote Plug & Sense models), and upload it to the device. The sketch will collect temperature data and send it to the server.

4. **Run the Server**: Start the FastAPI server by navigating to the `server/app` directory and running:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

5. **View Collected Data**: Access the FastAPI endpoints to view the data stored in the PostgreSQL database. You can retrieve the latest temperature record using the `/temperature/latest` endpoint.
