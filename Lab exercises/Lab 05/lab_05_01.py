string1 = input("Enter some text: ")
string2 = input("Enter some text: ")

common = ""
uncommon = ""

if len(string1) > len(string2):
    length = len(string2)
else:
    length = len(string1)

for i in range(length):
    if string1[i] == string2[i]:
        common += string1[i] + ' '
    else:
        uncommon += string1[i] + ' '

print("Common characters in the two inputs:\n>>>", common)
print("Uncommon characters in the two inputs:\n>>>", uncommon)