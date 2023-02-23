from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
  """Requirements for Task 2C"""
  N = 10
  stations = build_station_list()
  update_water_levels(stations)
  print(f"top {N} stations with highest relative water level:")
  print(*stations_highest_rel_level(stations, N), sep = "\n")
  
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()