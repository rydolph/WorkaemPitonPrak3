# test_calculator.py
import pytest
from calculator import ScientificCalculator

def test_add():
    calc = ScientificCalculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = ScientificCalculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    calc = ScientificCalculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = ScientificCalculator()
    assert calc.divide(6, 3) == 2

def test_solve_equation():
    calc = ScientificCalculator()
    assert calc.solve_equation("2*x + 3 = 7") == 2

def test_integrate():
    calc = ScientificCalculator()
    assert calc.integrate("x**2", 0, 1) == 1/3


def test_factorial():
    calc = ScientificCalculator()
    assert calc.factorial(5) == 120

def test_square_root():
    calc = ScientificCalculator()
    assert calc.square_root(16) == 4
