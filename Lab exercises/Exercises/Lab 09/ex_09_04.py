"""
Construct an outer function “out_circle” that takes radius 'r1' of an outer circle as argument and calculates its area. Also construct an inner function “in_circle” that calculates it's circumference with a smaller radius. Inner function should be enclosed within the outer function.
"""
from random import randint

def out_circle(r1):
    def in_circle(r2):
        return 2 * 3.14 * r2
    return 2 * 3.14 * r1, in_circle(r1-randint(0, int(r1)))

r1 = float(input("Enter radius of outer circle: "))
circumference = out_circle(r1)

print("Circumference of outer circle: ", circumference[0])
print("Circumference of inner circle: ", circumference[1])