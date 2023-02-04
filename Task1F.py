import floodsystem.geo as geo
import floodsystem.stationdata as stationdata
import floodsystem.station as station

def run():
    """Requirements for Task 1F"""
    inconsistent_stations = station.inconsistent_typical_range_stations(stationdata.build_station_list())
    print(sorted([station.name for station in inconsistent_stations]))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()