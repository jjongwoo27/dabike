import pandas as pd
import heapq
from haversine import haversine

stats = pd.read_csv("./logic/station_info.csv")


def get_near_stations(lat: float = 37.5556488, lon: float = 126.9106293):
    near_stations = []
    for stat in range(len(stats)):
        dis = haversine((lat, lon), (stats.loc[stat]['latitude'], stats.loc[stat]['longitude']), unit='km')
        if len(near_stations) <= 5:
            heapq.heappush(near_stations, (-dis, stat))
        else:
            if -heapq.heappop(near_stations)[0] > dis:
                heapq.heappush(near_stations, (-dis, stat))

    tmp = []
    for i in range(len(near_stations)):
        n_stat = heapq.heappop(near_stations)
        tmp.append(n_stat)

    result = {}
    for j in range(len(tmp)):
        result[str(stats.loc[tmp[4-j][1]]['station_name'])] = {
            "station_num": str(stats.loc[tmp[4-j][1]]['station_num']),
            "distance": float(-tmp[4-j][0])
        }

    return result
