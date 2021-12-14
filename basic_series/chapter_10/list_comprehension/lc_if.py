numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = [2,4,6,8,10]
evens = []
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
print(evens)

print([i for i in numbers if i % 2 == 0])
print([i for i in numbers if i % 2 != 0])