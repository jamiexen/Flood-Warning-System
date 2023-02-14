import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    """Fits a polynomial of degree p to the lists of dates and levels provided.
    
    \n Param dates: list of dates
    \n Param levels: list of levels
    \n Param p: degree of best fit polynomial"""
    times = matplotlib.dates.date2num(dates)
    shift = times[0]
    times = [time - shift for time in times]
    p_coeff = np.polyfit(times, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, shift
