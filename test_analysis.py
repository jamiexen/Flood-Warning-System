"""Test for plot function"""
from floodsystem import analysis as analysis
import datetime

def test_polyfit():
    """Tests that polyfit returns the expected polynomial from a given set of inputs"""
    poly, shift = analysis.polyfit([datetime.datetime(0,0,1), datetime.datetime(0,0,2), datetime.datetime(0,0,3), datetime.datetime(0,0,4)],
    [0,1,1,0], 2)
    assert(poly(0) == 0)
    assert(poly(1) == 1)
    assert(poly(2) == 1)
    assert(poly(3) == 0)
    assert(shift == 0)