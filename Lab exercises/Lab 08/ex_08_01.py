print("Average of 5 integer values:")

total = 0

for i in range(1, 6):
    value = int(input(f"Enter value no.{i}\n>>> "))
    total += value

avg = total / 5
print("\nAverage:", round(avg, 2))

print("End of program!")