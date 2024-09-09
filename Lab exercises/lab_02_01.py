print("ax^2 + bx + c")
a = int(input("Enter integer for a: "))
b = int(input("Enter integer for b: "))
c = int(input("Enter integer for c: "))

x1 = ((-b) + (b**2 - 4*a*c)**(1/2)) / (2*a)
x2 = ((-b) - (b**2 - 4*a*c)**(1/2)) / (2*a)

print("X1 =", x1, "\nX2 =", x2)