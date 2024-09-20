"""
Write code to input electricity units consumed. The program calculates and prints total electricity bill according to
the following condition.
For first 50 units Rs. 0.50/unit.
For next 100 units Rs. 0.75/unit.
For next 100 units Rs. 1.20/unit.
For units above 250 Rs. 1.50/unit.
"""

units = float(input("Enter the number of units: "))

if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 25 + (units - 50) * 0.75
elif units <= 250:
    bill = 100 + (units - 150) * 1.20
else:
    bill = 220 + (units - 250) * 1.50
