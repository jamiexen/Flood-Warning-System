"""Test for plot function"""
from floodsystem import analysis as analysis
from datetime import datetime as datetime
import pytest

def test_polyfit():
    """Tests that polyfit returns the expected polynomial from a given set of inputs"""
    poly, shift = analysis.polyfit([datetime(1,1,1), datetime(1,1,2), datetime(1,1,3), datetime(1,1,4)],
    [0,1,1,0], 2)
    assert(poly(0) == pytest.approx(0, 1e-15))
    assert(poly(1) == pytest.approx(1, 1e-15))
    assert(poly(2) == pytest.approx(1, 1e-15))
    assert(poly(3) == pytest.approx(0, 1e-15))