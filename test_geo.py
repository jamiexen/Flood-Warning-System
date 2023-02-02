"""Test for geo function"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

def test_distance():
    """Tests if distances are faesable"""
    station_list = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(station_list, p)
    for i in X:
      assert 0 < X[i][1] <1000

def test_station_names():
    """Test all the stations are in the list"""
    station_list = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(station_list, p)
    Y = X[:][0]
    Z = [station.name for station in station_list]
    for station in Z:
        assert station in Y
    
def test_sorting():
    """Tests sorting function has worked"""
    station_list = build_station_list()
    p = (52.2053, 0.1218)
    X = stations_by_distance(station_list, p)
    for i in range(len(X)-1):
        assert X[i][1] >= X[i+1][1]
        

def test_names():
    """tests that all station names are from the original list"""
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    X = stations_within_radius(stations, centre, r)
    Y = stations.name()
    A = len(X)
    assert X.count(Y) == A


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