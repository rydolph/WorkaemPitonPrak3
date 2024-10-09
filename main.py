# This is a sample Python script.
from calculator import ScientificCalculator

calc = ScientificCalculator()
print(calc.integrate("x**2 * 2 + x", 1, 1000000))
print(calc.add(12, 5))
print(calc.divide(4, 2))
print(calc.multiply(12, 2))
print(calc.factorial(5))
print(calc.solve_equation("x+2**8 = 4"))
print(calc.square_root(16))
print(calc.subtract(12, 5))

