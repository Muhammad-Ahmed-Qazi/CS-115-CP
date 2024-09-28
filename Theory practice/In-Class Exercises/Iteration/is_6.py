"""
Write a Python program that takes an integer from the user and determines if it is a prime number. Print appropriate messages. Prime numbers are those which have only two factors: 1 and the number itself.
"""

# Simple
number = int(input("Enter a number: "))
factors = 0

for i in range(1, number + 1):
    if number % i == 0:
        factors += 1

if factors == 2:
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")

# Medium
print(">>> Medium")
factors = 0

for i in range(1, round(number / 2) + 1):
    if number % i == 0:
        factors += 1

if factors == 1:
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")