import floodsystem.analysis as analysis
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib

def plot_water_levels(station, dates, levels):
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