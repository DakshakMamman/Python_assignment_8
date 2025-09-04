"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""

class Calculator:
    print("My Calculator")
    print("==============")

    def _init_(self):
        print("My calculator")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error Division Zero"
        else:
            return x / y

cal = Calculator()
print("Sum value:", cal.add(5,3))
print("Value:", cal.divide(10, 0))
