with open("data.txt", "r") as file:
    content = file.read()

content = content.split()
for word in content:
    print(word+",", end=" ")