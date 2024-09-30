number = int(input("Enter a number to print its table: "))

for i in range(1, 11):
    print(f"{number} x {i : >2} = {number * i}")
