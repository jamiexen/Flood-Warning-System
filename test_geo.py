"""Test for geo function"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def test_distance():
    """Tests if distances are faesable"""
    station_list = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(station_list, p)
    for i in range(len(X)):
      assert 0 <= X[i][2] < 1000

def test_station_names():
    """Test all the stations are in the list"""
    station_list = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(station_list, p)[:][0]
    Z = [station.name for station in station_list]
    Z = sorted_by_key(Z, 0)
    print(X)
    X = sorted_by_key(X, 0)
    for station, i in Z, len(Z):
        assert station in X[i]
    
def test_sorting():
    """Tests sorting function has worked"""
    station_list = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(station_list, p)
    for i in range(len(X)-1):
        assert X[i][2] <= X[i+1][2]
        

def test_names():
    """tests that all station names are from the original list"""
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10.0
    X = stations_within_radius(stations, centre, r)
    names = ()
    for station in stations:
      names.append(station.name)
    A = len(X)
    assert X.count(names) == A


#def test_range():
#    """tests that distances are between 0km and 10km"""
#    stations = build_station_list()
#    centre = (52.2053, 0.1218)
#    r = 10
#    X = stations_within_radius(stations, centre, r)
#    for station in stations:
#        if station.count(X) >= 1:
#            assert stations.
#        print(stations.station)
#        print(stations.count(station))