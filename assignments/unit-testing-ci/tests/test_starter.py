import pytest

from starter_code import add, multiply, divide, is_even


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 99) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert pytest.approx(divide(1, 3), 0.001) == 1 / 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
