# Copyright (C) 2018 Garth N. Wells

# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from haversine import haversine
from .utils import sorted_by_key
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
  distances = []
  stations = build_station_list()
  for station in stations:
    distances.append((station.name, station.town, haversine(station.coord, p)))
  distances = sorted_by_key(distances, 2)
  return distances
    
def stations_within_radius(stations, centre, r):
  Y = []
  X = stations_by_distance(stations, centre)
  for i in range(len(X)):
    if X[i][1] < r:
      Y.append(X[i][0])
  Y = sorted_by_key(Y, 0)
  return Y

