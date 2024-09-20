char = input("Enter a character: ")

if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
    print("Character is an alphabet.")
elif 48 <= ord(char) <= 57:
    print("Character is a digit.")
else:
    print("Character is neither an alphabet nor a digit.")