import pytest
from pytest_bdd import scenario, given, when, then
from calculator import ScientificCalculator

# Загрузка сценариев из feature файла
@scenario('features/calculator.feature', 'Adding two numbers')
def test_adding_two_numbers():
    pass

@scenario('features/calculator.feature', 'Solving an equation')
def test_solving_an_equation():
    pass

@scenario('features/calculator.feature', 'Integrating a function')
def test_integrating_a_function():
    pass

@scenario('features/calculator.feature', 'Calculating factorial')
def test_calculating_factorial():
    pass

@scenario('features/calculator.feature', 'Calculating square root')
def test_calculating_square_root():
    pass

@scenario('features/calculator.feature', 'Subtract two numbers')
def test_subtract_two_numbers():
    pass

@scenario('features/calculator.feature', 'Multiply two numbers')
def test_multiply_two_numbers():
    pass

@scenario('features/calculator.feature', 'Divide two numbers')
def test_divide_two_numbers():
    pass

# Общие шаги для всех сценариев
@pytest.fixture
def calculator():
    return ScientificCalculator()

@given('a calculator')
def given_calculator(calculator):
    return calculator

# Шаги для сложения
@when('I add 2 and 3')
def add_two_numbers(calculator):
    calculator.add(2, 3)

@then('the result should be 5')
def check_addition_result(calculator):
    assert calculator.result == 5

# Шаги для решения уравнения
@when('I solve the equation 2*x + 3 = 7')
def solve_equation(calculator):
    calculator.solve_equation('2*x + 3 = 7')

@then('the solution should be 2')
def check_equation_solution(calculator):
    assert calculator.result == 2

# Шаги для интегрирования функции
@when('I integrate "x**2" from 0 to 1')
def integrate_function(calculator):
    calculator.integrate('x**2', 0, 1)

@then('the integral result should be 0.3333333333333333')
def check_integral_result(calculator):
    assert calculator.result == 0.3333333333333333

# Шаги для вычисления факториала
@when('I calculate the factorial of 5')
def calculate_factorial(calculator):
    calculator.factorial(5)

@then('the factorial result should be 120')
def check_factorial_result(calculator):
    assert calculator.result == 120

# Шаги для вычисления квадратного корня
@when('I calculate the square root of 16')
def calculate_square_root(calculator):
    calculator.square_root(16)

@then('the square root result should be 4')
def check_square_root_result(calculator):
    assert calculator.result == 4

# Шаги для вычитания
@when('I subtract 5 from 10')
def subtract_two_numbers(calculator):
    calculator.subtract(10, 5)

@then('the result should be 5')
def check_subtraction_result(calculator):
    assert calculator.result == 5

# Шаги для умножения
@when('I multiply 5 by 10')
def multiply_two_numbers(calculator):
    calculator.multiply(5, 10)

@then('the result should be 50')
def check_multiplication_result(calculator):
    assert calculator.result == 50

# Шаги для деления
@when('I divide 10 by 2')
def divide_two_numbers(calculator):
    calculator.divide(10, 2)

@then('the result should be 5')
def check_division_result(calculator):
    assert calculator.result == 5
