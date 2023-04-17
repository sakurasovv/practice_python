a = [1, 4, 6]
b = [11, 33, 22]
result = []

for i in sorted(zip(b, a)):
     result.append(i[1])

print(result)