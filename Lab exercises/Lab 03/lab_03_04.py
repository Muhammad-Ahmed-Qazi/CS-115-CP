"""
Write a program that takes password from user as input. Validate the password on the following criteria.
Password length between 7 and 15 characters which contain at least one numeric digit and a special character is acceptable.
"""

password = input("Enter your password: ")
length = len(password)

has_digit = False
has_sp_char = False

if length >= 7 and length <= 15:
    for i in range(length):
        if password[i] >= '0' and password[i] <= '9':
            has_digit = True
        elif not (password[i] >= 'A' and password[i] <= 'Z') and not (password[i] >= 'a' and password[i] <= 'z'):
            has_sp_char = True

    if has_digit and has_sp_char:
        print("Password accepted.")
    else:
        print("Password not accepted. Password must contain at least one numeric digit and a special character.")
else:
    print("Unacceptable password. Password length must be between 7 and 15 characters.")