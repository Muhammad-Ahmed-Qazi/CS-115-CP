x = int(input("Enter the number: "))

for n in range(x):
    n += 1
    print("*" * (n))

"""
for n in range(-x, 0):
    n += 1
    print("*" * (0 - n + 1))
"""

for n in range(x, 0, -1):
    print("*" * n)