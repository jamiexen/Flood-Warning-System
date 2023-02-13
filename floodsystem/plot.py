from floodsystem import *
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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