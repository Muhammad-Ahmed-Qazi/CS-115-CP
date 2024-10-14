gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

# a. Create separate lists of strings and numbers
string = list()
numbers = list()

for element in gadgets:
    if "str" in str(type(element)):
        string.append(element)
    else:
        numbers.append(element)

# b. Sort the strings list in ascending order
string.sort()
print(string)

# c. Sort the strings list in descending order
string.sort(reverse= True)
print(string)

# d. Sort the number list from lowest to highest
numbers.sort()
print(numbers)

# e. Sort the numbers list from highest to lowest
numbers.sort(reverse= True)
print(numbers)