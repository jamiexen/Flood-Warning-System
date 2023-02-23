from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib
import floodsystem.station
import floodsystem.datafetcher as datafetcher
from datetime import timedelta, datetime

def run():
    """Requirements for Task 2G"""
    tol = 1.0
    stations = build_station_list()
    update_water_levels(stations)
    stations_at_risk_today = stations_level_over_threshold(stations, tol)     #currently just showing stations above usual range, this needs to be combined with other data from Task 2F
    
    stations_predicted = [] 
    for station in stations[5:]:
        
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id,
                        dt=timedelta(days=2))
        time = matplotlib.dates.date2num(dates[:1])
        
        if station.typical_range == None:
            pass
        else:     
            polynomials, shift = polyfit(dates, levels, 5)
            predicted_level = polynomials(time - shift + 1/24)
        
            if predicted_level > station.typical_range[1]:
                stations_predicted.append((station.name, predicted_level))
    
    return stations_at_risk_today, stations_predicted




print("stations at risk:", *run()[0], sep = "\n")
print("stations predicted at risk:", *run()[1], sep = "\n")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
