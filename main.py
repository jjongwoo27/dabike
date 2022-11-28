from fastapi import FastAPI
import datetime
from logic import distance as dis
from logic import recommend as rec

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "2022-2 DA Senior Project DA-BIKE", "time": datetime.datetime.now()}


@app.get("/location/")
async def near_stations(lat: float = 37.5556488, lon: float = 126.9106293):
    return dis.get_near_stations(lat, lon)


@app.get("/recommendation/")
async def recommended_stations(cafe: str = '1', food: str = '1', subway: str = '1', attraction: str = '1',
                               culture: str = '1', park: str = '1', humidity: int = 63, precipitation: float = 0.0,
                               temperature: float = 6.8, start_station: int = 102):
    comb = rec.get_combination(cafe, food, subway, attraction, culture, park, humidity, precipitation, temperature)

    return rec.get_recommended_stations(comb, start_station)
