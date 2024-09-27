"""
WRite a Python program that takes an integer from the user and prints its factors.
"""

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)