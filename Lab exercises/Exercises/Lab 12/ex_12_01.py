"""
Develop a program to replace last element of all tuples in a list.
"""

# List of tuples
tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Replace last element of all tuples with 10
tuples = [t[:-1] + (10,) for t in tuples]

# Display the updated list of tuples
print(tuples)