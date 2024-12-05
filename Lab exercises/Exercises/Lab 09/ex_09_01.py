"""
Develop a simple calculator (using functions) that defines addition, subtraction, multiplication and division operation. User selects the operation and provides the operands then output will be generated.
"""

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed"
    return num1 / num2

while True:
    print("Select operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 5:
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print("Result: ", addition(num1, num2))
    elif choice == 2:
        print("Result: ", subtraction(num1, num2))
    elif choice == 3:
        print("Result: ", multiplication(num1, num2))
    elif choice == 4:
        print("Result: ", division(num1, num2))
    else:
        print("Invalid choice")
