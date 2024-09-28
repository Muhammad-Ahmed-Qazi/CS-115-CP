"""
Write code to find average of five non-negative integers entered by the user and print average.
"""

total = 0

for i in range(5):
    num = int(input("Enter a non-negative integer: "))
    total += num

print("Average:", total / 5)