import pandas as pd

recommendation = pd.read_csv("./logic/recommendation.csv")
stats = pd.read_csv("./logic/station_info.csv")


def get_combination(cafe: str = '1', food: str = '1', subway: str = '1', attraction: str = '1', culture: str = '1',
                    park: str = '1', humidity: int = 63, precipitation: float = 0.0, temperature: float = 6.8):
    # categorization
    if humidity >= 71:
        humidity_cat = '1'
    else:
        humidity_cat = '0'

    if precipitation > 0:
        precipitation_cat = '1'
    else:
        precipitation_cat = '0'

    if temperature <= 4:
        temperature_cat = '0'
    elif 4 < temperature <= 8:
        temperature_cat = '1'
    elif 8 < temperature <= 11:
        temperature_cat = '2'
    elif 11 < temperature <= 16:
        temperature_cat = '3'
    elif 16 < temperature <= 19:
        temperature_cat = '4'
    elif 19 < temperature <= 22:
        temperature_cat = '5'
    elif 22 < temperature <= 27:
        temperature_cat = '6'
    else:
        temperature_cat = '7'

    combination = "{0}{1}{2}{3}{4}{5}-{6}{7}{8}".format(cafe, food, subway, attraction, culture, park, humidity_cat,
                                                        precipitation_cat, temperature_cat)

    return combination


def get_recommended_stations(comb: str = '', start_station: int = 102):
    rec_stats = recommendation.loc[recommendation[(recommendation['combi'] == comb)
                                                  & (recommendation['start_station'] == start_station)].index[-1]]

    result = {}
    for stat in rec_stats['end_station'].split(','):
        result[stats.loc[stats[stats['station_num'] == int(stat)].index[0]]['station_name']] = {
            "latitude": str(stats.loc[stats[stats['station_num'] == int(stat)].index[0]]['latitude']),
            "longitude": str(stats.loc[stats[stats['station_num'] == int(stat)].index[0]]['longitude'])
        }

    return result

# test
# print(get_recommended_stations('111111-000', 102))
