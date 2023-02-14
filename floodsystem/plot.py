import floodsystem.analysis as analysis
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib

def plot_water_levels(station, dates, levels):
    """Plots the water levels provided against the dates provided.
    Also includes lines for typical low and high levels
    \n Param stations: station data has been given for
    \n Param dates: list of dates to plot
    \n Param levels: list of water levels to plot"""
    if type(station) != object:
        raise TypeError("Inappropriate station input")
    if type(dates) != list:
        raise TypeError("Inappropriate date input")
    if type(levels) != list:
        raise TypeError("Innapropriate levels input")
    plt.plot(dates,levels, label = "Water level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.plot(dates, [station.typical_range[1] for i in range(len(dates))], label = "typical high")
    plt.plot(dates, [station.typical_range[0] for i in range(len(dates))], label = "typical low")
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water levels against dates, then computes and plots a best fit polynomial of degree p.
    Also includes lines for typical low and high levels
    \n Param stations: station data has been given for
    \n Param dates: list of dates to plot
    \n Param levels: list of water levels to plot
    \n Param p: degree of best fit polynomial"""
    if type(station) != object:
        raise TypeError("Inappropriate station input")
    if type(dates) != list:
        raise TypeError("Inappropriate date input")
    if type(levels) != list:
        raise TypeError("Innapropriate levels input")
    if type(p) != int:
        raise TypeError("Innapropriate p input")
    poly, shift = analysis.polyfit(dates, levels, p)
    plt.plot(dates, levels, label = "Water level")
    times = matplotlib.dates.date2num(dates)
    plt.plot(dates, [poly(time - shift) for time in times], label = "Best fit polynomial")
    plt.plot(dates, [station.typical_range[1] for i in range(len(dates))], label = "typical high")
    plt.plot(dates, [station.typical_range[0] for i in range(len(dates))], label = "typical low")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.legend()

    plt.tight_layout()
    plt.show()