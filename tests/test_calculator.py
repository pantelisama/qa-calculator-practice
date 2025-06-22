from src.calculator import add, subtract, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_divide_valid():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
