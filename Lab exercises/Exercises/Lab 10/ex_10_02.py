"""
Generate the sum of n (user defined) natural number through recursive function.
"""

def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)

limit = int(input("Enter the number of natural numbers to sum: "))
print(f"Sum of {limit} natural numbers: {sum_natural(limit)}")