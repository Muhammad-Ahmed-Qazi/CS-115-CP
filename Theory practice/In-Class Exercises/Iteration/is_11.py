"""
Write Python programs to display the following patterns. The number of lines should be taken as input from the user.
"""

lines = int(input("Enter the number of lines: "))

for i in range(1, lines + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
