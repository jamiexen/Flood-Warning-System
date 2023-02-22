from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_distance


stations = build_station_list()
update_water_levels(stations)
for station in stations[:1]:
  print(station.name)
  print(station.relative_water_level())


