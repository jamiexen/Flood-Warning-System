from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib
import floodsystem.station
import floodsystem.datafetcher as datafetcher
from datetime import timedelta, datetime
import floodsystem.plot as plot
'''
def run():
    """Requirements for Task 2G"""
    tol = 1.0
    stations = build_station_list()
    update_water_levels(stations)
    stations_at_risk_today = stations_level_over_threshold(stations, tol)     #currently just showing stations above usual range, this needs to be combined with other data from Task 2F
    
    stations_predicted = [] 
    stations = stations[:5]
    for station in stations:
        print(station.name)
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id,
                        dt=timedelta(days=2))
        time = matplotlib.dates.date2num(dates[:1])
        
        if station.typical_range == None or len(dates) != len(levels) or len(dates) == 0:
            pass
        else:
            polynomials, shift = polyfit(dates, levels, 5)
            predicted_level = polynomials(time - shift + 1/24)
        
            if predicted_level > station.typical_range[1]:
                stations_predicted.append((station.name, predicted_level))
    
    print("Stations at risk", stations_at_risk_today)
    print("Stations predicted at risk", stations_predicted)
'''

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    high_risk_stations = stations_level_over_threshold(stations, 0.8)
    high_risk_stations = [x[0] for x in high_risk_stations]

    medium_risk_stations = stations_level_over_threshold(stations, 0.6)
    medium_risk_stations = [x[0] for x in medium_risk_stations]
    i = 0
    while i < (len(medium_risk_stations)):
        if medium_risk_stations[i] in high_risk_stations:
            del(medium_risk_stations[i])
        i += 1
            
    low_risk_stations = []
    for station in stations:
        if station not in medium_risk_stations and station not in high_risk_stations:
            low_risk_stations.append(station)

    severe_risk_stations = []
    for station in high_risk_stations:
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id,
                        dt=timedelta(days=2))
        if station.typical_range == None or len(dates) != len(levels) or len(dates) == 0:
            pass
        else:
            time = matplotlib.dates.date2num(dates[-1])
            poly, shift = polyfit(dates, levels, 5)
            if poly(time - shift + 1/4) > station.typical_range[1]:
                
                #plot.plot_water_level_with_fit(station, dates, levels, 5)  #Commented code displays a plot of water level for debugging purposes
                
                severe_risk_stations.append(station)
                high_risk_stations.remove(station)
            else:
                #plot.plot_water_level_with_fit(station, dates, levels, 5)  #Commented code displays a plot of water level for debugging purposes
                pass


    print("Severe flood risk:")
    for station in severe_risk_stations:
        print(station.name)
        '''dates, levels = datafetcher.fetch_measure_levels(station.measure_id,
                        dt=timedelta(days=2))
        plot.plot_water_levels(station, dates, levels)'''
    print("High flood risk:")
    for station in high_risk_stations:
        print(station.name)
        '''dates, levels = datafetcher.fetch_measure_levels(station.measure_id,
                        dt=timedelta(days=2))
        plot.plot_water_levels(station, dates, levels)'''

    '''
    print("Medium flood risk:")
    for station in medium_risk_stations:
        print(station.name)
    print("Low flood risk:")
    for station in low_risk_stations:
        print(station.name)'''

    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
