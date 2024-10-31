def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except:
        return "Math error!"

def main():
    val1 = int(input("Enter value no.1: "))

    while val1 != -1:
        val2 = int(input("Enter value no. 2: "))

        while True:
            print("Operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
            operation = input("Enter no. of operation you want to perform: ")

            if operation in "1234":
                operation = int(operation)
                break
            else:
                print("Invalid choice! Please enter operation again!")

        if operation == 1:
            result = add(val1, val2)
        elif operation == 2:
            result = subtract(val1, val2)
        elif operation == 3:
            result = multiply(val1, val2)
        elif operation == 4:
            result = divide(val1, val2)

        print("\nResult =", result)
        val1 = int(input("Enter value no. 1: (-1 to exit) "))

if __name__ == "__main__":
    print("Calculator!")
    main()
