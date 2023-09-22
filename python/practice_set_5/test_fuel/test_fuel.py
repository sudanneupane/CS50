from fuel import convert, gauge
import pytest


def test_percentage():
    assert convert("5/20") == 25


def test_non_num():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_nothing():
    with pytest.raises(ValueError):
        convert("")


def test_for_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_for_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(20) == "20%"
    assert gauge(50) == "50%"
