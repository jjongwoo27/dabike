from fastapi import FastAPI
import datetime
from logic import stations_distance

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "2022-2 DA Senior Project DA-BIKE", "time": datetime.datetime.now()}


@app.get("/location/")
async def near_stations(lat: float=37.5556488, lon: float=126.9106293):
    return stations_distance.get_near_stations(lat, lon)


@app.get("/recommendation/")
async def recommended_stations(lat: float=37.5556488, lon: float=126.9106293):
    return {"latitude": lat, 'longitude': lon}



