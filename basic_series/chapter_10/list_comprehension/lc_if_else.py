numbers = [1,2,3,4,5,6,7,8,9,10]

# output = [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]
output = []
for i in numbers:
    if i % 2 == 0:
        output.append(i ** 2)
    else:
        output.append(-i)
print(output)

print([i**2 if i % 2 == 0 else -i for i in numbers])
