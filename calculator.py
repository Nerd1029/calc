num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


def addition(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def subtraction(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")

def multiplication(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}")

def division(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")

if operation == "+":
    addition(num1, num2)
elif operation == "-":
    subtraction(num1, num2)
elif operation == "*":
    multiplication(num1, num2)
elif operation == "/":
    division(num1, num2)
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.")