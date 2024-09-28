"""
Write a Python program to display the first n terms of harmonic series and their sum.
"""

terms = int(input("Enter the number of terms: "))
total = 0

for i in range(1, terms + 1):
    total += 1 / i
    print(f"1/{i}", end=" + " if i < terms else "\n") # Using ternary operator

print("Sum:", round(total, 6))