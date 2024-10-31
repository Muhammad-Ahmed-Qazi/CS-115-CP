def main():
    print("Addition of two numbers:")
    val1 = int(input("Enter first number\n>>> "))
    val2 = int(input("Enter second number\n>>> "))
    result = sum(val1, val2)
    print(f"\n{val1} + {val2} =", result)

def sum(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    main()
