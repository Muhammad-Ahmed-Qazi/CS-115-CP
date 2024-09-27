first_value = float(input("Enter a number: "))
second_value = float(input("Enter a second number: "))
third_value = float(input("Enter a third number: "))

max_value = first_value
min_value = first_value

if second_value > max_value:
    max_value = second_value
if third_value > max_value:
    max_value = third_value

if second_value < min_value:
    min_value = second_value
if third_value < min_value:
    min_value = third_value

print("Maximum:", max_value)
print("Minimum:", min_value)
