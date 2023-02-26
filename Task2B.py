from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
  """Requirements for Task 2B"""
  tol = 0.8
  stations = build_station_list()
  update_water_levels(stations)
  print(f"stations with a relative water level over {tol}:")
  station_list = [x[0] for x in stations_level_over_threshold(stations, tol)]
  output_list = []
  for i in range(len(station_list)):
    output_list.append([station_list[i].name, station_list[i].relative_water_level()])
  print(*output_list, sep = "\n")
  
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
