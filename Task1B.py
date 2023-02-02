from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def Task1B():
  stations = build_station_list()
  p = (52.2053, 0.1218)
  X = stations_by_distance(stations, p)
  print(f"Closest 10 Stations \n{ X[:10][0]}")
  print(f"Furthest 10 Stations \n{ X[-10:][0]}")
  
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    Task1B
