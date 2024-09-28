"""
Write a Python program that takes an integer from the user and prints its factors.
"""
import math

# Simple
number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)

# Medium - Fastest
print(">>> Medium")
for i in range(1, round(number / 2) + 1):
    if number % i == 0:
        print(i)

print(number)

# Advanced - less iterations but slower
print(">>> Advanced")
for i in range(1, int(math.sqrt(number)) + 1):
    if number % i == 0:
        print(i)
    if i != number // i:
        print(number // i)