from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

def test_threshold():
    """Tests that the relative water levels are in the correct order"""
    tol = 0.8
    stations = build_station_list()
    update_water_levels(stations)
    threshold_stations = stations_level_over_threshold(stations, tol)
    for i in range(len(threshold_stations)-1):
        assert threshold_stations[i][1] >= threshold_stations[i+1][1]
        
def test_highest_level():
    """Tests that the number of stations in the list is correct"""
    N = 10
    stations = build_station_list()
    update_water_levels(stations)
    assert len(stations_highest_rel_level(stations, N)) == N
