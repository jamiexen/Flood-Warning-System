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
    if X[i][2] < r:
      Y.append(X[i][0])
  Y = sorted_by_key(Y, 0)
  return Y

def rivers_with_station(stations):
  """Returns a set of names of all rivers with a monitoring station
  \n:Param stations: list of station objects"""
  rivers = set()
  for station in stations:
    rivers.add(station.river)
  return rivers

def stations_by_river(stations):
  """Returns a dictionary mapping river names to the list of station objects on that river.
  \n Param stations: list of station objects"""
  rivers_to_stations = {}
  for station in stations:
    if station.river in rivers_to_stations:
      rivers_to_stations[station.river].append(station)
    else:
      rivers_to_stations[station.river] = []
      rivers_to_stations[station.river].append(station)
  return rivers_to_stations