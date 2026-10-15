# from .src.black_practice.hands_on import divide_funds

from black_practice.hands_on import divide_funds


def test_first():
    assert divide_funds(100, 50) == 2.0


def test_zero_division(caplog):
    assert divide_funds(100, 0) is None
    assert "ZeroDivisionError" in caplog.text


def test_wrong_input(caplog):
    assert divide_funds("100", 2) is None
    assert "TypeError" in caplog.text


def test_float_int():
    assert divide_funds(10, 2.5) == 4

def test_none_input(caplog):
    assert divide_funds(100, None) is None
    assert "TypeError" in caplog.text
