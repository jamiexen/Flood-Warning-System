from floodsystem.flood import stations_level_over_threshold
#from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels

#import floodsystem.stationdata as stationdata
#import floodsystem.datafetcher as datafetcher
#from datetime import datetime, timedelta

def run():
    """Requirements for Task 2G"""
    tol = 1.0
    stations = build_station_list()
    update_water_levels(stations)
    stations_at_risk = stations_level_over_threshold(stations, tol)     #currently just showing stations above usual range, this needs to be combined with other data from Task 2F
    return stations_at_risk

print("stations at risk:", *run(), sep = "\n")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
