Feature: Scientific Calculator

  Scenario: Adding two numbers
    Given a calculator
    When I add 2 and 3
    Then the result should be 5

  Scenario: Solving an equation
    Given a calculator
    When I solve the equation 2*x + 3 = 7
    Then the solution should be 2

  Scenario: Integrating a function
    Given a calculator
    When I integrate "x**2" from 0 to 1
    Then the integral result should be 0.3333333333333333

  Scenario: Calculating factorial
    Given a calculator
    When I calculate the factorial of 5
    Then the factorial result should be 120

  Scenario: Calculating square root
    Given a calculator
    When I calculate the square root of 16
    Then the square root result should be 4

   Scenario: Subtract two numbers
    Given a calculator
    When I subtract 5 from 10
    Then the result should be 5

  Scenario: Multiply two numbers
    Given a calculator
    When I multiply 5 by 10
    Then the result should be 50

  Scenario: Divide two numbers
    Given a calculator
    When I divide 10 by 2
    Then the result should be 5
