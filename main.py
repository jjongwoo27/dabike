from fastapi import FastAPI
import datetime
from logic import distance as dis
from logic import recommend as rec

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "2022-2 DA Senior Project DA-BIKE", "time": datetime.datetime.now()}


@app.get("/api/location/")
async def near_stations(latitude: float = 37.5556488, longitude: float = 126.9106293):
    return dis.get_near_stations(latitude, longitude)


@app.get("/api/recommendation/")
async def recommended_stations(cafe: bool = True, food: bool = True, subway: bool = True, attraction: bool = True,
                               culture: bool = True, park: bool = True, humidity: int = 63, precipitation: float = 0.0,
                               temperature: float = 6.8, start_station: int = 102):
    comb = rec.get_combination(cafe, food, subway, attraction, culture, park, humidity, precipitation, temperature)
    return rec.get_recommended_stations(comb, start_station)
