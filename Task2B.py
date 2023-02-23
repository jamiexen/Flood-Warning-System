from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
  tol = 0.8
  stations = build_station_list()
  update_water_levels(stations)
  print(f"stations with a relative water level over {tol}:")
  print(*stations_level_over_threshold(stations, tol), sep = "\n")
  
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
