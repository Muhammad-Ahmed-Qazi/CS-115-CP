"""
Develop a script to find the longest word in the file.
"""

longest_word = ""

with open("/home/muhammad-ahmed-qazi/Documents/GitHub/CS-115-CP/Lab exercises/Exercises/lab13.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

print(f"The longest word in the file is: `{longest_word}`")