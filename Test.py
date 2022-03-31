from lengthmodule import *
from timemodule import *


def test_lengthmodule():
    # when
    m = km_m(1)
    cm = m_cm(1)
    km = cm_km(100)
    # then
    assert m == 1000
    assert cm == 100
    assert km == 0.001


def test_timemodule():
    # when
    m = sekmin(60)
    sek = hoursek(1)
    hour = minhour(60)
    # then
    assert m == 1
    assert sek == 3600
    assert hour == 1
