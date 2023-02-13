import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    times = matplotlib.dates.date2num(dates)
    shift = times[0]
    times = [time - shift for time in times]
    p_coeff = np.polyfit(times, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, shift   #Unsure if the second thing returned is actually the 'shift of the time axis'
