import floodsystem.geo as geo
import floodsystem.stationdata as stationdata

def run():
    """Requirements for Task 1D"""
    rivers = geo.rivers_with_station(stationdata.build_station_list())
    print(len(rivers), "stations. First 10 -", sorted(list(rivers))[:10])
    print("")
    stations = geo.stations_by_river(stationdata.build_station_list())
    print(sorted([station.name for station in stations["River Aire"]]))
    print(sorted([station.name for station in stations["River Cam"]]))
    print(sorted([station.name for station in stations["River Thames"]]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()