from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def Task1C():
  stations = build_station_list()
  centre = (52.2053, 0.1218)
  r = 10                
  X = stations_within_radius(stations, centre, r)     
  print(X)        

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    Task1C                                                                          