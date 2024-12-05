"""
Develop a script that takes a tuple from user and sorts it in reverse order.
"""

# Input tuple from user
tuple1 = eval(input("Enter a tuple: "))

# Sort the tuple in reverse order
tuple1 = tuple(sorted(tuple1, reverse=True))

# Display the sorted tuple
print(tuple1)