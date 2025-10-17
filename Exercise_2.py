class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

# 🧑‍💻 Get input from user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

    calc = Calculator()

    if operation == "add":
        result = calc.add(num1, num2)
    elif operation == "subtract":
        result = calc.subtract(num1, num2)
    elif operation == "multiply":
        result = calc.multiply(num1, num2)
    elif operation == "divide":
        result = calc.divide(num1, num2)
    else:
        result = "Invalid operation selected."

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")
