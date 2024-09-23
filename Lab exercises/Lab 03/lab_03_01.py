value = int(input("Enter a positive integer: "))

if value >= 0:
    print("It is an even integer." if value % 2 == 0 else "It is an odd integer.")