char = input("Enter a character: ")

if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
    print("Character is an alphabet.")
else:
    print("Character is not an alphabet.")