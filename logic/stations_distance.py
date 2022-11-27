import pandas as pd
import heapq
from haversine import haversine

stats = pd.read_csv("./logic/station_info.csv", encoding="cp949")


def get_near_stations(lat: float = 37.5556488, lon: float = 126.9106293):
    near_stations = []
    for stat in range(len(stats)):
        dis = haversine((lat, lon), (stats.loc[stat]['latitude'], stats.loc[stat]['longitude']), unit='km')
        if len(near_stations) <=5:
            heapq.heappush(near_stations, (-dis, stat))
        else:
            if -heapq.heappop(near_stations)[0] > dis:
                heapq.heappush(near_stations, (-dis, stat))

    result = {}
    for i in range(len(near_stations)):
        n_stat = heapq.heappop(near_stations)
        result[5-i] = {"station_num": str(stats.loc[n_stat[1]]['station_num']),
                       "station_name": str(stats.loc[n_stat[1]]['station_name']),
                       "distance": float(-n_stat[0])}

    return result

