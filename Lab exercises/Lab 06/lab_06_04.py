l = [86,86,85,85,85,83,23,45,84,1,2,0]
l.sort(reverse= True)

count = 0
first = l[count]
second = 0

while True:
    if l[count] != first:
        second = l[count]
        break
    count += 1

print(first, second)