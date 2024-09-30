stop = int(input("Enter limit for the series of even numbers: "))

print("Even number series:")

for i in range(0, stop, 2):
    print(i, end = " ")

print()