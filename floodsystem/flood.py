from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    A = []
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                A.append((station.name, station.relative_water_level()))
    A = sorted_by_key(A, 1, reverse = True)
    return A

def stations_highest_rel_level(stations, N):
    A = []
    for station in stations:
        if station.relative_water_level() != None:
            A.append((station.name, station.relative_water_level()))
    A = sorted_by_key(A, 1, reverse = True)
    A = A[:10]
    return A