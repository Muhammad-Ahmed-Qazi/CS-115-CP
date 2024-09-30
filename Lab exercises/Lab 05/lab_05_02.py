# Understanding that max. no. of asterisks is fixed but the number of lines with max. no. of asterisks is to be determined by the user.

max_lines = int(input("Enter no. of lines with max. asterisks: "))

for i in range(1, 10):
    print("*" * i)

max_asterisks = ("*" * 10) + "\n"
print(max_asterisks * max_lines, end = "")

for j in range(9, 0, -1):
    print("*" * j)