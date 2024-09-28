"""
Write a Python program to display the sum of the series [9 + 99 + 999 + ...]. The number of terms in the series is n. Take n as input from the user.
"""

n = int(input("Enter the number of terms: "))
total = 0

for i in range(1, n + 1):
    total += int("9" * i)
    print("9" * i, end=" + " if i < n else "\n") # Using ternary operator

print("Sum:", total)