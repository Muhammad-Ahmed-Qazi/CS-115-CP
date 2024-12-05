def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == '__main__':
    number = int(input("Enter an integer to find its factorial: "))

    print(f"Factorial of {number} = {factorial(number)}")