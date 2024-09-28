"""
Write a Python program to display the first n terms of Fibonacci series. In Fibonacci series, first two terms are 0 and 1 respectively, after that every term is the sum of the last two terms.
"""

terms = int(input("Enter the number of terms: "))
a, b = 0, 1

print("Fibonacci series:")
print(a, b, end=" ")
for i in range(terms - 2):
    a, b = b, a + b
    print(b, end=" " if i < terms - 3 else "\n") # Using ternary operator