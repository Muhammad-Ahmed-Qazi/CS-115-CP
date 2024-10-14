i = ["this", "is", "simple", "computer", "programming", "using", "python"]

print(i[:2] + i[3:5]) # ['this', 'is', 'computer', 'programming']
print(i[:3]) # ['this', 'is', 'simple']
print(i[:2] + i[4:]) # ['this', 'is', 'programming', 'using', 'python']
print(i[4:]) # ['programming', 'using', 'python']
print(list(reversed(i[:2])) + i[3:5]) # ['is', 'this', 'computer', 'programming']