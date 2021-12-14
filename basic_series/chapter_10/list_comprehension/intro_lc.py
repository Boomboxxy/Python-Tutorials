# List Comprehension
# with the help of list comprehension we can create the list in a single line.

# create a list of squares from numbers 1 to 100

a = []
for num in range(1,101):
    a.append(num ** 2)
print(a)

print([i**2 for i in range(1,101)])
# Syntax of LC = [append    for loop]

print([num * -1 for num in range(1,11)])

names = ["alan", "mark", "john", "joe"]
# ["a", "m", "j", "j"]

print([word[0] for word in names])