first_value = int(input("Enter a number: "))
sec_value = int(input("Enter a second number: "))

# print(max(first_value, sec_value))

if first_value > sec_value:
    print("Greater value is:", first_value)
elif sec_value > first_value:
    print("Greater value is:", sec_value)
else:
    print("Neither is greater.")