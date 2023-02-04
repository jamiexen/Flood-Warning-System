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
    Y = stations_by_distance(station_list, p)
    X = [station[0] for station in Y]
    Z = [station.name for station in station_list]
    assert all(item in Z for item in X)
    
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
    names = []
    for station in stations:
      names.append(station.name)
    print(names)
    print(X)
    assert all(item in names for item in X)

def test_rivers():
    """Tests that all rivers are in the set"""
    station_list = build_station_list()
    rivers = rivers_with_station(station_list)
    assert all(station.river in rivers for station in station_list)

def test_stations_by_river():
    """Tests that each station is mapped to by the correct river"""
    station_list = build_station_list()
    dict = stations_by_river(station_list)
    assert all(station.name in dict[station.river] for station in station_list)


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