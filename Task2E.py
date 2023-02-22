import floodsystem.geo as geo
import floodsystem.plot as plot
import floodsystem.stationdata as stationdata
import floodsystem.datafetcher as datafetcher
from datetime import datetime, timedelta

def run():
    """Requirements for Task 2E"""
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    
    i = 0
    while i < len(stations):
        if stations[i].latest_level == None:
            stations.remove(stations[i])
        else:
            i += 1

    stations.sort(key=lambda x: x.latest_level, reverse=True)
    stations = stations[:5]

    for i in range(len(stations)):
        dates, levels = datafetcher.fetch_measure_levels(stations[i].measure_id,
                                     dt=timedelta(days=10))
        plot.plot_water_levels(stations[i], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()