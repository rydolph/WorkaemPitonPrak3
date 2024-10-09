class ScientificCalculator:
    def __init__(self):
        self.result = None

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b != 0:
            self.result = a / b
        else:
            raise ValueError("Division by zero is not allowed.")
        return self.result

    def solve_equation(self, equation):
        from sympy import symbols, Eq, solve
        x = symbols('x')
        eq = Eq(eval(equation.split('=')[0]), eval(equation.split('=')[1]))
        solution = solve(eq, x)
        self.result = solution[0]
        return self.result

    def integrate(self, function, lower_bound, upper_bound):
        from sympy import symbols, integrate
        x = symbols('x')
        func = eval(function)
        self.result = integrate(func, (x, lower_bound, upper_bound)).evalf()
        return self.result

    def factorial(self, number):
        fact = 1
        for i in range(2, number + 1):
            fact *= i
        self.result = fact
        return self.result


    def square_root(self, number):
        self.result = number ** 0.5
        return self.result
