"""
Develop a program to read a file in a remote directory with a for loop.
"""
with open("/home/muhammad-ahmed-qazi/Documents/GitHub/CS-115-CP/Lab exercises/Exercises/lab13.txt", "r") as file:
    for line in file:
        print(line, end="")

