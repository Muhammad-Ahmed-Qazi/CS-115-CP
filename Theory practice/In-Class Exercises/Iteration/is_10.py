"""
Write Python programs to count the number of vowels in a sentence input by the user.
"""

sentence = input("Enter a sentence: ").lower()
vowels = 0

# Using range() function
for i in range(len(sentence)):
    if sentence[i] in "aeiou":
        vowels += 1

print("Number of vowels:", vowels)

# Using in operator
vowels = 0
for char in sentence:
    if char in "aeiou":
        vowels += 1

print("Number of vowels:", vowels)