from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    A = []
    for station in stations:
        if station.relative_water_level() != None:
#            print(station.relative_water_level())
            if station.relative_water_level() > tol:
                A.append((station.name, station.relative_water_level()))
    A = sorted_by_key(A, 1, reverse = True)
    return A
