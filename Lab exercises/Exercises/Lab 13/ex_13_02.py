"""
Develop a script that prints the words of file separated by commas.
"""

content = []
with open("/home/muhammad-ahmed-qazi/Documents/GitHub/CS-115-CP/Lab exercises/Exercises/lab13.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        content.extend(words)

for word in content:
    print(word, end=", ")

print()